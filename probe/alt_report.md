# 대체 출처 진단 결과

- 실행 시각: 2026-10-18 14:19 KST
- 검색어: 수내동 파크타운

## KB부동산

- 시작 페이지 https://kbland.kr/ → 상태 200
- 검색창을 찾지 못함
- 검색 결과에서 단지를 찾지 못함
- '매매' 탭 클릭
- 마지막 주소: https://kbland.kr/today?xy=37.51844095,126.92709865,17
- 페이지 제목: KB부동산 - 아파트 시세, 실거래가, 분양, 빌라시세, 예측시세
- 화면 글자에서 찾은 매물 수 표시: ['월세\n1', '매물 2']

| 방식 | 상태 | 주소 | 내용 | 원문 |
|---|---|---|---|---|
| GET | 200 | `https://nam.veta.naver.com/nac/2` | keys=['nac'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/temp/serviceAllowCnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/menu/menuList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.middle 10건, 항목 keys=['메뉴일련번호', '상위메뉴일련번호', '제목명', '서브명', '로그인내용', '회원유형명', '신규여부', '웹스키마내용'] |  |
| GET | 200 | `https://api.kbland.kr/land-property/property/getLocInfoCnt` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 1건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 1건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| GET | 200 | `https://api.kbland.kr/land-complex/count/complexes/rankings/views` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.ranks 100건, 항목 keys=['complexId', 'complexName', 'complexType', 'complexStatus', 'region', 'viewCount', 'rank | alt_samples/KB부동산_8.json |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 1건, 항목 keys=['색상', '단지기본일련번호', '노출종료일시', '리뉴얼이미지파일경로', '노출순위', '랜덤노출여부', 'PC웹링크명', 'PC웹서브링크설정코드'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 1건, 항목 keys=['색상', '단지기본일련번호', '노출종료일시', '리뉴얼이미지파일경로', '노출순위', '랜덤노출여부', 'PC웹링크명', 'PC웹서브링크설정코드'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://cam.kbdmp.com/moaimp` | bool |  |
| GET | 200 | `https://cam.kbdmp.com/wmoareq` | keys=['status', 'moaId', 'moaIdT', 'moaIdType', 'message', 'ads_count'], 가장 긴 목록 .ads_info.ads 2건, 항목 keys=['ads_no', 'cmp_no', 'group_no', 'cta_no_list', 'slot |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/v1/logData` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/today/V1/getBenefitExposureNaverAD` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/today/headlines` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 7건, 항목 keys=['입주민톡일련번호', '콘텐츠ID', '제목내용', '링크내용', '썸네일내용', '톡내용', '작성일시'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/today/V2/getBenefitExposureList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.BFVTD.list 12건, 항목 keys=['서비스코드', '이달의포인트', '서비스명', '순번', '제휴사명', '서비스식별자', '제휴사코드', 'TURL'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/banner/byPageTypeAds` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 1건, 항목 keys=['색상', '단지기본일련번호', '노출종료일시', '리뉴얼이미지파일경로', '노출순위', '랜덤노출여부', 'PC웹링크명', 'PC웹서브링크설정코드'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/today/top/lastUpdated` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://cam.kbdmp.com/moaimp` | bool |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/today/top/priceIncreases` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 3건, 항목 keys=['면적일련번호', '실거래기본일련번호', '단지기본일련번호', '단지명', '지역명', '공급면적타입', '변동가격', '거래금액'] | alt_samples/KB부동산_22.json |
| GET | 200 | `https://nam.veta.naver.com/nac/2` | keys=['nac'] |  |
| POST | 200 | `https://sspi.adpopcorn.com/v2_sdk/rev1/native` | keys=['IsTest', 'Result', 'CheckViewability', 'CollectInstalledApps', 'Mute', 'IsNativeVideo'] |  |
| GET | 200 | `https://nam.veta.naver.com/gfp/v1` | keys=['requestId', 'head', 'eventTracking', 'adUnit', 'randomNumber', 'adDivId'], 가장 긴 목록 .eventTracking.ackImpressions 1건, 항목 keys=['url'] |  |
| GET | 200 | `https://oapi.map.naver.com/v3/auth` | JSON 아님 |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/getAllPremiumComplexMarkerList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 4건, 항목 keys=['단지기본일련번호', '일반단지명', '단지마커altText내용', '분양단지위도', '분양단지명', '일반단지위도', '단지마커이미지파일경로', '단지마커홍보문구 |  |
| POST | 200 | `https://kr-col-ext.nelo.navercorp.com/_store` | keys=['code', 'message'] |  |
| GET | 200 | `https://cam.kbdmp.com/moaimp` | bool |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/scholMarkerList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data 3건, 항목 keys=['학교식별자', '학교명', '학교과정분류구분', 'wgs84경도', 'wgs84위도'] |  |
| GET | 200 | `https://api.kbland.kr/land-complex/map/allAreaNameList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.법정동리스트 34건, 항목 keys=['법정동명', '법정동코드', 'wgs84중심위도', 'wgs84중심경도'] |  |
| POST | 200 | `https://api.kbland.kr/land-complex/map/map250mBlwInfoList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.매물리스트 21건, 항목 keys=['매물개수', 'wgs84경도', '클러스터식별자', 'wgs84위도'] | alt_samples/KB부동산_34.json |
| POST | 200 | `https://api.kbland.kr/land-property/propList/stutCdFilter/count` | keys=['dataHeader', 'dataBody'] |  |
| GET | 200 | `https://api.kbland.kr/land-extra/userNotice/getUrgentNotice` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-complex/map/getAgentInfoList` | keys=['dataHeader', 'dataBody'], 가장 긴 목록 .dataBody.data.중개업소리스트 3건, 항목 keys=['대표자명', '중개업소식별자', 'wgs84경도', '중개업소명', '중개업소대표사진파일명', 'wgs84위도'] |  |
| GET | 200 | `https://cam.kbdmp.com/moaimp` | bool |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |
| POST | 200 | `https://api.kbland.kr/land-log-collect/ad/setAdLog` | keys=['dataHeader', 'dataBody'] |  |

## 직방

- 시작 페이지 https://www.zigbang.com/home/apt/map → 상태 200
- 검색창(input[placeholder*='검색'])에 '수내동 파크타운' 입력
- 검색 결과에서 단지를 찾지 못함
- 매물 탭을 찾지 못함
- 마지막 주소: https://www.zigbang.com/home/apt/danjis/1201?checking_subscription=true
- 페이지 제목: '수내동 파크타운대림' 실거래가, 시세, 주변정보 | Beyond Home, Zigbang
- 화면 글자에서 찾은 매물 수 표시: ['매매 13', '월세 4', '전세 8', '전세 12', '매매 26', '전세 11', '매물 1', '매물 1', '매물 3', '매물 1']

| 방식 | 상태 | 주소 | 내용 | 원문 |
|---|---|---|---|---|
| GET | 200 | `https://gum.criteo.com/sid/json` | keys=['sid', 'removeSid', 'bundle', 'info', 'optout'] |  |
| GET | 200 | `https://bzrcdn.openai.com/pixel-config/v1/2SZiF9BbSW2UAz59CMtbTu.json` | keys=['automatic_advanced_matching_enabled'] |  |
| GET | 200 | `https://nam.veta.naver.com/nac/2` | keys=['nac'] |  |
| POST | 200 | `https://cognito-identity.us-east-1.amazonaws.com/` | keys=['IdentityId'] |  |
| GET | 200 | `https://wa.onelink.me/v1/onelink` | keys=['cookie'] |  |
| POST | 200 | `https://cognito-identity.us-east-1.amazonaws.com/` | keys=['Credentials', 'IdentityId'] |  |
| GET | 200 | `https://apis.zigbang.com/v2/settings/map_provider` | keys=['value'] |  |
| PUT | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/endpoint` | keys=['RequestID', 'Message'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/common-config` | keys=['itemRequestTitle', 'itemRequestDescription', 'commissionDiscountText', 'commissionDiscountShortText', 'commissionDiscountShortText2', 'drawerItemRequestT | alt_samples/직방_8.json |
| POST | 200 | `https://wa.appsflyersdk.com/events` | keys=['cookie', 'domain'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/locals/polygon` | keys=['code', 'name', 'geojson', 'isPartnerArea', 'isItemRequest', 'isLocalItems'] | alt_samples/직방_10.json |
| POST | 200 | `https://firebaseinstallations.googleapis.com/v1/projects/api-project-163972169776/installa` | keys=['name', 'fid', 'refreshToken', 'authToken'] |  |
| GET | 200 | `https://wa.onelink.me/v1/onelink` | keys=['cookie'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/schools` | keys=['schools'], 가장 긴 목록 .schools 33건, 항목 keys=['id', 'name', 'school_code', 'lat', 'lng', 'stage', 'sullib', 'high_category'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/schools` | keys=['schools'], 가장 긴 목록 .schools 51건, 항목 keys=['id', 'name', 'school_code', 'lat', 'lng', 'stage', 'sullib', 'high_category'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/locals/prices/on-danjis` | keys=['filtered', 'unfiltered'], 가장 긴 목록 .filtered 191건, 항목 keys=['id', 'name', 'lat', 'lng', '총세대수', '사용승인일', '서비스구분', 'real_type'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/markers/campaigns/on-locals` | keys=['markers'], 가장 긴 목록 .markers 52건, 항목 keys=['id', 'areaDanjiId', 'areaDanjiName', 'title1', 'title2', 'title3', 'imageUrl', 'begunAt'] |  |
| POST | 200 | `https://firebaseremoteconfig.googleapis.com/v1/projects/api-project-163972169776/namespace` | keys=['entries', 'state', 'templateVersion'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/markers/stores` | keys=['markers'] |  |
| GET | 200 | `https://apis.zigbang.com/common/subway/all` | list 936건 |  |
| GET | 200 | `https://apis.zigbang.com/v2/app/settings/house` | keys=['vip'], 가장 긴 목록 .vip.zoomLevelPolicies 13건, 항목 keys=['zoomLevel', 'geohashLength', 'radius'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/locals/prices/on-danjis` | keys=['filtered', 'unfiltered'], 가장 긴 목록 .filtered 269건, 항목 keys=['id', 'name', 'lat', 'lng', '총세대수', '사용승인일', '서비스구분', 'real_type'] |  |
| POST | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/events/l` | keys=['Results'] |  |
| POST | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/events/l` | keys=['Results'] |  |
| POST | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/events/l` | keys=['Results'] |  |
| POST | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/events/l` | keys=['Results'] |  |
| POST | 200 | `https://kinesis.ap-northeast-1.amazonaws.com/` | keys=['FailedRecordCount', 'Records'], 가장 긴 목록 .Records 3건, 항목 keys=['SequenceNumber', 'ShardId'] |  |
| GET | 200 | `https://apis.zigbang.com/v2/search` | keys=['success', 'code', 'items', 'next', 'limit'], 가장 긴 목록 .items 4건, 항목 keys=['id', 'type', 'name', 'hint', 'description', 'lat', 'lng', 'zoom'] | alt_samples/직방_27.json |
| GET | 200 | `https://apis.zigbang.com/apt/schools` | keys=['schools'], 가장 긴 목록 .schools 47건, 항목 keys=['id', 'name', 'school_code', 'lat', 'lng', 'stage', 'sullib', 'high_category'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/schools` | keys=['schools'], 가장 긴 목록 .schools 10건, 항목 keys=['id', 'name', 'school_code', 'lat', 'lng', 'stage', 'sullib', 'high_category'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/locals/polygon` | keys=['code', 'name', 'geojson', 'isPartnerArea', 'isItemRequest', 'isLocalItems'] | alt_samples/직방_30.json |
| GET | 200 | `https://www.zigbang.com/_next/data/qYL3IrRqkXg3TQOzXGuh2/home/apt/danjis/1201.json` | keys=['query', 'pageProps', 'lang', 'i18nResources', '__N_SSP'], 가장 긴 목록 .pageProps.SSRData.danjis.현장투어 29건, 항목 keys=['title', 'desc', 'img'] | alt_samples/직방_31.json |
| GET | 200 | `https://apis.zigbang.com/apt/locals/prices/on-danjis` | keys=['filtered', 'unfiltered'], 가장 긴 목록 .filtered 32건, 항목 keys=['id', 'name', 'lat', 'lng', '총세대수', '사용승인일', '서비스구분', 'real_type'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/schools` | keys=['schools'], 가장 긴 목록 .schools 47건, 항목 keys=['id', 'name', 'school_code', 'lat', 'lng', 'stage', 'sullib', 'high_category'] |  |
| GET | 200 | `https://apis.zigbang.com/apt/locals/prices/on-danjis` | keys=['filtered', 'unfiltered'], 가장 긴 목록 .filtered 96건, 항목 keys=['id', 'name', 'lat', 'lng', '총세대수', '사용승인일', '서비스구분', 'real_type'] | alt_samples/직방_34.json |
| GET | 200 | `https://apis.zigbang.com/apt/locals/prices/on-danjis` | keys=['filtered', 'unfiltered'], 가장 긴 목록 .filtered 96건, 항목 keys=['id', 'name', 'lat', 'lng', '총세대수', '사용승인일', '서비스구분', 'real_type'] | alt_samples/직방_35.json |
| GET | 200 | `https://apis.zigbang.com/apt/agent/fee-tables` | keys=['sales', 'rent'], 가장 긴 목록 .sales 6건, 항목 keys=['minPrice', 'maxPrice', 'feeRate', 'limit'] | alt_samples/직방_36.json |
| GET | 200 | `https://apis.zigbang.com/apt/locals/polygon` | keys=['code', 'name', 'geojson', 'isPartnerArea', 'isItemRequest', 'isLocalItems'] | alt_samples/직방_37.json |
| GET | 200 | `https://apis.zigbang.com/apt/agent/fee-tables` | keys=['sales', 'rent'], 가장 긴 목록 .sales 6건, 항목 keys=['minPrice', 'maxPrice', 'feeRate', 'limit'] | alt_samples/직방_38.json |
| GET | 200 | `https://apis.zigbang.com/apt/danjis/1201/price-chart/related-danjis` | keys=['list'], 가장 긴 목록 .list 16건, 항목 keys=['id', 'name', 'dateText', 'household', 'local1', 'local2', 'local3'] | alt_samples/직방_39.json |
| GET | 200 | `https://apis.zigbang.com/apt/danjis/1201/price-chart/related-danjis` | keys=['list'], 가장 긴 목록 .list 16건, 항목 keys=['id', 'name', 'dateText', 'household', 'local1', 'local2', 'local3'] | alt_samples/직방_40.json |
| GET | 200 | `https://apis.zigbang.com/apt/danjis/1201/price-chart` | keys=['list', 'summary'], 가장 긴 목록 .list 2건, 항목 keys=['label', 'type', 'data'] | alt_samples/직방_41.json |
| GET | 200 | `https://apis.zigbang.com/apt/danjis/1201/rt-prices` | keys=['data', 'areaInfos', 'hasNext'], 가장 긴 목록 .data 5건, 항목 keys=['rtId', 'rtDealDate', 'rtFloor', 'dongName', 'rtArea', 'rtDealType', 'rtPrice', 'rtPriceRent'] | alt_samples/직방_42.json |
| GET | 200 | `https://apis.zigbang.com/house/v1/chat/settings` | keys=['status'] |  |
| POST | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/events/l` | keys=['Results'] |  |
| POST | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/events/l` | keys=['Results'] |  |
| POST | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/events/l` | keys=['Results'] |  |
| POST | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/events/l` | keys=['Results'] |  |
| POST | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/events/l` | keys=['Results'] |  |
| POST | 200 | `https://kinesis.ap-northeast-1.amazonaws.com/` | keys=['FailedRecordCount', 'Records'], 가장 긴 목록 .Records 5건, 항목 keys=['SequenceNumber', 'ShardId'] |  |
| POST | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/events/l` | keys=['Results'] |  |
| POST | 200 | `https://kinesis.ap-northeast-1.amazonaws.com/` | keys=['FailedRecordCount', 'Records'], 가장 긴 목록 .Records 2건, 항목 keys=['SequenceNumber', 'ShardId'] |  |
| POST | 202 | `https://pinpoint.us-east-1.amazonaws.com/v1/apps/d4d3937c27a14a44b98032c1df9866f4/events/l` | keys=['Results'] |  |

## land.naver.com

- 시작 페이지 https://land.naver.com/ → 상태 200
- 직접 이동 https://land.naver.com/complex/complexDetail?hscpNo=3084 → 상태 404, 최종 https://land.naver.com/complex/complexDetail?hscpNo=3084
- 진행 중 실패: Page.goto: Timeout 30000ms exceeded.
Call log:
  - navigating to "https://land.naver.com/article/complexInfo.naver?hscpNo=3084", waiting until "domcontentloaded"


| 방식 | 상태 | 주소 | 내용 | 원문 |
|---|---|---|---|---|
| GET | 200 | `https://nam.veta.naver.com/nac/1/WMxYBQxihMdP` | keys=['nac'] | alt_samples/land.naver.com_0.json |
| GET | 200 | `https://nam.veta.naver.com/gfp/v1` | keys=['requestId', 'head', 'eventTracking', 'adUnit', 'randomNumber', 'adDivId'], 가장 긴 목록 .ads 2건, 항목 keys=['encrypted', 'connectionType', 'adProviderType', 'ad | alt_samples/land.naver.com_1.json |
| GET | 200 | `https://land.naver.com/news/airsList.naver` | keys=['page', 'pageSize', 'totalPages', 'totalElements', 'list'], 가장 긴 목록 .list 5건, 항목 keys=['pressCorporationId', 'pressCorporationName', 'articleId', 'title', | alt_samples/land.naver.com_2.json |
| GET | 200 | `https://land.naver.com/complex/tours.naver` | keys=['code', 'message', 'timeStamp', 'data'], 가장 긴 목록 .data 12건, 항목 keys=['complexNumber', 'complexName', 'complexTourThumbnail', 'complexTourViewer', 'filming | alt_samples/land.naver.com_3.json |
| GET | 200 | `https://nam.veta.naver.com/gfp/v1` | keys=['requestId', 'head', 'eventTracking', 'adUnit', 'randomNumber', 'adDivId'], 가장 긴 목록 .ads 2건, 항목 keys=['encrypted', 'connectionType', 'adProviderType', 'ad | alt_samples/land.naver.com_4.json |
| GET | 200 | `https://land.naver.com/bannerList.naver` | keys=['bannerList'], 가장 긴 목록 .bannerList 1건, 항목 keys=['id', 'typeId', 'thumbnailUrl', 'outLinkUrl', 'guidancePhrase', 'exposeStartDateTime', 'exposeEndDateTime' | alt_samples/land.naver.com_5.json |

