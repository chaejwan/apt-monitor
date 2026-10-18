"""텔레그램 알림."""

import json
import urllib.request

ICONS = {"신규": "🆕", "삭제": "❌", "재등록": "🔁", "가격인상": "🔺", "가격인하": "🔻",
         "조건진입": "➕", "조건이탈": "➖"}


def fmt_price(manwon: int) -> str:
    """만원 단위 금액을 '26억 5,000' 처럼 표시합니다."""
    if not manwon:
        return "0"
    eok, rest = divmod(int(manwon), 10000)
    if not eok:
        return f"{rest:,}만"
    return f"{eok}억" + (f" {rest:,}" if rest else "")


def fmt_house_price(e: dict) -> str:
    text = fmt_price(e["price"])
    if e.get("tradeType") == "월세":
        text += f"/{e.get('rent', 0):,}"
    return text


def format_event(e: dict) -> str:
    line = (f"{ICONS.get(e['type'], '•')} {e['type']} {e['tradeType']} {e['area']} "
            f"{e['dong']}동 {e['floor']}층 {e['direction']} {fmt_house_price(e)}")
    if "before" in e:
        before = fmt_price(e["before"])
        if e.get("tradeType") == "월세":
            before += f"/{e.get('beforeRent', 0):,}"
        line += f" (← {before})"
    return line


def build_messages(events: list[dict], watches: list[dict], complex_names: dict) -> list[str]:
    """관심 조건별로 알림 메시지를 만듭니다. 알림을 끈 조건과 조건에 안 맞는 변화는 뺍니다."""
    messages = []
    for w in watches:
        if w.get("enabled") is False or w.get("notify") is False:
            continue
        mine = [e for e in events if w["id"] in e["watches"]]
        if not mine:
            continue
        name = complex_names.get(str(w["complexNo"]), w["complexNo"])
        lines = [f"🏠 {w.get('name') or name}"] + [format_event(e) for e in mine[:30]]
        if len(mine) > 30:
            lines.append(f"… 외 {len(mine) - 30}건")
        messages.append("\n".join(lines))
    return messages


def send_telegram(token: str, chat_id: str, text: str) -> None:
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=json.dumps({"chat_id": chat_id, "text": text, "disable_web_page_preview": True}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        resp.read()
