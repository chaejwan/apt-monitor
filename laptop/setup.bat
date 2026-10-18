@echo off
rem 노트북에서 처음 한 번 실행합니다: 파이썬 가상환경과 브라우저를 준비합니다.
chcp 65001 >nul
cd /d "%~dp0.."

set "PY=python"
where py >nul 2>nul && set "PY=py -3"

if not exist .venv (
    echo [1/3] 파이썬 가상환경 만드는 중...
    %PY% -m venv .venv || goto :error
)
call .venv\Scripts\activate.bat

echo [2/3] 필요한 패키지 설치 중...
python -m pip install --upgrade pip -q || goto :error
python -m pip install -q -r laptop\requirements.txt || goto :error

echo [3/3] 브라우저 설치 중... (1~2분)
python -m playwright install chromium || goto :error

rem 수집 결과를 commit할 때 쓸 이름 (이 저장소에만 적용)
git config user.name "apt-monitor laptop"
git config user.email "chaejwan@users.noreply.github.com"

echo.
echo 설치가 끝났습니다.
pause
exit /b 0

:error
echo.
echo 설치 중 오류가 났습니다. 위 메시지를 확인해 주세요.
pause
exit /b 1
