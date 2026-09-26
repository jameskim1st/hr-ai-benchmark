#!/usr/bin/env python3
"""
wiki_mcp.py — HR AI Benchmark wiki를 MCP(stdio) 서버로 노출한다. 다른 프로젝트 세션(제안서 작성 등)에서 wiki를 검색·읽기·인용 검증할 수 있다.

등록: 저장소 루트의 .mcp.json 참조 (claude mcp add hr-wiki -- python scripts/wiki_mcp.py)
도구:
  wiki_search(query, scope="usecases", limit=10)  — frontmatter+본문 grep 기반 검색 (임베딩 없음). 결과: slug, title, evidence_grade, depth, 매치 줄
  wiki_read(slug)                                  — 페이지 전체 (visibility=internal 은 기본 차단, include_internal=True 시 허용)
  wiki_sources(slug)                               — use case가 인용한 source 페이지 요약 (tier, publisher, url, raw 스냅샷 유무)
  wiki_verify_quote(slug, quote)                   — 인용문/수치가 그 use case의 raw 스냅샷에 실제로 있는지 (텍스트 존재만 증명)
  wiki_stats()                                     — 규모·등급 분포
읽기 전용. 어떤 도구도 파일을 쓰지 않는다.
"""
import os, re, sys, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wikilib as w
try:
    from mcp.server.mcpserver import MCPServer as _Server   # mcp >= 2.x
except ImportError:
    from mcp.server.fastmcp import FastMCP as _Server       # mcp 1.x

mcp = _Server('hr-ai-benchmark-wiki')
SCOPES = {'usecases': ['usecases'], 'all': ['usecases', 'enterprise-ai', 'reference', 'vendors', 'companies', 'syntheses'],
          'sources': ['sources'], 'enterprise-ai': ['enterprise-ai'], 'syntheses': ['syntheses']}


def _find(slug):
    for p in glob.glob(os.path.join(w.WIKI, '**', slug + '.md'), recursive=True):
        return p
    return None


@mcp.tool()
def wiki_search(query: str, scope: str = 'usecases', limit: int = 10) -> list:
    """Search wiki pages by keyword(s) (space-separated, AND). scope: usecases|all|sources|enterprise-ai|syntheses."""
    terms = [t.lower() for t in query.split() if t.strip()]
    out = []
    for sub in SCOPES.get(scope, SCOPES['usecases']):
        for rel, p in w.pages(sub):
            fm, body, _ = w.load(p)
            if (fm or {}).get('visibility') == 'internal':
                continue
            txt = w.read(p); low = txt.lower()
            if all(t in low for t in terms):
                lines = [l.strip() for l in body.split('\n') if any(t in l.lower() for t in terms)][:3]
                out.append({'slug': rel.split('/')[-1], 'path': rel, 'title': (fm or {}).get('title'), 'company': (fm or {}).get('company'),
                            'evidence_grade': (fm or {}).get('evidence_grade'), 'depth': (fm or {}).get('depth'),
                            'primary_category': (fm or {}).get('primary_category'), 'matches': lines})
    out.sort(key=lambda r: (str(r.get('evidence_grade') or 'Z'), r['slug']))
    return out[:limit]


@mcp.tool()
def wiki_read(slug: str, include_internal: bool = False) -> str:
    """Return the full markdown of a page by slug. Internal (client-confidential) pages are refused unless include_internal=True."""
    p = _find(slug)
    if not p:
        return f'NOT FOUND: {slug} (grep 먼저 — 부재를 확인한 뒤 없다고 말할 것)'
    fm, _, _ = w.load(p)
    if (fm or {}).get('visibility') == 'internal' and not include_internal:
        return f'INTERNAL: {slug} is client-confidential (visibility: internal). Pass include_internal=True only for internal use.'
    return w.read(p)


@mcp.tool()
def wiki_sources(slug: str) -> list:
    """List the source pages a use case cites, with tier/publisher/url and whether a raw snapshot exists."""
    p = _find(slug)
    if not p:
        return [{'error': f'NOT FOUND: {slug}'}]
    fm, _, _ = w.load(p)
    srcs = fm.get('sources') or []
    srcs = [srcs] if isinstance(srcs, str) else srcs
    out = []
    for s in srcs:
        ss = s.replace('sources/', '').replace('.md', '').strip()
        sp = os.path.join(w.WIKI, 'sources', ss + '.md')
        if not os.path.exists(sp):
            out.append({'ref': s, 'status': 'unresolved'}); continue
        sfm, _, _ = w.load(sp)
        raw = (sfm or {}).get('raw')
        out.append({'slug': ss, 'title': (sfm or {}).get('title'), 'tier': (sfm or {}).get('tier'), 'publisher': (sfm or {}).get('publisher'),
                    'independent': (sfm or {}).get('independent'), 'url': (sfm or {}).get('url'),
                    'raw_snapshot': bool(raw and os.path.exists(os.path.join(w.ROOT, raw))), 'snapshot_quality': (sfm or {}).get('snapshot_quality')})
    return out


@mcp.tool()
def wiki_verify_quote(slug: str, quote: str) -> dict:
    """Check whether a quote or number literally appears in the raw snapshots (or source Key Quotes) cited by the use case. Proves presence only, not truth."""
    p = _find(slug)
    if not p:
        return {'error': f'NOT FOUND: {slug}'}
    fm, _, _ = w.load(p)
    srcs = fm.get('sources') or []
    srcs = [srcs] if isinstance(srcs, str) else srcs
    q = quote.strip(); qn = q.replace(',', '').lower()
    hits = []
    for s in srcs:
        ss = s.replace('sources/', '').replace('.md', '').strip()
        sp = os.path.join(w.WIKI, 'sources', ss + '.md')
        if not os.path.exists(sp):
            continue
        sfm, sbody, _ = w.load(sp)
        texts = [('source-page', sbody)]
        raw = (sfm or {}).get('raw')
        if raw and os.path.exists(os.path.join(w.ROOT, raw)):
            texts.append(('raw', w.read(os.path.join(w.ROOT, raw))))
        for kind, t in texts:
            tl = t.replace(',', '').lower()
            i = tl.find(qn)
            if i >= 0:
                hits.append({'source': ss, 'where': kind, 'context': t[max(0, i - 120):i + len(q) + 120].replace('\n', ' ')})
    return {'found': bool(hits), 'hits': hits[:5], 'note': '인용이 존재함을 증명할 뿐 참임을 증명하지 않는다.'}


@mcp.tool()
def wiki_stats() -> dict:
    """Counts by page type, evidence grade and depth."""
    c = collections.Counter(); g = collections.Counter(); d = collections.Counter()
    for rel, p in w.pages():
        sub = rel.split('/')[0] if '/' in rel else 'root'
        c[sub] += 1
        if sub == 'usecases':
            fm, _, _ = w.load(p)
            g[(fm or {}).get('evidence_grade', '?')] += 1; d[(fm or {}).get('depth', '?')] += 1
    return {'pages': dict(c), 'evidence_grade': dict(g), 'depth': dict(d)}


if __name__ == '__main__':
    mcp.run()
