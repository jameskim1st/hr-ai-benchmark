#!/usr/bin/env python3
"""
check_quotes.py — Grounding Invariant 검사: use case 본문의 수치가 인용 소스의 raw 스냅샷에 실제로 존재하는가.

용법:
  python scripts/check_quotes.py                # 전체 (보고만)
  python scripts/check_quotes.py <usecase-slug> # 한 페이지 상세
  python scripts/check_quotes.py --json

규칙:
  - 본문(코드블록 제외)에서 숫자 토큰을 뽑는다: 퍼센트(75%), 금액($21M, 300억), 큰 수(23,000 / 3,000+ / 1.5M / 5만), 연도-월 제외
  - 각 use case의 sources → source 페이지 → raw: 경로의 텍스트를 합친다 (snapshot_quality unavailable 제외)
  - 숫자 토큰이 raw 텍스트 어디에도 없으면 '근거 미확인'으로 보고. 한글 단위(만·억)는 숫자로 환산해 비교한다.
  - 판정은 '텍스트가 거기 있다'만 증명한다. 참·거짓은 사람이 판단.
출력: 페이지별 (전체 수치 수, 미확인 수, 미확인 목록). 미확인 비율 50% 초과는 lint에서 warning으로 승격.
"""
import os, re, sys, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wikilib as w

NUM = re.compile(r'(?<![\w.-])(\$?\d{1,3}(?:,\d{3})+(?:\.\d+)?[MBK]?\+?|\$?\d+(?:\.\d+)?\s?(?:%|M|B|K|억|만|천|배|x)\+?|\d+(?:\.\d+)?%)(?![\w-])')
SKIP_CTX = re.compile(r'(19|20)\d{2}[-./]')  # dates


def numbers(text):
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    text = re.sub(r'\[\[[^\]]*\]\]', '', text)
    out = []
    for m in NUM.finditer(text):
        s = m.group(1)
        ctx = text[max(0, m.start() - 6):m.end() + 2]
        if SKIP_CTX.search(ctx):
            continue
        out.append(s)
    return out


def variants(tok):
    t = tok.replace('$', '').replace('+', '').replace(' ', '')
    v = {t, tok}
    m = re.match(r'^([\d.,]+)(%|M|B|K|억|만|천|배|x)?$', t)
    if m:
        n = m.group(1); unit = m.group(2) or ''
        plain = n.replace(',', '')
        v |= {n, plain}
        try:
            f = float(plain)
            if unit == 'M': v |= {f'{int(f*1_000_000):,}', f'{int(f*1_000_000)}', f'{f:g} million', f'{f:g}M'}
            if unit == 'B': v |= {f'{int(f*1_000_000_000):,}', f'{f:g} billion', f'{f:g}B'}
            if unit == 'K': v |= {f'{int(f*1000):,}', f'{int(f*1000)}'}
            if unit == '만': v |= {f'{int(f*10000):,}', f'{int(f*10000)}', f'{f:g}만'}
            if unit == '억': v |= {f'{int(f*100_000_000):,}', f'{f:g}억'}
            if unit == '%': v |= {f'{f:g}%', f'{f:g} percent', f'{f:g}퍼센트'}
            if f == int(f):
                v |= {str(int(f)), f'{int(f):,}'}
        except ValueError:
            pass
    return {x for x in v if x}


def raw_text_for(fm, sfm_cache):
    srcs = fm.get('sources') or []
    srcs = [srcs] if isinstance(srcs, str) else srcs
    texts = []; n_raw = 0
    for s in srcs:
        slug = s.replace('sources/', '').replace('.md', '').strip()
        sp = os.path.join(w.WIKI, 'sources', slug + '.md')
        if not os.path.exists(sp):
            continue
        sfm, sbody, _ = w.load(sp)
        texts.append(sbody)  # source page quotes count too
        raw = (sfm or {}).get('raw')
        if raw and os.path.exists(os.path.join(w.ROOT, raw)) and (sfm or {}).get('snapshot_quality') != 'unavailable':
            texts.append(w.read(os.path.join(w.ROOT, raw))); n_raw += 1
    return '\n'.join(texts), n_raw


def check(rel, p):
    fm, body, _ = w.load(p)
    toks = numbers(body)
    corpus, n_raw = raw_text_for(fm, {})
    corpus_n = corpus.replace(',', '')
    missing = []
    for t in dict.fromkeys(toks):
        if not any(v in corpus or v.replace(',', '') in corpus_n for v in variants(t)):
            missing.append(t)
    return {'page': rel, 'numbers': len(set(toks)), 'missing': len(missing), 'missing_list': missing[:25], 'raw_files': n_raw}


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    as_json = '--json' in sys.argv
    results = []
    for sub in ('usecases', 'enterprise-ai'):
        for rel, p in w.pages(sub):
            if args and rel.split('/')[-1] not in args:
                continue
            results.append(check(rel, p))
    if as_json:
        print(json.dumps(results, ensure_ascii=False, indent=1)); return
    tot = sum(r['numbers'] for r in results); mis = sum(r['missing'] for r in results)
    print(f"pages {len(results)} · 수치 토큰 {tot} · raw에서 미확인 {mis} ({(mis/tot*100 if tot else 0):.0f}%)")
    for r in sorted(results, key=lambda r: -(r['missing'] / r['numbers'] if r['numbers'] else 0)):
        if r['numbers'] == 0:
            continue
        flag = '⚠️' if r['numbers'] and r['missing'] / r['numbers'] > 0.5 else '  '
        print(f"{flag} {r['page']:60s} {r['missing']:3d}/{r['numbers']:3d} raw={r['raw_files']}  {', '.join(r['missing_list'][:8])}")


if __name__ == '__main__':
    main()
