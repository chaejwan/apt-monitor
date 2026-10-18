@echo off
rem 네이버 매물을 수집해 변화 이력을 남기고, 텔레그램으로 알린 뒤 GitHub에 올립니다.
rem   더블클릭: 화면에 진행 상황을 보여 줌
rem   collect.bat auto: 작업 스케줄러용 (laptop\logs 에 기록, 창 대기 없음)
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
cd /d "%~dp0.."

if /i "%~1"=="auto" (
    if not exist laptop\logs mkdir laptop\logs
    call :run >> "laptop\logs\collect.log" 2>&1
    exit /b
)
call :run
pause
exit /b

:run
echo ==== %date% %time% ====
call .venv\Scripts\activate.bat || exit /b 1
git pull --rebase -q
python -m collector.collect
git add data
git commit -q -m "매물 수집 기록 갱신 [skip ci]" && git push -q
exit /b 0
