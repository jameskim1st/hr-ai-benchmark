# register_weekly_task.ps1 — Windows 작업 스케줄러에 주간 작업 등록 (매주 월요일 08:00, PC가 켜져 있을 때)
# 해제: schtasks /Delete /TN "HR-AI-Benchmark-Weekly" /F
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$script = Join-Path $root "scripts\weekly.ps1"
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$script`"" -WorkingDirectory $root
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 8:00am
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -RunOnlyIfNetworkAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 2)
Register-ScheduledTask -TaskName "HR-AI-Benchmark-Weekly" -Action $action -Trigger $trigger -Settings $settings -Description "HR AI Benchmark wiki: weekly lint/grade/export/digest" -Force | Out-Null
Write-Host "registered: HR-AI-Benchmark-Weekly (Mon 08:00). Remove with: schtasks /Delete /TN HR-AI-Benchmark-Weekly /F"
