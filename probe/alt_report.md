# 대체 출처 진단 결과

- 실행 시각: 2026-10-18 16:19 KST
- 검색어: 수내동 파크타운

직방 검색으로 찾은 단지: [(1201, '파크타운대림'), (1202, '파크타운롯데'), (1203, '파크타운삼익'), (1204, '파크타운서안')]

## KB부동산_지도

- 시작 페이지 https://kbland.kr/map?xy=37.37389802923607,127.12223910124835,18 → 상태 200
- 마지막 주소: https://kbland.kr/map?xy=37.37389802923607,127.12223910124835,18
- 페이지 제목: KB부동산 - 아파트 시세, 실거래가, 분양, 빌라시세, 예측시세
- 화면 글자에서 찾은 매물 수 표시: 없음

| 방식 | 상태 | 주소 | 내용 | 원문 |
|---|---|---|---|---|
| GET | 200 | `https://nam.veta.naver.com/nac/2` | keys=['nac'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/count/complexes/rankings/views` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.ranks 100건, 항목 keys=['complexId', 'complexName', 'complexType', 'complexStatus', 'region', 'viewCount', 'rank | alt_samples/KB부동산_지도_2.json |
| GET | 200 | `https://api.kbland.kr/land-extra/temp/serviceAllowCnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-property/property/getLocInfoCnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 1건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| GET | 200 | `https://api.kbland.kr/land-extra/menu/menuList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.middle 10건, 항목 keys=['메뉴일련번호', '상위메뉴일련번호', '제목명', '서브명', '로그인내용', '회원유형명', '신규여부', '웹스키마내용'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 1건, 항목 keys=['색상', '단지기본일련번호', '노출종료일시', '리뉴얼이미지파일경로', '노출순위', '랜덤노출여부', 'PC웹링크명', 'PC웹서브링크설정코드'] |  |

KB부동산 지도에서 찾은 단지: {'296088': '도덕파크타운(2단지)'}

