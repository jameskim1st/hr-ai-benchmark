#!/usr/bin/env python3
"""
v3: markdown→HTML 변환 + headline 추출 + company 전략 추출
"""
import os, re, json, yaml
from pathlib import Path

BASE = Path(__file__).parent.parent
UC_DIR = BASE / "wiki" / "usecases"
CO_DIR = BASE / "wiki" / "companies"
OUT = BASE / "wiki" / "exports" / "usecases.json"
CO_OUT = BASE / "wiki" / "exports" / "companies.json"

# ── Markdown → HTML 변환 ──
def md2html(text):
    if not text:
        return ''
    # **bold** → <strong>
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # *italic* (single) → <em>
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    # ⚠️ 등 이모지 접두사는 유지
    # [[wikilinks]] 제거
    text = re.sub(r'\[\[([^\]|]+)\|?[^\]]*\]\]', r'\1', text)
    # `code` → <code>
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # bullet lists: "- item" → <li>
    lines = text.split('\n')
    out = []
    in_list = False
    for line in lines:
        stripped = line.strip()
        if re.match(r'^[-*]\s+', stripped):
            if not in_list:
                out.append('<ul>')
                in_list = True
            item = re.sub(r'^[-*]\s+', '', stripped)
            out.append(f'<li>{item}</li>')
        else:
            if in_list:
                out.append('</ul>')
                in_list = False
            if stripped:
                out.append(stripped)
            elif out and out[-1] != '<br>':
                out.append('<br>')
    if in_list:
        out.append('</ul>')
    return '\n'.join(out)

# ── 섹션 추출 ──
def section_text(body, heading, max_lines=10):
    patterns = [
        rf"^###?\s+.*{re.escape(heading)}.*$",
        rf"^##\s+{re.escape(heading)}.*$",
    ]
    for pat in patterns:
        m = re.search(pat, body, re.MULTILINE | re.IGNORECASE)
        if m:
            start = m.end()
            lines = body[start:].split("\n")
            result = []
            for line in lines[1:]:
                if re.match(r'^#{1,3}\s+', line):
                    break
                stripped = line.strip()
                if stripped and not stripped.startswith('```'):
                    result.append(stripped)
                if len(result) >= max_lines:
                    break
            return '\n'.join(result)
    return ''

def extract_bullets(body, heading, keys):
    text = section_text(body, heading, max_lines=25)
    if not text:
        return {}
    result = {}
    for key in keys:
        pat = rf'\*\*{re.escape(key)}\*\*[:\s]*(.+?)(?:\n|$)'
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            val = m.group(1).strip()
            val = re.sub(r'\[\[.*?\]\]', '', val)
            val = re.sub(r'[✅⚠️❓🚫🔴]', '', val).strip()
            val = re.sub(r'\*\*(.+?)\*\*', r'\1', val)  # remove bold
            if val and '미공개' not in val[:15]:
                result[key] = val[:250]
    return result

def _clean_step(s):
    """Step 문자열 정제 — bold·wikilink·이모지·연속 공백·leading colon/bullet 제거.
    너무 짧거나(<3) 너무 길면(>120) None.
    'Label: -' 처럼 본문이 빈 dash인 경우 Label만 사용."""
    s = s.strip()
    s = re.sub(r'\[\[.*?\]\]', '', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'[✅⚠️❓🚫🔴📌]', '', s)
    # sub-bullet leak: 'Label: - sub' → 'Label: sub' (leading '- ' 후속에서 stripped)
    s = re.sub(r':\s*[-*•]\s*', ': ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'^[-*•]\s*', '', s)
    s = re.sub(r'^[:：]\s*', '', s)
    s = re.sub(r'\s*[:：]\s*$', '', s)
    # trailing dangling dash/punctuation
    s = re.sub(r'\s*[-—–]\s*$', '', s).strip()
    # 'Label: -' 같이 본문이 빈 케이스 → Label만 사용
    if re.search(r':\s*[-—–]?\s*$', s):
        s = re.sub(r'\s*[:：]\s*[-—–]?\s*$', '', s).strip()
    if not s or len(s) < 3 or len(s) > 120:
        return None
    # 의미 없는 단순 punctuation·dash·digit-only 케이스
    if re.match(r'^[\s\-—–:_.\d]+$', s):
        return None
    return s


def extract_process(body):
    before = ''
    after_steps = []
    # Before — `**Before**` 또는 `**Before (any)**`
    m = re.search(
        r'\*\*Before(?:\s*\([^)]*\))?\*\*[:\s]*(.+?)(?=\*\*After|\n\*\*|\n###|\n##)',
        body, re.DOTALL | re.IGNORECASE
    )
    if m:
        before = m.group(1).strip()
        before = re.sub(r'\[\[.*?\]\]', '', before)
        before = re.sub(r'\n\s*[-*]\s*', ' / ', before)
        before = re.sub(r'\*\*(.+?)\*\*', r'\1', before)
        before = before[:400]

    # After — `**After**` 또는 `**After (anything: To-be / 7 phases / 파일럿 / 추진 중 / 제안 architecture 등)**`
    m = re.search(
        r'\*\*After(?:\s*\([^)]*\))?\*\*[:\s]*(.+?)(?=\*\*Human|\*\*Trigger|\*\*Scope|\*\*HITL|\*\*Frequency|\n###|\n##)',
        body, re.DOTALL | re.IGNORECASE
    )
    if m:
        at = m.group(1).strip()
        at = re.sub(r'\[\[.*?\]\]', '', at)  # wikilink의 "01." 같은 가짜 step 매칭 방지

        # Pattern 1: numbered list (1. ... 2. ...) — bold label과 본문 모두 캡처
        steps = re.findall(
            r'^\s*\d+\.\s*(\*\*[^*]+\*\*)?\s*[:：]?\s*(.*?)(?=\n\s*\d+\.|\n\*\*[A-Z가-힣]|\n###|\n##|$)',
            at, re.DOTALL | re.MULTILINE
        )
        if steps:
            for bold, text in steps[:8]:
                first_line = (text or '').strip().split('\n')[0].strip()
                # 본문 첫 줄이 비어있으면(콜론·줄바꿈만) bold label로 fallback
                if not first_line and bold:
                    first_line = bold.strip('*: \t')
                # bold + 본문 둘 다 있으면 "Bold: 본문" 형태로 결합 (의미 보존)
                elif first_line and bold:
                    label = bold.strip('*: \t')
                    if label and label.lower() not in first_line.lower():
                        first_line = f'{label}: {first_line}'
                cleaned = _clean_step(first_line)
                if cleaned:
                    after_steps.append(cleaned)

        # Pattern 2: top-level bullets (`- item`) — numbered 없을 때만
        if not after_steps:
            for line in at.split('\n'):
                stripped = line.lstrip()
                # top-level bullet only (no leading whitespace)
                if line == stripped and re.match(r'^[-*]\s+', stripped):
                    item = re.sub(r'^[-*]\s+', '', stripped)
                    cleaned = _clean_step(item.split('\n')[0])
                    if cleaned:
                        after_steps.append(cleaned)
                if len(after_steps) >= 8:
                    break

        # Pattern 3: arrow-separated narrative ("X → Y → Z")
        if not after_steps and ('→' in at or '->' in at):
            # 첫 줄만 사용 (narrative 가정)
            first_line = at.split('\n')[0].strip()
            parts = re.split(r'\s*[→]\s*|\s*->\s*', first_line)
            for p in parts[:8]:
                cleaned = _clean_step(p)
                if cleaned:
                    after_steps.append(cleaned)

    # Pattern 4: Mermaid fallback
    if not after_steps:
        mermaids = re.findall(r'```mermaid\s*\n(.*?)```', body, re.DOTALL)
        for mc in mermaids[:1]:
            seen = set()
            # subgraph 라벨 제외하기 위해 라인 단위로 처리, subgraph 라인은 skip
            for line in mc.split('\n'):
                if re.match(r'\s*subgraph\b', line) or re.match(r'\s*end\s*$', line):
                    continue
                for mm in re.finditer(r'\[([^\]"]+)\]|\["([^"]+)"\]', line):
                    txt = mm.group(1) or mm.group(2)
                    # mermaid 내 줄바꿈 표기 (\n 리터럴 + <br/>) → 공백
                    txt = re.sub(r'<br\s*/?>', ' ', txt)
                    txt = txt.replace('\\n', ' ').replace('\n', ' ')
                    txt = re.sub(r'\s+', ' ', txt).strip()
                    cleaned = _clean_step(txt)
                    if cleaned and cleaned not in seen:
                        seen.add(cleaned)
                        after_steps.append(cleaned)
            if after_steps:
                break

    # Pattern 5: top-level bullets in Process section (Before/After 없는 케이스)
    # Solution Architecture 또는 ## Process 섹션에서 first-level bullet 추출
    if not after_steps:
        for sec_name in ['Process', 'Solution Architecture']:
            sec = section_text(body, sec_name, max_lines=30)
            if not sec:
                continue
            for line in sec.split('\n'):
                stripped = line.lstrip()
                if line == stripped and re.match(r'^[-*]\s+\*\*', stripped):
                    # `- **Label**: desc` 형태 — Label만 사용
                    m2 = re.match(r'^[-*]\s+\*\*([^*]+)\*\*[:\s]', stripped)
                    if m2:
                        cleaned = _clean_step(m2.group(1))
                        if cleaned and cleaned.lower() not in {'before', 'after', 'hitl', 'frequency', 'scope of autonomy', 'trigger', 'human-in-the-loop'}:
                            after_steps.append(cleaned)
                if len(after_steps) >= 8:
                    break
            if after_steps:
                break

    return before, after_steps[:8]

def headline(summary):
    """Summary에서 use case가 어떤 서비스/과제인지 이해하기 쉽도록
    2~3 문장 (최대 400자) 추출. 잘린 문장 회피."""
    if not summary:
        return ''
    text = summary.replace('\n', ' ')
    # 마크다운 제거
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\[\[.*?\]\]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    # 문장 단위로 분할 — 마침표는 뒤에 공백 또는 줄끝일 때만 (1.5B·A.I 등 보호)
    sentences = re.findall(r'.+?(?:[.!?。](?=\s|$)|[!?。])', text)
    if not sentences:
        return text[:400]
    # 2~3 문장 누적, 400자 한도
    out = ''
    for s in sentences[:4]:
        candidate = (out + ' ' + s.strip()).strip() if out else s.strip()
        if len(candidate) > 400 and out:
            break
        out = candidate
        if len(out) >= 250:
            break
    return out[:400]

# ── Use Case 처리 ──
def process_uc(fp):
    content = fp.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return None
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except:
        return None
    if not fm.get('title'):
        return None
    body = parts[2].strip()

    d = {
        'slug': fm.get('slug', fp.stem),
        'title': fm.get('title', ''),
        'primary_category': fm.get('primary_category', ''),
        'subcategory': fm.get('subcategory', ''),
        'company': fm.get('company', ''),
        'industry': fm.get('industry', []),
        'region': fm.get('region', []),
        'employee_class': fm.get('employee_class', []),
        'vendor': fm.get('vendor', []),
        'vendor_type': fm.get('vendor_type', []),
        'ai_tech_type': fm.get('ai_tech_type', []),
        'ai_tech_subtype': fm.get('ai_tech_subtype', []),
        'confidence': 0.0,
        'stage': fm.get('stage', ''),
        'frequency': fm.get('frequency', ''),
        'first_seen': str(fm.get('first_seen', '')),
        'last_confirmed': str(fm.get('last_confirmed', '')),
        'output': fm.get('output', ''),
        'tags': fm.get('tags', []),
        'sources': [str(s) for s in (fm.get('sources') or [])],
    }
    for f in ['industry','region','employee_class','vendor','vendor_type','ai_tech_type','ai_tech_subtype','tags','sources']:
        if isinstance(d[f], str): d[f] = [d[f]]
        elif not isinstance(d[f], list): d[f] = []
    try: d['confidence'] = float(fm.get('confidence', 0))
    except: pass

    # Summary는 Excel 개요·HTML 양쪽에서 사용 — bullet/줄바꿈 보존 위해 충분히 크게
    raw_summary = section_text(body, 'Summary', 20)
    d['summary'] = md2html(raw_summary)
    d['headline'] = headline(raw_summary)
    d['problem'] = md2html(section_text(body, 'Problem', 6))

    m = re.search(r'###\s+기대효과 요약\s*\n(.+)', body)
    d['impact_summary'] = md2html(m.group(1).strip()) if m else ''

    d['consulting'] = md2html(section_text(body, 'Consulting Angle', 4))

    sys_keys = ['Core HRIS', 'AI 시스템 배치', '배포 환경', '연동·통합', '사용자 접점', '인증·권한']
    d['system'] = extract_bullets(body, 'System', sys_keys)
    if not d['system']:
        d['system'] = extract_bullets(body, 'Infrastructure', sys_keys)

    data_keys = ['입력 데이터 소스', '데이터 규모', '전처리·정제', '학습 vs RAG', '데이터 거버넌스', '민감정보 처리']
    d['data'] = extract_bullets(body, 'Data', data_keys)

    model_keys = ['Foundation model', '모델 유형', '제공 방식', '커스터마이징 기법', 'Orchestration', '평가·가드레일']
    d['model'] = extract_bullets(body, 'Model', model_keys)

    before, after_steps = extract_process(body)
    d['process_before'] = md2html(before) if before else ''
    d['process_steps'] = after_steps

    return d

# ── Company 처리 ──
def process_co(fp):
    content = fp.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return None
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except:
        return None
    body = parts[2].strip()

    d = {
        'slug': fp.stem,
        'name': fm.get('name', fp.stem),
        'industry': fm.get('industry', []),
        'region': fm.get('region', []),
        'size': fm.get('size_employees', ''),
    }
    if isinstance(d['industry'], str): d['industry'] = [d['industry']]
    if isinstance(d['region'], str): d['region'] = [d['region']]

    # 본문 첫 단락 (# 제목 다음)
    lines = body.split('\n')
    desc_lines = []
    started = False
    for line in lines:
        if line.startswith('# '):
            started = True
            continue
        if started:
            if line.startswith('## ') or line.startswith('```'):
                break
            stripped = line.strip()
            if stripped:
                desc_lines.append(stripped)
            if len(desc_lines) >= 3:
                break
    d['description'] = md2html('\n'.join(desc_lines))

    # HR AI 전략 / 핵심 수치 / Consulting Angle
    strategy = section_text(body, 'HR AI', 6)
    if not strategy:
        strategy = section_text(body, '핵심', 6)
    d['strategy'] = md2html(strategy)

    ca = section_text(body, 'Consulting Angle', 6)
    d['consulting'] = md2html(ca)

    return d

# ── Main ──
def main():
    # Use cases
    ucs = []
    for fp in sorted(UC_DIR.glob('*.md')):
        r = process_uc(fp)
        if r:
            ucs.append(r)
    ucs.sort(key=lambda x: -x['confidence'])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(ucs, f, ensure_ascii=False, indent=2)
    print(f"Use cases: {len(ucs)} -> {OUT.stat().st_size/1024:.0f}KB")

    # Companies
    cos = []
    for fp in sorted(CO_DIR.glob('*.md')):
        r = process_co(fp)
        if r:
            cos.append(r)
    with open(CO_OUT, 'w', encoding='utf-8') as f:
        json.dump(cos, f, ensure_ascii=False, indent=2)
    print(f"Companies: {len(cos)} -> {CO_OUT.stat().st_size/1024:.0f}KB")

    # Stats
    has_hl = sum(1 for u in ucs if u.get('headline'))
    has_sys = sum(1 for u in ucs if u.get('system'))
    has_data = sum(1 for u in ucs if u.get('data'))
    has_model = sum(1 for u in ucs if u.get('model'))
    has_steps = sum(1 for u in ucs if u.get('process_steps'))
    has_tech = sum(1 for u in ucs if u.get('ai_tech_type'))
    has_subtype = sum(1 for u in ucs if u.get('ai_tech_subtype'))
    has_co_str = sum(1 for c in cos if c.get('strategy'))
    print(f"Headlines: {has_hl}, System: {has_sys}, Data: {has_data}, Model: {has_model}, Steps: {has_steps}")
    print(f"AI tech type: {has_tech}/{len(ucs)}, subtype: {has_subtype}/{len(ucs)}")
    print(f"Companies with strategy: {has_co_str}/{len(cos)}")

if __name__ == '__main__':
    main()
