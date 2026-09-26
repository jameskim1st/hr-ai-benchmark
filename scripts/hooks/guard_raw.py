#!/usr/bin/env python3
"""PreToolUse 훅 — raw/ 아래 파일의 Write/Edit를 차단한다 (raw는 불변).
Claude Code가 stdin으로 넘기는 JSON에서 tool_input.file_path를 읽는다. 차단 시 exit 2 + stderr 사유.
예외: raw/inbox/ (사람·클리퍼가 넣는 곳)와 scripts/fetch_raw.py가 만드는 신규 파일은 Bash 경유라 이 훅을 타지 않는다."""
import sys, json, os
try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)
fp = (data.get('tool_input') or {}).get('file_path') or ''
fp = fp.replace('\\', '/')
if '/raw/' in fp or fp.startswith('raw/'):
    if '/raw/inbox/' in fp or fp.startswith('raw/inbox/'):
        sys.exit(0)
    sys.stderr.write(f'BLOCKED: raw/ 는 불변 원본입니다 ({fp}). 새 스냅샷은 scripts/fetch_raw.py 로 만들고, 기존 파일은 수정·삭제하지 않습니다.\n')
    sys.exit(2)
sys.exit(0)
