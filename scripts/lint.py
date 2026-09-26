#!/usr/bin/env python3
"""
lint.py — 결정론적 wiki 점검 (보고만 한다. 자동 수정 없음)

용법:
  python scripts/lint.py                 # 전체 점검, 사람이 읽는 리포트
  python scripts/lint.py --json          # JSON 출력 (스킬·훅·CI용)
  python scripts/lint.py --quick <file>  # 한 파일만 빠른 점검 (PostToolUse 훅용). critical이 있으면 exit 2
  python scripts/lint.py --write-report  # wiki/syntheses/lint-YYYY-MM-DD.md 로 저장
  python scripts/lint.py --strict        # critical > 0 이면 exit 2

점검 항목 (CLAUDE.md §7):
  C (critical): broken wikilink, 필수 frontmatter 누락, 잘못된 taxonomy 값, ai_tech_subtype 부모 불일치,
                sources 항목이 source 페이지로 안 이어짐, visibility=internal 페이지가 export에 포함,
                날짜 형식 오류, evidence_grade/confidence 미계산(grade.py 미실행)
  W (warning):  stale(12개월 초과), 금지어, 필수 섹션 누락, B/C/D 근거 없는 서술, Mermaid 없음(depth=full),
                Consulting Angle 빈약, source 페이지에 raw 스냅샷 없음, 미해결 contradiction, 400줄 초과 페이지,
                last_confirmed_estimated
  I (info):     orphan 페이지, 카테고리/중그룹 커버리지 0건, 중복 의심(같은 회사+벤더), index 카운트 불일치,
                Tier 1·2 독립 소스 0건
"""
import os, re, sys, json, glob, datetime, collections, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wikilib as w

REQ = ['title', 'slug', 'primary_category', 'subcategory', 'tags', 'company', 'industry', 'region', 'vendor',
       'vendor_type', 'ai_tech_type', 'ai_tech_subtype', 'stage', 'frequency', 'first_seen', 'last_confirmed',
       'confidence', 'sources', 'visibility', 'case_type']
GRADE_FIELDS = ['evidence_grade', 'corroborated_by', 'freshness', 'depth']
SECTIONS = ['## Summary', '## Problem', '## Solution Architecture', '### A.', '### B.', '### C.', '### D.', '### E.',
            '## Impact', '## Governance', '## Contradictions', '## Consulting Angle']
SUBCATS = set()  # filled from CLAUDE taxonomy file if present


def load_taxonomy():
    p = os.path.join(w.ROOT, '.claude', 'rules', 'taxonomy.md')
    if not os.path.exists(p):
        p = os.path.join(w.ROOT, 'CLAUDE.md')
    txt = w.read(p)
    for m in re.finditer(r'^- \*\*([^*]+)\*\*:', txt, re.M):
        SUBCATS.add(m.group(1).strip())
    for m in re.finditer(r'^\s+- \*([^*]+)\*:', txt, re.M):
        SUBCATS.add(m.group(1).strip())


class Lint:
    def __init__(self):
        self.f = collections.defaultdict(list)  # (sev, code) -> [(page, detail)]
        self.pages = {}
        self.fms = {}
        self.bodies = {}
        for rel, p in w.pages():
            txt = w.read(p)
            self.pages[rel] = txt
            fm, body, _ = w.load(p)
            self.fms[rel] = fm
            self.bodies[rel] = body
        self.names = set(self.pages) | {'CLAUDE'}
        self.base = collections.defaultdict(list)
        for n in self.pages:
            self.base[n.split('/')[-1]].append(n)
        self.inbound = collections.Counter()

    def add(self, sev, code, page, detail=''):
        if (page, detail) not in self.f[(sev, code)]:
            self.f[(sev, code)].append((page, detail))

    def resolve(self, target):
        t = target.split('|')[0].split('#')[0].strip()
        if t.endswith('.md'):
            t = t[:-3]
        if t in self.names:
            return t
        if t in self.base:
            return self.base[t][0]
        return None

    # ---------- checks
    def links(self, only=None):
        for n, txt in self.pages.items():
            body = re.sub(r'```.*?```', '', txt, flags=re.S)
            for m in re.finditer(r'\[\[([^\]]+)\]\]', body):
                tgt = m.group(1)
                if tgt.startswith('#') or tgt in ('wikilink', '페이지이름'):
                    continue
                r = self.resolve(tgt)
                if r is None:
                    if n.startswith('syntheses/lint-') or n == 'log' or n.startswith('syntheses/system-review'):
                        continue
                    if only is None or n == only:
                        self.add('C', 'broken-link', n, tgt)
                else:
                    self.inbound[r] += 1
        if only is None:
            for n in self.pages:
                if self.inbound[n] == 0 and not n.startswith('sources/') and n.split('/')[0] not in ('syntheses',) \
                        and n not in ('index', 'log', 'dashboard', 'guide', 'guide-html-export'):
                    self.add('I', 'orphan', n)

    def usecase(self, n):
        fm, body = self.fms[n], self.bodies[n]
        if fm is None:
            self.add('C', 'no-frontmatter', n); return
        for k in REQ:
            if k not in fm or fm[k] in (None, '', []):
                self.add('C', 'missing-field', n, k)
        missing_grade = [k for k in GRADE_FIELDS if k not in fm]
        if missing_grade:
            self.add('C', 'not-graded', n, ','.join(missing_grade) + ' 없음 — python scripts/grade.py 실행 필요')
        if fm.get('primary_category') not in w.CATS:
            self.add('C', 'bad-category', n, str(fm.get('primary_category')))
        if SUBCATS and fm.get('subcategory') and fm['subcategory'] not in SUBCATS:
            self.add('W', 'unknown-subcategory', n, str(fm['subcategory']))
        if fm.get('visibility') not in ('public', 'internal'):
            self.add('C', 'bad-visibility', n, str(fm.get('visibility')))
        tt = fm.get('ai_tech_type') or []; st = fm.get('ai_tech_subtype') or []
        tt = [tt] if isinstance(tt, str) else tt; st = [st] if isinstance(st, str) else st
        allowed = set().union(*[w.TYPES.get(t, set()) for t in tt])
        for s in st:
            if s not in allowed:
                self.add('C', 'subtype-parent-mismatch', n, f'{s} not under {tt}')
        for k in ('first_seen', 'last_confirmed'):
            v = str(fm.get(k) or '')
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', v):
                self.add('C', 'bad-date', n, f'{k}={v}')
            if fm.get(k + '_estimated'):
                self.add('W', 'date-estimated', n, f'{k}={v} (추정값, 소스 발행일로 확정 필요)')
        lc = w.parse_date(fm.get('last_confirmed'))
        if lc and (w.TODAY - lc).days > 365:
            self.add('W', 'stale', n, f'last_confirmed={lc}')
        srcs = fm.get('sources') or []
        srcs = [srcs] if isinstance(srcs, str) else srcs
        tiers = []
        for s in srcs:
            r = self.resolve(s)
            if r is None or not r.startswith('sources/'):
                self.add('C', 'unresolved-source', n, s[:90])
            else:
                sfm = self.fms.get(r) or {}
                tiers.append(str(sfm.get('tier')))
        if not srcs:
            self.add('C', 'no-sources', n)
        if srcs and not any(t in ('1', '2') for t in tiers):
            self.add('I', 'no-independent-source', n)
        b2 = re.sub(r'```.*?```', '', body, flags=re.S)
        # banned words (ignore inside blockquote lines which may quote sources)
        prose = '\n'.join(l for l in b2.split('\n') if not l.strip().startswith('>'))
        hits = [x for x in w.BANNED if x in prose]
        if hits:
            self.add('W', 'banned-word', n, ','.join(h.strip() for h in hits))
        for sec in SECTIONS:
            if sec not in body:
                self.add('W', 'missing-section', n, sec)
        # B/C/D ungrounded bullets
        secs = w.sections(body)
        ungrounded = 0
        for h, c in secs.items():
            if re.match(r'^[BCD]\.', h):
                for line in c.split('\n'):
                    ls = line.strip()
                    if not ls.startswith('-'):
                        continue
                    if any(k in ls for k in ('[[', '미공개', '❓', '⚠️', '✅', 'not disclosed')):
                        continue
                    if re.search(r'\d|[A-Z][a-z]{2,}', ls):
                        ungrounded += 1
        if ungrounded >= 3:
            self.add('W', 'ungrounded-bcd', n, f'B/C/D에 인용·미공개 표기 없는 서술 {ungrounded}건')
        if fm.get('depth') == 'full' and '```mermaid' not in body:
            self.add('W', 'no-mermaid', n)
        ca = re.search(r'## Consulting Angle(.*?)(\n## |\Z)', body, re.S)
        if not ca or len(ca.group(1).strip()) < 120:
            self.add('W', 'thin-consulting-angle', n)
        if re.search(r'상태:\s*unresolved', body):
            self.add('W', 'unresolved-contradiction', n)
        if len(body.split('\n')) > 400:
            self.add('W', 'page-too-long', n, f'{len(body.split(chr(10)))} lines')

    def source(self, n):
        fm = self.fms[n]
        if fm is None:
            self.add('C', 'no-frontmatter', n); return
        for k in ('title', 'tier', 'url'):
            if k not in fm or fm[k] in (None, ''):
                self.add('C', 'missing-field', n, k)
        if str(fm.get('tier')) not in ('1', '2', '3', '4'):
            self.add('C', 'bad-tier', n, str(fm.get('tier')))
        raw = fm.get('raw')
        if not raw:
            if not fm.get('deprecated') and fm.get('source_type') not in ('consulting-document',):
                self.add('W', 'source-no-raw', n)
        elif not os.path.exists(os.path.join(w.ROOT, raw)):
            self.add('C', 'source-raw-missing', n, raw)
        if fm.get('source_type') == 'multi-source-compilation' and not fm.get('deprecated'):
            self.add('W', 'compilation-source', n, '개별 source로 분해 필요')

    def coverage(self):
        cnt = collections.Counter(); sub = collections.Counter(); pair = collections.defaultdict(list)
        for n, fm in self.fms.items():
            if n.startswith('usecases/') and fm:
                cnt[fm.get('primary_category')] += 1
                sub[fm.get('subcategory')] += 1
                v = fm.get('vendor'); v = tuple(v) if isinstance(v, list) else (v,)
                pair[(str(fm.get('company')).lower(), v)].append(n)
        for c in w.CATS:
            if cnt[c] == 0:
                self.add('I', 'category-gap', c)
        for s in SUBCATS:
            if sub[s] == 0:
                self.add('I', 'subcategory-gap', s)
        for k, v in pair.items():
            if len(v) > 1 and k[0] not in ('_다수', 'ibm', 'moderna', 'walmart', 'microsoft', 'workday', 'jpmorgan chase', 'sk하이닉스', 'siemens', 'accenture', 'deloitte', 'amazon', 'cisco') and not k[0].startswith('_'):
                self.add('I', 'possible-duplicate', ', '.join(v), f'company={k[0]} vendor={k[1]}')
        # index drift
        idx = self.pages.get('index', '')
        m = re.search(r'\*\*(\d+)건 use case', idx)
        actual = sum(1 for n in self.fms if n.startswith('usecases/'))
        if m and int(m.group(1)) != actual:
            self.add('I', 'index-drift', 'index', f'index says {m.group(1)}, actual {actual}')
        # internal in exports
        ex = os.path.join(w.ROOT, 'wiki', 'exports', 'usecases.json')
        if os.path.exists(ex):
            try:
                data = json.load(open(ex, encoding='utf-8'))
                internal = {n.split('/')[-1] for n, fm in self.fms.items() if fm and fm.get('visibility') == 'internal'}
                leaked = [d['slug'] for d in data if d.get('slug') in internal]
                if leaked:
                    self.add('C', 'internal-in-export', 'exports/usecases.json', ', '.join(leaked))
            except Exception as e:
                self.add('W', 'export-unreadable', 'exports/usecases.json', str(e))

    def run(self, only=None):
        load_taxonomy()
        self.links(only)
        for n in self.fms:
            if only and n != only:
                continue
            if n.startswith('usecases/'):
                self.usecase(n)
            elif n.startswith('sources/'):
                self.source(n)
        if only is None:
            self.coverage()
        return self.f

    # ---------- output
    def counts(self):
        c = collections.Counter()
        for (sev, code), v in self.f.items():
            c[sev] += len(v)
        return c

    def report(self):
        out = []
        c = self.counts()
        out.append(f"# Lint {w.TODAY.isoformat()} — critical {c['C']} · warning {c['W']} · info {c['I']}")
        uc = sum(1 for n in self.fms if n.startswith('usecases/'))
        src = sum(1 for n in self.fms if n.startswith('sources/'))
        out.append(f"scope: usecases {uc} · sources {src} · pages {len(self.pages)}\n")
        for sev, label in (('C', '🔴 Critical'), ('W', '🟡 Warning'), ('I', '🔵 Info')):
            items = [(code, v) for (s, code), v in sorted(self.f.items()) if s == sev]
            if not items:
                continue
            out.append(f"## {label} ({sum(len(v) for _, v in items)})")
            for code, v in sorted(items, key=lambda kv: -len(kv[1])):
                out.append(f"\n### {code} ({len(v)})")
                for page, detail in v[:40]:
                    out.append(f"- [[{page}]] {detail}" if '/' in page else f"- {page} {detail}")
                if len(v) > 40:
                    out.append(f"- … +{len(v) - 40}")
            out.append('')
        return '\n'.join(out)

    def to_json(self):
        return {'date': w.TODAY.isoformat(), 'counts': dict(self.counts()),
                'findings': [{'severity': s, 'code': code, 'page': p, 'detail': d} for (s, code), v in self.f.items() for p, d in v]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--quick', metavar='FILE')
    ap.add_argument('--write-report', action='store_true')
    ap.add_argument('--strict', action='store_true')
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    L = Lint()
    only = None
    if a.quick:
        p = os.path.abspath(a.quick)
        if not p.startswith(os.path.join(w.ROOT, 'wiki')) or not p.endswith('.md'):
            print('quick: not a wiki page, skipped'); return 0
        only = os.path.relpath(p, w.WIKI).replace('\\', '/')[:-3]
        if only not in L.pages:
            print('quick: page not found (new file?)'); return 0
    L.run(only)
    if a.json:
        print(json.dumps(L.to_json(), ensure_ascii=False, indent=1))
    else:
        print(L.report())
    if a.write_report:
        out = os.path.join(w.WIKI, 'syntheses', f'lint-{w.TODAY.isoformat()}.md')
        fmm = f"---\ntype: lint-report\ngenerated_at: {w.TODAY.isoformat()}\ngenerator: scripts/lint.py\n"
        cc = L.counts()
        fmm += f"critical: {cc['C']}\nwarning: {cc['W']}\ninfo: {cc['I']}\n---\n\n"
        w.write(out, fmm + L.report())
        print(f'\nreport written: {os.path.relpath(out, w.ROOT)}')
    if (a.strict or a.quick) and L.counts()['C'] > 0:
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
