# 진단 결과

- 실행 시각: 2026-10-18 21:35 KST
- 단지번호: 3084
- 실행 환경 IP: {"ip":"183.99.10.163"}

## 0. 사이트별 접속 여부

네이버 전체가 막혔는지 부동산만 막혔는지, 대체 출처는 열리는지 확인합니다.

| 사이트 | 상태 | 걸린 시간 | 비고 |
|---|---|---|---|
| 네이버 메인 | 200 | 0.1s | https://www.naver.com/ |
| 네이버 검색 | 200 | 0.1s | https://search.naver.com/search.naver?query=%ED%8C%8C%ED%81% |
| 네이버 지도 | 200 | 0.1s | https://map.naver.com/p/ |
| land.naver.com | 200 | 0.1s | https://land.naver.com/ |
| new.land.naver.com | 200 | 0.1s | https://new.land.naver.com/404 |
| fin.land.naver.com | 200 | 0.2s | https://fin.land.naver.com/map?layer=NobwRAlgJmBcYAsD2BbApmA |
| KB부동산 | 200 | 0.1s | https://kbland.kr/ |
| KB부동산 API | 404 | 0.1s | HTTP 오류(서버는 응답함) |
| 직방 | 200 | 0.1s | https://www.zigbang.com/ |
| 직방 API | 403 | 0.2s | HTTP 오류(서버는 응답함) |
| 호갱노노 | 200 | 0.1s | https://hogangnono.com/ |
| 아실 | 200 | 0.1s | https://asil.kr/asil/index.jsp |
| 공공데이터포털 API | 400 | 0.0s | HTTP 오류(서버는 응답함) |
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

### https://fin.land.naver.com/complexes/3084

- 페이지 상태: 200, 최종 주소: https://fin.land.naver.com/map?layer=NobwRAlgJmBcYGMD2BbADgGwKYA8D6UWALgIYQZgA0YaJATiSgM5zjLrY4CSMsAzAAYAHABYAvtSZZ6CABY
- '^매매\s*\d+$' 클릭 실패: Locator.click: Timeout 4000ms exceeded.
Call log:
  - waiting for get_by_text(re
- '^매물$' 클릭 실패: Locator.click: Timeout 4000ms exceeded.
Call log:
  - waiting for get_by_text(re
- Authorization 헤더를 쓴 요청: 없음

| # | 방식 | 상태 | 크기 | 주소(쿼리 포함) | 내용 |
|---|---|---|---|---|---|
| 5 | POST | 204 | 0 | `/front-api/v1/telemetry` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 6 | GET | 200 | 0 | `/front-api/v1/auth/userInfo` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 7 | GET | 401 | 0 | `/front-api/v1/user/recentView?size=10&userChannelType=PC&page=0` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 8 | GET | 200 | 0 | `/front-api/v1/complex/myHouseAuthInfo?complexNumber=3084&count=2&needHoMarketPrice=true` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 9 | GET | 200 | 0 | `/front-api/v1/news/market-report/last-updated-date` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 10 | GET | 200 | 0 | `/front-api/v1/complex/asking-price?complexNumber=3084&pyeongTypeNumber=0&realEstateType=A01&tradeType=A1` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 11 | GET | 200 | 0 | `/front-api/v1/complex/marketPrice/recent?complexNumber=3084&pyeongTypeNumber=0&realEstateType=A01&cpList[]=kab&cpList[]=kbstar&cpList[]=neonet` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 12 | GET | 200 | 0 | `/front-api/v1/complex/v2/pyeong/realPrice?complexNumber=3084&tradeType=A1&pyeongTypeNumber=0&page=0&size=1` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 13 | GET | 200 | 0 | `/front-api/v1/complex/pyeongGroups?complexNumber=3084` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 14 | GET | 200 | 0 | `/front-api/v1/complex/pyeong/realPrice/list?complexNumber=3084&endDate=2026-10-18&pyeongTypeNumber=0&realEstateType=A01&startDate=2025-10-18&tradeType=A1` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 15 | GET | 200 | 0 | `/front-api/v1/complex/interior/portfolios/recommended/exists?complexNumber=3084` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 16 | GET | 200 | 0 | `/front-api/v1/complex/hoMarketPriceExist?complexNumber=3084` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 17 | GET | 200 | 0 | `/front-api/v1/complex/interior/portfolios/exists?complexNumber=3084` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 18 | GET | 200 | 0 | `/front-api/v1/complex/loan/kbPrice?complexNumber=3084&pyeongTypeNumberList[]=0` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 19 | GET | 200 | 0 | `/front-api/v1/complex/v2/pyeong/realPrice?complexNumber=3084&pyeongTypeNumber=0&page=0&size=3&tradeType=A1` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 20 | GET | 200 | 0 | `/front-api/v1/complex/pyeong/realPrice/summary?complexNumber=3084&pyeongTypeNumber=0&tradeType=A1&startDate=2026-07-18` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 21 | GET | 200 | 0 | `/front-api/v1/legalDivision/searchByCoordinate?longitude=126.98275426088257&latitude=37.566535&type=EUP` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 22 | GET | 200 | 0 | `/front-api/v1/realtor/existsInComplex?complexNumber=3084` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 23 | GET | 200 | 0 | `/front-api/v1/complex/marketPrice/list?complexNumber=3084&pyeongTypeNumber=0&startDate=2025-10-18&endDate=2026-10-18&realEstateType=A01&cpList[]=kab&cpList[]=kbstar&cpList[]=neonet` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 24 | GET | 200 | 0 | `/front-api/v1/loan/mortgage/partnerProduct?productTypes[]=LOAN-MORTGAGE` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 25 | GET | 200 | 0 | `/front-api/v1/complex/article/stats?complexNumber=3084` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 26 | GET | 200 | 0 | `/front-api/v1/realtor/advertisement?complexNumber=3084&advertisementRerankChannelType=property.complex.price&tradeTypes[]=A1&stmsId=100426651&url=/map?layer=NobwRAlgJmBcYGMD2BbADgGwKYA8D6UWALgIYQZgA0YaJATiSgM5zjLrY4CSMsA` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 27 | GET | 200 | 0 | `/front-api/v1/complex/marketPrice/list?complexNumber=3084&pyeongTypeNumber=0&startDate=2025-10-01&endDate=2026-10-18&cpList[]=kab&cpList[]=kbstar&cpList[]=neonet` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 28 | PUT | 401 | 0 | `/front-api/v1/complex/auth/mount` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 29 | POST | 401 | 0 | `/front-api/v1/user/recentView` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 30 | POST | 401 | 0 | `/front-api/v1/user/legalDivisionView` | 원문 없음 Response.body: Protocol error (Network.getResponseBody): No  |
| 34 | GET | 200 | 0 | `/front-api/v1/loan/mortgage/ltvInfo?loanPurpose=BUY&consumerCategory=ZERO_WITHOUT_FIRST_PURCHASE&legalDivisionNumber=4113510200&realEstateType=APT` | 원문 없음 Response.body: Target page, context or browser has been clos |

### 같은 API를 브라우저 없이 다시 호출

| # | 상태 | 크기 | 주소 | 내용 |
|---|---|---|---|---|
| 8 | 429 | 47 | `/front-api/v1/complex/myHouseAuthInfo` | keys=['detailCode', 'message'] |
| 9 | 429 | 47 | `/front-api/v1/news/market-report/last-updated-date` | keys=['detailCode', 'message'] |
| 10 | 429 | 47 | `/front-api/v1/complex/asking-price` | keys=['detailCode', 'message'] |
| 11 | 429 | 47 | `/front-api/v1/complex/marketPrice/recent` | keys=['detailCode', 'message'] |
| 12 | 429 | 47 | `/front-api/v1/complex/v2/pyeong/realPrice` | keys=['detailCode', 'message'] |
| 13 | 429 | 47 | `/front-api/v1/complex/pyeongGroups` | keys=['detailCode', 'message'] |
| 14 | 429 | 47 | `/front-api/v1/complex/pyeong/realPrice/list` | keys=['detailCode', 'message'] |
| 15 | 429 | 47 | `/front-api/v1/complex/interior/portfolios/recommended/exists` | keys=['detailCode', 'message'] |
| 16 | 429 | 47 | `/front-api/v1/complex/hoMarketPriceExist` | keys=['detailCode', 'message'] |
| 17 | 429 | 47 | `/front-api/v1/complex/interior/portfolios/exists` | keys=['detailCode', 'message'] |
| 18 | 429 | 47 | `/front-api/v1/complex/loan/kbPrice` | keys=['detailCode', 'message'] |
| 19 | 429 | 47 | `/front-api/v1/complex/v2/pyeong/realPrice` | keys=['detailCode', 'message'] |
| 20 | 429 | 47 | `/front-api/v1/complex/pyeong/realPrice/summary` | keys=['detailCode', 'message'] |
| 21 | 429 | 47 | `/front-api/v1/legalDivision/searchByCoordinate` | keys=['detailCode', 'message'] |
| 22 | 429 | 47 | `/front-api/v1/realtor/existsInComplex` | keys=['detailCode', 'message'] |
| 23 | 429 | 47 | `/front-api/v1/complex/marketPrice/list` | keys=['detailCode', 'message'] |
| 24 | 429 | 47 | `/front-api/v1/loan/mortgage/partnerProduct` | keys=['detailCode', 'message'] |
| 25 | 429 | 47 | `/front-api/v1/complex/article/stats` | keys=['detailCode', 'message'] |
| 26 | 429 | 47 | `/front-api/v1/realtor/advertisement` | keys=['detailCode', 'message'] |
| 27 | 429 | 47 | `/front-api/v1/complex/marketPrice/list` | keys=['detailCode', 'message'] |
| 34 | 429 | 47 | `/front-api/v1/loan/mortgage/ltvInfo` | keys=['detailCode', 'message'] |

## 3. 국토부 실거래 API

- MOLIT_API_KEY 시크릿이 없어 건너뜀

