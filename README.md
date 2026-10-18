# apt-monitor
부동산 매물·실거래 모니터

관심 아파트 단지·평형·거래조건에 맞는 매물을 주기적으로 수집해 표와 지도로 보여주고,
매물 변화(신규·삭제·호가 변동)를 이력으로 남겨 텔레그램으로 알려줍니다.
설계는 [docs/DESIGN.md](docs/DESIGN.md)를 참고하세요.

- 네이버 매물 수집: **노트북**에서 실행 (네이버가 GitHub Actions 같은 해외 IP를 차단하기 때문)
- 실거래 수집·화면·알림: GitHub Actions와 GitHub Pages

## 노트북 준비 (처음 한 번)

1. [Python](https://www.python.org/downloads/)을 설치합니다. 설치 첫 화면에서 **Add python.exe to PATH**를 꼭 체크하세요.
2. [Git for Windows](https://git-scm.com/download/win)를 설치합니다. 옵션은 기본값 그대로 두면 됩니다.
3. 명령 프롬프트(cmd)를 열고 저장소를 받습니다.
   ```
   cd %USERPROFILE%
   git clone https://github.com/chaejwan/apt-monitor
   ```
4. 탐색기에서 `apt-monitor\laptop\setup.bat`을 더블클릭합니다. 파이썬 패키지와 브라우저를 설치합니다.

## 매물 수집 (1단계)

1. **텔레그램 알림 설정** — `laptop\.env.example`을 같은 폴더에 `.env`로 복사하고 봇 토큰과 chat id를 채웁니다.
2. **관심 조건** — [config/watchlists.json](config/watchlists.json)에 단지·평형·거래유형·가격·층·향·동·키워드를 적습니다.
   GitHub 웹에서 연필 아이콘으로 고치면 노트북이 다음 수집 때 받아 갑니다.
3. **첫 수집** — `laptop\collect.bat`을 더블클릭합니다. 첫 수집은 기준만 잡고 알림을 보내지 않습니다.
4. **자동 실행 등록** — `laptop\register_task.bat`을 더블클릭하면 매일 8:07·13:07·19:07에 수집합니다.
   노트북이 꺼져 있었으면 켜진 뒤 바로 실행합니다. 기록은 `laptop\logs\collect.log`에 남습니다.

수집 결과는 저장소에 남습니다.

| 파일 | 내용 |
|---|---|
| `data/complexes/<단지번호>.json` | 단지 정보, 평형·동 목록 (7일마다 갱신) |
| `data/listings/<단지번호>.json` | 집별 상태: 최초·최근 확인 시각, 가격 이력, 진행/삭제 |
| `data/events/YYYY-MM.jsonl` | 변화 이력: 신규·삭제·재등록·가격인상·가격인하·조건진입·조건이탈 |
| `data/status.json` | 마지막 수집 결과 요약 |

진단 도구(`laptop\probe.bat`, `probe/`)는 네이버 화면이 바뀌어 수집이 깨졌을 때 원인을 찾는 데 씁니다.
