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

def extract_process(body):
    before = ''
    after_steps = []
    # Before — match both "**Before**" and "**Before (As-is)**"
    m = re.search(r'\*\*Before(?:\s*\(As-is\))?\*\*[:\s]*(.+?)(?=\*\*After|\n\*\*|\n###|\n##)', body, re.DOTALL | re.IGNORECASE)
    if m:
        before = m.group(1).strip()
        before = re.sub(r'\n\s*[-*]\s*', ' / ', before)
        before = re.sub(r'\*\*(.+?)\*\*', r'\1', before)
        before = before[:400]
    # After steps — match both "**After**" and "**After (To-be)**"
    m = re.search(r'\*\*After(?:\s*\(To-be\))?\*\*[:\s]*(.+?)(?=\*\*Human|\*\*Trigger|\*\*Scope|\*\*HITL|\*\*Frequency|\n###|\n##)', body, re.DOTALL | re.IGNORECASE)
    if m:
        at = m.group(1).strip()
        steps = re.findall(r'\d+\.\s*(?:\*\*[^*]+\*\*\s*)?(.+?)(?=\n\s*\d+\.|\n\*\*|\n###|\n##|$)', at, re.DOTALL)
        if steps:
            for s in steps[:8]:
                step = s.strip().split('\n')[0]
                step = re.sub(r'\*\*(.+?)\*\*', r'\1', step)
                step = re.sub(r'\[\[.*?\]\]', '', step)
                step = re.sub(r'[✅⚠️❓]', '', step).strip()
                if step and len(step) < 100:
                    after_steps.append(step)
    # Mermaid fallback
    if not after_steps:
        mermaids = re.findall(r'```mermaid\s*\n(.*?)```', body, re.DOTALL)
        for mc in mermaids[:1]:
            for mm in re.finditer(r'\[([^\]"]+)\]|\["([^"]+)"\]', mc):
                txt = mm.group(1) or mm.group(2)
                txt = re.sub(r'<br/?>', ' ', txt).strip()
                if txt and len(txt) < 80:
                    after_steps.append(txt)
            if after_steps:
                break
    return before, after_steps[:8]

def headline(summary):
    """Summary에서 첫 문장을 headline으로 추출"""
    if not summary:
        return ''
    # 첫 문장 (마침표·느낌표·물음표까지)
    m = re.match(r'(.+?[.!?。])', summary.replace('\n', ' '))
    if m:
        h = m.group(1).strip()
        # 마크다운 제거
        h = re.sub(r'\*\*(.+?)\*\*', r'\1', h)
        h = re.sub(r'\[\[.*?\]\]', '', h)
        return h[:150]
    return summary.split('\n')[0][:150]

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
        'tags': fm.get('tags', []),
    }
    for f in ['industry','region','employee_class','vendor','vendor_type','ai_tech_type','ai_tech_subtype','tags']:
        if isinstance(d[f], str): d[f] = [d[f]]
        elif not isinstance(d[f], list): d[f] = []
    try: d['confidence'] = float(fm.get('confidence', 0))
    except: pass

    raw_summary = section_text(body, 'Summary', 4)
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
