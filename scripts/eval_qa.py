#!/usr/bin/env python3
"""
eval_qa.py — 골든 Q&A 회귀 평가. wiki만 보고 답해야 하는 질문 30개를 Claude Code headless로 물어 정규식 채점.

용법:
  python scripts/eval_qa.py                # 전체 (claude -p 30회 호출 — 비용 발생)
  python scripts/eval_qa.py --ids 1,4,5    # 일부만
  python scripts/eval_qa.py --offline      # LLM 호출 없이 '페이지 자체에 기대 답이 있는가'만 검사 (데이터 회귀용, 무료)

채점: expect 항목마다 정규식 대안(|)이 답변에 하나라도 있으면 통과. 문항 통과 = 모든 expect 통과.
결과: evals/results/qa-YYYY-MM-DD.json + 요약 출력. 통과율이 직전 결과보다 10%p 이상 떨어지면 exit 2.
"""
import os, re, sys, json, subprocess, argparse, datetime, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wikilib as w

QA = os.path.join(w.ROOT, 'evals', 'golden-qa.json')
RES = os.path.join(w.ROOT, 'evals', 'results')


def find_page(slug):
    if slug == 'CLAUDE':
        return os.path.join(w.ROOT, 'CLAUDE.md')
    for p in glob.glob(os.path.join(w.WIKI, '**', slug + '.md'), recursive=True):
        return p
    return None


def ask(q):
    prompt = (f"다음 질문에 C:\\AI\\AI-HR\\Benchmark 의 wiki/ 페이지만 근거로 답하라. 웹 검색 금지. 답은 3문장 이내, 근거 페이지 슬러그를 괄호로. 모르면 '데이터 없음'.\n질문: {q}")
    r = subprocess.run(['claude', '-p', prompt, '--output-format', 'text', '--allowedTools', 'Read,Grep,Glob'],
                       capture_output=True, text=True, encoding='utf-8', cwd=w.ROOT, timeout=300)
    return (r.stdout or '') + ('' if r.returncode == 0 else f'\n[stderr] {r.stderr[-300:]}')


def grade(ans, expect):
    return all(re.search(e, ans, re.I) for e in expect)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ids'); ap.add_argument('--offline', action='store_true')
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    qa = json.load(open(QA, encoding='utf-8'))
    if a.ids:
        ids = {int(x) for x in a.ids.split(',')}
        qa = [x for x in qa if x['id'] in ids]
    results = []
    for item in qa:
        if a.offline:
            p = find_page(item['page'])
            ans = w.read(p) if p else ''
        else:
            ans = ask(item['q'])
        ok = grade(ans, item['expect'])
        results.append({'id': item['id'], 'ok': ok, 'q': item['q'], 'answer': ans[:600] if not a.offline else '(offline)', 'page_found': bool(find_page(item['page']))})
        print(('✅' if ok else '❌'), item['id'], item['q'][:60], '' if ok else f"  expect {item['expect']}")
    n = len(results); k = sum(r['ok'] for r in results)
    rate = k / n if n else 0
    print(f"\npass {k}/{n} = {rate:.0%}  mode={'offline' if a.offline else 'llm'}")
    os.makedirs(RES, exist_ok=True)
    prev = sorted(glob.glob(os.path.join(RES, 'qa-*.json')))
    out = os.path.join(RES, f"qa-{datetime.date.today().isoformat()}{'-offline' if a.offline else ''}.json")
    json.dump({'date': datetime.date.today().isoformat(), 'mode': 'offline' if a.offline else 'llm', 'pass': k, 'n': n, 'results': results}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if prev and not a.ids:
        last = json.load(open(prev[-1], encoding='utf-8'))
        if last.get('mode') == ('offline' if a.offline else 'llm') and last['n'] and (last['pass'] / last['n'] - rate) >= 0.10:
            print(f"REGRESSION: {last['pass']}/{last['n']} → {k}/{n}"); sys.exit(2)


if __name__ == '__main__':
    main()
