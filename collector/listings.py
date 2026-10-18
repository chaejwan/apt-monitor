"""매물 정리(집 단위로 묶기), 관심 조건 판정, 이전 수집과의 비교.

- 네이버는 같은 집을 여러 중개사가 올린 매물을 한 묶음(duplicatedArticleInfo)으로 줍니다.
  이 묶음을 '집' 하나로 보고, 묶음 안 매물번호가 하나라도 겹치면 이전 수집의 같은 집으로 봅니다.
- 가격은 묶음 안 최저가(만원)를 씁니다. 대표 매물이 바뀌어도 가짜 가격 변동이 생기지 않게 하기 위해서입니다.
- 삭제는 두 번 연속 보이지 않을 때만 판정합니다.
"""

TRADE_NAMES = {"A1": "매매", "B1": "전세", "B2": "월세", "B3": "단기임대"}
DIRECTIONS = {
    "SS": "남향", "NN": "북향", "EE": "동향", "WW": "서향",
    "ES": "남동향", "WS": "남서향", "EN": "북동향", "WN": "북서향",
}
REMOVE_AFTER_MISSES = 2


def _won_to_manwon(value) -> int:
    return int(value or 0) // 10000


def to_house(item: dict) -> dict:
    """네이버 목록 항목 하나를 집 하나로 정리합니다."""
    rep = item["representativeArticleInfo"]
    dup = item.get("duplicatedArticleInfo") or {}
    group = dup.get("articleInfoList") or [rep]
    numbers = sorted({a["articleNumber"] for a in group} | {rep["articleNumber"]})

    trade = TRADE_NAMES.get(rep.get("tradeType"), rep.get("tradeType"))
    price_info = rep.get("priceInfo") or {}
    group_price = dup.get("representativePriceInfo") or {}

    def lowest(field: str) -> int:
        rng = group_price.get(field) or {}
        return _won_to_manwon(rng.get("minPrice") if rng.get("minPrice") else price_info.get(field))

    detail = rep.get("articleDetail") or {}
    floor = detail.get("floorDetailInfo") or {}
    space = rep.get("spaceInfo") or {}
    coords = (rep.get("address") or {}).get("coordinates") or {}
    return {
        "articles": numbers,
        "rep": rep["articleNumber"],
        "tradeType": trade,
        "dong": rep.get("dongName") or "",
        "floor": detail.get("floorInfo") or "",
        "targetFloor": floor.get("targetFloor") or "",
        "totalFloor": floor.get("totalFloor") or "",
        "direction": DIRECTIONS.get(detail.get("direction"), detail.get("direction") or ""),
        "area": space.get("supplySpaceName") or "",
        "supply": space.get("supplySpace"),
        "exclusive": space.get("exclusiveSpace"),
        # 매매는 매매가, 전세·월세는 보증금
        "price": lowest("dealPrice") if trade == "매매" else lowest("warrantyPrice"),
        "rent": lowest("rentPrice") if trade == "월세" else 0,
        "managementFee": _won_to_manwon(price_info.get("managementFeeAmount")),
        "feature": detail.get("articleFeatureDescription") or "",
        "confirmed": (rep.get("verificationInfo") or {}).get("articleConfirmDate") or "",
        "realtors": dup.get("realtorCount") or 1,
        "broker": (rep.get("brokerInfo") or {}).get("brokerageName") or "",
        "lat": coords.get("yCoordinate"),
        "lng": coords.get("xCoordinate"),
    }


def matches(watch: dict, house: dict) -> bool:
    """관심 조건 하나에 집이 맞는지 판정합니다. 비어 있는 조건은 제한 없음으로 봅니다."""
    if watch.get("enabled") is False:
        return False
    if watch.get("tradeTypes") and house["tradeType"] not in watch["tradeTypes"]:
        return False
    if watch.get("areas") and house["area"] not in watch["areas"]:
        return False
    low, high = (watch.get("price") or {}).get(house["tradeType"]) or (None, None)
    if low is not None and house["price"] < low:
        return False
    if high is not None and house["price"] > high:
        return False
    if house["tradeType"] == "월세" and watch.get("rentMax") is not None and house["rent"] > watch["rentMax"]:
        return False

    floor_rule = watch.get("floor") or {}
    target, total = house["targetFloor"], house["totalFloor"]
    if floor_rule.get("excludeLow"):
        # 층이 '저/중/고'로만 나오는 매물도 있습니다.
        if target == "저" or (target.isdigit() and int(target) <= floor_rule["excludeLow"]):
            return False
    if floor_rule.get("excludeTop") and target.isdigit() and target == total:
        return False

    if watch.get("directions") and house["direction"] not in watch["directions"]:
        return False
    if watch.get("dongs") and house["dong"] not in watch["dongs"]:
        return False
    keywords = watch.get("keywords") or {}
    if keywords.get("include") and not any(k in house["feature"] for k in keywords["include"]):
        return False
    if any(k in house["feature"] for k in keywords.get("exclude") or []):
        return False
    return True


def matching_watches(watches: list[dict], house: dict) -> list[str]:
    return [w["id"] for w in watches if matches(w, house)]


def _summary(house: dict) -> dict:
    keys = ("tradeType", "dong", "floor", "direction", "area", "price", "rent")
    return {k: house.get(k) for k in keys}


def update(state: dict, houses: list[dict], fetched_types: set[str], ts: str,
           watches: list[dict]) -> list[dict]:
    """이번 수집 결과로 상태를 갱신하고 변화 이력(이벤트) 목록을 돌려줍니다.

    fetched_types: 이번에 목록을 제대로 받은 거래유형. 받지 못한 유형의 집은 삭제로 보지 않습니다.
    처음 수집하는 단지는 기준만 잡고 이벤트를 만들지 않습니다.
    """
    stored: dict = state.setdefault("houses", {})
    baseline = not stored
    events: list[dict] = []
    owner = {num: hid for hid, h in stored.items() for num in h["articles"]}
    seen: set[str] = set()

    def event(kind: str, house: dict, watch_ids: list[str], **extra) -> None:
        if not baseline:
            events.append({"ts": ts, "complexNo": state.get("complexNo"), "type": kind,
                           "house": house["id"], "watches": watch_ids, **_summary(house), **extra})

    for cur in houses:
        hid = next((owner[n] for n in cur["articles"] if n in owner and owner[n] not in seen), None)
        if hid is None:
            hid = cur["rep"]
            while hid in stored:  # 드물게 이전 집 id와 겹치면 새 id를 만듭니다
                hid += "+"
            new = {**cur, "id": hid, "firstSeen": ts, "lastSeen": ts, "missing": 0,
                   "status": "active", "priceHistory": [[ts, cur["price"], cur["rent"]]]}
            stored[hid] = new
            event("신규", new, matching_watches(watches, new))
        else:
            old = stored[hid]
            before_watches = set(matching_watches(watches, old))
            was_removed = old["status"] == "removed"
            changed = (cur["price"], cur["rent"]) != (old["price"], old["rent"])
            before_price, before_rent = old["price"], old["rent"]
            old.update(cur, id=hid, lastSeen=ts, missing=0, status="active")
            old.pop("removedAt", None)
            now_watches = matching_watches(watches, old)
            if changed:
                old["priceHistory"].append([ts, cur["price"], cur["rent"]])
            if was_removed:
                event("재등록", old, now_watches)
            elif changed:
                up = (cur["price"], cur["rent"]) > (before_price, before_rent)
                event("가격인상" if up else "가격인하", old, sorted(before_watches | set(now_watches)),
                      before=before_price, beforeRent=before_rent)
                for wid in sorted(set(now_watches) - before_watches):
                    event("조건진입", old, [wid])
                for wid in sorted(before_watches - set(now_watches)):
                    event("조건이탈", old, [wid])
        seen.add(hid)

    for hid, old in stored.items():
        if hid in seen or old["status"] != "active" or old["tradeType"] not in fetched_types:
            continue
        old["missing"] = old.get("missing", 0) + 1
        if old["missing"] >= REMOVE_AFTER_MISSES:
            old["status"] = "removed"
            old["removedAt"] = ts
            event("삭제", old, matching_watches(watches, old))
    return events
