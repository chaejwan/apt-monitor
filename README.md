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

## 현재 단계: 노트북에서 네이버 진단

`apt-monitor\laptop\probe.bat`을 더블클릭하면 노트북에서 네이버부동산 API를 진단하고
결과를 [probe/report.md](probe/report.md)로 GitHub에 올립니다.
처음 push할 때 GitHub 로그인 창이 뜨면 로그인해 주세요.
