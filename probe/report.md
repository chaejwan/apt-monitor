# 진단 결과

- 실행 시각: 2026-10-18 22:42 KST
- 단지번호: 3084
- 실행 환경 IP: {"ip":"183.99.10.163"}

## 0. 사이트별 접속 여부

네이버 전체가 막혔는지 부동산만 막혔는지, 대체 출처는 열리는지 확인합니다.

| 사이트 | 상태 | 걸린 시간 | 비고 |
|---|---|---|---|
| 네이버 메인 | 200 | 0.1s | https://www.naver.com/ |
| 네이버 검색 | 200 | 0.1s | https://search.naver.com/search.naver?query=%ED%8C%8C%ED%81% |
| 네이버 지도 | 200 | 0.1s | https://map.naver.com/p/ |
| land.naver.com | 200 | 1.0s | https://land.naver.com/ |
| new.land.naver.com | 200 | 0.2s | https://new.land.naver.com/404 |
| fin.land.naver.com | 200 | 0.2s | https://fin.land.naver.com/map?layer=NobwRAlgJmBcYAsD2BbApmA |
| KB부동산 | 200 | 0.1s | https://kbland.kr/ |
| KB부동산 API | 404 | 0.1s | HTTP 오류(서버는 응답함) |
| 직방 | 200 | 0.1s | https://www.zigbang.com/ |
| 직방 API | 403 | 0.2s | HTTP 오류(서버는 응답함) |
| 호갱노노 | 200 | 0.1s | https://hogangnono.com/ |
| 아실 | 200 | 0.1s | https://asil.kr/asil/index.jsp |
| 공공데이터포털 API | 400 | 0.1s | HTTP 오류(서버는 응답함) |
| 카카오 API | 404 | 0.1s | HTTP 오류(서버는 응답함) |

## 1. HTTP 직접 요청

| 확인 항목 | 상태 | 크기 | 내용 | 원문 |
|---|---|---|---|---|
| new.land 단지 페이지 | 200 | 7203 | text: <!DOCTYPE html> <html lang="ko"> <head> <meta charset="utf-8"> <title>네이버 :: 세상의 모든 지식, 네이버</title> <style type="text/cs | probe\samples\http_new.land_단지_페이지.txt |
| new.land 단지 API | 429 | 76 | keys=['success', 'code', 'message'] | probe\samples\http_new.land_단지_API.txt |
| new.land 매물 API | 429 | 76 | keys=['success', 'code', 'message'] | probe\samples\http_new.land_매물_API.txt |
| m.land 매물 목록 | 200 | 4 | JSON 값: None | probe\samples\http_m.land_매물_목록.txt |
| fin.land 단지 페이지 | 200 | 154309 | text: <!DOCTYPE html><html lang="ko" data-sentry-component="RootLayout" data-sentry-source-file="layout.tsx"><head><meta charS | probe\samples\http_fin.land_단지_페이지.txt |

- 페이지 HTML에서 찾은 JWT 토큰: 없음

## 2. 브라우저 렌더링 중 오간 JSON 응답

- 브라우저: 설치된 Chrome
- 지도 페이지 상태: 200
- 3초 뒤 주소: https://fin.land.naver.com/map?tradeTypes=A1-B1&realEstateTypes=A01-A04-B01&layer=NobwRAlgJmBcYGMD2BbADgGwKYA8
- 8초 뒤 주소: https://fin.land.naver.com/map?tradeTypes=A1-B1&realEstateTypes=A01-A04-B01&layer=NobwRAlgJmBcYGMD2BbADgGwKYA8
- 404로 넘어갔는지: 아니오(정상)

- 매물 탭 클릭 성공 → https://fin.land.naver.com/map?center=3znqmb-2ADRJg&zoom=15&tradeTypes=A1-B1&realEstateTypes=A01-A04-B01&layer

### 페이지 안에서 직접 부른 API

| 상태 | 크기 | 주소 | 내용 | 원문 |
|---|---|---|---|---|
| 200 | 400 | `/front-api/v1/complex/article/stats?complexNumber=3084` | keys=['isSuccess', 'detailCode', 'message', 'result'], result keys=['count', 'price'] 목록={} | probe\samples\inpage_0.json |
| 200 | 9284 | `/front-api/v1/complex/pyeongList?complexNumber=3084` | keys=['isSuccess', 'detailCode', 'message', 'result'], result 13건 | probe\samples\inpage_1.json |
| 200 | 2991 | `/front-api/v1/complex/pyeongGroups?complexNumber=3084` | keys=['isSuccess', 'detailCode', 'message', 'result'], result 10건 | probe\samples\inpage_2.json |
| 200 | 66 | `/front-api/v1/complex/asking-price?complexNumber=3084&pyeongTypeNumber=0&realEstateType=A01&tradeType=A1` | keys=['isSuccess', 'detailCode', 'message', 'result'], result keys=[] 목록={} | probe\samples\inpage_3.json |
| 200 | 1112 | `/front-api/v1/complex?complexNumber=3084` | keys=['isSuccess', 'detailCode', 'message', 'result'], result keys=['name', 'type', 'address', 'coordinates', 'totalHouseholdNumber', 'lease | probe\samples\inpage_4.json |
| 200 | 4025 | `/front-api/v1/complex/buildingList?complexNumber=3084` | keys=['isSuccess', 'detailCode', 'message', 'result'], result 41건 | probe\samples\inpage_5.json |
| 200 | 1292 | `/front-api/v1/complex/mapComplexSummaryInfo?complexNumber=3084` | keys=['isSuccess', 'detailCode', 'message', 'result'], result keys=['complexInfo', 'articlePriceInfoDto', 'articleCountInfoDto', 'totalComme | probe\samples\inpage_6.json |

### 화면이 POST로 부른 API를 같은 본문으로 다시 호출

| 상태 | 크기 | 주소 | 요청 본문 | 내용 | 원문 |
|---|---|---|---|---|---|
| 200 | 16701 | `/front-api/v1/complex/complexClusters` | `{"filter":{"tradeTypes":["A1","B1"],"realEstateTypes":["A01","A04","B01"],"roomCount":[],"bathRoomCount":[],"optionTypes":[],"oneRoomShapeTypes":[],"moveInTypes":[],"filtersExclusiveSpace":false,"floorTypes":[],"directionTypes":[],"hasArticlePhoto":false,"isAuthorizedByOwner":false,"parkingTypes":[]` | keys=['isSuccess', 'detailCode', 'message', 'result'], result keys=['totalCount', 'clusters', 'points'] 목록={'clusters': 36, 'points': 0} | probe\samples\post_0.json |
| 200 | 122 | `/front-api/v1/article/boundedArticlesCount` | `{"filter":{"tradeTypes":["A1","B1"],"realEstateTypes":["A01","A04","B01"],"roomCount":[],"bathRoomCount":[],"optionTypes":[],"oneRoomShapeTypes":[],"moveInTypes":[],"filtersExclusiveSpace":false,"floorTypes":[],"directionTypes":[],"hasArticlePhoto":false,"isAuthorizedByOwner":false,"parkingTypes":[]` | keys=['isSuccess', 'detailCode', 'message', 'result'], result keys=['seed', 'hasNextPage', 'totalCount', 'list'] 목록={'list': 0} | probe\samples\post_1.json |
| 200 | 6553 | `/front-api/v1/article/map/articleClusters` | `{"filter":{"tradeTypes":["A1","B1"],"realEstateTypes":["A01","A04","B01"],"roomCount":[],"bathRoomCount":[],"optionTypes":[],"oneRoomShapeTypes":[],"moveInTypes":[],"filtersExclusiveSpace":false,"floorTypes":[],"directionTypes":[],"hasArticlePhoto":false,"isAuthorizedByOwner":false,"parkingTypes":[]` | keys=['isSuccess', 'detailCode', 'message', 'result'], result keys=['totalCount', 'clusters'] 목록={'clusters': 51} | probe\samples\post_2.json |
| 200 | 30 | `/front-api/v1/preSale/pinExposure` | `{"boundingBox":{"left":127.10179360568259,"right":127.12883027255265,"top":37.378636717987035,"bottom":37.36438060471119},"userChannelType":"PC"}` | keys=['isSuccess', 'result'], result 0건 | probe\samples\post_3.json |
| 200 | 419136 | `/front-api/v1/complex/article/list` | `{"size":30,"complexNumber":3084,"tradeTypes":["A1"],"pyeongTypes":[],"dongNumbers":[],"userChannelType":"PC","articleSortType":"RANKING_DESC","lastInfo":[]}` | keys=['isSuccess', 'detailCode', 'message', 'result'], result keys=['seed', 'lastInfo', 'hasNextPage', 'totalCount', 'list'] 목록={'lastInfo': | probe\samples\post_4.json |

### 화면이 스스로 부른 API (주소만)

- GET 200 `/front-api/v1/auth/userInfo`
- GET 200 `/front-api/v1/complex/myHouseAuthInfo?complexNumber=3084&count=2&needHoMarketPrice=true`
- PUT 200 `/front-api/v1/complex/auth/mount`
- GET 200 `/front-api/v1/complex/pyeongGroups?complexNumber=3084`
- GET 200 `/front-api/v1/complex/interior/portfolios/exists?complexNumber=3084`
- GET 200 `/front-api/v1/complex/pyeongList?complexNumber=3084`
- GET 200 `/front-api/v1/complex/v2/pyeong/realPrice?complexNumber=3084&tradeType=A1&pyeongTypeNumber=0&page=0&size=1`
- GET 200 `/front-api/v1/complex/marketPrice/recent?complexNumber=3084&pyeongTypeNumber=0&realEstateType=A01&cpList[]=kab&cpList[]=kbstar&cpList[]=neonet`
- GET 200 `/front-api/v1/complex/interior/portfolios/recommended/exists?complexNumber=3084`
- GET 200 `/front-api/v1/complex/pyeong/realPrice/summary?complexNumber=3084&pyeongTypeNumber=0&tradeType=A1&startDate=2026-07-18`
- GET 200 `/front-api/v1/complex/pyeong/realPrice/list?complexNumber=3084&endDate=2026-10-18&pyeongTypeNumber=0&realEstateType=A01&startDate=2025-10-18&tradeType=A1`
- GET 200 `/front-api/v1/complex/marketPrice/list?complexNumber=3084&pyeongTypeNumber=0&startDate=2025-10-18&endDate=2026-10-18&realEstateType=A01&cpList[]=kab&cpList[]=kbstar&cpList[]=neonet`
- GET 200 `/front-api/v1/news/market-report/last-updated-date`
- GET 200 `/front-api/v1/realtor/existsInComplex?complexNumber=3084`
- GET 200 `/front-api/v1/complex/v2/pyeong/realPrice?complexNumber=3084&pyeongTypeNumber=0&page=0&size=3&tradeType=A1`
- GET 200 `/front-api/v1/complex/article/stats?complexNumber=3084`
- GET 200 `/front-api/v1/complex/asking-price?complexNumber=3084&pyeongTypeNumber=0&realEstateType=A01&tradeType=A1`
- GET 200 `/front-api/v1/complex/loan/kbPrice?complexNumber=3084&pyeongTypeNumberList[]=0`
- GET 200 `/front-api/v1/loan/mortgage/partnerProduct?productTypes[]=LOAN-MORTGAGE`
- GET 200 `/front-api/v1/complex/hoMarketPriceExist?complexNumber=3084`
- POST 200 `/front-api/v1/user/recentView`
- GET 200 `/front-api/v1/loan/mortgage/ltvInfo?loanPurpose=BUY&consumerCategory=ZERO_WITHOUT_FIRST_PURCHASE&legalDivisionNumber=4113510200&realEstateType=APT`
- GET 200 `/front-api/v1/complex/marketPrice/list?complexNumber=3084&pyeongTypeNumber=0&startDate=2025-10-01&endDate=2026-10-18&cpList[]=kab&cpList[]=kbstar&cpList[]=neonet`
- GET 200 `/front-api/v1/realtor/advertisement?complexNumber=3084&advertisementRerankChannelType=property.complex.price&tradeTypes[]=A1&stmsId=100426651&url=/map?tradeTypes=A1-B1&realEstateTypes=A01-A04-B01&laye`
- GET 200 `/front-api/v1/legalDivision/searchByCoordinate?longitude=127.12009696088256&latitude=37.371509&type=EUP`
- GET 200 `/front-api/v1/user/recentView?size=10&userChannelType=PC&page=0`
- POST 200 `/front-api/v1/user/legalDivisionView`
- GET 200 `/front-api/v1/complex/marketPrice/recent?complexNumber=3084&pyeongTypeNumber=6&realEstateType=A01&cpList[]=kab&cpList[]=kbstar&cpList[]=neonet`
- GET 200 `/front-api/v1/complex/v2/pyeong/realPrice?complexNumber=3084&pyeongTypeNumber=6&page=0&size=3&tradeType=A1`
- GET 200 `/front-api/v1/complex/pyeong/realPrice/summary?complexNumber=3084&pyeongTypeNumber=6&tradeType=A1&startDate=2026-07-18`
- GET 200 `/front-api/v1/complex/v2/pyeong/realPrice?complexNumber=3084&tradeType=A1&pyeongTypeNumber=6&page=0&size=1`
- GET 200 `/front-api/v1/complex/pyeong/realPrice/list?complexNumber=3084&endDate=2026-10-18&pyeongTypeNumber=6&realEstateType=A01&startDate=2025-10-18&tradeType=A1`
- GET 200 `/front-api/v1/complex/marketPrice/list?complexNumber=3084&pyeongTypeNumber=6&startDate=2025-10-01&endDate=2026-10-18&cpList[]=kab&cpList[]=kbstar&cpList[]=neonet`
- GET 200 `/front-api/v1/complex/marketPrice/list?complexNumber=3084&pyeongTypeNumber=6&startDate=2025-10-18&endDate=2026-10-18&realEstateType=A01&cpList[]=kab&cpList[]=kbstar&cpList[]=neonet`
- GET 200 `/front-api/v1/complex/asking-price?complexNumber=3084&pyeongTypeNumber=6&realEstateType=A01&tradeType=A1`
- GET 200 `/front-api/v1/complex/pyeong/realPrice/summary?complexNumber=3084&pyeongTypeNumber=6&tradeType=A1&startDate=2023-10-18`
- GET 200 `/front-api/v1/complex/loan/kbPrice?complexNumber=3084&pyeongTypeNumberList[]=6`
- GET 200 `/front-api/v1/complex/vr/representativeSameType?pyeongTypeNumber=6&complexNumber=3084`
- GET 200 `/front-api/v1/complex/pyeongPrice/pyeongType?complexNumber=3084&pyeongTypeNumber=6&tradeType=A1`
- GET 200 `/front-api/v1/complex/mapComplexSummaryInfo?complexNumber=3084`
- GET 200 `/front-api/v1/data-service/banner/propertyCommon?typeId=102`
- POST 200 `/front-api/v1/preSale/pinExposure`
- POST 200 `/front-api/v1/article/boundedArticlesCount`
- POST 200 `/front-api/v1/complex/complexClusters`
- POST 200 `/front-api/v1/article/map/articleClusters`
- GET 200 `/front-api/v1/complex/buildingList?complexNumber=3084`
- POST 200 `/front-api/v1/complex/article/list`
- GET 200 `/front-api/v1/preSale/legalDivisionPromotion?legalDivisionNumber=4113510200&userChannelType=PC`
- GET 200 `/front-api/v1/complex/article/stats?complexNumber=3084`
- GET 200 `/front-api/v1/complex/pyeongList?complexNumber=3084`
- GET 200 `/front-api/v1/complex/pyeongGroups?complexNumber=3084`
- GET 200 `/front-api/v1/complex/asking-price?complexNumber=3084&pyeongTypeNumber=0&realEstateType=A01&tradeType=A1`
- GET 200 `/front-api/v1/complex?complexNumber=3084`
- GET 200 `/front-api/v1/complex/buildingList?complexNumber=3084`
- GET 200 `/front-api/v1/complex/mapComplexSummaryInfo?complexNumber=3084`
- POST 200 `/front-api/v1/complex/complexClusters`
- POST 200 `/front-api/v1/article/boundedArticlesCount`
- POST 200 `/front-api/v1/article/map/articleClusters`
- POST 200 `/front-api/v1/preSale/pinExposure`
- POST 200 `/front-api/v1/complex/article/list`

## 3. 국토부 실거래 API

- MOLIT_API_KEY 시크릿이 없어 건너뜀

