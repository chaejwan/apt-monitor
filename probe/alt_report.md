# 대체 출처 진단 결과

- 실행 시각: 2026-10-18 16:29 KST
- 검색어: 수내동 파크타운

직방 검색으로 찾은 단지: [(1201, '파크타운대림'), (1202, '파크타운롯데'), (1203, '파크타운삼익'), (1204, '파크타운서안')]

- KB 단지 4635: ' ' 시세, 가격, 매매, 전세 | KB시세는 KB부동산
- KB 단지 4636: '수내동 파크타운(롯데)' 시세, 가격, 매매, 전세 | KB시세는 KB부동산
- KB 단지 4637: '수내동 파크타운(서안)' 시세, 가격, 매매, 전세 | KB시세는 KB부동산
- KB 단지 4638: '수내동 파크타운(대림)' 시세, 가격, 매매, 전세 | KB시세는 KB부동산
- KB 단지 4639: '정자동 상록마을(우성)' 시세, 가격, 매매, 전세 | KB시세는 KB부동산
- KB 단지 4640: '정자동 상록마을(라이프)' 시세, 가격, 매매, 전세 | KB시세는 KB부동산

매물을 확인할 KB 단지: {'4636': '수내동 파크타운(롯데)', '4637': '수내동 파크타운(서안)', '4638': '수내동 파크타운(대림)'}

## KB부동산_수내동 파크타운(롯데)

- 시작 페이지 https://kbland.kr/c/4636 → 상태 200
- '^매매\s*\d+$' 클릭 → 로그인 창이 뜸
- '^전세\s*\d+$' 를 찾지 못함 → 로그인 창이 뜸
- '^월세\s*\d+$' 를 찾지 못함 → 로그인 창이 뜸
- '동별매물' 를 찾지 못함 → 로그인 창이 뜸
- 마지막 주소: https://kbland.kr/c/4636?xy=37.3721346,127.1156982,17
- 페이지 제목: '수내동 파크타운(롯데)' 시세, 가격, 매매, 전세 | KB시세는 KB부동산
- 화면 글자에서 찾은 매물 수 표시: ['매매 13', '전세 0', '월세 0', '월세\n124', '매매124', '전세124', '월세124', '매매\n22', '전세\n9', '매매5']

| 방식 | 상태 | 주소 | 내용 | 원문 |
|---|---|---|---|---|
| GET | 200 | `https://api.kbland.kr/land-property/property/getLocInfoCnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/temp/serviceAllowCnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/menu/menuList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.middle 10건, 항목 keys=['메뉴일련번호', '상위메뉴일련번호', '제목명', '서브명', '로그인내용', '회원유형명', '신규여부', '웹스키마내용'] |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 1건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| GET | 200 | `https://api.kbland.kr/land-complex/count/complexes/rankings/views` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.ranks 100건, 항목 keys=['complexId', 'complexName', 'complexType', 'complexStatus', 'region', 'viewCount', 'rank | alt_samples/KB부동산_수내동 파크타운(롯데)_5.json |
| GET | 200 | `https://api.kbland.kr/land-extra/loanCnsel/dlbrCtnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complex/complexMain` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.data 32건, 항목 keys=['순번', '전체이미지경로_800'] | alt_samples/KB부동산_수내동 파크타운(롯데)_7.json |
| POST | 200 | `https://api.kbland.kr/land-complex/count/complexes/4636/views` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://kr-col-ext.nelo.navercorp.com/_store` | keys=['code', 'message'] |  |
| GET | 200 | `https://oapi.map.naver.com/v3/auth` | JSON 아님 |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 1건, 항목 keys=['색상', '단지기본일련번호', '노출종료일시', '리뉴얼이미지파일경로', '노출순위', '랜덤노출여부', 'PC웹링크명', 'PC웹서브링크설정코드'] |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 2건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/scholMarkerList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 5건, 항목 keys=['학교식별자', '학교명', '학교과정분류구분', 'wgs84경도', 'wgs84위도'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/getAllPremiumComplexMarkerList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 4건, 항목 keys=['단지기본일련번호', '일반단지명', '단지마커altText내용', '분양단지위도', '분양단지명', '일반단지위도', '단지마커이미지파일경로', '단지마커홍보문구 |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 2건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| GET | 200 | `https://api.kbland.kr/land-benefit/localAd/banner/bannerList` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-complex/count/regions/4113510200/views` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-price/price/complex/preSaleChart` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complex/mpriByType` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 10건, 항목 keys=['단지기본일련번호', '공급면적', '계약면적', '월세건수', '공급면적평N', '주택형타입내용', '매매일반거래가', '전세건수'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexConcern/cnrnHscmInfo` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-community/talk/talkCount` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complex/typInfo` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 10건, 항목 keys=['단지기본일련번호', '공용면적', '공급면적', '어드민평면도URL주소', '네이버단지코드', '계약면적', '월세건수', '사용여부'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexResteBrhs/list` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 2건, 항목 keys=['사무실전화번호', '위치보기표시여부', '대표자명', '중개업소미공개여부', '중개업소식별자', '주소', 'wgs84경도', '중개업소명'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexComm/dongList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 12건, 항목 keys=['단지기본일련번호', '동별총세대수', '대표단지여부', '동명', '사용승인일', '매물종별구분', '건물최고층수', '동일련번호'] | alt_samples/KB부동산_수내동 파크타운(롯데)_25.json |
| POST | 200 | `https://api.kbland.kr/land-complex/serch/srchLstMsg` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/hubLink/hubLinkedInfo` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.hubListInfo 5건, 항목 keys=['카드명', '공통이미지일련번호', '이미지파일경로명', '데이터허브연계관리일련번호', '이미지파일명', '다크모드컬러', '링크명', '데이 |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexSchool/list` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 27건, 항목 keys=['홈페이지URL', '총교사수', '어린이집명', '총학생수', 'wgs84포인트', '어린이집식별자', '개원일내용', '소속행정기관명'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexComm/dongUseDayChk` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-benefit/localAd/banner/bannerList` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-complex/map/getAgentInfoList` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-complex/map/map250mBlwInfoList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.매물리스트 23건, 항목 keys=['매물개수', 'wgs84경도', '클러스터식별자', 'wgs84위도'] | alt_samples/KB부동산_수내동 파크타운(롯데)_33.json |
| GET | 200 | `https://api.kbland.kr/land-price/price/BasePrcInfoNew` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.시세 1건, 항목 keys=['단지기본일련번호', '전세계약시작년월일', '공급면적', '계약면적', '전세변동금액', '주택형타입내용', '매매일반거래가', '연결구분코드'] |  |
| GET | 200 | `https://cam.kbdmp.com/moaimp` | bool |  |
| GET | 200 | `https://api.kbland.kr/land-price/price/complex/preSaleChart` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.시세 61건, 항목 keys=['기준년월', '매매일반거래가', '전세일반거래가', '전세가율', '실거래전세가율', '시세갭가격', '실거래갭가격', '매매실거래거래량'] | alt_samples/KB부동산_수내동 파크타운(롯데)_36.json |
| GET | 200 | `https://api.kbland.kr/land-complex/map/scholMarkerList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 5건, 항목 keys=['학교식별자', '학교명', '학교과정분류구분', 'wgs84경도', 'wgs84위도'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/v1/logData` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 4건, 항목 keys=['색상', '단지기본일련번호', '리뉴얼이미지파일경로', '분양일정구분명', '사후접수계약종료일', 'wgs84경도', '사후접수계약시작일', '사후접수당첨자발표일 |  |
| GET | 200 | `https://api.kbland.kr/land-complex/housePlanner/rePrparaInfo` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.규제기준 4건, 항목 keys=['규제명', '대출상한금액', '규제기준일련번호'] | alt_samples/KB부동산_수내동 파크타운(롯데)_40.json |
| POST | 200 | `https://api.kbland.kr/land-log-collect/v1/logData` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-complex/map/getAgentInfoList` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/allAreaNameList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.시군구리스트 47건, 항목 keys=['법정동코드', 'wgs84중심위도', 'wgs84중심경도', '시군구명'] |  |
| POST | 200 | `https://api.kbland.kr/land-property/propList/stutCdFilter/count` | keys=['dataHeader', 'dataBody'] | alt_samples/KB부동산_수내동 파크타운(롯데)_45.json |
| GET | 200 | `https://api.kbland.kr/land-extra/userNotice/getUrgentNotice` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://cam.kbdmp.com/moaimp` | bool |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/v1/logData` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/localAd/localAdLog` | keys=['dataHeader', 'dataBody'] |  |

## KB부동산_수내동 파크타운(서안)

- 시작 페이지 https://kbland.kr/c/4637 → 상태 200
- '^매매\s*\d+$' 클릭 → 로그인 창이 뜸
- '^전세\s*\d+$' 를 찾지 못함 → 로그인 창이 뜸
- '^월세\s*\d+$' 를 찾지 못함 → 로그인 창이 뜸
- '동별매물' 를 찾지 못함 → 로그인 창이 뜸
- 마지막 주소: https://kbland.kr/c/4637?xy=37.3721346,127.1156982,17
- 페이지 제목: '수내동 파크타운(서안)' 시세, 가격, 매매, 전세 | KB시세는 KB부동산
- 화면 글자에서 찾은 매물 수 표시: ['매매 13', '전세 1', '월세 3', '월세\n157', '매매157', '전세157', '월세157', '매매\n23', '전세\n11', '매매0']

| 방식 | 상태 | 주소 | 내용 | 원문 |
|---|---|---|---|---|
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/temp/serviceAllowCnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/menu/menuList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.middle 10건, 항목 keys=['메뉴일련번호', '상위메뉴일련번호', '제목명', '서브명', '로그인내용', '회원유형명', '신규여부', '웹스키마내용'] |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 1건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| GET | 200 | `https://api.kbland.kr/land-complex/count/complexes/rankings/views` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.ranks 100건, 항목 keys=['complexId', 'complexName', 'complexType', 'complexStatus', 'region', 'viewCount', 'rank | alt_samples/KB부동산_수내동 파크타운(서안)_4.json |
| POST | 200 | `https://api.kbland.kr/land-complex/count/complexes/4637/views` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-property/property/getLocInfoCnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/loanCnsel/dlbrCtnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complex/complexMain` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.data 25건, 항목 keys=['순번', '전체이미지경로_800'] | alt_samples/KB부동산_수내동 파크타운(서안)_8.json |
| POST | 200 | `https://kr-col-ext.nelo.navercorp.com/_store` | keys=['code', 'message'] |  |
| GET | 200 | `https://oapi.map.naver.com/v3/auth` | JSON 아님 |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 1건, 항목 keys=['색상', '단지기본일련번호', '노출종료일시', '리뉴얼이미지파일경로', '노출순위', '랜덤노출여부', 'PC웹링크명', 'PC웹서브링크설정코드'] |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 2건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 2건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| POST | 200 | `https://api.kbland.kr/land-complex/count/regions/4113510200/views` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/getAllPremiumComplexMarkerList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 4건, 항목 keys=['단지기본일련번호', '일반단지명', '단지마커altText내용', '분양단지위도', '분양단지명', '일반단지위도', '단지마커이미지파일경로', '단지마커홍보문구 |  |
| GET | 200 | `https://api.kbland.kr/land-price/price/complex/preSaleChart` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexConcern/cnrnHscmInfo` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-benefit/localAd/banner/bannerList` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexResteBrhs/list` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 1건, 항목 keys=['사무실전화번호', '위치보기표시여부', '대표자명', '중개업소미공개여부', '중개업소식별자', '주소', 'wgs84경도', '중개업소명'] |  |
| GET | 200 | `https://api.kbland.kr/land-community/talk/talkCount` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/hubLink/hubLinkedInfo` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.hubListInfo 5건, 항목 keys=['카드명', '공통이미지일련번호', '이미지파일경로명', '데이터허브연계관리일련번호', '이미지파일명', '다크모드컬러', '링크명', '데이 |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complex/typInfo` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 13건, 항목 keys=['단지기본일련번호', '공용면적', '공급면적', '어드민평면도URL주소', '네이버단지코드', '계약면적', '월세건수', '사용여부'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexComm/dongList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 10건, 항목 keys=['단지기본일련번호', '동별총세대수', '대표단지여부', '동명', '사용승인일', '매물종별구분', '건물최고층수', '동일련번호'] | alt_samples/KB부동산_수내동 파크타운(서안)_24.json |
| GET | 200 | `https://api.kbland.kr/land-complex/complex/mpriByType` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 13건, 항목 keys=['단지기본일련번호', '공급면적', '계약면적', '월세건수', '공급면적평N', '주택형타입내용', '매매일반거래가', '전세건수'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexComm/dongUseDayChk` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-complex/serch/srchLstMsg` | keys=['dataHeader', 'dataBody'] | alt_samples/KB부동산_수내동 파크타운(서안)_27.json |
| GET | 200 | `https://api.kbland.kr/land-complex/complexSchool/list` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 25건, 항목 keys=['홈페이지URL', '총교사수', '어린이집명', '총학생수', 'wgs84포인트', '어린이집식별자', '개원일내용', '소속행정기관명'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/scholMarkerList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 5건, 항목 keys=['학교식별자', '학교명', '학교과정분류구분', 'wgs84경도', 'wgs84위도'] |  |
| GET | 200 | `https://api.kbland.kr/land-benefit/localAd/banner/bannerList` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-complex/map/map250mBlwInfoList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.매물리스트 23건, 항목 keys=['매물개수', 'wgs84경도', '클러스터식별자', 'wgs84위도'] | alt_samples/KB부동산_수내동 파크타운(서안)_32.json |
| GET | 200 | `https://cam.kbdmp.com/moaimp` | bool |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/allAreaNameList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.시군구리스트 47건, 항목 keys=['법정동코드', 'wgs84중심위도', 'wgs84중심경도', '시군구명'] |  |
| GET | 200 | `https://api.kbland.kr/land-price/price/BasePrcInfoNew` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.시세 1건, 항목 keys=['단지기본일련번호', '전세계약시작년월일', '공급면적', '계약면적', '전세변동금액', '주택형타입내용', '매매일반거래가', '연결구분코드'] |  |
| GET | 200 | `https://api.kbland.kr/land-price/price/complex/preSaleChart` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.시세 61건, 항목 keys=['기준년월', '매매일반거래가', '전세일반거래가', '전세가율', '실거래전세가율', '시세갭가격', '실거래갭가격', '매매실거래거래량'] | alt_samples/KB부동산_수내동 파크타운(서안)_36.json |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 4건, 항목 keys=['색상', '단지기본일련번호', '리뉴얼이미지파일경로', '분양일정구분명', '사후접수계약종료일', 'wgs84경도', '사후접수계약시작일', '사후접수당첨자발표일 |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/housePlanner/rePrparaInfo` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.규제기준 4건, 항목 keys=['규제명', '대출상한금액', '규제기준일련번호'] | alt_samples/KB부동산_수내동 파크타운(서안)_39.json |
| POST | 200 | `https://api.kbland.kr/land-property/propList/stutCdFilter/count` | keys=['dataHeader', 'dataBody'] | alt_samples/KB부동산_수내동 파크타운(서안)_40.json |
| POST | 200 | `https://api.kbland.kr/land-complex/map/getAgentInfoList` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/v1/logData` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/userNotice/getUrgentNotice` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/v1/logData` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://cam.kbdmp.com/moaimp` | bool |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/localAd/localAdLog` | keys=['dataHeader', 'dataBody'] |  |

## KB부동산_수내동 파크타운(대림)

- 시작 페이지 https://kbland.kr/c/4638 → 상태 200
- '^매매\s*\d+$' 클릭 → 로그인 창이 뜸
- '^전세\s*\d+$' 를 찾지 못함 → 로그인 창이 뜸
- '^월세\s*\d+$' 를 찾지 못함 → 로그인 창이 뜸
- '동별매물' 를 찾지 못함 → 로그인 창이 뜸
- 마지막 주소: https://kbland.kr/c/4638?xy=37.3721346,127.1156982,17
- 페이지 제목: '수내동 파크타운(대림)' 시세, 가격, 매매, 전세 | KB시세는 KB부동산
- 화면 글자에서 찾은 매물 수 표시: ['매매 39', '전세 2', '월세 0', '월세\n157', '매매157', '전세157', '월세157', '매매\n24', '전세\n11', '매매3']

| 방식 | 상태 | 주소 | 내용 | 원문 |
|---|---|---|---|---|
| GET | 200 | `https://api.kbland.kr/land-extra/temp/serviceAllowCnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/menu/menuList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.middle 10건, 항목 keys=['메뉴일련번호', '상위메뉴일련번호', '제목명', '서브명', '로그인내용', '회원유형명', '신규여부', '웹스키마내용'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/count/complexes/rankings/views` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.ranks 100건, 항목 keys=['complexId', 'complexName', 'complexType', 'complexStatus', 'region', 'viewCount', 'rank | alt_samples/KB부동산_수내동 파크타운(대림)_3.json |
| GET | 200 | `https://api.kbland.kr/land-property/property/getLocInfoCnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/loanCnsel/dlbrCtnt` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-complex/count/complexes/4638/views` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complex/complexMain` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.data 25건, 항목 keys=['순번', '전체이미지경로_800'] | alt_samples/KB부동산_수내동 파크타운(대림)_7.json |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 1건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| POST | 200 | `https://kr-col-ext.nelo.navercorp.com/_store` | keys=['code', 'message'] |  |
| GET | 200 | `https://oapi.map.naver.com/v3/auth` | JSON 아님 |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 2건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 1건, 항목 keys=['색상', '단지기본일련번호', '노출종료일시', '리뉴얼이미지파일경로', '노출순위', '랜덤노출여부', 'PC웹링크명', 'PC웹서브링크설정코드'] |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 2건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/getAllPremiumComplexMarkerList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 4건, 항목 keys=['단지기본일련번호', '일반단지명', '단지마커altText내용', '분양단지위도', '분양단지명', '일반단지위도', '단지마커이미지파일경로', '단지마커홍보문구 |  |
| GET | 200 | `https://api.kbland.kr/land-price/price/complex/preSaleChart` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-complex/count/regions/4113510200/views` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-benefit/localAd/banner/bannerList` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexConcern/cnrnHscmInfo` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/hubLink/hubLinkedInfo` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.hubListInfo 5건, 항목 keys=['카드명', '공통이미지일련번호', '이미지파일경로명', '데이터허브연계관리일련번호', '이미지파일명', '다크모드컬러', '링크명', '데이 |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexComm/dongList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 9건, 항목 keys=['단지기본일련번호', '동별총세대수', '대표단지여부', '동명', '사용승인일', '매물종별구분', '건물최고층수', '동일련번호'] | alt_samples/KB부동산_수내동 파크타운(대림)_21.json |
| POST | 200 | `https://api.kbland.kr/land-complex/serch/srchLstMsg` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complex/typInfo` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 12건, 항목 keys=['단지기본일련번호', '공용면적', '공급면적', '어드민평면도URL주소', '네이버단지코드', '계약면적', '월세건수', '사용여부'] |  |
| GET | 200 | `https://api.kbland.kr/land-community/talk/talkCount` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexComm/dongUseDayChk` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexResteBrhs/list` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 1건, 항목 keys=['사무실전화번호', '위치보기표시여부', '대표자명', '중개업소미공개여부', '중개업소식별자', '주소', 'wgs84경도', '중개업소명'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complex/mpriByType` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 12건, 항목 keys=['단지기본일련번호', '공급면적', '계약면적', '월세건수', '공급면적평N', '주택형타입내용', '매매일반거래가', '전세건수'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/complexSchool/list` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 28건, 항목 keys=['홈페이지URL', '총교사수', '어린이집명', '총학생수', 'wgs84포인트', '어린이집식별자', '개원일내용', '소속행정기관명'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/scholMarkerList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 5건, 항목 keys=['학교식별자', '학교명', '학교과정분류구분', 'wgs84경도', 'wgs84위도'] |  |
| POST | 200 | `https://api.kbland.kr/land-complex/map/map250mBlwInfoList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.매물리스트 23건, 항목 keys=['매물개수', 'wgs84경도', '클러스터식별자', 'wgs84위도'] | alt_samples/KB부동산_수내동 파크타운(대림)_30.json |
| GET | 200 | `https://api.kbland.kr/land-benefit/localAd/banner/bannerList` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 4건, 항목 keys=['색상', '단지기본일련번호', '리뉴얼이미지파일경로', '분양일정구분명', '사후접수계약종료일', 'wgs84경도', '사후접수계약시작일', '사후접수당첨자발표일 |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/allAreaNameList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.시군구리스트 47건, 항목 keys=['법정동코드', 'wgs84중심위도', 'wgs84중심경도', '시군구명'] |  |
| GET | 200 | `https://cam.kbdmp.com/moaimp` | bool |  |
| GET | 200 | `https://api.kbland.kr/land-price/price/complex/preSaleChart` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.시세 61건, 항목 keys=['기준년월', '매매일반거래가', '전세일반거래가', '전세가율', '실거래전세가율', '시세갭가격', '실거래갭가격', '매매실거래거래량'] | alt_samples/KB부동산_수내동 파크타운(대림)_36.json |
| GET | 200 | `https://api.kbland.kr/land-price/price/BasePrcInfoNew` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.시세 1건, 항목 keys=['단지기본일련번호', '전세계약시작년월일', '공급면적', '계약면적', '전세변동금액', '주택형타입내용', '매매일반거래가', '연결구분코드'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/housePlanner/rePrparaInfo` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.규제기준 4건, 항목 keys=['규제명', '대출상한금액', '규제기준일련번호'] | alt_samples/KB부동산_수내동 파크타운(대림)_39.json |
| POST | 200 | `https://api.kbland.kr/land-complex/map/getAgentInfoList` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-property/propList/stutCdFilter/count` | keys=['dataHeader', 'dataBody'] | alt_samples/KB부동산_수내동 파크타운(대림)_41.json |
| POST | 200 | `https://api.kbland.kr/land-log-collect/v1/logData` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/userNotice/getUrgentNotice` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/v1/logData` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://cam.kbdmp.com/moaimp` | bool |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/localAd/localAdLog` | keys=['dataHeader', 'dataBody'] |  |

