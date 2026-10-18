"""네이버부동산·국토부 실거래 API가 GitHub Actions 환경에서 응답하는지 진단합니다.

결과는 probe/report.md 에 마크다운으로, 응답 원문 일부는 probe/samples/ 에 저장합니다.

사용법:
    python probe/naver_probe.py --complex 111515            # HTTP 직접 요청만
    python probe/naver_probe.py --complex 111515 --browser  # 브라우저 렌더링 + 오간 JSON 응답 수집
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SAMPLES = HERE / "samples"
REPORT = HERE / "report.md"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
)
JWT_RE = re.compile(r"eyJ[\w-]{10,}\.[\w-]{10,}\.[\w-]{10,}")

lines: list[str] = []


def out(text: str = "") -> None:
    print(text)
    lines.append(text)


def save_sample(name: str, body: bytes) -> str:
    SAMPLES.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^\w.-]+", "_", name)[:80]
    path = SAMPLES / safe
    path.write_bytes(body[:200_000])
    return str(path.relative_to(HERE.parent))


def fetch(url: str, headers: dict | None = None) -> tuple[int, bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status, resp.read(), resp.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        return e.code, e.read(), e.headers.get("Content-Type", "")
    except Exception as e:  # 연결 자체 실패
        return 0, str(e).encode(), ""


def describe(body: bytes, ctype: str) -> str:
    if "json" in ctype or body[:1] in (b"{", b"["):
        try:
            data = json.loads(body)
        except ValueError:
            return "JSON 파싱 실패"
        if isinstance(data, dict):
            keys = list(data)[:8]
            extra = ""
            for k in ("articleList", "result", "body", "items"):
                if isinstance(data.get(k), list):
                    extra = f", {k} {len(data[k])}건"
                elif isinstance(data.get(k), dict):
                    inner = {ik: len(iv) for ik, iv in data[k].items() if isinstance(iv, list)}
                    extra = f", {k} keys={list(data[k])[:8]} 목록={inner}"
            return f"keys={keys}{extra}"
        if isinstance(data, list):
            return f"list {len(data)}건"
        return f"JSON 값: {str(data)[:40]}"
    text = body[:200].decode("utf-8", "replace").replace("\n", " ")
    return f"text: {text[:120]}"


def reach_checks() -> None:
    out("## 0. 사이트별 접속 여부")
    out()
    out("네이버 전체가 막혔는지 부동산만 막혔는지, 대체 출처는 열리는지 확인합니다.")
    out()
    targets = [
        ("네이버 메인", "https://www.naver.com/"),
        ("네이버 검색", "https://search.naver.com/search.naver?query=%ED%8C%8C%ED%81%AC%ED%83%80%EC%9A%B4"),
        ("네이버 지도", "https://map.naver.com/"),
        ("land.naver.com", "https://land.naver.com/"),
        ("new.land.naver.com", "https://new.land.naver.com/"),
        ("fin.land.naver.com", "https://fin.land.naver.com/"),
        ("KB부동산", "https://kbland.kr/"),
        ("KB부동산 API", "https://api.kbland.kr/"),
        ("직방", "https://www.zigbang.com/"),
        ("직방 API", "https://apis.zigbang.com/"),
        ("호갱노노", "https://hogangnono.com/"),
        ("아실", "https://asil.kr/"),
        ("공공데이터포털 API", "https://apis.data.go.kr/"),
        ("카카오 API", "https://dapi.kakao.com/"),
    ]
    out("| 사이트 | 상태 | 걸린 시간 | 비고 |")
    out("|---|---|---|---|")
    for name, url in targets:
        start = time.time()
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                status, note = resp.status, resp.geturl()[:60]
        except urllib.error.HTTPError as e:
            status, note = e.code, "HTTP 오류(서버는 응답함)"
        except Exception as e:
            status, note = 0, str(e)[:60]
        out(f"| {name} | {status} | {time.time() - start:.1f}s | {note} |")
    out()


def http_checks(complex_no: str) -> None:
    out("## 1. HTTP 직접 요청")
    out()
    page_url = f"https://new.land.naver.com/complexes/{complex_no}"
    status, body, ctype = fetch(page_url)
    tokens = JWT_RE.findall(body.decode("utf-8", "replace")) if status == 200 else []
    token = tokens[0] if tokens else None

    articles_qs = urllib.parse.urlencode({
        "realEstateType": "APT", "tradeType": "", "tag": "::::::::",
        "rentPriceMin": 0, "rentPriceMax": 900000000, "priceMin": 0, "priceMax": 900000000,
        "areaMin": 0, "areaMax": 900000000, "showArticle": "false", "sameAddressGroup": "false",
        "priceType": "RETAIL", "page": 1, "complexNo": complex_no, "type": "list", "order": "rank",
    })
    api = "https://new.land.naver.com/api"
    referer = {"Referer": page_url, "Accept": "application/json"}
    auth = {**referer, "Authorization": f"Bearer {token}"} if token else None

    checks = [
        ("new.land 단지 페이지", page_url, None, (status, body, ctype)),
        ("new.land 단지 API", f"{api}/complexes/{complex_no}?sameAddressGroup=false", referer, None),
        ("new.land 매물 API", f"{api}/articles/complex/{complex_no}?{articles_qs}", referer, None),
    ]
    if auth:
        checks += [
            ("new.land 단지 API (+토큰)", f"{api}/complexes/{complex_no}?sameAddressGroup=false", auth, None),
            ("new.land 매물 API (+토큰)", f"{api}/articles/complex/{complex_no}?{articles_qs}", auth, None),
        ]
    checks += [
        ("m.land 매물 목록", "https://m.land.naver.com/complex/getComplexArticleList?"
         f"hscpNo={complex_no}&tradTpCd=A1:B1:B2&order=date_&showR0=N&page=1",
         {"Referer": "https://m.land.naver.com/"}, None),
        ("fin.land 단지 페이지", f"https://fin.land.naver.com/complexes/{complex_no}", None, None),
    ]

    out("| 확인 항목 | 상태 | 크기 | 내용 | 원문 |")
    out("|---|---|---|---|---|")
    for name, url, headers, cached in checks:
        try:
            status, body, ctype = cached or fetch(url, headers)
            sample = save_sample(f"http_{name}.txt", body) if body else ""
            out(f"| {name} | {status} | {len(body)} | {describe(body, ctype)} | {sample} |")
        except Exception as e:
            out(f"| {name} | 오류 | - | {str(e)[:80]} | |")
        time.sleep(1.5)
    out()
    out(f"- 페이지 HTML에서 찾은 JWT 토큰: {'있음' if token else '없음'}")
    out()


# 사용자가 평소 브라우저에서 연 파크타운 지도 주소 (layer 값에 단지가 들어 있음)
MAP_URL = ("https://fin.land.naver.com/map?tradeTypes=A1-B1&realEstateTypes=A01-A04-B01&layer="
           "NobwRAlgJmBcYGMD2BbADgGwKYA8D6UWALgIYQZgA0YaJATiSgM5zjLrY4CSMsAzAAYAHABYAvtSZZ6CABYAFeoxaxwpAEZwwRBgDsmJBEQhJdYCWDrEArnV0l12ODutYxAXSA")

# 페이지 안에서 직접 부를 API. {c} 는 단지번호. 매물 목록은 이름을 몰라 후보를 여럿 시도합니다.
IN_PAGE_APIS = [
    "/front-api/v1/complex/article/stats?complexNumber={c}",
    "/front-api/v1/complex/pyeongList?complexNumber={c}",
    "/front-api/v1/complex/pyeongGroups?complexNumber={c}",
    "/front-api/v1/complex/asking-price?complexNumber={c}&pyeongTypeNumber=0&realEstateType=A01&tradeType=A1",
    "/front-api/v1/complex?complexNumber={c}",
    "/front-api/v1/complex/article/list?complexNumber={c}&tradeTypes[]=A1&page=0&size=30",
    "/front-api/v1/complex/article/list?complexNumber={c}&tradeType=A1&page=0&size=30",
    "/front-api/v1/complex/articles?complexNumber={c}&tradeType=A1&page=0&size=30",
    "/front-api/v1/article/list?complexNumber={c}&tradeType=A1&page=0&size=30",
    "/front-api/v1/complex/article/v2/list?complexNumber={c}&tradeType=A1&page=0&size=30",
]


def browser_checks(complex_no: str) -> None:
    out("## 2. 브라우저 렌더링 중 오간 JSON 응답")
    out()
    from playwright.sync_api import sync_playwright

    SAMPLES.mkdir(parents=True, exist_ok=True)
    profile = HERE.parent / "laptop" / ".browser-profile"
    with sync_playwright() as p:
        # 자동화 브라우저로 보이면 네이버가 404로 돌려보내므로, 설치된 Chrome을 자동화 표시 없이 띄웁니다.
        opts = dict(headless=os.environ.get("HEADED") != "1", locale="ko-KR", timezone_id="Asia/Seoul",
                    viewport={"width": 1400, "height": 900},
                    args=["--disable-blink-features=AutomationControlled"],
                    ignore_default_args=["--enable-automation"])
        try:
            ctx = p.chromium.launch_persistent_context(str(profile), channel="chrome", **opts)
            out("- 브라우저: 설치된 Chrome")
        except Exception as e:
            out(f"- 설치된 Chrome 실행 실패({str(e)[:60]}), 내장 Chromium 사용")
            ctx = p.chromium.launch_persistent_context(
                str(profile), executable_path=os.environ.get("CHROMIUM_PATH") or None, **opts)
        ctx.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        seen: list[tuple[str, int, str]] = []
        ctx.on("response", lambda r: seen.append((r.request.method, r.status, r.url))
               if "front-api" in r.url else None)
        # 화면이 POST로 부르는 API는 요청 본문과 헤더를 함께 남겨, 나중에 같은 요청을 다시 보냅니다.
        posts: list[dict] = []

        replaying = [False]

        def on_request(req):
            # 진단이 직접 다시 보내는 요청은 기록하지 않습니다 (기록하면 목록이 끝없이 늘어남).
            if replaying[0]:
                return
            if "front-api" in req.url and req.method == "POST" and "/user/" not in req.url \
                    and "telemetry" not in req.url:
                headers = {k: v for k, v in req.headers.items()
                           if k.lower() not in ("cookie", "content-length", "host") and not k.startswith(":")}
                posts.append({"url": req.url, "body": req.post_data or "", "headers": headers})

        ctx.on("request", on_request)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        try:
            resp = page.goto(MAP_URL, wait_until="domcontentloaded", timeout=45_000)
            out(f"- 지도 페이지 상태: {resp.status if resp else '응답 없음'}")
            for sec in (3, 8):
                page.wait_for_timeout(sec * 1000 - (3000 if sec == 8 else 0))
                out(f"- {sec}초 뒤 주소: {page.url[:110]}")
            page.screenshot(path=str(SAMPLES / "browser_1_지도.png"))
            ok = "fin.land.naver.com" in page.url
            out(f"- 404로 넘어갔는지: {'아니오(정상)' if ok else '예'}")
            out()

            if ok:
                # 매매 탭 클릭으로 화면이 부르는 매물 목록 API를 잡아 봅니다.
                for loc in (page.get_by_text(re.compile(r"^매매\s*\d+$")),
                            page.locator("text=/^매매/").filter(has_text=re.compile(r"\d")),
                            page.get_by_role("tab", name=re.compile("매물")),
                            page.get_by_text("매물", exact=True)):
                    try:
                        loc.first.click(timeout=3000)
                        page.wait_for_timeout(4000)
                        out(f"- 매물 탭 클릭 성공 → {page.url[:110]}")
                        break
                    except Exception:
                        continue
                else:
                    out("- 매물 탭 클릭 실패")
                page.screenshot(path=str(SAMPLES / "browser_2_매물.png"))
                out()

                out("### 페이지 안에서 직접 부른 API")
                out()
                out("| 상태 | 크기 | 주소 | 내용 | 원문 |")
                out("|---|---|---|---|---|")
                extra = ["/front-api/v1/complex/buildingList?complexNumber={c}",
                         "/front-api/v1/complex/mapComplexSummaryInfo?complexNumber={c}"]
                for i, path in enumerate(IN_PAGE_APIS[:5] + extra):
                    url = path.format(c=complex_no)
                    res = page.evaluate(
                        "async (u) => { const r = await fetch(u, {credentials: 'include'});"
                        " return [r.status, await r.text()]; }", url)
                    body = res[1].encode("utf-8")
                    sample = save_sample(f"inpage_{i}.json", body)
                    out(f"| {res[0]} | {len(body)} | `{urllib.parse.unquote(url)[:120]}` | "
                        f"{describe(body, 'json')[:140]} | {sample} |")
                    page.wait_for_timeout(700)
                out()

                out("### 화면이 POST로 부른 API를 같은 본문으로 다시 호출")
                out()
                (SAMPLES / "posts.json").write_text(json.dumps(posts, ensure_ascii=False, indent=1),
                                                    encoding="utf-8")
                out("| 상태 | 크기 | 주소 | 요청 본문 | 내용 | 원문 |")
                out("|---|---|---|---|---|---|")
                replaying[0] = True
                # 같은 주소·본문은 한 번만, 최대 10개까지만 다시 보냅니다.
                unique = list({(r["url"], r["body"]): r for r in posts}.values())[:10]
                for i, req in enumerate(unique):
                    res = page.evaluate(
                        "async ([u, b, h]) => { const r = await fetch(u, {method: 'POST', body: b,"
                        " headers: h, credentials: 'include'}); return [r.status, await r.text()]; }",
                        [req["url"], req["body"], req["headers"]])
                    body = res[1].encode("utf-8")
                    sample = save_sample(f"post_{i}.json", body)
                    short = req["url"].replace("https://fin.land.naver.com", "")
                    out(f"| {res[0]} | {len(body)} | `{short}` | `{req['body'][:300]}` | "
                        f"{describe(body, 'json')[:140]} | {sample} |")
                    page.wait_for_timeout(700)
                out()
        except Exception as e:
            out(f"- 진행 중 실패: {str(e)[:200]}")
            out()
        ctx.close()

    out("### 화면이 스스로 부른 API (주소만)")
    out()
    for method, status, url in seen:
        out(f"- {method} {status} `{urllib.parse.unquote(url).replace('https://fin.land.naver.com', '')[:200]}`")
    out()


def molit_check() -> None:
    out("## 3. 국토부 실거래 API")
    out()
    key = os.environ.get("MOLIT_API_KEY")
    if not key:
        out("- MOLIT_API_KEY 시크릿이 없어 건너뜀")
        out()
        return
    ym = (dt.date.today().replace(day=1) - dt.timedelta(days=1)).strftime("%Y%m")
    for name, svc in [("매매", "RTMSDataSvcAptTradeDev/getRTMSDataSvcAptTradeDev"),
                      ("전월세", "RTMSDataSvcAptRent/getRTMSDataSvcAptRent")]:
        url = (f"https://apis.data.go.kr/1613000/{svc}?serviceKey={urllib.parse.quote(key, safe='')}"
               f"&LAWD_CD=11710&DEAL_YMD={ym}&numOfRows=5&pageNo=1")
        status, body, ctype = fetch(url)
        sample = save_sample(f"molit_{name}.xml", body)
        text = body[:300].decode("utf-8", "replace").replace("\n", " ")
        out(f"- {name} ({ym}, 송파구): 상태 {status}, {len(body)} bytes, 원문 {sample}")
        out(f"  - `{text[:200]}`")
    out()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--complex", required=True, help="네이버 단지번호 (단지 주소의 /complexes/ 뒤 숫자)")
    ap.add_argument("--browser", action="store_true")
    args = ap.parse_args()

    out("# 진단 결과")
    out()
    out(f"- 실행 시각: {dt.datetime.now(dt.timezone(dt.timedelta(hours=9))):%Y-%m-%d %H:%M} KST")
    out(f"- 단지번호: {args.complex}")
    try:
        status, body, _ = fetch("https://api.ipify.org?format=json")
        out(f"- 실행 환경 IP: {body.decode()[:60]}")
    except Exception:
        pass
    out()

    reach_checks()
    try:
        http_checks(args.complex)
    except Exception as e:
        out(f"HTTP 진단 실패: {e}")
        out()
    if args.browser:
        try:
            browser_checks(args.complex)
        except Exception as e:
            out(f"브라우저 진단 실패: {e}")
            out()
    molit_check()

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
