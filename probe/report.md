# 진단 결과

- 실행 시각: 2026-10-18 11:19 KST
- 단지번호: 3084
- 실행 환경 IP: {"ip":"64.236.176.195"}

## 0. 사이트별 접속 여부

네이버 전체가 막혔는지 부동산만 막혔는지, 대체 출처는 열리는지 확인합니다.

| 사이트 | 상태 | 걸린 시간 | 비고 |
|---|---|---|---|
| 네이버 메인 | 200 | 0.8s | https://www.naver.com/ |
| 네이버 검색 | 403 | 1.0s | HTTP 오류(서버는 응답함) |
| 네이버 지도 | 200 | 1.7s | https://map.naver.com/p/ |
| land.naver.com | 200 | 1.1s | https://land.naver.com/ |
| new.land.naver.com | 0 | 12.9s | The read operation timed out |
| fin.land.naver.com | 0 | 12.9s | The read operation timed out |
| KB부동산 | 200 | 1.1s | https://kbland.kr/ |
| KB부동산 API | 404 | 1.1s | HTTP 오류(서버는 응답함) |
| 직방 | 200 | 0.5s | https://www.zigbang.com/ |
| 직방 API | 403 | 0.3s | HTTP 오류(서버는 응답함) |
| 호갱노노 | 200 | 0.6s | https://hogangnono.com/ |
| 아실 | 200 | 2.1s | https://asil.kr/asil/index.jsp |
| 공공데이터포털 API | 400 | 1.0s | HTTP 오류(서버는 응답함) |
| 카카오 API | 404 | 1.0s | HTTP 오류(서버는 응답함) |

## 1. HTTP 직접 요청

| 확인 항목 | 상태 | 크기 | 내용 | 원문 |
|---|---|---|---|---|
| new.land 단지 페이지 | 0 | 28 | text: The read operation timed out | probe/samples/http_new.land_단지_페이지.txt |
| new.land 단지 API | 0 | 28 | text: The read operation timed out | probe/samples/http_new.land_단지_API.txt |
| new.land 매물 API | 0 | 28 | text: The read operation timed out | probe/samples/http_new.land_매물_API.txt |
| m.land 매물 목록 | 0 | 28 | text: The read operation timed out | probe/samples/http_m.land_매물_목록.txt |
| fin.land 단지 페이지 | 0 | 28 | text: The read operation timed out | probe/samples/http_fin.land_단지_페이지.txt |

- 페이지 HTML에서 찾은 JWT 토큰: 없음

## 2. 브라우저 렌더링 중 오간 JSON 응답

### https://new.land.naver.com/complexes/3084

- 페이지 로딩 실패: Page.goto: Timeout 45000ms exceeded.
Call log:
  - navigating to "https://new.land.naver.com/complexes/3084", waiting until "networkidle"

- Authorization 헤더를 쓴 요청: 없음

| 방식 | 상태 | 크기 | 주소 | 내용 |
|---|---|---|---|---|

### https://fin.land.naver.com/complexes/3084

- 페이지 로딩 실패: Page.goto: Timeout 45000ms exceeded.
Call log:
  - navigating to "https://fin.land.naver.com/complexes/3084", waiting until "networkidle"

- Authorization 헤더를 쓴 요청: 없음

| 방식 | 상태 | 크기 | 주소 | 내용 |
|---|---|---|---|---|

## 3. 국토부 실거래 API

- MOLIT_API_KEY 시크릿이 없어 건너뜀

