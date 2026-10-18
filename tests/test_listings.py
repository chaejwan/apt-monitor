import unittest

from collector import listings, notify


def item(numbers, price, dong="107", floor="16/21", area="124B", trade="A1", feature="", rent=0):
    """네이버 목록 항목 모양을 흉내 냅니다 (가격은 원 단위)."""
    target, total = floor.split("/")
    rep = {
        "articleNumber": numbers[0], "dongName": dong, "tradeType": trade,
        "spaceInfo": {"supplySpaceName": area, "supplySpace": 124.58, "exclusiveSpace": 101.91},
        "articleDetail": {"direction": "ES", "articleFeatureDescription": feature, "floorInfo": floor,
                          "floorDetailInfo": {"targetFloor": target, "totalFloor": total}},
        "verificationInfo": {"articleConfirmDate": "2026-10-17"},
        "brokerInfo": {"brokerageName": "제일공인중개사사무소"},
        "address": {"coordinates": {"xCoordinate": 127.12, "yCoordinate": 37.37}},
        "priceInfo": {"dealPrice": price if trade == "A1" else 0,
                      "warrantyPrice": price if trade != "A1" else 0, "rentPrice": rent},
    }
    out = {"representativeArticleInfo": rep}
    if len(numbers) > 1:
        out["duplicatedArticleInfo"] = {
            "realtorCount": len(numbers),
            "articleInfoList": [{**rep, "articleNumber": n} for n in numbers],
            "representativePriceInfo": {"dealPrice": {"minPrice": price if trade == "A1" else 0}},
        }
    return out


def houses(*items):
    return [listings.to_house(i) for i in items]


WATCH_ALL = {"id": "all", "complexNo": "3084"}


class ToHouseTest(unittest.TestCase):
    def test_group_and_units(self):
        h = listings.to_house(item(["2", "1"], 2_600_000_000))
        self.assertEqual(h["articles"], ["1", "2"])
        self.assertEqual(h["price"], 260000)
        self.assertEqual(h["direction"], "남동향")
        self.assertEqual(h["tradeType"], "매매")


class MatchTest(unittest.TestCase):
    def test_conditions(self):
        h = listings.to_house(item(["1"], 2_600_000_000, floor="3/21", feature="올수리 남향"))
        self.assertTrue(listings.matches(WATCH_ALL, h))
        self.assertFalse(listings.matches({"tradeTypes": ["전세"]}, h))
        self.assertFalse(listings.matches({"areas": ["105"]}, h))
        self.assertFalse(listings.matches({"price": {"매매": [None, 250000]}}, h))
        self.assertTrue(listings.matches({"price": {"매매": [250000, None]}}, h))
        self.assertFalse(listings.matches({"floor": {"excludeLow": 3}}, h))
        self.assertTrue(listings.matches({"floor": {"excludeLow": 2}}, h))
        self.assertFalse(listings.matches({"keywords": {"exclude": ["올수리"]}}, h))
        self.assertTrue(listings.matches({"keywords": {"include": ["세안고", "올수리"]}}, h))
        self.assertFalse(listings.matches({"directions": ["남향"]}, h))


class UpdateTest(unittest.TestCase):
    def run_once(self, state, *items, fetched=("매매",), ts="t"):
        return listings.update(state, houses(*items), set(fetched), ts, [WATCH_ALL])

    def test_first_run_is_baseline(self):
        state = {"complexNo": "3084"}
        self.assertEqual(self.run_once(state, item(["1"], 100)), [])
        self.assertEqual(len(state["houses"]), 1)

    def test_new_price_and_removal(self):
        state = {"complexNo": "3084"}
        self.run_once(state, item(["1"], 2_600_000_000), item(["2"], 2_000_000_000), ts="t1")
        # 다른 중개사가 같은 집을 올려 묶음이 바뀌고 가격이 내려감, 새 집 하나 등장, 2번 집은 한 번 안 보임
        events = self.run_once(state, item(["9", "1"], 2_500_000_000), item(["3"], 1_000_000_000), ts="t2")
        kinds = sorted(e["type"] for e in events)
        self.assertEqual(kinds, ["가격인하", "신규"])
        down = next(e for e in events if e["type"] == "가격인하")
        self.assertEqual((down["before"], down["price"]), (260000, 250000))
        self.assertEqual(down["watches"], ["all"])
        # 2번 집이 두 번 연속 안 보이면 삭제
        events = self.run_once(state, item(["1"], 2_500_000_000), item(["3"], 1_000_000_000), ts="t3")
        self.assertEqual([e["type"] for e in events], ["삭제"])
        # 다시 나타나면 재등록
        events = self.run_once(state, item(["1"], 2_500_000_000), item(["3"], 1_000_000_000),
                               item(["2"], 2_000_000_000), ts="t4")
        self.assertEqual([e["type"] for e in events], ["재등록"])

    def test_unfetched_trade_type_is_not_removed(self):
        state = {"complexNo": "3084"}
        self.run_once(state, item(["1"], 100), item(["5"], 100, trade="B1"), fetched=("매매", "전세"))
        for _ in range(3):
            events = self.run_once(state, item(["1"], 100), fetched=("매매",))
        self.assertEqual(events, [])
        self.assertEqual(state["houses"]["5"]["status"], "active")

    def test_condition_enter_on_price_drop(self):
        watch = {"id": "cheap", "price": {"매매": [None, 250000]}}
        state = {"complexNo": "3084"}
        listings.update(state, houses(item(["1"], 2_600_000_000)), {"매매"}, "t1", [watch])
        events = listings.update(state, houses(item(["1"], 2_450_000_000)), {"매매"}, "t2", [watch])
        self.assertEqual([e["type"] for e in events], ["가격인하", "조건진입"])


class NotifyTest(unittest.TestCase):
    def test_price_format(self):
        self.assertEqual(notify.fmt_price(265000), "26억 5,000")
        self.assertEqual(notify.fmt_price(260000), "26억")
        self.assertEqual(notify.fmt_price(9500), "9,500만")

    def test_messages_only_for_watched(self):
        e = {"type": "신규", "tradeType": "매매", "area": "124B", "dong": "107", "floor": "16/21",
             "direction": "남동향", "price": 260000, "rent": 0, "watches": ["w1"]}
        msgs = notify.build_messages([e], [{"id": "w1", "name": "파크타운", "complexNo": "3084"},
                                           {"id": "w2", "complexNo": "3084"}], {})
        self.assertEqual(len(msgs), 1)
        self.assertIn("🆕 신규 매매 124B 107동 16/21층 남동향 26억", msgs[0])


if __name__ == "__main__":
    unittest.main()
