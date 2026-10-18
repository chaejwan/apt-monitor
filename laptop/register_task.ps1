# Registers a Windows scheduled task that runs collect.bat at 08:07, 13:07 and 19:07.
# If the laptop was off or asleep at that time, the task runs as soon as possible afterwards.
$dir = Split-Path -Parent $MyInvocation.MyCommand.Path
$bat = Join-Path $dir "collect.bat"

$action = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$bat`" auto"
$triggers = @(
    (New-ScheduledTaskTrigger -Daily -At "08:07"),
    (New-ScheduledTaskTrigger -Daily -At "13:07"),
    (New-ScheduledTaskTrigger -Daily -At "19:07")
)
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries -RunOnlyIfNetworkAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 30) -MultipleInstances IgnoreNew

Register-ScheduledTask -TaskName "apt-monitor collect" -Action $action -Trigger $triggers `
    -Settings $settings -Description "apt-monitor: Naver listing collection" -Force | Out-Null

Write-Host "Registered scheduled task 'apt-monitor collect' (08:07 / 13:07 / 19:07)."
