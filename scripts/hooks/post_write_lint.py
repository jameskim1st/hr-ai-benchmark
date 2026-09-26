#!/usr/bin/env python3
"""PostToolUse 훅 — wiki/ 아래 md 파일을 Write/Edit한 직후 lint.py --quick 을 돌려 결과를 Claude에게 보여준다.
critical이 있으면 exit 2 (Claude가 즉시 고치도록 피드백). wiki 밖 파일이면 조용히 통과."""
import sys, json, os, subprocess
try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)
fp = (data.get('tool_input') or {}).get('file_path') or ''
fpn = fp.replace('\\', '/')
if '/wiki/' not in fpn or not fpn.endswith('.md'):
    sys.exit(0)
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
r = subprocess.run([sys.executable, os.path.join(root, 'scripts', 'lint.py'), '--quick', fp], capture_output=True, text=True, encoding='utf-8', cwd=root)
out = (r.stdout or '') + (r.stderr or '')
if r.returncode == 2:
    sys.stderr.write('lint --quick: critical 발견 — 저장한 페이지를 바로 수정하세요.\n' + out[-3000:])
    sys.exit(2)
if out.strip():
    print(out[-1500:])
sys.exit(0)
