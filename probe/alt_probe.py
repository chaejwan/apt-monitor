"""네이버 외 매물 출처(KB부동산, 직방)가 GitHub Actions 환경에서 매물을 주는지 진단합니다.

브라우저로 각 사이트의 단지 페이지를 열어 매물 탭을 누르고, 그 과정에서 오간 JSON 응답을 기록합니다.
결과는 probe/alt_report.md, 응답 원문은 probe/alt_samples/ 에 저장합니다.

사용법:
    python probe/alt_probe.py --keyword 파크타운 --address 수내동
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
SAMPLES = HERE / "alt_samples"
REPORT = HERE / "alt_report.md"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
)
# 매물 응답에서 흔히 보이는 키 — 이런 키가 있으면 매물 목록 후보로 표시합니다.
LISTING_HINTS = re.compile(r"매물|가격|호가|층|article|price|floor|deposit|rent|sale|item", re.I)

lines: list[str] = []


def out(text: str = "") -> None:
    print(text)
    lines.append(text)


def summarize(body: bytes) -> str:
    try:
        data = json.loads(body)
    except ValueError:
        return "JSON 아님"
    if isinstance(data, list):
        return f"list {len(data)}건"
    if not isinstance(data, dict):
        return type(data).__name__
    parts = [f"keys={list(data)[:6]}"]
    # 가장 긴 리스트를 찾아 건수를 표시합니다.
    best = None

    def walk(node, path, depth):
        nonlocal best
        if depth > 4:
            return
        if isinstance(node, list) and node and isinstance(node[0], dict):
            if best is None or len(node) > best[1]:
                best = (path, len(node), list(node[0])[:8])
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, f"{path}.{k}", depth + 1)

    walk(data, "", 0)
    if best:
        parts.append(f"가장 긴 목록 {best[0] or '.'} {best[1]}건, 항목 keys={best[2]}")
    return ", ".join(parts)


def try_search(page, keyword: str) -> str:
    """페이지에서 검색창을 찾아 키워드를 넣고 엔터를 칩니다."""
    selectors = [
        "input[type=search]",
        "input[placeholder*='검색']",
        "input[placeholder*='단지']",
        "input[placeholder*='지역']",
        "input[placeholder*='주소']",
        "input[type=text]",
    ]
    # 검색창이 버튼 뒤에 숨어 있는 사이트를 위해 검색 버튼을 먼저 눌러 봅니다.
    for opener in ("[aria-label*='검색']", "button:has-text('검색')", "a:has-text('검색')"):
        try:
            page.locator(opener).first.click(timeout=1500)
            page.wait_for_timeout(800)
            break
        except Exception:
            continue
    for sel in selectors:
        try:
            box = page.locator(sel).first
            box.click(timeout=2000)
            box.fill(keyword)
            page.wait_for_timeout(2000)
            box.press("Enter")
            page.wait_for_timeout(3000)
            return f"검색창({sel})에 '{keyword}' 입력"
        except Exception:
            continue
    return "검색창을 찾지 못함"


def click_text(page, texts: list[str], wait: int = 3000) -> str | None:
    for t in texts:
        try:
            page.get_by_text(t).first.click(timeout=2500)
            page.wait_for_timeout(wait)
            return t
        except Exception:
            continue
    return None


def explore(ctx, name: str, start_url: str, keyword: str, address: str, direct_urls: list[str],
            tabs: list[str] | None = None, search: bool = True) -> list[dict]:
    out(f"## {name}")
    out()
    seen: list[dict] = []

    def on_response(resp):
        if "json" not in resp.headers.get("content-type", ""):
            return
        try:
            body = resp.body()
        except Exception:
            return
        seen.append({"url": resp.url, "status": resp.status, "method": resp.request.method,
                     "post": (resp.request.post_data or "")[:300], "body": body})

    SAMPLES.mkdir(parents=True, exist_ok=True)
    page = ctx.new_page()
    page.on("response", on_response)
    steps = []
    try:
        resp = page.goto(start_url, wait_until="domcontentloaded", timeout=40_000)
        page.wait_for_timeout(4000)
        steps.append(f"시작 페이지 {start_url} → 상태 {resp.status if resp else '없음'}")
        if keyword and search:
            steps.append(try_search(page, f"{address} {keyword}".strip()))
            hit = click_text(page, [f"{keyword}", keyword.replace(" ", "")])
            steps.append(f"검색 결과 '{hit}' 클릭" if hit else "검색 결과에서 단지를 찾지 못함")
            tab = click_text(page, ["매물", "매매", "단지 매물", "전체 매물"])
            steps.append(f"'{tab}' 탭 클릭" if tab else "매물 탭을 찾지 못함")
        for url in direct_urls:
            r = page.goto(url, wait_until="domcontentloaded", timeout=30_000)
            page.wait_for_timeout(4000)
            steps.append(f"직접 이동 {url} → 상태 {r.status if r else '없음'}, 최종 {page.url[:90]}")
        for t in tabs or []:
            label = getattr(t, "pattern", t)
            hit = click_text(page, [t])
            page.wait_for_timeout(2000)
            login = page.get_by_text("로그인 하면").or_(page.get_by_text("로그인이 필요")).count() > 0
            steps.append((f"'{label}' 클릭" if hit else f"'{label}' 를 찾지 못함")
                         + (" → 로그인 창이 뜸" if login else ""))
            if login:
                page.screenshot(path=str(SAMPLES / f"{name}_로그인.png"))
                page.keyboard.press("Escape")
                page.wait_for_timeout(800)
            # 목록이 스크롤로 더 불러와지는 사이트를 위해 아래로 몇 번 내립니다.
            for _ in range(3):
                page.mouse.wheel(0, 1500)
                page.wait_for_timeout(800)
        steps.append(f"마지막 주소: {page.url}")
        title = page.title()
        steps.append(f"페이지 제목: {title}")
        text = page.inner_text("body")[:100_000]
        found = [m.group(0) for m in re.finditer(r"매[매물]\s*\d+|전세\s*\d+|월세\s*\d+", text)][:10]
        steps.append(f"화면 글자에서 찾은 매물 수 표시: {found or '없음'}")
        SAMPLES.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(SAMPLES / f"{name}.png"), full_page=False)
    except Exception as e:
        steps.append(f"진행 중 실패: {str(e)[:200]}")

    for s in steps:
        out(f"- {s}")
    out()
    out("| 방식 | 상태 | 주소 | 내용 | 원문 |")
    out("|---|---|---|---|---|")
    SAMPLES.mkdir(parents=True, exist_ok=True)
    for i, r in enumerate(seen):
        desc = summarize(r["body"])
        sample = ""
        text = r["body"][:400_000].decode("utf-8", "replace")
        if (keyword.replace(" ", "") in text.replace(" ", "") or LISTING_HINTS.search(desc)
                or "propList" in r["url"] or "/items" in r["url"]):
            fname = f"{name}_{i}.json"
            (SAMPLES / fname).write_text(
                json.dumps({"url": r["url"], "method": r["method"], "post": r["post"]}, ensure_ascii=False)
                + "\n" + text, encoding="utf-8")
            sample = f"alt_samples/{fname}"
        short = urllib.parse.unquote(r["url"].split("?")[0])[:90]
        out(f"| {r['method']} | {r['status']} | `{short}` | {desc[:160]} | {sample} |")
    out()
    page.close()
    return seen


def find_ids(seen: list[dict], keyword: str, id_keys: tuple[str, ...]) -> dict[str, str]:
    """수집한 JSON에서 이름에 키워드가 들어간 항목의 id를 찾습니다."""
    found: dict[str, str] = {}

    def walk(node):
        if isinstance(node, dict):
            name = next((v for v in node.values() if isinstance(v, str) and keyword in v), None)
            ident = next((node[k] for k in id_keys if node.get(k)), None)
            if name and ident:
                found.setdefault(str(ident), name)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    for r in seen:
        try:
            walk(json.loads(r["body"]))
        except ValueError:
            continue
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--keyword", required=True, help="단지명 (예: 파크타운)")
    ap.add_argument("--address", default="", help="동 이름 (예: 수내동) — 같은 이름 단지 구분용")
    ap.add_argument("--zigbang", action="store_true", help="직방 단지 페이지도 열어 보기")
    args = ap.parse_args()

    out("# 대체 출처 진단 결과")
    out()
    out(f"- 실행 시각: {dt.datetime.now(dt.timezone(dt.timedelta(hours=9))):%Y-%m-%d %H:%M} KST")
    out(f"- 검색어: {args.address} {args.keyword}")
    out()

    from playwright.sync_api import sync_playwright

    tabs = ["매물", "매매", "전세", "월세"]
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
        ctx = browser.new_context(user_agent=UA, locale="ko-KR", timezone_id="Asia/Seoul",
                                  viewport={"width": 1400, "height": 900})

        # 직방: 검색 API로 단지를 찾고 단지 페이지마다 매물 탭을 엽니다.
        q = urllib.parse.quote(f"{args.address} {args.keyword}".strip())
        danjis, center = [], None
        try:
            resp = ctx.request.get(f"https://apis.zigbang.com/v2/search?leaseYn=N&os=web&q={q}&serviceType=아파트")
            danjis = [it for it in resp.json().get("items", [])
                      if it.get("type") == "apartment" and args.keyword in it.get("name", "")]
        except Exception as e:
            out(f"직방 검색 실패: {e}")
        out(f"직방 검색으로 찾은 단지: {[(d['id'], d['name']) for d in danjis]}")
        out()
        for d in danjis[:4]:
            center = center or (d.get("lat"), d.get("lng"))
        if args.zigbang:
            for d in danjis[:4]:
                explore(ctx, f"직방_{d['name']}", f"https://www.zigbang.com/home/apt/danjis/{d['id']}",
                        args.keyword, "", [], tabs=tabs, search=False)

        # KB부동산: 단지 좌표로 지도를 열어 단지 id를 찾고, 단지 페이지마다 매물 탭을 엽니다.
        if center and center[0]:
            seen = explore(ctx, "KB부동산_지도", f"https://kbland.kr/map?xy={center[0]},{center[1]},18",
                           args.keyword, "", [], search=False)
            kb_ids = find_ids(seen, args.keyword, ("단지기본일련번호", "complexId", "단지일련번호"))
            out(f"KB부동산 지도에서 찾은 단지: {kb_ids or '없음'}")
            out()
            kb_tabs = [re.compile(r"^매매\s*\d+$"), re.compile(r"^전세\s*\d+$"),
                       re.compile(r"^월세\s*\d+$"), "동별매물"]
            for kb_id, kb_name in list(kb_ids.items())[:4]:
                if not kb_name.startswith(args.keyword):  # '도덕파크타운' 같은 다른 단지는 건너뜀
                    continue
                explore(ctx, f"KB부동산_{kb_name}", f"https://kbland.kr/c/{kb_id}",
                        args.keyword, "", [], tabs=kb_tabs, search=False)
        browser.close()

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
