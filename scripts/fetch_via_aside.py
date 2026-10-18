#!/usr/bin/env python3
"""
fetch_via_aside.py — Aside 브라우저(사용자 로그인 세션)의 REPL로 페이지 본문을 받아 raw/ 스냅샷으로 저장한다.

용법:
  python scripts/fetch_via_aside.py <url> <out_path> [--publisher X] [--wait 10]
  python scripts/fetch_via_aside.py --unavailable [--dry-run]   # snapshot_quality: unavailable 인 source 전부 재시도

동작:
  1. `aside repl` 에 Playwright식 JS를 넘겨 탭을 열고 wait초 대기(Cloudflare 챌린지 통과) 후 본문 innerText 추출
     (article → main → [role=main] → body 순). 에이전트·LLM은 쓰지 않는다 (결정론적, 프롬프트 인젝션 영향 없음).
  2. fetch_raw.py와 같은 frontmatter로 저장. fetched_via: aside-repl, snapshot_quality: full|partial|failed
  3. --unavailable: wiki/sources/*.md 중 snapshot_quality=unavailable 이고 url이 http 인 것을 순회해 raw를 만들고
     source 페이지 frontmatter(raw, snapshot_quality, fetched_via)를 갱신한다. 결과표를 출력.
전제: Aside 앱 실행 중 + `aside login` 완료. CLI 경로는 ASIDE_CLI 환경변수 또는 기본 경로.
"""
import os, sys, re, json, hashlib, datetime, subprocess, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wikilib as w

ASIDE = os.environ.get('ASIDE_CLI') or os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Aside', 'CLI', 'current', 'aside.exe')
JS = ("const page = await openTab('{url}'); await new Promise(r => setTimeout(r, {wait}000)); "
      "const title = await page.title(); "
      "const t = await page.evaluate(() => {{ const el = document.querySelector('article') || document.querySelector('main') || document.querySelector('[role=main]') || document.body; return el ? el.innerText : ''; }}); "
      "const pub = await page.evaluate(() => {{ const m = document.querySelector('meta[property=\"article:published_time\"], meta[name=\"pubdate\"], meta[name=\"date\"], time[datetime]'); return m ? (m.getAttribute('content') || m.getAttribute('datetime') || '') : ''; }}); "
      "console.log('@@TITLE@@' + title); console.log('@@PUB@@' + pub); console.log('@@LEN@@' + t.length); console.log('@@TEXT@@'); console.log(t); try {{ await page.close(); }} catch (e) {{}}")


def fetch(url, wait=10):
    if "'" in url:
        return {'ok': False, 'error': 'quote in url'}
    code = JS.format(url=url, wait=wait)
    try:
        r = subprocess.run([ASIDE, 'repl', code], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=150)
    except Exception as e:
        return {'ok': False, 'error': str(e)[:200]}
    out = r.stdout or ''
    if '@@TEXT@@' not in out:
        return {'ok': False, 'error': (out + r.stderr)[-300:].strip()}
    title = re.search(r'@@TITLE@@(.*)', out); pub = re.search(r'@@PUB@@(.*)', out)
    text = out.split('@@TEXT@@', 1)[1]
    text = re.sub(r'\n\[\w+ \| \d+ms\]\s*$', '', text).strip()  # trailing "[ok | 10724ms]"
    text = re.sub(r'\x1b\[[0-9;]*m', '', text)
    return {'ok': True, 'title': (title.group(1).strip() if title else ''), 'pub': (pub.group(1).strip() if pub else ''), 'text': text}


def save(url, out, res, publisher='', date=''):
    text = res.get('text', '') if res.get('ok') else ''
    n = len(text)
    quality = 'full' if n >= 1500 else 'partial' if n >= 300 else 'failed'
    h = hashlib.sha256(text.encode('utf-8')).hexdigest()[:16] if text else ''
    title = (res.get('title') or '').replace('"', "'")
    pub = date or (res.get('pub') or '')[:10] or 'unknown'
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    fm = ['---', f'url: "{url}"', f'title: "{title}"', f'publisher: "{publisher}"', f'publication_date: {pub}',
          f'fetched_at: {datetime.date.today().isoformat()}', 'fetched_via: aside-repl', f'content_hash: "{h}"',
          f'snapshot_quality: {quality}', f'chars: {n}',
          'note: "raw 스냅샷 — 수정 금지. 사용자 로그인 브라우저(Aside)에서 innerText로 추출. 내비게이션·광고 문구가 섞일 수 있음."', '---', '']
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(fm) + f'# {title}\n\n' + (text if text else f"(추출 실패: {res.get('error', '')})") + '\n')
    return quality, n


def slugify(s):
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return s[:60] or 'page'


def run_unavailable(dry):
    rows = []
    for rel, p in w.pages('sources'):
        fm, _, _ = w.load(p)
        if fm.get('snapshot_quality') != 'unavailable' or fm.get('deprecated'):
            continue
        url = str(fm.get('url') or '')
        if not url.startswith('http'):
            continue
        slug = rel.split('/')[-1]
        sub = 'vendors' if str(fm.get('source_type')) in ('vendor', 'company') else 'reports' if str(fm.get('source_type')) == 'analyst' else 'articles'
        date = str(fm.get('publication_date') or 'unknown')[:10]
        d = date if re.match(r'^\d{4}-\d{2}-\d{2}$', date) else datetime.date.today().isoformat()
        out = os.path.join(w.ROOT, 'raw', sub, f'{d}-{slug}.md')
        if dry:
            rows.append((slug, url, 'dry')); continue
        res = fetch(url)
        quality, n = save(url, out, res, publisher=str(fm.get('publisher') or ''), date=date if re.match(r'^\d{4}-\d{2}', date) else '')
        if quality != 'failed':
            w.set_fields(p, {'raw': os.path.relpath(out, w.ROOT).replace('\\', '/'), 'snapshot_quality': quality, 'fetched_via': 'aside-repl'}, after='tier')
        rows.append((slug, quality, n, (res.get('title') or res.get('error') or '')[:60]))
        print(' | '.join(str(x) for x in rows[-1]), flush=True)
    ok = sum(1 for r in rows if r[1] in ('full', 'partial'))
    print(f'\n{ok}/{len(rows)} recovered (full/partial)')


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser()
    ap.add_argument('url', nargs='?'); ap.add_argument('out', nargs='?')
    ap.add_argument('--publisher', default=''); ap.add_argument('--date', default=''); ap.add_argument('--wait', type=int, default=10)
    ap.add_argument('--unavailable', action='store_true'); ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    if not os.path.exists(ASIDE):
        print(json.dumps({'ok': False, 'error': f'aside CLI not found: {ASIDE}'})); sys.exit(1)
    if a.unavailable:
        run_unavailable(a.dry_run); return
    if not a.url or not a.out:
        ap.error('url and out required')
    res = fetch(a.url, a.wait)
    quality, n = save(a.url, a.out, res, a.publisher, a.date)
    print(json.dumps({'ok': quality != 'failed', 'quality': quality, 'chars': n, 'title': res.get('title', '')[:80], 'out': a.out, 'error': res.get('error', '')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
