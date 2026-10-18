@echo off
rem 작업 스케줄러에 매일 8:07, 13:07, 19:07 매물 수집을 등록합니다. (노트북이 꺼져 있었으면 켜진 뒤 바로 실행)
chcp 65001 >nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0register_task.ps1"
if errorlevel 1 (
    echo 등록에 실패했습니다. 위 메시지를 확인해 주세요.
) else (
    echo 작업 스케줄러에 등록했습니다. 해제하려면 작업 스케줄러에서 "apt-monitor collect"를 삭제하세요.
)
pause
