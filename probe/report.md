# 진단 결과

- 실행 시각: 2026-10-18 10:57 KST
- 단지번호: 3084
- 실행 환경 IP: {"ip":"128.24.161.90"}

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

