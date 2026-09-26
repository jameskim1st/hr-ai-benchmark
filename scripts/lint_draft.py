import os, re, sys, json, glob, datetime, collections
sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'C:\AI\AI-HR\Benchmark'
WIKI = os.path.join(ROOT, 'wiki')
TODAY = datetime.date(2026, 9, 27)

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

def fm(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m: return None, text
    d = {}
    cur = None
    for line in m.group(1).split('\n'):
        if re.match(r'^\s*-\s', line) and cur:
            d.setdefault(cur, [])
            if not isinstance(d[cur], list): d[cur] = []
            d[cur].append(re.sub(r'^\s*-\s*', '', line).strip().strip('"'))
        elif re.match(r'^[\w_]+:', line):
            k, _, v = line.partition(':')
            k = k.strip(); v = v.split('#')[0].strip() if not v.strip().startswith('"') else v.strip()
            v = v.strip().strip('"')
            if v.startswith('[') and v.endswith(']'):
                v = [x.strip().strip('"').strip("'") for x in v[1:-1].split(',') if x.strip()]
            d[k] = v if v != '' else None
            cur = k
    return d, text[m.end():]

pages = {}
for p in glob.glob(os.path.join(WIKI, '**', '*.md'), recursive=True):
    rel = os.path.relpath(p, WIKI).replace('\\', '/')
    pages[rel[:-3]] = read(p)
names = set(pages)
basenames = collections.defaultdict(list)
for n in names: basenames[n.split('/')[-1]].append(n)
# CLAUDE.md is at root
extra = {'CLAUDE'}

def resolve(target):
    t = target.split('|')[0].split('#')[0].strip()
    if t.endswith('.md'): t = t[:-3]
    if t in names or t in extra: return t
    if t in basenames and len(basenames[t]) >= 1: return basenames[t][0]
    return None

# ---- link check
broken = collections.defaultdict(list)
inbound = collections.Counter()
for n, txt in pages.items():
    body = re.sub(r'```.*?```', '', txt, flags=re.S)
    for m in re.finditer(r'\[\[([^\]]+)\]\]', body):
        r = resolve(m.group(1))
        if r is None: broken[n].append(m.group(1))
        else: inbound[r] += 1

print('=== BROKEN WIKILINKS:', sum(len(v) for v in broken.values()), 'in', len(broken), 'pages')
for n, v in sorted(broken.items()):
    print(f'  {n}: {sorted(set(v))[:8]}')

orphans = [n for n in names if inbound[n] == 0 and not n.startswith('sources/') and n not in ('index','log','dashboard','guide','guide-html-export')]
print('\n=== ORPHANS (no inbound links, non-source):', len(orphans))
for o in sorted(orphans): print('  ', o)

# ---- usecases
CATS = {"Talent Acquisition","Onboarding & Transitions","Learning & Development","Performance & Talent Management","Total Rewards","Employee Experience & HR Ops","Strategic Workforce & Governance"}
REQ = ['title','slug','primary_category','subcategory','tags','company','industry','region','vendor','vendor_type','ai_tech_type','ai_tech_subtype','stage','frequency','first_seen','last_confirmed','confidence','sources']
BANNED = ['아마도','추정','보통 ','일반적으로','대개','대체로','통상',' likely',' probably',' typically',' generally','most likely','추측']
TYPES = {'generative':{'text-generation','summarization-qa','multimodal','information-extraction'},'predictive':{'prediction','clustering-classification','recommendation-ranking'},'recognition':{'ocr','speech-recognition'},'decision-optimization':{'optimization'},'automation':{'rpa'}}
TIER_W = {'1':0.35,'2':0.20,'3':0.10,'4':0.15}

src_tier = {}
src_url = {}
for n, txt in pages.items():
    if n.startswith('sources/'):
        d, _ = fm(txt)
        src_tier[n] = str(d.get('tier')) if d else None
        src_url[n] = d.get('url') if d else None

rows = []
issues = collections.defaultdict(list)
for n, txt in sorted(pages.items()):
    if not n.startswith('usecases/'): continue
    d, body = fm(txt)
    if d is None: issues['no_frontmatter'].append(n); continue
    for k in REQ:
        if k not in d or d[k] in (None, '', []): issues['missing_'+k].append(n)
    if d.get('primary_category') not in CATS: issues['bad_category'].append((n, d.get('primary_category')))
    if d.get('slug') and d['slug'] != n.split('/')[-1]: issues['slug_mismatch'].append((n, d['slug']))
    # ai tech parent/child
    tt = d.get('ai_tech_type') or []; st = d.get('ai_tech_subtype') or []
    if isinstance(tt, str): tt=[tt]
    if isinstance(st, str): st=[st]
    allowed = set().union(*[TYPES.get(t,set()) for t in tt])
    for s in st:
        if s not in allowed: issues['subtype_parent_mismatch'].append((n, tt, s))
    # sources existence
    srcs = d.get('sources') or []
    if isinstance(srcs, str): srcs=[srcs]
    tiers = []
    for s in srcs:
        r = resolve(s)
        if r is None: issues['missing_source_page'].append((n, s))
        else: tiers.append(src_tier.get(r))
    # confidence formula
    try:
        conf = float(d.get('confidence'))
    except: conf = None; issues['bad_confidence'].append(n)
    base = sum(TIER_W.get(t,0) for t in tiers)
    lc = d.get('last_confirmed')
    try:
        lcd = datetime.date.fromisoformat(str(lc)[:10]); age = (TODAY-lcd).days/30.4
        rec = 0.10 if age<=6 else 0 if age<=12 else -0.15 if age<=24 else -0.30
    except: lcd=None; age=None; rec=0; issues['bad_last_confirmed'].append((n, lc))
    unresolved = len(re.findall(r'상태:\s*unresolved', body))
    calc = max(0,min(1, base+rec-0.2*unresolved))
    if conf is not None and abs(calc-conf) > 0.15: issues['confidence_off_formula'].append((n, conf, round(calc,2), tiers, round(age or 0,1)))
    if age is not None and age > 12: issues['stale'].append((n, lc))
    if conf is not None and conf < 0.4: issues['low_conf'].append(n)
    if not any(t in ('1','2') for t in tiers): issues['tier_imbalance'].append(n)
    # banned words in body (exclude code blocks)
    b2 = re.sub(r'```.*?```','',body,flags=re.S)
    hits = [w for w in BANNED if w in b2]
    if hits: issues['banned_words'].append((n, hits))
    # sections
    for sec in ['## Summary','## Problem','## Solution Architecture','### A.','### B.','### C.','### D.','### E.','## Impact','## Governance','## Contradictions','## Consulting Angle']:
        if sec not in body: issues['missing_section_'+sec.strip('#').strip()].append(n)
    nd = body.count('미공개')
    mer = body.count('```mermaid')
    if mer == 0: issues['no_mermaid'].append(n)
    if unresolved: issues['unresolved_contradiction'].append((n, unresolved))
    ca = re.search(r'## Consulting Angle(.*?)(\n## |\Z)', body, re.S)
    if ca and len(ca.group(1).strip()) < 80: issues['thin_consulting_angle'].append(n)
    # citation coverage in Solution Architecture
    sa = re.search(r'## Solution Architecture(.*?)\n## Impact', body, re.S)
    cites = len(re.findall(r'\[\[sources/', sa.group(1))) if sa else 0
    if sa and cites == 0: issues['sa_no_citations'].append(n)
    rows.append(dict(n=n, conf=conf, calc=round(calc,2), tiers=tiers, nsrc=len(srcs), age=round(age,1) if age else None, nd=nd, mer=mer, cites=cites, stage=d.get('stage'), region=d.get('region'), cat=d.get('primary_category'), words=len(body.split())))

print('\n=== USECASE ISSUES')
for k, v in sorted(issues.items(), key=lambda kv:-len(kv[1])):
    print(f'\n[{k}] {len(v)}')
    for item in v[:12]: print('   ', item)
    if len(v)>12: print('    ...')

print('\n=== USECASE STATS')
confs = [r['conf'] for r in rows if r['conf'] is not None]
print('n=', len(rows), 'avg conf=', round(sum(confs)/len(confs),3), '>=0.5:', sum(c>=0.5 for c in confs), '>=0.7:', sum(c>=0.7 for c in confs), '<0.4:', sum(c<0.4 for c in confs))
print('avg sources/usecase=', round(sum(r['nsrc'] for r in rows)/len(rows),2), ' avg 미공개 count=', round(sum(r['nd'] for r in rows)/len(rows),1), ' avg mermaid=', round(sum(r['mer'] for r in rows)/len(rows),2), ' avg words=', round(sum(r['words'] for r in rows)/len(rows)))
print('stage dist:', collections.Counter(r['stage'] for r in rows))
print('cat dist:', collections.Counter(r['cat'] for r in rows))
print('region dist:', collections.Counter(tuple(r['region']) if isinstance(r['region'],list) else r['region'] for r in rows))
print('src count dist:', collections.Counter(r['nsrc'] for r in rows))
print('sources per page shared: top sources by usage:')
uc_src = collections.Counter()
for n, txt in pages.items():
    if n.startswith('usecases/'):
        d,_ = fm(txt)
        for s in (d.get('sources') or []):
            r = resolve(s); uc_src[r]+=1
for s,c in uc_src.most_common(12): print('   ', c, s, 'tier', src_tier.get(s))
print('sources with url:', sum(1 for v in src_url.values() if v), '/', len(src_url))
print('source tier dist:', collections.Counter(src_tier.values()))
# raw coverage
raws = glob.glob(os.path.join(ROOT,'raw','**','*.*'), recursive=True)
print('raw files:', len(raws), ' sources pages:', len(src_tier), '-> sources without raw backing ~', len(src_tier)-len([r for r in raws if r.endswith('.md')]))
# sources orphan
src_in = [n for n in src_tier if uc_src[n]==0]
print('sources not referenced by any usecase frontmatter:', len(src_in), src_in[:15])
json.dump(rows, open(os.path.join(os.path.dirname(__file__),'rows.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)
