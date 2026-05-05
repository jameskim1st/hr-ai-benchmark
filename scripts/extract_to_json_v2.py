#!/usr/bin/env python3
"""
v2: System/Data/Model + Process Before/After 상세 추출
"""
import os, re, json, yaml
from pathlib import Path

DIR = Path(__file__).parent.parent / "wiki" / "usecases"
OUT = Path(__file__).parent.parent / "wiki" / "exports" / "usecases.json"

def parse_fm(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1]) or {}, parts[2].strip()
            except: pass
    return {}, content

def section_text(body, heading, max_lines=8):
    """## 또는 ### 헤딩 아래 텍스트 추출 (다음 ##/### 전까지)"""
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
                if stripped:
                    result.append(stripped)
                if len(result) >= max_lines:
                    break
            return "\n".join(result)
    return ""

def extract_bullets(body, heading, keys):
    """특정 헤딩 아래에서 **key**: value 형식의 bullet을 딕셔너리로 추출"""
    text = section_text(body, heading, max_lines=20)
    if not text:
        return {}
    result = {}
    for key in keys:
        pat = rf'\*\*{re.escape(key)}\*\*[:\s]*(.+?)(?:\n|$)'
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            val = m.group(1).strip()
            val = re.sub(r'\[\[.*?\]\]', '', val)  # wikilinks 제거
            val = re.sub(r'[✅⚠️❓🚫]', '', val).strip()
            if val and val != '_미공개_' and '미공개' not in val[:10]:
                result[key] = val[:200]
    return result

def extract_process_before_after(body):
    """Before (As-is)와 After (To-be)를 추출"""
    before = ""
    after = ""

    # Before 추출
    m = re.search(r'\*\*Before\s*\(As-is\)\*\*[:\s]*(.+?)(?=\*\*After|\n\*\*|\n###|\n##)', body, re.DOTALL | re.IGNORECASE)
    if m:
        before = m.group(1).strip()
        before = re.sub(r'\n\s*-\s*', ' / ', before)
        before = before[:300]

    # After 추출
    m = re.search(r'\*\*After\s*\(To-be\)\*\*[:\s]*(.+?)(?=\*\*Human|\*\*Trigger|\*\*Scope|\n###|\n##)', body, re.DOTALL | re.IGNORECASE)
    if m:
        after_text = m.group(1).strip()
        # 번호 목록 추출
        steps = re.findall(r'\d+\.\s*(?:\*\*[^*]+\*\*\s*)?(.+?)(?=\n\s*\d+\.|\n\*\*|\n###|\n##|$)', after_text, re.DOTALL)
        if steps:
            after = " → ".join([s.strip().split('\n')[0][:80] for s in steps[:6]])
        else:
            after = after_text.split('\n')[0][:300]

    return before, after

def extract_mermaid_steps(mermaid_code):
    """Mermaid에서 노드 텍스트를 순서대로 추출"""
    if not mermaid_code:
        return []
    steps = []
    for m in re.finditer(r'\[([^\]"]+)\]|\["([^"]+)"\]', mermaid_code):
        text = m.group(1) or m.group(2)
        text = re.sub(r'<br/?>', ' ', text).strip()
        if text and text not in steps and len(text) < 80 and not text.startswith('style'):
            steps.append(text)
    return steps[:10]

def process_file(fp):
    content = fp.read_text(encoding='utf-8')
    fm, body = parse_fm(content)
    if not fm.get('title'):
        return None

    d = {
        'slug': fm.get('slug', fp.stem),
        'title': fm.get('title', ''),
        'primary_category': fm.get('primary_category', ''),
        'subcategory': fm.get('subcategory', ''),
        'company': fm.get('company', ''),
        'industry': fm.get('industry', []),
        'region': fm.get('region', []),
        'vendor': fm.get('vendor', []),
        'vendor_type': fm.get('vendor_type', []),
        'confidence': fm.get('confidence', 0),
        'stage': fm.get('stage', ''),
        'tags': fm.get('tags', []),
    }

    # 리스트 정규화
    for f in ['industry','region','vendor','vendor_type','tags']:
        if isinstance(d[f], str): d[f] = [d[f]]
        elif not isinstance(d[f], list): d[f] = []

    try: d['confidence'] = float(d['confidence'])
    except: d['confidence'] = 0.0

    # Summary + Problem + Impact + Consulting
    d['summary'] = section_text(body, 'Summary', 3)
    d['problem'] = section_text(body, 'Problem', 5)

    # 기대효과 요약
    m = re.search(r'###\s+기대효과 요약\s*\n(.+)', body)
    d['impact_summary'] = m.group(1).strip() if m else ''

    d['consulting'] = section_text(body, 'Consulting Angle', 3)

    # ★ System & Infrastructure
    sys_keys = ['Core HRIS', 'AI 시스템 배치', '배포 환경', '연동·통합', '사용자 접점', '인증·권한']
    d['system'] = extract_bullets(body, 'System', sys_keys)
    # 영문 variant
    if not d['system']:
        d['system'] = extract_bullets(body, 'Infrastructure', sys_keys)

    # ★ Data
    data_keys = ['입력 데이터 소스', '데이터 규모', '전처리·정제', '학습 vs RAG', '데이터 거버넌스', '민감정보 처리']
    d['data'] = extract_bullets(body, 'Data', data_keys)

    # ★ Model
    model_keys = ['Foundation model', '모델 유형', '제공 방식', '커스터마이징 기법', 'Orchestration', '평가·가드레일']
    d['model'] = extract_bullets(body, 'Model', model_keys)

    # ★ Process Before/After
    before, after = extract_process_before_after(body)
    d['process_before'] = before
    d['process_after'] = after

    # ★ Process steps (from Mermaid)
    steps = []
    mermaids = re.findall(r'```mermaid\s*\n(.*?)```', body, re.DOTALL)
    for mc in mermaids[:2]:
        s = extract_mermaid_steps(mc)
        if s and len(s) > len(steps):
            steps = s
    d['process_steps'] = steps

    return d

def main():
    files = sorted(DIR.glob("*.md"))
    print(f"Processing {len(files)} files")

    results = []
    for f in files:
        r = process_file(f)
        if r:
            results.append(r)
            sys_cnt = len(r.get('system', {}))
            data_cnt = len(r.get('data', {}))
            steps_cnt = len(r.get('process_steps', []))
            print(f"  {f.stem}: sys={sys_cnt} data={data_cnt} steps={steps_cnt} conf={r['confidence']}")

    results.sort(key=lambda x: -x['confidence'])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    size = OUT.stat().st_size
    print(f"\nDone: {len(results)} cases, {size/1024:.0f}KB")

    # Stats
    has_sys = sum(1 for r in results if r.get('system'))
    has_data = sum(1 for r in results if r.get('data'))
    has_model = sum(1 for r in results if r.get('model'))
    has_steps = sum(1 for r in results if r.get('process_steps'))
    has_ba = sum(1 for r in results if r.get('process_before') or r.get('process_after'))
    print(f"System info: {has_sys}/{len(results)}")
    print(f"Data info: {has_data}/{len(results)}")
    print(f"Model info: {has_model}/{len(results)}")
    print(f"Process steps: {has_steps}/{len(results)}")
    print(f"Before/After: {has_ba}/{len(results)}")

if __name__ == '__main__':
    main()
