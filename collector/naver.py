"""네이버페이 부동산(fin.land.naver.com) 매물 조회.

네이버는 브라우저가 아닌 요청(429)과 자동화 브라우저(404 페이지로 돌려보냄)를 막으므로,
설치된 Chrome을 자동화 표시 없이 띄워 fin.land 페이지를 연 뒤 그 페이지 안에서 API를 부릅니다.
"""

import json
import os
import random
import time
import urllib.parse
from pathlib import Path

ORIGIN = "https://fin.land.naver.com"
# 아무 fin.land 페이지나 열려 있으면 같은 출처로 API를 부를 수 있습니다.
START_URL = ORIGIN + "/map?tradeTypes=A1-B1&realEstateTypes=A01-A04-B01"

TRADE_CODES = {"매매": "A1", "전세": "B1", "월세": "B2"}

_FETCH_JS = """async ([url, method, body, headers]) => {
  const opts = {method, headers, credentials: 'include', signal: AbortSignal.timeout(20000)};
  if (body !== null) opts.body = body;
  const r = await fetch(url, opts);
  return [r.status, await r.text()];
}"""


class NaverError(Exception):
    pass


class NaverLand:
    def __init__(self, profile_dir: Path, headless: bool = True, log=print):
        self.profile_dir = profile_dir
        self.headless = headless
        self.log = log
        self.attest = None  # 화면이 보낸 요청의 x-attest 헤더 (거절당했을 때 다시 시도용)

    def __enter__(self):
        from playwright.sync_api import sync_playwright

        self._pw = sync_playwright().start()
        try:
            self._open(self.headless)
            if not self._page_ok() and self.headless:
                self.log("화면 없는 브라우저가 막혀 브라우저 창을 띄워 다시 시도합니다.")
                self.ctx.close()
                self._open(False)
            if not self._page_ok():
                raise NaverError(f"네이버 부동산 페이지가 열리지 않습니다: {self.page.url[:100]}")
        except Exception as e:
            self.__exit__()
            raise e if isinstance(e, NaverError) else NaverError(f"브라우저 준비 실패: {str(e)[:150]}")
        return self

    def __exit__(self, *exc):
        try:
            if getattr(self, "ctx", None):
                self.ctx.close()
        except Exception:
            pass
        finally:
            self._pw.stop()

    def _open(self, headless: bool) -> None:
        opts = dict(headless=headless, locale="ko-KR", timezone_id="Asia/Seoul",
                    viewport={"width": 1400, "height": 900},
                    args=["--disable-blink-features=AutomationControlled"],
                    ignore_default_args=["--enable-automation"])
        try:
            self.ctx = self._pw.chromium.launch_persistent_context(str(self.profile_dir), channel="chrome", **opts)
        except Exception:
            self.log("설치된 Chrome을 찾지 못해 내장 Chromium을 씁니다.")
            self.ctx = self._pw.chromium.launch_persistent_context(
                str(self.profile_dir), executable_path=os.environ.get("CHROMIUM_PATH") or None, **opts)
        self.ctx.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.ctx.on("request", self._remember_attest)
        self.page = self.ctx.pages[0] if self.ctx.pages else self.ctx.new_page()
        self.page.goto(START_URL, wait_until="domcontentloaded", timeout=45_000)
        self.page.wait_for_timeout(6000)

    def _remember_attest(self, req) -> None:
        value = req.headers.get("x-attest")
        if value and "front-api" in req.url:
            self.attest = value

    def _page_ok(self) -> bool:
        return self.page.url.startswith(ORIGIN)

    def _fetch(self, method: str, path: str, body: dict | None = None) -> dict:
        url = ORIGIN + path
        headers = {"accept": "application/json, text/plain, */*"}
        payload = None
        if body is not None:
            headers["content-type"] = "application/json"
            payload = json.dumps(body, ensure_ascii=False)
        for attempt in range(2):
            if attempt and self.attest:
                headers["x-attest"] = self.attest
            try:
                status, text = self.page.evaluate(_FETCH_JS, [url, method, payload, headers])
            except Exception as e:
                status, text = 0, str(e)
            if status == 200:
                data = json.loads(text)
                if data.get("isSuccess", True):
                    return data.get("result", data)
                status, text = 200, data.get("message") or data.get("detailCode", "")
            self.log(f"  {method} {path[:60]} → {status} {text[:80]}")
            time.sleep(3)
        raise NaverError(f"{method} {path} 실패 ({status})")

    def get(self, path: str, **params) -> dict:
        query = []
        for k, v in params.items():
            if isinstance(v, (list, tuple)):
                query += [(f"{k}[]", x) for x in v]
            else:
                query.append((k, v))
        return self._fetch("GET", path + ("?" + urllib.parse.urlencode(query) if query else ""))

    def pause(self) -> None:
        time.sleep(random.uniform(1.2, 2.2))

    def complex_info(self, complex_no: str) -> dict:
        info = self.get("/front-api/v1/complex", complexNumber=complex_no)
        self.pause()
        info["pyeongList"] = self.get("/front-api/v1/complex/pyeongList", complexNumber=complex_no)
        self.pause()
        info["buildingList"] = self.get("/front-api/v1/complex/buildingList", complexNumber=complex_no)
        self.pause()
        return info

    def article_stats(self, complex_no: str) -> dict:
        return self.get("/front-api/v1/complex/article/stats", complexNumber=complex_no)

    def articles(self, complex_no: str, trade_code: str, max_pages: int = 30) -> list[dict]:
        """한 거래유형의 매물 목록 전체를 페이지를 넘기며 받습니다."""
        items: list[dict] = []
        last_info: list = []
        for _ in range(max_pages):
            result = self._fetch("POST", "/front-api/v1/complex/article/list", {
                "size": 30, "complexNumber": int(complex_no), "tradeTypes": [trade_code],
                "pyeongTypes": [], "dongNumbers": [], "userChannelType": "PC",
                "articleSortType": "RANKING_DESC", "lastInfo": last_info,
            })
            items += result.get("list") or []
            self.pause()
            if not result.get("hasNextPage") or not result.get("lastInfo"):
                break
            last_info = result["lastInfo"]
        return items
