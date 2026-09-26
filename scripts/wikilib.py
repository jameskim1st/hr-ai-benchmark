#!/usr/bin/env python3
"""
wikilib.py — wiki 페이지 frontmatter 읽기/쓰기 공용 모듈 (lint.py, grade.py, build_index.py 등이 사용)

frontmatter는 단순 YAML 서브셋만 다룬다: `key: value`, `key: [a, b]`, `key:\n  - a\n  - b`.
값 뒤 `# 주석`은 보존한다 (재작성 시 원 라인을 그대로 유지하고 변경된 키만 교체).
"""
import os, re, glob, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, 'wiki')
TODAY = datetime.date.today()

CATS = ["Talent Acquisition", "Onboarding & Transitions", "Learning & Development",
        "Performance & Talent Management", "Total Rewards", "Employee Experience & HR Ops",
        "Strategic Workforce & Governance"]
TYPES = {'generative': {'text-generation', 'summarization-qa', 'multimodal', 'information-extraction'},
         'predictive': {'prediction', 'clustering-classification', 'recommendation-ranking'},
         'recognition': {'ocr', 'speech-recognition'},
         'decision-optimization': {'optimization'},
         'automation': {'rpa'}}
BANNED = ['아마도', '추정', '보통 ', '일반적으로', '대개', '대체로', '통상', ' likely', ' probably', ' typically', ' generally', 'most likely', '추측']
# 페이지 유형별 디렉토리
PAGE_DIRS = {'usecases': 'usecase', 'enterprise-ai': 'enterprise-ai', 'reference': 'reference',
             'sources': 'source', 'vendors': 'vendor', 'companies': 'company',
             'categories': 'category', 'syntheses': 'synthesis'}


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def write(path, text):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def split_fm(text):
    """(fm_lines:list[str], body:str) — frontmatter 없으면 (None, text)"""
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return None, text
    return m.group(1).split('\n'), text[m.end():]


def _parse_scalar(v):
    v = v.strip()
    if v.startswith('"') and v.endswith('"') and len(v) >= 2:
        return v[1:-1]
    if v.startswith("'") and v.endswith("'") and len(v) >= 2:
        return v[1:-1]
    # strip trailing comment
    v = re.split(r'\s+#', v)[0].strip()
    if v.startswith('[') and v.endswith(']'):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [x.strip().strip('"').strip("'") for x in re.split(r',\s*', inner) if x.strip()]
    if v == '':
        return None
    return v


def parse_fm(lines):
    d = {}
    cur = None
    for line in lines:
        if re.match(r'^\s+-\s', line) and cur:
            if not isinstance(d.get(cur), list):
                d[cur] = []
            item = re.sub(r'^\s+-\s*', '', line)
            item = re.split(r'\s+#', item)[0].strip().strip('"').strip("'")
            d[cur].append(item)
        elif re.match(r'^[A-Za-z_][\w]*:', line):
            k, _, v = line.partition(':')
            k = k.strip()
            d[k] = _parse_scalar(v)
            cur = k
    return d


def load(path):
    text = read(path)
    lines, body = split_fm(text)
    fm = parse_fm(lines) if lines else None
    return fm, body, lines


def fmt_value(v):
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, list):
        return '[' + ', '.join(str(x) for x in v) + ']'
    if v is None:
        return ''
    s = str(v)
    if re.search(r'[:#"\[\]{}]|^\s|\s$', s) and not re.match(r'^\d{4}-\d{2}(-\d{2})?$', s):
        return '"' + s.replace('"', "'") + '"'
    return s


def set_fields(path, updates, after=None):
    """frontmatter의 키를 갱신/추가한다. 기존 키는 그 자리에서 값만 교체(주석 유지 안 함 — 값이 바뀌므로).
    새 키는 `after` 키 바로 뒤(없으면 frontmatter 끝)에 추가. 리스트 블록(- item) 키는 통째로 교체."""
    text = read(path)
    lines, body = split_fm(text)
    if lines is None:
        raise ValueError(f'no frontmatter: {path}')
    out = []
    i = 0
    done = set()
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^([A-Za-z_][\w]*):', line)
        if m and m.group(1) in updates:
            k = m.group(1)
            # skip block list continuation
            j = i + 1
            while j < len(lines) and re.match(r'^\s+-\s', lines[j]):
                j += 1
            out.append(f'{k}: {fmt_value(updates[k])}')
            done.add(k)
            i = j
            continue
        out.append(line)
        i += 1
    new_keys = [k for k in updates if k not in done]
    if new_keys:
        ins = [f'{k}: {fmt_value(updates[k])}' for k in new_keys]
        idx = None
        if after:
            for n, line in enumerate(out):
                if re.match(rf'^{re.escape(after)}:', line):
                    idx = n + 1
                    while idx < len(out) and re.match(r'^\s+-\s', out[idx]):
                        idx += 1
                    break
        if idx is None:
            out.extend(ins)
        else:
            out[idx:idx] = ins
    write(path, '---\n' + '\n'.join(out) + '\n---\n' + body)


def pages(sub=None):
    """(relpath_without_ext, abs_path) for all wiki md pages (optionally one subdir)."""
    pat = os.path.join(WIKI, sub, '*.md') if sub else os.path.join(WIKI, '**', '*.md')
    for p in sorted(glob.glob(pat, recursive=not sub)):
        rel = os.path.relpath(p, WIKI).replace('\\', '/')[:-3]
        yield rel, p


def sections(body):
    """{heading_text: content} for ## and ### headings (code blocks stripped)."""
    b = re.sub(r'```.*?```', '', body, flags=re.S)
    parts = re.split(r'^(#{2,3} .+)$', b, flags=re.M)
    d = {}
    for i in range(1, len(parts), 2):
        d[parts[i].lstrip('# ').strip()] = parts[i + 1]
    return d


def parse_date(v):
    if not v:
        return None
    s = str(v)[:10]
    for f in ('%Y-%m-%d', '%Y-%m', '%Y'):
        try:
            return datetime.datetime.strptime(s, f).date()
        except ValueError:
            pass
    return None
