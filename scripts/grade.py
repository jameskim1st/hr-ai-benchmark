#!/usr/bin/env python3
"""
grade.py — use case의 근거 등급·신뢰도·신선도·깊이를 결정론적으로 계산해 frontmatter에 쓴다.

용법:
  python scripts/grade.py            # 전체 계산 + 기록
  python scripts/grade.py --dry-run  # 변경 예정만 출력
  python scripts/grade.py --check    # frontmatter 값과 계산값이 다른 페이지만 출력 (exit 2)

계산 규칙 (CLAUDE.md §4 — 2026-09-27 개정):
  independent source = source 페이지 frontmatter `independent: true` (tier 1·2, academic, government)
  corroborated_by    = 서로 다른 publisher의 independent source 수
  evidence_grade     = A: independent 2+ | B: independent 1 | C: 벤더·자사 보고만 (tier 3·4) | D: source 0 또는 전부 unresolved/unavailable
  recency            = last_confirmed 기준 +0.10 (≤6개월) / 0 (≤12) / -0.10 (≤24) / -0.20 (>24)
  contradiction      = 미해결 [!contradiction] 1건당 -0.15
  confidence         = clamp(base[grade] + recency + contradiction, 0.05, 0.95)   base: A 0.70, B 0.45, C 0.25, D 0.10
  freshness          = fresh (≤12개월) | stale (>12개월) | unverified (grade D)
  depth              = full: B·C·D·E 중 3개 이상이 실질 내용 + Mermaid 1개 이상
                       partial: B·C·D·E 중 1~2개 실질 내용
                       stub: 실질 내용 0개 또는 A~E 섹션 자체가 3개 이상 없음
  '실질 내용' = 해당 섹션의 bullet 중 `미공개`·`❓`가 아닌 것이 2개 이상
"""
import os, re, sys, argparse, datetime, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wikilib as w

BASE = {'A': 0.70, 'B': 0.45, 'C': 0.25, 'D': 0.10}


def source_info():
    info = {}
    for rel, p in w.pages('sources'):
        fm, _, _ = w.load(p)
        if not fm:
            continue
        tier = str(fm.get('tier'))
        indep = fm.get('independent')
        if indep is None:
            indep = tier in ('1', '2') or fm.get('source_type') in ('academic', 'government', 'analyst', 'media')
        else:
            indep = str(indep).lower() == 'true'
        unavailable = fm.get('snapshot_quality') == 'unavailable' or fm.get('deprecated') in (True, 'true')
        info[rel.split('/')[-1]] = {'tier': tier, 'independent': bool(indep), 'publisher': str(fm.get('publisher') or fm.get('title') or rel).lower()[:40], 'unavailable': unavailable}
    return info


def section_substance(body):
    secs = w.sections(body)
    present = {k[0]: v for k, v in secs.items() if re.match(r'^[A-E]\.', k)}
    substantive = 0
    for L in 'BCDE':
        c = present.get(L)
        if not c:
            continue
        good = 0
        for line in c.split('\n'):
            ls = line.strip()
            if ls.startswith('-') and not any(x in ls for x in ('미공개', '❓', 'not disclosed')):
                if len(ls) > 25:
                    good += 1
        if good >= 2:
            substantive += 1
    return present, substantive


def compute(fm, body, sinfo):
    srcs = fm.get('sources') or []
    srcs = [srcs] if isinstance(srcs, str) else srcs
    pubs = set(); n_ind = 0; n_dep = 0; resolved = 0
    for s in srcs:
        slug = s.replace('sources/', '').replace('.md', '').strip()
        i = sinfo.get(slug)
        if not i or i['unavailable']:
            continue
        resolved += 1
        if i['independent']:
            if i['publisher'] not in pubs:
                n_ind += 1
            pubs.add(i['publisher'])
        else:
            n_dep += 1
    if resolved == 0:
        grade = 'D'
    elif n_ind >= 2:
        grade = 'A'
    elif n_ind == 1:
        grade = 'B'
    else:
        grade = 'C'
    lc = w.parse_date(fm.get('last_confirmed'))
    months = (w.TODAY - lc).days / 30.44 if lc else 99
    rec = 0.10 if months <= 6 else 0.0 if months <= 12 else -0.10 if months <= 24 else -0.20
    unresolved = len(re.findall(r'상태:\s*unresolved', body))
    conf = max(0.05, min(0.95, BASE[grade] + rec - 0.15 * unresolved))
    fresh = 'unverified' if grade == 'D' else ('fresh' if months <= 12 else 'stale')
    present, subst = section_substance(body)
    mermaid = body.count('```mermaid')
    if len(present) < 2 or subst == 0:
        depth = 'stub'
    elif subst >= 3 and mermaid >= 1:
        depth = 'full'
    else:
        depth = 'partial'
    return {'evidence_grade': grade, 'corroborated_by': n_ind, 'confidence': round(conf, 2), 'freshness': fresh, 'depth': depth,
            'graded_at': w.TODAY.isoformat()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true'); ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    sinfo = source_info()
    diffs = 0; dist = collections.Counter(); depth = collections.Counter()
    for sub in ('usecases', 'enterprise-ai'):
        for rel, p in w.pages(sub):
            fm, body, _ = w.load(p)
            if not fm:
                continue
            new = compute(fm, body, sinfo)
            dist[new['evidence_grade']] += 1; depth[new['depth']] += 1
            changed = {k: v for k, v in new.items() if k != 'graded_at' and str(fm.get(k)) != str(v)}
            if changed:
                diffs += 1
                if a.check or a.dry_run:
                    print(f"{rel}: " + ', '.join(f"{k} {fm.get(k)}→{v}" for k, v in changed.items()))
            if not (a.check or a.dry_run):
                w.set_fields(p, new, after='confidence')
    print(f"\ngrade dist: {dict(dist)}  depth dist: {dict(depth)}  pages changed: {diffs}")
    if a.check and diffs:
        sys.exit(2)


if __name__ == '__main__':
    main()
