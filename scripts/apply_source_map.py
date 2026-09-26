#!/usr/bin/env python3
"""
apply_source_map.py — 소스 재구축 에이전트들의 mapping JSON을 use case frontmatter에 적용한다 (2026-09-27 일회성 + 재실행 가능).

입력: scratchpad의 map_S1..S5.json  (각 항목: ref, source_slug|null, used_by[], note)
동작:
  1. 각 use case의 sources 목록에서 mapping에 있는 ref 문자열을 `sources/<slug>.md`로 치환. null이면 제거하고 `sources_unresolved:` 리스트에 보존.
  2. compilation source(4개)를 인용한 use case는 mapping의 used_by/supports 정보로 개별 source로 교체. compilation 페이지는 `deprecated: true`, `superseded_by:` 기록.
  3. source 페이지의 `supports:`에 자기를 인용하는 use case를 역주입(빠진 것만).
"""
import os, re, sys, json, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wikilib as w

COMP = ['kr-conglomerate-2026-q2-research', 'korea-conglomerate-hr-ai-2025-2026', 'us-large-enterprise-hr-ai-2025-2026', 'ibm-hr-ai-portfolio-2025-2026']


def main(map_dir):
    sys.stdout.reconfigure(encoding='utf-8')
    entries = []
    for f in sorted(glob.glob(os.path.join(map_dir, 'map_S*.json'))):
        try:
            entries += json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print('bad map file', f, e)
    ref2slug = {}
    comp_users = collections.defaultdict(lambda: collections.defaultdict(set))  # usecase -> set(slugs) from compilation decomposition
    ibm = collections.defaultdict(set)
    for e in entries:
        ref = (e.get('ref') or '').strip()
        slug = e.get('source_slug')
        if slug and not os.path.exists(os.path.join(w.WIKI, 'sources', slug + '.md')):
            print('  mapping points to missing source page:', slug); slug = None
        if ref.startswith('ibm:'):
            if slug: ibm[ref[4:]].add(slug)
            continue
        if ref.startswith('http') and e.get('used_by'):
            for u in e['used_by']:
                if slug: comp_users[u]['x'].add(slug)
        ref2slug[ref] = slug
        for u in e.get('used_by') or []:
            if slug: comp_users[u]['x'].add(slug)
    existing = {os.path.basename(p)[:-3] for p in glob.glob(os.path.join(w.WIKI, 'sources', '*.md'))}
    changed = 0; unresolved_total = 0
    for sub in ('usecases', 'enterprise-ai', 'reference'):
        for rel, p in w.pages(sub):
            fm, body, _ = w.load(p)
            slug = rel.split('/')[-1]
            srcs = fm.get('sources') or []
            srcs = [srcs] if isinstance(srcs, str) else srcs
            new = []; unresolved = list(fm.get('sources_unresolved') or []) if isinstance(fm.get('sources_unresolved'), list) else []
            touched = False
            for s in srcs:
                s_clean = s.strip().strip('"')
                base = s_clean.replace('sources/', '').replace('.md', '').strip()
                if base in existing and base not in COMP:
                    new.append(f'sources/{base}.md'); continue
                if base in COMP:
                    adds = sorted(comp_users.get(slug, {}).get('x', set()) | ibm.get(slug, set()))
                    if adds:
                        new += [f'sources/{a}.md' for a in adds]; touched = True
                    else:
                        new.append(f'sources/{base}.md')  # keep deprecated link if nothing replaced it
                    continue
                m = ref2slug.get(s_clean)
                if m is None:
                    # try URL match
                    u = re.search(r'https?://\S+', s_clean)
                    if u and u.group(0) in ref2slug: m = ref2slug[u.group(0)]
                if m:
                    new.append(f'sources/{m}.md'); touched = True
                else:
                    if s_clean not in unresolved: unresolved.append(s_clean)
                    touched = True
            # dedupe keep order
            seen = set(); new2 = []
            for x in new:
                if x not in seen: seen.add(x); new2.append(x)
            if touched or new2 != srcs:
                upd = {'sources': new2}
                if unresolved: upd['sources_unresolved'] = unresolved
                w.set_fields(p, upd); changed += 1
                unresolved_total += len(unresolved)
    # deprecate compilations
    for c in COMP:
        p = os.path.join(w.WIKI, 'sources', c + '.md')
        if os.path.exists(p):
            fm, _, _ = w.load(p)
            if not fm.get('deprecated'):
                w.set_fields(p, {'deprecated': True, 'deprecated_note': '2026-09-27 개별 source 페이지로 분해됨 — 링크 해석용으로만 유지, 인용 금지', 'independent': False})
    # back-fill supports
    cites = collections.defaultdict(set)
    for sub in ('usecases', 'enterprise-ai', 'reference'):
        for rel, p in w.pages(sub):
            fm, _, _ = w.load(p)
            for s in (fm.get('sources') or []):
                cites[s.replace('sources/', '').replace('.md', '')].add(rel.split('/')[-1])
    for rel, p in w.pages('sources'):
        fm, _, _ = w.load(p)
        cur = fm.get('supports') or []
        cur = [cur] if isinstance(cur, str) else cur
        want = sorted(set(cur) | cites.get(rel.split('/')[-1], set()))
        if want != cur and want:
            w.set_fields(p, {'supports': want})
    print(f'usecases changed: {changed}; unresolved refs kept in sources_unresolved: {unresolved_total}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
