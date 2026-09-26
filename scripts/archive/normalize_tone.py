#!/usr/bin/env python3
"""
표준화 (tone & format normalization) — 140 use case markdown files.

규칙:
1. Section headers — CLAUDE.md spec parens로 통일
2. Markers — ⭐→★, ❌→🚫, 🚨→🚫, ✅ 검증→✅ Fact
3. 'R9 research'·'Agent research' 등 Claude session artifact paren 제거
"""
import os, re, glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Section header rules: (regex pattern, replacement) — [ \t]*$ used to avoid eating newlines
HEADER_RULES = [
    (r'^## Problem / Why(?:[ \t]*\([^)]*\))?[ \t]*$', '## Problem / Why (도입 배경)'),
    (r'^## Solution Architecture(?:[ \t]*\([^)]*\))?[ \t]*$', '## Solution Architecture'),
    (r'^## Impact / Metrics(?:[ \t]*\([^)]*\))?[ \t]*$', '## Impact / Metrics (기대효과)'),
    (r'^### A\. Process(?:[ \t]*\([^)]*\))?[ \t]*$', '### A. Process (프로세스)'),
    (r'^### B\. System & Infrastructure(?:[ \t]*\([^)]*\))?[ \t]*$', '### B. System & Infrastructure (시스템·인프라)'),
    (r'^### C\. Data(?:[ \t]*\([^)]*\))?[ \t]*$', '### C. Data (데이터)'),
    (r'^### D\. Model(?:[ \t]*\([^)]*\))?[ \t]*$', '### D. Model (모델)'),
    (r'^### E\. Organization & Team(?:[ \t]*\([^)]*\))?[ \t]*$', '### E. Organization & Team (조직·팀 구조)'),
    (r'^### F\. Diagrams(?:[ \t]*\([^)]*\))?[ \t]*$', '### F. Diagrams (도식)'),
    # `### B/C/D. System` (multi-section combined) — leave alone
]

# Marker substitutions (apply globally in body)
# 🚨는 "alert" 의미로 의도적 사용 가능 — 제외
MARKER_RULES = [
    ('⭐', '★'),
    ('❌', '🚫'),
    ('✅ 검증', '✅ Fact'),
    ('✅ Verified', '✅ Fact'),
]


def normalize_file(fp, dry_run=False):
    with open(fp, 'r', encoding='utf-8') as f:
        original = f.read()
    new = original
    changes = []

    # Headers (line-by-line for precise change detection)
    lines = new.split('\n')
    for i, line in enumerate(lines):
        for pat, rep in HEADER_RULES:
            m = re.match(pat, line)
            if m and line.rstrip() != rep:
                old = line
                lines[i] = rep
                changes.append(f'  HDR: "{old.rstrip()}" → "{rep}"')
                break
    new = '\n'.join(lines)

    # Markers (global replace; safe since they're text symbols, not code)
    for old, repl in MARKER_RULES:
        if old in new:
            count = new.count(old)
            new = new.replace(old, repl)
            changes.append(f'  MRK: "{old}" → "{repl}" ({count}×)')

    if new != original and not dry_run:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new)
    return changes


def main():
    dry_run = '--dry-run' in sys.argv
    # Apply to all wiki content folders (not just usecases)
    folders = ['wiki/usecases', 'wiki/syntheses', 'wiki/sources', 'wiki/companies', 'wiki/vendors', 'wiki/categories']
    files = []
    for d in folders:
        files.extend(sorted(glob.glob(f'{d}/*.md')))
    total_changed = 0
    total_changes = 0
    for fp in files:
        changes = normalize_file(fp, dry_run=dry_run)
        if changes:
            total_changed += 1
            total_changes += len(changes)
            print(f'\n{os.path.relpath(fp).replace(chr(92),"/")}:')
            for c in changes:
                print(c)
    print()
    print(f'Files scanned: {len(files)}')
    print(f'Files changed: {total_changed}')
    print(f'Total changes: {total_changes}')
    if dry_run:
        print('(dry-run mode — no file writes)')


if __name__ == '__main__':
    main()
