#!/usr/bin/env python3
"""
usecases.json + HTML template -> single interactive HTML file
Design: Clean minimalist (Linear/Vercel aesthetic)
"""
import json, os

JSON_PATH = os.path.join(os.path.dirname(__file__), '..', 'wiki', 'exports', 'usecases.json')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'wiki', 'exports', 'hr-ai-usecase-collection.html')

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data_js = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#fff;--bg2:#f8f9fa;--bg3:#f1f3f5;
  --text:#111;--text2:#495057;--text3:#868e96;
  --border:#e9ecef;--accent:#228be6;--accent-bg:#e7f5ff;
  --radius:10px;--shadow:0 1px 2px rgba(0,0,0,.05);
  --cat-ta:#228be6;--cat-ob:#12b886;--cat-ld:#7950f2;
  --cat-pm:#fd7e14;--cat-tr:#40c057;--cat-ex:#5c7cfa;--cat-sw:#f06595;
}
.dark{
  --bg:#0d1117;--bg2:#161b22;--bg3:#21262d;
  --text:#e6edf3;--text2:#8b949e;--text3:#484f58;
  --border:#30363d;--accent:#58a6ff;--accent-bg:#1c2d42;
  --shadow:0 1px 2px rgba(0,0,0,.3);
}
body{font-family:'Pretendard Variable',system-ui,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;-webkit-font-smoothing:antialiased;transition:background .2s,color .2s}
a{color:var(--accent);text-decoration:none}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
header{border-bottom:1px solid var(--border);padding:28px 0 0;background:var(--bg);position:sticky;top:0;z-index:100}
header h1{font-size:1.35rem;font-weight:700;letter-spacing:-.02em}
header p{font-size:.78rem;color:var(--text3);margin-top:1px}
.hdr{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.hdr-r{display:flex;gap:6px;align-items:center}
.sbox{width:220px;padding:6px 10px 6px 32px;border:1px solid var(--border);border-radius:7px;font-size:.78rem;background:var(--bg);color:var(--text);outline:none;transition:border .15s}
.sbox:focus{border-color:var(--accent)}
.swrap{position:relative}
.swrap svg{position:absolute;left:9px;top:50%;transform:translateY(-50%);width:15px;height:15px;color:var(--text3)}
.btn{padding:5px 10px;border:1px solid var(--border);border-radius:7px;font-size:.72rem;background:var(--bg);color:var(--text2);cursor:pointer;transition:all .15s;line-height:1}
.btn:hover{background:var(--bg2)}
.btn.on{background:var(--accent-bg);border-color:var(--accent);color:var(--accent)}
.tabs{display:flex;gap:0;padding:16px 0 0}
.tab{padding:7px 16px;font-size:.78rem;font-weight:500;color:var(--text3);cursor:pointer;border-bottom:2px solid transparent;transition:all .15s}
.tab:hover{color:var(--text2)}
.tab.on{color:var(--accent);border-bottom-color:var(--accent)}
.flts{display:flex;gap:6px;align-items:center;padding:14px 0;flex-wrap:wrap}
.fsel{padding:4px 26px 4px 9px;border:1px solid var(--border);border-radius:6px;font-size:.72rem;background:var(--bg);color:var(--text2);cursor:pointer;outline:none;appearance:none;-webkit-appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='10' viewBox='0 0 24 24' fill='none' stroke='%23868e96' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 7px center;transition:border .15s}
.fsel:focus{border-color:var(--accent)}
.fcnt{font-size:.72rem;color:var(--text3);margin-left:auto}
.fcl{font-size:.68rem;color:var(--accent);cursor:pointer}.fcl:hover{text-decoration:underline}
.csec{margin:24px 0}
.chdr{display:flex;align-items:center;gap:8px;padding:10px 0;cursor:pointer;user-select:none}
.chdr:hover .cname{color:var(--accent)}
.cdot{width:7px;height:7px;border-radius:50%;flex-shrink:0}
.cname{font-size:.92rem;font-weight:600;letter-spacing:-.01em;transition:color .15s}
.ccnt{font-size:.62rem;font-weight:600;padding:1px 7px;border-radius:8px;background:var(--bg3);color:var(--text3)}
.cchv{margin-left:auto;width:14px;height:14px;color:var(--text3);transition:transform .2s}
.cchv.open{transform:rotate(180deg)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(460px,1fr));gap:10px;padding:6px 0 20px}
@media(max-width:520px){.grid{grid-template-columns:1fr}}
.card{background:var(--bg);border:1px solid var(--border);border-radius:var(--radius);padding:16px 20px;cursor:pointer;transition:box-shadow .2s,border-color .15s}
.card:hover{box-shadow:var(--shadow);border-color:color-mix(in srgb,var(--accent) 30%,var(--border))}
.cco{font-size:.85rem;font-weight:600;letter-spacing:-.01em}
.cti{font-size:.75rem;color:var(--text2);margin-top:1px;line-height:1.4}
.cmeta{display:flex;align-items:center;gap:5px;margin-top:8px;flex-wrap:wrap}
.tg{font-size:.62rem;padding:1px 7px;border-radius:3px;background:var(--bg3);color:var(--text3);white-space:nowrap}
.tg.kr{background:#fff3e0;color:#e65100}.dark .tg.kr{background:#3d2800;color:#ffb74d}
.cnum{margin-left:auto;font-size:.72rem;font-weight:600;font-variant-numeric:tabular-nums}
.cbar{width:100%;height:2px;background:var(--bg3);border-radius:1px;margin-top:7px;overflow:hidden}
.cfill{height:100%;border-radius:1px}
.cimp{font-size:.72rem;color:var(--text2);margin-top:8px;line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.cdet{display:none;margin-top:14px;padding-top:14px;border-top:1px solid var(--border);font-size:.75rem;color:var(--text2);line-height:1.7}
.cdet.open{display:block;animation:fi .2s ease}
@keyframes fi{from{opacity:0;transform:translateY(-3px)}to{opacity:1;transform:none}}
.dsec{margin-top:12px}
.dlbl{font-size:.62rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--text3);margin-bottom:4px}
.dtxt{white-space:pre-line}
.mbox{margin-top:6px;padding:14px;background:var(--bg2);border-radius:7px;overflow-x:auto}
.mbox svg{max-width:100%;height:auto}
.cbox{margin-top:10px;padding:10px 14px;border-left:2px solid var(--accent);background:var(--accent-bg);border-radius:0 7px 7px 0;font-size:.72rem;line-height:1.6}
.cocard{background:var(--bg);border:1px solid var(--border);border-radius:var(--radius);padding:16px 20px;margin-bottom:10px}
.coname{font-size:.92rem;font-weight:600}
.coav{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.78rem;font-weight:700;color:#fff;flex-shrink:0}
.covbar{display:flex;gap:2px;height:5px;margin-top:6px;border-radius:2px;overflow:hidden}
.covseg{flex:1;border-radius:1px}
.cocases{margin-top:10px}
.cocr{display:flex;align-items:center;gap:7px;padding:5px 0;font-size:.75rem;border-bottom:1px solid var(--border)}
.cocr:last-child{border-bottom:none}
.mwrap{overflow-x:auto;margin:20px 0}
.mtx{border-collapse:collapse;font-size:.68rem;width:100%}
.mtx th{padding:7px 5px;font-weight:600;text-align:left;border-bottom:2px solid var(--border);background:var(--bg);position:sticky;top:0;white-space:nowrap}
.mtx td{padding:5px;border-bottom:1px solid var(--border);text-align:center}
.mtx td:first-child{text-align:left;font-weight:500;white-space:nowrap}
.mtx tr:hover td{background:var(--bg2)}
.mpill{display:inline-block;padding:1px 7px;border-radius:3px;font-size:.62rem;font-weight:600;font-variant-numeric:tabular-nums}
footer{border-top:1px solid var(--border);padding:20px 0;margin-top:40px;font-size:.68rem;color:var(--text3);text-align:center}
.dark .card,.dark .cocard{background:var(--bg2);border-color:var(--border)}
.dark .mbox{background:var(--bg3)}
.dark select,.dark input{background:var(--bg2);color:var(--text);border-color:var(--border)}
.dark header{background:var(--bg);border-color:var(--border)}
@media(max-width:768px){.hdr{flex-direction:column;align-items:flex-start}.sbox{width:100%}.grid{grid-template-columns:1fr}}
"""

JS = r"""
const CATS=[
  {key:'Talent Acquisition',short:'TA',color:'var(--cat-ta)'},
  {key:'Onboarding & Transitions',short:'OB',color:'var(--cat-ob)'},
  {key:'Learning & Development',short:'LD',color:'var(--cat-ld)'},
  {key:'Performance & Talent Management',short:'Perf',color:'var(--cat-pm)'},
  {key:'Total Rewards',short:'TR',color:'var(--cat-tr)'},
  {key:'Employee Experience & HR Ops',short:'EX',color:'var(--cat-ex)'},
  {key:'Strategic Workforce & Governance',short:'Gov',color:'var(--cat-sw)'}
];
function ci(c){return CATS.find(x=>x.key===c)||{short:'?',color:'#888'}}
let dk=false,kr=false,ct='category',flt=[...USECASES];
function toggleDark(){dk=!dk;document.documentElement.classList.toggle('dark',dk);mermaid.initialize({startOnLoad:false,theme:dk?'dark':'default'})}
function toggleKR(){kr=!kr;document.getElementById('krBtn').classList.toggle('on',kr);af()}
function st(t){ct=t;document.querySelectorAll('.tab').forEach(e=>e.classList.toggle('on',e.dataset.t===t));['category','company','matrix'].forEach(v=>document.getElementById('v'+v).style.display=v===t?'':'none');ren()}
function cf(){document.getElementById('fI').value='';document.getElementById('fR').value='';document.getElementById('fC').value='0';document.getElementById('searchInput').value='';kr=false;document.getElementById('krBtn').classList.remove('on');af()}
function af(){
  const q=document.getElementById('searchInput').value.toLowerCase(),
    ind=document.getElementById('fI').value,
    reg=document.getElementById('fR').value,
    conf=parseFloat(document.getElementById('fC').value)||0;
  flt=USECASES.filter(u=>{
    if(kr&&!(u.region||[]).includes('kr'))return false;
    if(q&&!JSON.stringify(u).toLowerCase().includes(q))return false;
    if(ind&&!(u.industry||[]).includes(ind))return false;
    if(reg&&!(u.region||[]).includes(reg))return false;
    if(u.confidence<conf)return false;
    return true;
  });
  const h=q||ind||reg||conf>0||kr;
  document.getElementById('cAll').style.display=h?'':'none';
  document.getElementById('fcnt').textContent=flt.length+' / '+USECASES.length;
  ren();
}
function cc(c){return c>=.5?'var(--cat-tr)':c>=.3?'var(--cat-pm)':'var(--cat-sw)'}
function esc(s){return s?s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'):''}
function rc(u,i){
  const c=ci(u.primary_category),cn=u.confidence||0,tags=[];
  if(u.vendor&&u.vendor.length)tags.push(Array.isArray(u.vendor)?u.vendor[0]:u.vendor);
  if(u.industry&&u.industry.length)tags.push(u.industry[0]);
  if((u.region||[]).includes('kr'))tags.push('KR');
  let h=`<div class="card" onclick="tc(${i})" id="c${i}"><div style="display:flex;gap:9px"><div class="cdot" style="background:${c.color};margin-top:5px"></div><div style="flex:1;min-width:0"><div class="cco">${esc(typeof u.company==='string'?u.company:'')}</div><div class="cti">${esc(u.title)}</div><div class="cmeta">`;
  tags.forEach(t=>{h+=`<span class="tg${t==='KR'?' kr':''}">${esc(t)}</span>`});
  h+=`<span class="cnum" style="color:${cc(cn)}">${cn.toFixed(2)}</span></div><div class="cbar"><div class="cfill" style="width:${cn*100}%;background:${cc(cn)}"></div></div>`;
  if(u.impact_summary)h+=`<div class="cimp">${esc(u.impact_summary)}</div>`;
  h+=`</div></div><div class="cdet" id="d${i}">`;
  if(u.problem)h+=`<div class="dsec"><div class="dlbl">Pain Point</div><div class="dtxt">${esc(u.problem)}</div></div>`;
  if(u.impact_summary)h+=`<div class="dsec"><div class="dlbl">Impact</div><div class="dtxt">${esc(u.impact_summary)}</div></div>`;
  if(u.mermaid&&u.mermaid.length)u.mermaid.forEach((m,mi)=>{h+=`<div class="dsec"><div class="dlbl">Diagram</div><div class="mbox"><pre class="msrc" data-c="${i}" data-i="${mi}" style="display:none">${esc(m)}</pre><div id="mm${i}_${mi}"></div></div></div>`});
  if(u.consulting)h+=`<div class="dsec"><div class="dlbl">Consulting Angle</div><div class="cbox">${esc(u.consulting)}</div></div>`;
  if(u.tags&&u.tags.length)h+=`<div class="dsec" style="display:flex;gap:3px;flex-wrap:wrap;margin-top:10px">${u.tags.map(t=>'<span class="tg">'+esc(t)+'</span>').join('')}</div>`;
  h+=`</div></div>`;return h;
}
async function tc(i){
  const d=document.getElementById('d'+i);if(!d)return;
  const o=d.classList.contains('open');d.classList.toggle('open');
  if(!o){for(const s of d.querySelectorAll('.msrc')){const idx=s.dataset.i,t=document.getElementById('mm'+i+'_'+idx);if(t&&!t.innerHTML){try{const id='m'+i+'_'+idx+'_'+Date.now();const{svg}=await mermaid.render(id,s.textContent);t.innerHTML=svg}catch(e){t.innerHTML='<small style="color:var(--text3)">render error</small>'}}}}
}
function ren(){if(ct==='category')renCat();else if(ct==='company')renCo();else renMx()}
function renCat(){
  let h='';CATS.forEach(cat=>{const cs=flt.filter(u=>u.primary_category===cat.key).sort((a,b)=>b.confidence-a.confidence);if(!cs.length)return;
  h+=`<div class="csec"><div class="chdr" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'':'none';this.querySelector('.cchv').classList.toggle('open')"><div class="cdot" style="background:${cat.color}"></div><span class="cname">${cat.key}</span><span class="ccnt">${cs.length}</span><svg class="cchv" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></div><div class="grid">`;
  cs.forEach(u=>{h+=rc(u,USECASES.indexOf(u))});h+='</div></div>'});
  document.getElementById('vcategory').innerHTML=h;
}
function renCo(){
  const g={};flt.forEach(u=>{const co=typeof u.company==='string'?u.company:'Unknown';if(!g[co])g[co]=[];g[co].push(u)});
  const s=Object.entries(g).sort((a,b)=>b[1].length-a[1].length);let h='';
  const cl=['#228be6','#12b886','#7950f2','#fd7e14','#40c057','#5c7cfa','#f06595','#fab005','#20c997','#845ef7'];
  s.forEach(([co,cs],i)=>{const catS=new Set(cs.map(u=>u.primary_category));const ini=(co.replace(/[^A-Za-z\uAC00-\uD7A3]/g,'').charAt(0)||'?').toUpperCase();
  h+=`<div class="cocard"><div style="display:flex;align-items:center;gap:10px"><div class="coav" style="background:${cl[i%cl.length]}">${ini}</div><div style="flex:1"><div class="coname">${esc(co)}</div><div class="covbar">`;
  CATS.forEach(c=>{h+=`<div class="covseg" style="background:${catS.has(c.key)?c.color:'var(--bg3)'}"></div>`});
  h+=`</div></div><span style="font-size:.72rem;color:var(--text3)">${cs.length}</span></div><div class="cocases">`;
  cs.sort((a,b)=>b.confidence-a.confidence).forEach(u=>{const c2=ci(u.primary_category);h+=`<div class="cocr"><div class="cdot" style="background:${c2.color};width:5px;height:5px"></div><span style="flex:1">${esc(u.title)}</span><span class="cnum" style="color:${cc(u.confidence)};font-size:.68rem">${u.confidence.toFixed(2)}</span></div>`});
  h+='</div></div>'});document.getElementById('vcompany').innerHTML=h;
}
function renMx(){
  const co={};flt.forEach(u=>{const c=typeof u.company==='string'?u.company:'Unknown';if(!co[c])co[c]={};co[c][u.primary_category]=u});
  const s=Object.keys(co).sort();let h='<div class="mwrap"><table class="mtx"><thead><tr><th>Company</th>';
  CATS.forEach(c=>{h+=`<th style="color:${c.color}">${c.short}</th>`});h+='</tr></thead><tbody>';
  s.forEach(c=>{h+='<tr><td>'+esc(c)+'</td>';CATS.forEach(cat=>{const u=co[c][cat.key];if(u){const v=u.confidence;const bg=v>=.5?'rgba(34,197,94,.12)':v>=.3?'rgba(253,126,20,.1)':'rgba(240,101,149,.1)';const fg=v>=.5?'#16a34a':v>=.3?'#ea580c':'#e11d48';h+=`<td><span class="mpill" style="background:${bg};color:${fg}">${v.toFixed(2)}</span></td>`}else h+='<td></td>'});h+='</tr>'});
  h+='</tbody></table></div>';document.getElementById('vmatrix').innerHTML=h;
}
function init(){
  mermaid.initialize({startOnLoad:false,theme:'default'});
  const inds=new Set();USECASES.forEach(u=>(u.industry||[]).forEach(i=>inds.add(i)));
  const sel=document.getElementById('fI');[...inds].sort().forEach(i=>{const o=document.createElement('option');o.value=i;o.textContent=i;sel.appendChild(o)});
  const krC=USECASES.filter(u=>(u.region||[]).includes('kr')).length;
  const coC=new Set(USECASES.map(u=>u.company).filter(Boolean)).size;
  document.getElementById('stats').textContent=`${USECASES.length} cases · 7 categories · ${coC} companies · ${krC} Korean`;
  document.getElementById('fcnt').textContent=USECASES.length+' / '+USECASES.length;
  document.getElementById('searchInput').addEventListener('input',af);
  ren();
}
init();
"""

HTML_BODY = """
<header>
<div class="wrap">
  <div class="hdr">
    <div><h1>HR AI Use Case Collection</h1><p id="stats"></p></div>
    <div class="hdr-r">
      <div class="swrap">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        <input type="text" id="searchInput" class="sbox" placeholder="Search...">
      </div>
      <button class="btn" id="krBtn" onclick="toggleKR()">\U0001F1F0\U0001F1F7</button>
      <button class="btn" onclick="toggleDark()">\u263D</button>
    </div>
  </div>
  <div class="tabs">
    <div class="tab on" data-t="category" onclick="st('category')">Category</div>
    <div class="tab" data-t="company" onclick="st('company')">Company</div>
    <div class="tab" data-t="matrix" onclick="st('matrix')">Matrix</div>
  </div>
</div>
</header>
<main class="wrap">
  <div class="flts">
    <select class="fsel" id="fI" onchange="af()"><option value="">Industry</option></select>
    <select class="fsel" id="fR" onchange="af()">
      <option value="">Region</option><option value="kr">Korea</option>
      <option value="na">North America</option><option value="eu">Europe</option>
      <option value="apac">APAC</option><option value="global">Global</option>
    </select>
    <select class="fsel" id="fC" onchange="af()">
      <option value="0">All confidence</option>
      <option value="0.5">\u2265 0.50</option><option value="0.4">\u2265 0.40</option>
      <option value="0.3">\u2265 0.30</option>
    </select>
    <span class="fcl" id="cAll" style="display:none" onclick="cf()">Clear</span>
    <span class="fcnt" id="fcnt"></span>
  </div>
  <div id="vcategory"></div>
  <div id="vcompany" style="display:none"></div>
  <div id="vmatrix" style="display:none"></div>
</main>
<footer><div class="wrap">HR AI Benchmark \u00b7 81 Use Cases \u00b7 2026-04-13</div></footer>
"""

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HR AI Use Case Collection</title>
<link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<style>{CSS}</style>
</head>
<body>
{HTML_BODY}
<script>
const USECASES={data_js};
{JS}
</script>
</body>
</html>"""

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

size = os.path.getsize(OUT_PATH)
print(f"DONE: {size/1024:.0f}KB -> {OUT_PATH}")
