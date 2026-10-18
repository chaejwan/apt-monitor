# 진단 결과

- 실행 시각: 2026-10-18 21:28 KST
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

### https://fin.land.naver.com/complexes/3084

- 페이지 상태: 200, 최종 주소: https://fin.land.naver.com/map?layer=NobwRAlgJmBcYGMD2BbADgGwKYA8D6UWALgIYQZgA0YaJATiSgM5zjLrY4CSMsAzAAYAHABYAvtSZZ6CABYAFeoxaxwpAEZwwRBgDsmJBEQhJdYMWIC6QA
- Authorization 헤더를 쓴 요청: 없음

| 방식 | 상태 | 크기 | 주소 | 내용 |
|---|---|---|---|---|
| POST | 200 | 2 | `https://sentry-fin.naver.com/api/76/envelope/` | keys=[] |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/auth/userInfo` | JSON 파싱 실패 |
| GET | 401 | 0 | `https://fin.land.naver.com/front-api/v1/user/recentView` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/news/market-report/last-updated-date` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/pyeongGroups` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/asking-price` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/interior/portfolios/recommended/exists` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/realtor/existsInComplex` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/myHouseAuthInfo` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/interior/portfolios/exists` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/article/stats` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/pyeongList` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/v2/pyeong/realPrice` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/pyeong/realPrice/summary` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/v2/pyeong/realPrice` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/hoMarketPriceExist` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/marketPrice/list` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/loan/mortgage/ltvInfo` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/pyeong/realPrice/list` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/loan/mortgage/partnerProduct` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/marketPrice/recent` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/realtor/advertisement` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/marketPrice/list` | JSON 파싱 실패 |
| PUT | 401 | 0 | `https://fin.land.naver.com/front-api/v1/complex/auth/mount` | JSON 파싱 실패 |
| POST | 401 | 0 | `https://fin.land.naver.com/front-api/v1/user/recentView` | JSON 파싱 실패 |
| POST | 401 | 0 | `https://fin.land.naver.com/front-api/v1/user/legalDivisionView` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/legalDivision/searchByCoordinate` | JSON 파싱 실패 |
| GET | 200 | 0 | `https://fin.land.naver.com/front-api/v1/complex/loan/kbPrice` | JSON 파싱 실패 |
| POST | 200 | 0 | `https://tr.pay.naver.com/trace/web` | JSON 파싱 실패 |
| POST | 200 | 0 | `https://sentry-fin.naver.com/api/76/envelope/` | JSON 파싱 실패 |
| POST | 200 | 0 | `https://sentry-fin.naver.com/api/76/envelope/` | JSON 파싱 실패 |
| POST | 200 | 0 | `https://sentry-fin.naver.com/api/76/envelope/` | JSON 파싱 실패 |
| POST | 200 | 0 | `https://sentry-fin.naver.com/api/76/envelope/` | JSON 파싱 실패 |

## 3. 국토부 실거래 API

- MOLIT_API_KEY 시크릿이 없어 건너뜀

