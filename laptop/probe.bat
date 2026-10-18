@echo off
rem 노트북(국내 IP)에서 네이버부동산 API가 어떻게 응답하는지 진단하고, 결과를 GitHub에 올립니다.
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
rem 브라우저 창을 띄워 실제 사람이 보는 것과 같은 화면으로 확인합니다.
set HEADED=1
cd /d "%~dp0.."
call .venv\Scripts\activate.bat || goto :error

git pull --rebase -q || goto :error
if exist probe\samples rmdir /s /q probe\samples
python probe\naver_probe.py --complex 3084 --browser || goto :error

git add probe\report.md probe\samples
git commit -q -m "노트북 수집 진단 결과 갱신 [skip ci]"
git push -q || goto :error

echo.
echo 진단 결과를 GitHub에 올렸습니다.
pause
exit /b 0

:error
echo.
echo 진단 중 오류가 났습니다. 위 메시지를 확인해 주세요.
pause
exit /b 1
