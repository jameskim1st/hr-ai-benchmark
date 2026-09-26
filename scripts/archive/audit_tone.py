#!/usr/bin/env python3
"""tone & format audit across 140 use case markdown files."""
import os, re, glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = sorted(glob.glob('wiki/usecases/*.md'))
print(f'Total files: {len(files)}')

# 1. Section header variance
section_patterns = {}
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    headers = re.findall(r'^(##\s+.+|###\s+.+)$', c, re.MULTILINE)
    for h in headers:
        h = h.strip()
        section_patterns.setdefault(h, []).append(os.path.basename(fp))

# group by normalized core (drop parens)
norm = {}
for h, fps in section_patterns.items():
    base = re.sub(r'\([^)]+\)', '', h).strip().lower()
    norm.setdefault(base, []).append((h, len(fps)))

print()
print('=== Section variants (similar headers in different forms) ===')
for base, variants in sorted(norm.items()):
    if len(variants) > 1:
        total = sum(n for _, n in variants)
        print(f'  [{total} total] {base}:')
        for v, n in sorted(variants, key=lambda x: -x[1]):
            print(f'    {n:3d}× {v}')

# 2. Korean ending style
print()
print('=== Korean ending style (sample) ===')
for ending in ['습니다', '입니다', '한다', '이다', '함', '됨']:
    count = 0
    for fp in files:
        with open(fp, 'r', encoding='utf-8') as f:
            c = f.read()
        count += len(re.findall(rf'{ending}[\.\s]', c))
    print(f'  "{ending}": {count} occurrences')

# 3. Markers
print()
print('=== Marker emoji usage ===')
for marker in ['✅ Fact', '✅ 검증', '✅ Verified', '⚠️ 벤더 주장', '⚠️ 자사 보고', '⚠️ 미공개', '🚫', '🚨', '❌', '📌', '📋', '⭐', '★']:
    count = sum(1 for fp in files if marker in open(fp, 'r', encoding='utf-8').read())
    print(f'  {marker}: {count} files')

# 4. Bullet markers
print()
print('=== Bullet markers ===')
dash_files = sum(1 for fp in files if re.search(r'^- ', open(fp, 'r', encoding='utf-8').read(), re.MULTILINE))
star_files = sum(1 for fp in files if re.search(r'^\* ', open(fp, 'r', encoding='utf-8').read(), re.MULTILINE))
print(f'  - bullet: {dash_files} files')
print(f'  * bullet: {star_files} files')

# 5. Solution Architecture section style
print()
print('=== Solution Architecture sub-section style ===')
for pat in [r'### A\. Process', r'### Process', r'### A\.\s+Process \(프로세스\)', r'## Solution Architecture$', r'## Solution Architecture \(요약\)']:
    count = sum(1 for fp in files if re.search(pat, open(fp, 'r', encoding='utf-8').read(), re.MULTILINE))
    print(f'  /{pat}/: {count} files')
