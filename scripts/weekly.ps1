# weekly.ps1 — 주간 자동 사이클 (Windows 작업 스케줄러용)
#   1) 결정론적 lint (스크립트, LLM 아님) → 리포트 파일 저장
#   2) grade 재계산 (freshness가 시간에 따라 바뀌므로)
#   3) export 재빌드 (HTML/Excel)
#   4) inbox에 새 파일이 있으면 Claude에게 triage만 시킨다 (--dry-run, 페이지 생성 없음)
#   5) Claude에게 /hr-digest weekly 를 시킨다 (wiki 데이터만으로 digest 페이지 생성)
#   6) git commit (push는 하지 않는다 — 사람이 확인 후)
# 등록: powershell -ExecutionPolicy Bypass -File scripts/register_weekly_task.ps1
# 비용: 4)·5)는 claude -p 호출 (구독/API 과금). 원치 않으면 $RunClaude = $false
param([switch]$NoClaude)
$ErrorActionPreference = 'Continue'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $root
$env:PYTHONIOENCODING = 'utf-8'
$log = Join-Path $root "logs"
New-Item -ItemType Directory -Force $log | Out-Null
$stamp = Get-Date -Format 'yyyy-MM-dd'
$out = Join-Path $log "weekly-$stamp.log"
"=== weekly $stamp ===" | Out-File $out -Encoding utf8

python scripts/grade.py 2>&1 | Tee-Object -Append $out
python scripts/lint.py --write-report 2>&1 | Select-Object -First 5 | Tee-Object -Append $out
python scripts/build_index.py 2>&1 | Tee-Object -Append $out
python scripts/build_all.py 2>&1 | Select-Object -Last 15 | Tee-Object -Append $out

$RunClaude = -not $NoClaude
if ($RunClaude) {
  $inbox = Get-ChildItem raw/inbox -File -ErrorAction SilentlyContinue
  if ($inbox) {
    "inbox: $($inbox.Count) files -> triage (dry-run)" | Tee-Object -Append $out
    claude -p "/hr-ingest raw/inbox --dry-run" --output-format text 2>&1 | Tee-Object -Append $out
  }
  claude -p "/hr-digest weekly" --output-format text 2>&1 | Tee-Object -Append $out
}

git add -A wiki/syntheses wiki/index.md wiki/exports wiki/usecases wiki/enterprise-ai logs 2>$null
git commit -q -m "chore(weekly): lint report + grade refresh + export rebuild ($stamp)" 2>&1 | Tee-Object -Append $out
"done" | Tee-Object -Append $out
