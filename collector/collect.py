"""관심 조건(config/watchlists.json)의 단지 매물을 수집하고, 변화 이력을 남기고, 텔레그램으로 알립니다.

사용법 (저장소 최상위에서):
    python -m collector.collect              # 수집 + 알림
    python -m collector.collect --no-notify  # 알림 없이 수집만
    python -m collector.collect --headed     # 브라우저 창을 띄워서 수집
"""

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

from . import listings, notify
from .naver import TRADE_CODES, NaverError, NaverLand

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "watchlists.json"
DATA = ROOT / "data"
ENV_FILE = ROOT / "laptop" / ".env"
PROFILE = ROOT / "laptop" / ".browser-profile"
KST = dt.timezone(dt.timedelta(hours=9))
COMPLEX_REFRESH_DAYS = 7


def log(msg: str) -> None:
    print(f"[{dt.datetime.now(KST):%H:%M:%S}] {msg}", flush=True)


def load_env() -> None:
    """laptop/.env 의 KEY=VALUE 줄을 환경변수로 읽습니다 (저장소에는 올리지 않는 파일)."""
    if not ENV_FILE.exists():
        return
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def read_json(path: Path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def needed_trade_types(watches: list[dict]) -> list[str]:
    """단지의 관심 조건들이 보는 거래유형. 거래유형을 정하지 않은 조건이 있으면 전부 받습니다."""
    types: set[str] = set()
    for w in watches:
        if not w.get("tradeTypes"):
            return list(TRADE_CODES)
        types.update(w["tradeTypes"])
    return [t for t in TRADE_CODES if t in types]


def collect_complex(nv: NaverLand, complex_no: str, watches: list[dict], ts: str) -> tuple[list[dict], dict]:
    info_path = DATA / "complexes" / f"{complex_no}.json"
    info = read_json(info_path, None)
    fresh = info and dt.datetime.fromisoformat(info["fetchedAt"]) > dt.datetime.now(KST) - dt.timedelta(
        days=COMPLEX_REFRESH_DAYS)
    if not fresh:
        log(f"  단지 정보 갱신")
        info = {**nv.complex_info(complex_no), "complexNo": complex_no, "fetchedAt": ts}
        write_json(info_path, info)

    stats = nv.article_stats(complex_no)
    nv.pause()
    houses: list[dict] = []
    fetched: set[str] = set()
    status = {"name": info.get("name"), "stats": stats.get("count"), "fetched": {}, "errors": []}
    for trade in needed_trade_types(watches):
        try:
            items = nv.articles(complex_no, TRADE_CODES[trade])
        except NaverError as e:
            status["errors"].append(f"{trade}: {e}")
            log(f"  {trade} 목록 실패: {e}")
            continue
        got = [listings.to_house(it) for it in items]
        houses += got
        fetched.add(trade)
        status["fetched"][trade] = len(got)
        log(f"  {trade} {len(got)}집 (매물 {sum(len(h['articles']) for h in got)}건)")

    state_path = DATA / "listings" / f"{complex_no}.json"
    state = read_json(state_path, {"complexNo": complex_no})
    events = listings.update(state, houses, fetched, ts, watches)
    state["updated"] = ts
    write_json(state_path, state)
    return events, status


def append_events(events: list[dict], ts: str) -> None:
    if not events:
        return
    path = DATA / "events" / f"{ts[:7]}.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        for e in events:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-notify", action="store_true")
    ap.add_argument("--headed", action="store_true")
    args = ap.parse_args()
    load_env()

    watches = [w for w in read_json(CONFIG, {"watches": []})["watches"] if w.get("enabled", True)]
    by_complex: dict[str, list[dict]] = {}
    for w in watches:
        by_complex.setdefault(str(w["complexNo"]), []).append(w)
    if not by_complex:
        log("관심 조건이 없습니다. config/watchlists.json 을 확인하세요.")
        return 1

    ts = dt.datetime.now(KST).isoformat(timespec="seconds")
    all_events: list[dict] = []
    run = {"ts": ts, "complexes": {}}
    try:
        with NaverLand(PROFILE, headless=not args.headed, log=log) as nv:
            for complex_no, ws in by_complex.items():
                log(f"단지 {complex_no} 수집")
                try:
                    events, status = collect_complex(nv, complex_no, ws, ts)
                except NaverError as e:
                    log(f"  실패: {e}")
                    run["complexes"][complex_no] = {"errors": [str(e)]}
                    continue
                all_events += events
                run["complexes"][complex_no] = {**status, "events": len(events)}
    except NaverError as e:
        log(f"네이버 접속 실패: {e}")
        run["error"] = str(e)

    append_events(all_events, ts)
    write_json(DATA / "status.json", run)
    log(f"변화 {len(all_events)}건")

    names = {no: (s.get("name") or no) for no, s in run["complexes"].items()}
    messages = notify.build_messages(all_events, watches, names)
    token, chat = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    for text in messages:
        if args.no_notify or not (token and chat):
            print("--- 알림(보내지 않음) ---\n" + text)
            continue
        try:
            notify.send_telegram(token, chat, text)
        except Exception as e:
            log(f"텔레그램 전송 실패: {e}")

    ok = any(not s.get("errors") for s in run["complexes"].values())
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
