# apt-monitor
부동산 매물·실거래 모니터

관심 아파트 단지·평형·거래조건에 맞는 매물을 주기적으로 수집해 표와 지도로 보여주고,
매물 변화(신규·삭제·호가 변동)를 이력으로 남겨 텔레그램으로 알려줍니다.
설계는 [docs/DESIGN.md](docs/DESIGN.md)를 참고하세요.

## 현재 단계: 0. 수집 진단

GitHub Actions 환경에서 네이버부동산·국토부 API가 응답하는지 확인합니다.

1. 네이버부동산에서 관심 단지를 열고 주소의 `/complexes/` 뒤 숫자(단지번호)를 확인합니다.
2. **Actions → 수집 진단 → Run workflow** 에 단지번호를 넣고 실행합니다.
3. 결과는 실행 화면 요약과 [probe/report.md](probe/report.md)에 기록됩니다.
