#!/usr/bin/env python3
"""
build_index.py — wiki/index.md 를 데이터에서 생성한다 (손글씨 카운트 금지).

- 상단 요약 카운트(use case·source·company·vendor·enterprise-ai·reference·synthesis)와 근거 등급·depth 분포
- 대그룹별 Dataview 블록(Obsidian에서 자동 표) + Dataview 없이도 보이도록 정적 목록(슬러그·회사·등급)
- companies / vendors / enterprise-ai / reference / syntheses 목록
index가 150페이지를 넘는 카테고리는 categories/0N 페이지로 샤딩되어 있으므로 index에는 상위 20건만 싣는다.
"""
import os, sys, collections, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wikilib as w


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    data = collections.defaultdict(list)
    for rel, p in w.pages():
        fm, body, _ = w.load(p)
        sub = rel.split('/')[0] if '/' in rel else ''
        data[sub].append((rel, fm or {}))
    uc = data['usecases']
    grade = collections.Counter(f.get('evidence_grade', '?') for _, f in uc)
    depth = collections.Counter(f.get('depth', '?') for _, f in uc)
    fresh = collections.Counter(f.get('freshness', '?') for _, f in uc)
    public = sum(1 for _, f in uc if f.get('visibility') != 'internal')
    kr = sum(1 for _, f in uc if 'kr' in (f.get('region') or []))
    L = []
    L.append('# HR AI Benchmark — Index\n')
    L.append(f'> 이 페이지는 `scripts/build_index.py`가 생성한다 (마지막 생성 {w.TODAY.isoformat()}). 손으로 편집하지 말 것. 규칙은 [[CLAUDE|CLAUDE.md]] + `.claude/rules/`.\n')
    L.append('## 규모\n')
    L.append('| 유형 | 건수 | 비고 |\n|---|---|---|')
    L.append(f"| use case (HR 프로세스 AI 도입 사례) | **{len(uc)}** | public {public} · KR {kr} |")
    L.append(f"| enterprise-ai (전사 GenAI 플랫폼 — 참고) | {len(data['enterprise-ai'])} | use case 카운트에서 제외 |")
    L.append(f"| reference (법령·리포트·맥락) | {len(data['reference'])} | |")
    L.append(f"| sources | {len(data['sources'])} | raw 스냅샷 연결 {sum(1 for _, f in data['sources'] if f.get('raw'))} |")
    L.append(f"| companies / vendors | {len(data['companies'])} / {len(data['vendors'])} | |")
    L.append(f"| syntheses | {len(data['syntheses'])} | lint·digest·compare·research 포함 |")
    L.append('')
    L.append(f"근거 등급: A {grade['A']} · B {grade['B']} · C {grade['C']} · D {grade['D']}  ｜  depth: full {depth['full']} · partial {depth['partial']} · stub {depth['stub']}  ｜  freshness: fresh {fresh['fresh']} · stale {fresh['stale']} · unverified {fresh['unverified']}\n")
    L.append('등급 정의: **A** 독립(Tier 1·2) 소스 2개 이상 · **B** 독립 1개 · **C** 벤더·자사 보고만 · **D** 미검증/소스 없음. 제안서 인용은 A·B + depth full 권장.\n')
    L.append('## 🧭 진입점\n')
    L.append('- 📖 [[guide]] · 📤 [[guide-html-export]] · 📋 [[dashboard]] · 🔎 [[taxonomy-crosswalk]] (SHRM·Bersin·AIHR 대응표)')
    L.append('- 📚 카테고리: ' + ' · '.join(f'[[{r.split("/")[-1]}]]' for r, _ in sorted(data['categories'])))
    L.append('- 🛠 운영: `/hr-ingest` `/hr-lint` `/hr-verify` `/hr-research` `/hr-digest` `/hr-compare` · 빌드 `python scripts/build_all.py`\n')
    L.append('## 📊 카테고리별 Use Cases\n')
    L.append('```dataview\nTABLE WITHOUT ID primary_category AS "카테고리", length(rows) AS "건수", length(filter(rows, (r) => r.evidence_grade = "A" OR r.evidence_grade = "B")) AS "A·B 등급"\nFROM "wiki/usecases"\nGROUP BY primary_category\nSORT length(rows) DESC\n```\n')
    for i, cat in enumerate(w.CATS, 1):
        items = sorted([(r, f) for r, f in uc if f.get('primary_category') == cat], key=lambda x: (x[1].get('evidence_grade', 'Z'), -float(x[1].get('confidence') or 0)))
        L.append(f'### {i}. {cat} ({len(items)}건)\n')
        L.append(f'```dataview\nTABLE WITHOUT ID file.link AS "Use Case", company AS "기업", vendor AS "벤더", evidence_grade AS "등급", depth AS "depth", region AS "지역"\nFROM "wiki/usecases"\nWHERE primary_category = "{cat}"\nSORT evidence_grade ASC, confidence DESC\n```\n')
        L.append('<details><summary>정적 목록 (Dataview 없을 때)</summary>\n')
        for r, f in items[:40]:
            slug = r.split('/')[-1]
            L.append(f"- [[{slug}]] — {f.get('company', '')} · {f.get('evidence_grade', '?')}/{f.get('depth', '?')}" + (' · 🔒' if f.get('visibility') == 'internal' else ''))
        if len(items) > 40:
            L.append(f'- … +{len(items) - 40} (카테고리 페이지 참조)')
        L.append('\n</details>\n')
    def listing(title, key, fmt):
        L.append(f'## {title} ({len(data[key])})\n')
        for r, f in sorted(data[key]):
            L.append(fmt(r, f))
        L.append('')
    listing('🏢 Companies', 'companies', lambda r, f: f"- [[{r.split('/')[-1]}]]")
    listing('🧩 Vendors', 'vendors', lambda r, f: f"- [[{r.split('/')[-1]}]]")
    listing('🏗 Enterprise-AI (전사 GenAI 플랫폼 — HR 전용 use case 아님)', 'enterprise-ai', lambda r, f: f"- [[{r.split('/')[-1]}]] — {f.get('company', '')} · {f.get('evidence_grade', '?')}")
    listing('📜 Reference (법령·리포트·맥락)', 'reference', lambda r, f: f"- [[{r.split('/')[-1]}]] — {f.get('reference_type', '')}")
    L.append(f"## 🧪 Syntheses ({len(data['syntheses'])})\n")
    for r, f in sorted(data['syntheses'], key=lambda x: str(x[1].get('generated_at', '')), reverse=True):
        L.append(f"- [[{r.split('/')[-1]}]] — {f.get('type', '')} · {f.get('generated_at', '')}")
    L.append('')
    L.append(f"## 📚 Sources ({len(data['sources'])})\n")
    L.append('```dataview\nTABLE WITHOUT ID file.link AS "Source", tier AS "Tier", publisher AS "Publisher", publication_date AS "발행", snapshot_quality AS "raw"\nFROM "wiki/sources"\nWHERE !deprecated\nSORT publication_date DESC\n```\n')
    w.write(os.path.join(w.WIKI, 'index.md'), '\n'.join(L))
    print(f"index.md written: usecases {len(uc)}, sources {len(data['sources'])}, enterprise-ai {len(data['enterprise-ai'])}, reference {len(data['reference'])}")


if __name__ == '__main__':
    main()
