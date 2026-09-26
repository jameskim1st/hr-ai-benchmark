#!/usr/bin/env python3
"""
fetch_raw.py — URL을 내려받아 raw/ 스냅샷(markdown)으로 저장한다.

용법:
  python scripts/fetch_raw.py <url> <out_path> [--title "..."] [--publisher "..."] [--date YYYY-MM-DD]

동작:
  1. requests로 HTML 다운로드 (User-Agent 지정, 20초 타임아웃)
  2. trafilatura로 본문 텍스트 추출 (실패 시 <p> 태그 fallback)
  3. frontmatter(url, title, publisher, fetched_at, publication_date, content_hash, snapshot_quality, chars) + 본문을 out_path에 저장
  4. stdout에 JSON 한 줄 출력: {"ok": bool, "chars": N, "status": http_status, "quality": "...", "out": path}

snapshot_quality:
  full     — 본문 1,500자 이상 추출
  partial  — 300~1,500자 (paywall·요약만 노출)
  failed   — 추출 실패 (파일은 header만 저장, 에이전트가 WebFetch 등으로 보완 후 quality를 llm-extracted로 갱신)
"""
import sys, json, hashlib, argparse, datetime, re, os

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument('url'); ap.add_argument('out')
    ap.add_argument('--title', default=''); ap.add_argument('--publisher', default=''); ap.add_argument('--date', default='')
    a = ap.parse_args()
    text, status, title = '', 0, a.title
    try:
        import requests
        r = requests.get(a.url, timeout=20, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36', 'Accept-Language': 'ko,en;q=0.8'})
        status = r.status_code
        if not r.encoding or r.encoding.lower() in ('iso-8859-1', 'ascii'):
            r.encoding = r.apparent_encoding or 'utf-8'
        html = r.text
        try:
            import trafilatura
            text = trafilatura.extract(html, include_comments=False, include_tables=True, favor_recall=True) or ''
            if not title:
                md = trafilatura.extract_metadata(html)
                if md and md.title: title = md.title
                if md and md.date and not a.date: a.date = md.date
        except Exception:
            text = ''
        if not text:
            paras = re.findall(r'<p[^>]*>(.*?)</p>', html, re.S | re.I)
            text = '\n\n'.join(re.sub(r'<[^>]+>', '', p).strip() for p in paras if len(p) > 40)
        if not title:
            m = re.search(r'<title[^>]*>(.*?)</title>', html, re.S | re.I)
            if m: title = re.sub(r'\s+', ' ', m.group(1)).strip()
    except Exception as e:
        text = ''
        err = str(e)
    else:
        err = ''
    text = text.strip()
    n = len(text)
    quality = 'full' if n >= 1500 else 'partial' if n >= 300 else 'failed'
    h = hashlib.sha256(text.encode('utf-8')).hexdigest()[:16] if text else ''
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    fm = ['---', f'url: "{a.url}"', f'title: "{title.replace(chr(34), chr(39))}"', f'publisher: "{a.publisher}"',
          f'publication_date: {a.date or "unknown"}', f'fetched_at: {datetime.date.today().isoformat()}',
          f'http_status: {status}', f'content_hash: "{h}"', f'snapshot_quality: {quality}', f'chars: {n}',
          'note: "raw 스냅샷 — 수정 금지. 본문은 trafilatura 자동 추출 결과이며 광고·내비게이션이 섞일 수 있음."', '---', '']
    body = text if text else f'(추출 실패: http_status={status} {err})'
    with open(a.out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(fm) + f'# {title}\n\n' + body + '\n')
    print(json.dumps({'ok': quality != 'failed', 'chars': n, 'status': status, 'quality': quality, 'out': a.out, 'title': title[:80]}, ensure_ascii=False))

if __name__ == '__main__':
    main()
