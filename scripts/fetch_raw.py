#!/usr/bin/env python3
"""
fetch_raw.py — URL을 내려받아 raw/ 스냅샷(markdown)으로 저장한다.

용법:
  python scripts/fetch_raw.py <url> <out_path> [--title "..."] [--publisher "..."] [--date YYYY-MM-DD] [--no-fallback]

동작:
  1. requests로 HTML 다운로드 → trafilatura 본문 추출 (fetched_via: direct)
  2. 1,500자 미만이면 폴백 체인:  Jina Reader(r.jina.ai) → Aside 브라우저 REPL(사용자 로그인 세션, 앱 실행 중일 때) → Wayback 원문(id_)
     각 단계는 더 긴 본문을 얻었을 때만 채택. (fetched_via: jina | aside | wayback)
  3. frontmatter(url, title, publisher, fetched_at, publication_date, fetched_via, content_hash, snapshot_quality, chars) + 본문 저장
  4. stdout에 JSON 한 줄: {"ok", "chars", "status", "quality", "via", "out", "title"}

snapshot_quality:  full ≥1,500자 · partial 300~1,500자 · failed <300자 (헤더만 저장, 에이전트가 수동 보완 후 llm-extracted/unavailable로 갱신)
환경변수: JINA_API_KEY(선택, 없으면 익명 20 RPM), ASIDE_CLI(선택, 기본 %LOCALAPPDATA%/Aside/CLI/current/aside.exe)
"""
import sys, json, hashlib, argparse, datetime, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'


def _extract(html):
    try:
        import trafilatura
        t = trafilatura.extract(html, include_comments=False, include_tables=True, favor_recall=True) or ''
        md = trafilatura.extract_metadata(html)
        return t, (md.title if md and md.title else ''), (md.date if md and md.date else '')
    except Exception:
        paras = re.findall(r'<p[^>]*>(.*?)</p>', html, re.S | re.I)
        return '\n\n'.join(re.sub(r'<[^>]+>', '', p).strip() for p in paras if len(p) > 40), '', ''


def _via_direct(url):
    import requests
    r = requests.get(url, timeout=20, headers={'User-Agent': UA, 'Accept-Language': 'ko,en;q=0.8'})
    if not r.encoding or r.encoding.lower() in ('iso-8859-1', 'ascii'):
        r.encoding = r.apparent_encoding or 'utf-8'
    text, title, date = _extract(r.text)
    if not title:
        m = re.search(r'<title[^>]*>(.*?)</title>', r.text, re.S | re.I)
        if m:
            title = re.sub(r'\s+', ' ', m.group(1)).strip()
    return text, title, date, r.status_code


def _via_jina(url):
    """r.jina.ai 프록시 — 헤드리스 렌더 후 마크다운. HR Brew·Business Wire 등 Cloudflare/Akamai 차단에 유효."""
    import requests
    h = {'Accept': 'text/plain', 'User-Agent': UA}
    k = os.environ.get('JINA_API_KEY')
    if k:
        h['Authorization'] = 'Bearer ' + k
    r = requests.get('https://r.jina.ai/' + url, timeout=60, headers=h)
    if r.status_code != 200:
        return '', ''
    body = r.text
    m = re.match(r'Title:\s*(.*)', body)
    title = m.group(1).strip() if m else ''
    body = re.sub(r'^(Title|URL Source|Published Time|Markdown Content):.*\n', '', body, flags=re.M).strip()
    if re.search(r'Just a moment|Page Unavailable|AbuseAlleviationError|Access Denied', body[:300]):
        return '', ''
    return body, title


def _via_aside(url):
    """Aside 브라우저 REPL — 사용자 로그인 세션으로 본문 innerText. Aside 앱 실행 중일 때만 동작."""
    try:
        import fetch_via_aside as fa
    except Exception:
        return '', ''
    if not os.path.exists(fa.ASIDE):
        return '', ''
    res = fa.fetch(url, wait=10)
    if not res.get('ok'):
        return '', ''
    title = res.get('title') or ''
    if re.search(r'404|Page Not Found|Access Denied|Just a moment', title):
        return '', ''
    return res.get('text', ''), title


def _via_wayback(url):
    """Wayback Machine 가장 가까운 스냅샷의 원문(id_)을 받아 추출. Bloomberg 등 구독지에 유효할 때가 있다."""
    import requests
    r = requests.get('https://archive.org/wayback/available', params={'url': url}, timeout=30)
    snap = (r.json().get('archived_snapshots') or {}).get('closest') or {}
    if not snap.get('url'):
        return '', ''
    wb = re.sub(r'/web/(\d+)/', r'/web/\1id_/', snap['url'])
    r2 = requests.get(wb, timeout=60, headers={'User-Agent': UA})
    if r2.status_code != 200:
        return '', ''
    text, title, _ = _extract(r2.text)
    return text, title


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument('url'); ap.add_argument('out')
    ap.add_argument('--title', default=''); ap.add_argument('--publisher', default=''); ap.add_argument('--date', default='')
    ap.add_argument('--no-fallback', action='store_true', help='direct 요청만 (Jina·Aside·Wayback 폴백 생략)')
    a = ap.parse_args()
    text, title, status, via, err = '', a.title, 0, 'direct', ''
    try:
        text, t0, d0, status = _via_direct(a.url)
        title = title or t0
        if d0 and not a.date:
            a.date = d0
    except Exception as e:
        err = str(e)[:200]
    text = (text or '').strip()
    if len(text) < 1500 and not a.no_fallback:
        for name, fn in (('jina', _via_jina), ('aside', _via_aside), ('wayback', _via_wayback)):
            try:
                t2, title2 = fn(a.url)
            except Exception:
                t2, title2 = '', ''
            t2 = (t2 or '').strip()
            if len(t2) > len(text):
                text, via = t2, name
                if title2 and (not title or re.search(r'Just a moment|Access Denied|Are you a robot', title)):
                    title = title2
            if len(text) >= 1500:
                break
    n = len(text)
    quality = 'full' if n >= 1500 else 'partial' if n >= 300 else 'failed'
    h = hashlib.sha256(text.encode('utf-8')).hexdigest()[:16] if text else ''
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    title = (title or '').replace('"', "'")
    fm = ['---', f'url: "{a.url}"', f'title: "{title}"', f'publisher: "{a.publisher}"',
          f'publication_date: {a.date or "unknown"}', f'fetched_at: {datetime.date.today().isoformat()}',
          f'http_status: {status}', f'fetched_via: {via}', f'content_hash: "{h}"', f'snapshot_quality: {quality}', f'chars: {n}',
          'note: "raw 스냅샷 — 수정 금지. 본문은 자동 추출 결과이며 광고·내비게이션이 섞일 수 있음."', '---', '']
    body = text if text else f'(추출 실패: http_status={status} {err})'
    with open(a.out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(fm) + f'# {title}\n\n' + body + '\n')
    print(json.dumps({'ok': quality != 'failed', 'chars': n, 'status': status, 'quality': quality, 'via': via, 'out': a.out, 'title': title[:80]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
