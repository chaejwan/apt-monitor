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
            return f"keys={keys}{extra}"
        return f"list {len(data)}건"
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
        status, body, ctype = cached or fetch(url, headers)
        sample = save_sample(f"http_{name}.txt", body) if body else ""
        out(f"| {name} | {status} | {len(body)} | {describe(body, ctype)} | {sample} |")
        time.sleep(1.5)
    out()
    out(f"- 페이지 HTML에서 찾은 JWT 토큰: {'있음' if token else '없음'}")
    out()


def browser_checks(complex_no: str) -> None:
    out("## 2. 브라우저 렌더링 중 오간 JSON 응답")
    out()
    from playwright.sync_api import sync_playwright

    pages = [
        f"https://new.land.naver.com/complexes/{complex_no}",
        f"https://fin.land.naver.com/complexes/{complex_no}",
    ]
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(user_agent=UA, locale="ko-KR", timezone_id="Asia/Seoul")
        for page_url in pages:
            seen: list[dict] = []
            auth_headers: set[str] = set()

            def on_request(req):
                h = req.headers.get("authorization")
                if h:
                    auth_headers.add(f"{urllib.parse.urlparse(req.url).netloc} → {h[:20]}…")

            def on_response(resp):
                ctype = resp.headers.get("content-type", "")
                if "json" not in ctype:
                    return
                try:
                    body = resp.body()
                except Exception:
                    body = b""
                seen.append({"url": resp.url, "status": resp.status, "method": resp.request.method,
                             "size": len(body), "desc": describe(body, ctype), "body": body})

            page = ctx.new_page()
            page.on("request", on_request)
            page.on("response", on_response)
            out(f"### {page_url}")
            out()
            try:
                resp = page.goto(page_url, wait_until="domcontentloaded", timeout=45_000)
                out(f"- 페이지 상태: {resp.status if resp else '응답 없음'}, 최종 주소: {page.url}")
                page.wait_for_timeout(8000)
                # 매물 목록을 띄우기 위해 매물 탭으로 보이는 요소를 눌러 봅니다.
                for label in ("매물", "단지 매물", "매매"):
                    try:
                        page.get_by_text(label, exact=True).first.click(timeout=2000)
                        page.wait_for_timeout(2500)
                        break
                    except Exception:
                        continue
            except Exception as e:
                out(f"- 페이지 로딩 실패: {e}")
            out(f"- Authorization 헤더를 쓴 요청: {sorted(auth_headers) or '없음'}")
            out()
            out("| 방식 | 상태 | 크기 | 주소 | 내용 |")
            out("|---|---|---|---|---|")
            for i, r in enumerate(seen):
                short = r["url"].split("?")[0]
                out(f"| {r['method']} | {r['status']} | {r['size']} | `{short}` | {r['desc']} |")
                if r["size"] and re.search(r"article|complex|price|deal", r["url"], re.I):
                    save_sample(f"browser_{urllib.parse.urlparse(page_url).netloc}_{i}.json", r["body"])
                    (SAMPLES / f"browser_{urllib.parse.urlparse(page_url).netloc}_{i}.url").write_text(r["url"])
            out()
            page.close()
        browser.close()


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
    http_checks(args.complex)
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
