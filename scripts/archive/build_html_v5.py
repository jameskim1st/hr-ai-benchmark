#!/usr/bin/env python3
"""
v5: Process full-width + System/Data/Model 3-col + no Mermaid
"""
import json, os

JSON_PATH = os.path.join(os.path.dirname(__file__), '..', 'wiki', 'exports', 'usecases.json')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'wiki', 'exports', 'hr-ai-usecase-collection.html')

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data_js = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

CSS = r"""
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#fff;--bg2:#fafafa;--bg3:#f4f4f5;
  --text:#18181b;--text2:#52525b;--text3:#a1a1aa;
  --border:#e4e4e7;--accent:#2563eb;--accent-bg:#eff6ff;
  --green:#16a34a;--yellow:#ca8a04;--red:#dc2626;
  --r:10px;
  --cat-ta:#2563eb;--cat-ob:#0d9488;--cat-ld:#7c3aed;
  --cat-pm:#ea580c;--cat-tr:#16a34a;--cat-ex:#4f46e5;--cat-sw:#e11d48;
}
.dark{
  --bg:#09090b;--bg2:#18181b;--bg3:#27272a;
  --text:#fafafa;--text2:#a1a1aa;--text3:#52525b;
  --border:#27272a;--accent:#60a5fa;--accent-bg:#172554;
}
body{font-family:'Pretendard Variable','Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;-webkit-font-smoothing:antialiased;transition:background .25s,color .25s}
.w{max-width:1100px;margin:0 auto;padding:0 20px}
header{background:var(--bg);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100;padding:20px 0 0}
.ht{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
h1{font-size:1.25rem;font-weight:700;letter-spacing:-.025em}
.hs{font-size:.72rem;color:var(--text3);margin-top:1px}
.hr{display:flex;gap:6px;align-items:center}
.si{position:relative}.si svg{position:absolute;left:8px;top:50%;transform:translateY(-50%);width:14px;height:14px;color:var(--text3)}
.si input{width:200px;padding:6px 10px 6px 28px;border:1px solid var(--border);border-radius:8px;font-size:.75rem;background:var(--bg);color:var(--text);outline:none}
.si input:focus{border-color:var(--accent)}
.ib{width:32px;height:32px;display:flex;align-items:center;justify-content:center;border:1px solid var(--border);border-radius:8px;background:var(--bg);color:var(--text2);cursor:pointer;font-size:.85rem;transition:all .15s}
.ib:hover{background:var(--bg2)}.ib.on{background:var(--accent-bg);border-color:var(--accent);color:var(--accent)}
.tabs{display:flex;gap:0;margin-top:14px}
.tab{padding:8px 16px;font-size:.78rem;font-weight:500;color:var(--text3);cursor:pointer;border-bottom:2px solid transparent;transition:all .12s}
.tab:hover{color:var(--text2)}.tab.on{color:var(--accent);border-color:var(--accent);font-weight:600}
.fl{display:flex;gap:6px;align-items:center;padding:12px 0;flex-wrap:wrap}
.fs{padding:5px 24px 5px 8px;border:1px solid var(--border);border-radius:6px;font-size:.72rem;background:var(--bg);color:var(--text2);cursor:pointer;outline:none;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='10' viewBox='0 0 24 24' fill='none' stroke='%23a1a1aa' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 6px center}
.fc{font-size:.72rem;color:var(--text3);margin-left:auto}
.fx{font-size:.68rem;color:var(--accent);cursor:pointer}.fx:hover{text-decoration:underline}
.sec{margin:20px 0}
.sh{display:flex;align-items:center;gap:8px;padding:10px 0;cursor:pointer;user-select:none}
.sh:hover .sn{color:var(--accent)}
.sd{width:7px;height:7px;border-radius:50%;flex-shrink:0}
.sn{font-size:.88rem;font-weight:600;transition:color .12s}
.sc{font-size:.6rem;font-weight:600;padding:1px 6px;border-radius:6px;background:var(--bg3);color:var(--text3)}
.sv{margin-left:auto;width:14px;height:14px;color:var(--text3);transition:transform .2s}.sv.open{transform:rotate(180deg)}
.gr{display:grid;grid-template-columns:1fr;gap:1px;background:var(--border);border:1px solid var(--border);border-radius:var(--r);overflow:hidden;margin-bottom:16px}

/* Card */
.uc{background:var(--bg);padding:16px 20px;cursor:pointer;transition:background .12s}
.uc:hover{background:var(--bg2)}
.uc-row{display:grid;grid-template-columns:7px 1fr auto;gap:10px;align-items:start}
.uc-dot{width:7px;height:7px;border-radius:50%;margin-top:6px}
.uc-co{font-size:.82rem;font-weight:600}
.uc-ti{font-size:.72rem;color:var(--text2);margin-top:1px}
.uc-conf{font-size:.72rem;font-weight:700;font-variant-numeric:tabular-nums}
.uc-tags{display:flex;gap:4px;margin-top:6px;flex-wrap:wrap}
.tg{font-size:.6rem;padding:1px 6px;border-radius:3px;background:var(--bg3);color:var(--text3)}
.tg.kr{background:#fef3c7;color:#92400e}.dark .tg.kr{background:#422006;color:#fbbf24}
.uc-imp{font-size:.7rem;color:var(--text2);margin-top:6px;line-height:1.5}

/* Detail */
.det{display:none;margin-top:14px;padding-top:14px;border-top:1px solid var(--border)}
.det.open{display:block;animation:fi .15s ease}
@keyframes fi{from{opacity:0}to{opacity:1}}

/* ★ 통일 템플릿: 새 레이아웃 */
/* Row 1: Pain Point (full) */
/* Row 2: Process Flow (full, 크게) */
/* Row 3: System | Data | Model (3열) */
/* Row 4: Impact Before→After (full) */
/* Row 5: Consulting (full) */

.tpl-sec{padding:12px 16px;background:var(--bg2);border-radius:8px;margin-top:10px}
.tpl-hd{font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--text3);margin-bottom:6px;display:flex;align-items:center;gap:5px}
.tpl-hd i{font-style:normal;font-size:.7rem}
.tpl-bd{font-size:.72rem;color:var(--text2);line-height:1.65;white-space:pre-line}

/* Process: 풀 폭, 더 넓은 공간 */
.flow-wrap{padding:16px;background:var(--bg2);border-radius:8px;margin-top:10px;overflow-x:auto}
.flow{display:flex;align-items:center;gap:0;padding:8px 0;min-width:min-content}
.flow-step{
  padding:8px 14px;
  background:var(--bg);border:1px solid var(--border);border-radius:7px;
  font-size:.7rem;font-weight:500;color:var(--text);
  white-space:nowrap;flex-shrink:0;
  max-width:200px;overflow:hidden;text-overflow:ellipsis;
}
.flow-step.hl{background:var(--accent-bg);border-color:var(--accent);color:var(--accent)}
.flow-arr{color:var(--text3);font-size:.8rem;padding:0 6px;flex-shrink:0}
.flow-before-after{
  display:flex;gap:0;align-items:stretch;margin-top:6px;
}
.flow-ba-box{flex:1;padding:8px 14px;font-size:.68rem;line-height:1.5}
.flow-ba-before{background:#fef2f2;color:#991b1b;border-radius:7px 0 0 7px;border:1px solid #fecaca}
.dark .flow-ba-before{background:#2c1111;color:#fca5a5;border-color:#5c2222}
.flow-ba-after{background:#f0fdf4;color:#166534;border-radius:0 7px 7px 0;border:1px solid #bbf7d0;border-left:0}
.dark .flow-ba-after{background:#0c2a14;color:#86efac;border-color:#1a5c2e}
.flow-ba-mid{display:flex;align-items:center;padding:0 3px;background:var(--bg3);font-size:.85rem;color:var(--text3)}
.flow-ba-label{font-size:.55rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;opacity:.6;margin-bottom:2px}

/* 3열 그리드: System | Data | Model */
.three{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:10px}
@media(max-width:700px){.three{grid-template-columns:1fr}}
.info-block{padding:12px 14px;background:var(--bg2);border-radius:8px}
.info-row{display:flex;gap:6px;font-size:.68rem;padding:3px 0;border-bottom:1px solid var(--border)}
.info-row:last-child{border-bottom:none}
.info-key{font-weight:600;color:var(--text3);min-width:60px;flex-shrink:0;font-size:.62rem}
.info-val{color:var(--text2);word-break:break-word}

/* Consulting */
.cbox{padding:10px 14px;border-left:2px solid var(--accent);background:var(--accent-bg);border-radius:0 7px 7px 0;font-size:.7rem;line-height:1.6;color:var(--text2);margin-top:10px}

/* Company view */
.cv{background:var(--bg);border:1px solid var(--border);border-radius:var(--r);padding:16px 20px;margin-bottom:8px}
.cv-n{font-size:.88rem;font-weight:600}
.cv-a{width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;color:#fff;flex-shrink:0}
.cv-b{display:flex;gap:2px;height:5px;margin-top:5px;border-radius:2px;overflow:hidden}
.cv-s{flex:1;border-radius:1px}
.cv-r{display:flex;align-items:center;gap:6px;padding:4px 0;font-size:.72rem;border-bottom:1px solid var(--border)}
.cv-r:last-child{border-bottom:none}

/* Matrix */
.mx-w{overflow-x:auto;margin:16px 0}
.mx{border-collapse:collapse;font-size:.65rem;width:100%}
.mx th{padding:6px 4px;font-weight:600;text-align:left;border-bottom:2px solid var(--border);background:var(--bg);position:sticky;top:0;white-space:nowrap}
.mx td{padding:4px;border-bottom:1px solid var(--border);text-align:center}
.mx td:first-child{text-align:left;font-weight:500;white-space:nowrap}
.mx tr:hover td{background:var(--bg2)}
.mp{display:inline-block;padding:1px 6px;border-radius:3px;font-size:.6rem;font-weight:600}

footer{border-top:1px solid var(--border);padding:16px 0;margin-top:32px;font-size:.65rem;color:var(--text3);text-align:center}
.dark .uc,.dark .cv{background:var(--bg2)}.dark .tpl-sec,.dark .flow-wrap,.dark .info-block{background:var(--bg3)}
.dark .flow-step{background:var(--bg3);border-color:var(--border)}
.dark select,.dark input{background:var(--bg2);color:var(--text);border-color:var(--border)}
.dark header{background:var(--bg)}
@media(max-width:700px){.ht{flex-direction:column;align-items:flex-start}.si input{width:100%}}
"""

JS = r"""
const C=[
{k:'Talent Acquisition',s:'TA',c:'var(--cat-ta)'},
{k:'Onboarding & Transitions',s:'OB',c:'var(--cat-ob)'},
{k:'Learning & Development',s:'LD',c:'var(--cat-ld)'},
{k:'Performance & Talent Management',s:'Perf',c:'var(--cat-pm)'},
{k:'Total Rewards',s:'TR',c:'var(--cat-tr)'},
{k:'Employee Experience & HR Ops',s:'EX',c:'var(--cat-ex)'},
{k:'Strategic Workforce & Governance',s:'Gov',c:'var(--cat-sw)'}
];
const ci=c=>C.find(x=>x.k===c)||{s:'?',c:'#888'};
const cc=v=>v>=.5?'var(--green)':v>=.3?'var(--yellow)':'var(--red)';
const esc=s=>s?(s+'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'):'';
const nd='<span style="color:var(--text3);font-size:.68rem">Not disclosed</span>';
let dk=0,kr=0,ct='cat',F=[...D];
function tDk(){dk=!dk;document.documentElement.classList.toggle('dark',dk)}
function tKR(){kr=!kr;document.getElementById('kb').classList.toggle('on',kr);af()}
function sT(t){ct=t;document.querySelectorAll('.tab').forEach(e=>e.classList.toggle('on',e.dataset.t===t));['cat','co','mx'].forEach(v=>document.getElementById('v'+v).style.display=v===t?'':'none');ren()}
function cF(){document.getElementById('fI').value='';document.getElementById('fR').value='';document.getElementById('fC').value='0';document.getElementById('q').value='';kr=0;document.getElementById('kb').classList.remove('on');af()}
function af(){
  const q=document.getElementById('q').value.toLowerCase(),
    i=document.getElementById('fI').value,
    r=document.getElementById('fR').value,
    c=parseFloat(document.getElementById('fC').value)||0;
  F=D.filter(u=>{
    if(kr&&!(u.region||[]).includes('kr'))return 0;
    if(q&&!JSON.stringify(u).toLowerCase().includes(q))return 0;
    if(i&&!(u.industry||[]).includes(i))return 0;
    if(r&&!(u.region||[]).includes(r))return 0;
    return u.confidence>=c;
  });
  document.getElementById('cA').style.display=(q||i||r||c>0||kr)?'':'none';
  document.getElementById('fn').textContent=F.length+' / '+D.length;
  ren();
}

function renderFlow(steps){
  if(!steps||!steps.length)return nd;
  return '<div class="flow">'+steps.map((s,i)=>{
    const hl=/(AI|GPT|Agent|Olivia|Ava|LLM|watsonx|Joule|Skye|Copilot|inAIR|AICT|Gloat|Paradox)/i.test(s);
    return(i>0?'<span class="flow-arr">\u2192</span>':'')+
      '<div class="flow-step'+(hl?' hl':'')+'" title="'+esc(s)+'">'+esc(s)+'</div>';
  }).join('')+'</div>';
}

function renderBA(u){
  const b=u.process_before,a=u.process_after,imp=u.impact_summary;
  if(b||a){
    return `<div class="flow-before-after">
      <div class="flow-ba-box flow-ba-before"><div class="flow-ba-label">Before</div>${esc(b)||'Not disclosed'}</div>
      <div class="flow-ba-mid">\u2192</div>
      <div class="flow-ba-box flow-ba-after"><div class="flow-ba-label">After</div>${esc(a)||'Not disclosed'}</div>
    </div>${imp?'<div style="margin-top:6px;font-size:.68rem;color:var(--text2)">'+esc(imp)+'</div>':''}`;
  }
  if(imp)return '<div style="font-size:.7rem;color:var(--text2);line-height:1.5">'+esc(imp)+'</div>';
  return nd;
}

function renderInfoBlock(title,icon,obj){
  if(!obj||!Object.keys(obj).length)return `<div class="info-block"><div class="tpl-hd"><i>${icon}</i> ${title}</div>${nd}</div>`;
  let h=`<div class="info-block"><div class="tpl-hd"><i>${icon}</i> ${title}</div>`;
  for(const[k,v] of Object.entries(obj)){
    h+=`<div class="info-row"><span class="info-key">${esc(k)}</span><span class="info-val">${esc(v)}</span></div>`;
  }
  return h+'</div>';
}

function card(u,idx){
  const c=ci(u.primary_category),cn=u.confidence||0;
  const tags=[];
  if(u.vendor&&u.vendor.length)tags.push(Array.isArray(u.vendor)?u.vendor[0]:u.vendor);
  if(u.industry&&u.industry.length)tags.push(u.industry[0]);
  if((u.region||[]).includes('kr'))tags.push('KR');

  let h=`<div class="uc" onclick="tog(${idx})" id="u${idx}">`;
  h+=`<div class="uc-row">
    <div class="uc-dot" style="background:${c.c}"></div>
    <div>
      <div class="uc-co">${esc(typeof u.company==='string'?u.company:'')}</div>
      <div class="uc-ti">${esc(u.title)}</div>
      <div class="uc-tags">${tags.map(t=>'<span class="tg'+(t==='KR'?' kr':'')+'">'+esc(t)+'</span>').join('')}</div>
      ${u.impact_summary?'<div class="uc-imp">'+esc(u.impact_summary).substring(0,140)+'</div>':''}
    </div>
    <div class="uc-conf" style="color:${cc(cn)}">${cn.toFixed(2)}</div>
  </div>`;

  // Detail
  h+=`<div class="det" id="d${idx}">`;

  // 1. Pain Point (full)
  if(u.problem){
    h+=`<div class="tpl-sec"><div class="tpl-hd"><i>\ud83d\udccb</i> Pain Point</div><div class="tpl-bd">${esc(u.problem)}</div></div>`;
  }

  // 2. Process Flow (full, 넓게)
  h+=`<div class="flow-wrap"><div class="tpl-hd"><i>\ud83d\udd35</i> Process Flow</div>${renderFlow(u.process_steps)}</div>`;

  // 3. System | Data | Model (3열)
  h+=`<div class="three">`;
  h+=renderInfoBlock('System','\ud83d\udfe2',u.system);
  h+=renderInfoBlock('Data','\ud83d\udfe1',u.data);
  h+=renderInfoBlock('Model','\ud83d\udfe3',u.model);
  h+=`</div>`;

  // 4. Impact Before→After (full)
  h+=`<div class="tpl-sec"><div class="tpl-hd"><i>\ud83d\udcca</i> Impact (Before \u2192 After)</div><div class="tpl-bd">${renderBA(u)}</div></div>`;

  // 5. Consulting
  if(u.consulting){h+=`<div class="cbox">\ud83d\udca1 ${esc(u.consulting)}</div>`}

  // Tags
  if(u.tags&&u.tags.length){h+=`<div style="display:flex;gap:3px;flex-wrap:wrap;margin-top:10px">${u.tags.map(t=>'<span class="tg">'+esc(t)+'</span>').join('')}</div>`}

  h+=`</div></div>`;
  return h;
}

function tog(i){const d=document.getElementById('d'+i);if(d)d.classList.toggle('open')}

function renCat(){
  let h='';C.forEach(cat=>{
    const cs=F.filter(u=>u.primary_category===cat.k).sort((a,b)=>b.confidence-a.confidence);
    if(!cs.length)return;
    h+=`<div class="sec"><div class="sh" onclick="const g=this.nextElementSibling;g.style.display=g.style.display==='none'?'':'none';this.querySelector('.sv').classList.toggle('open')"><div class="sd" style="background:${cat.c}"></div><span class="sn">${cat.k}</span><span class="sc">${cs.length}</span><svg class="sv" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></div><div class="gr">`;
    cs.forEach(u=>h+=card(u,D.indexOf(u)));h+=`</div></div>`;
  });document.getElementById('vcat').innerHTML=h;
}

function renCo(){
  const g={};F.forEach(u=>{const co=typeof u.company==='string'?u.company:'Unknown';if(!g[co])g[co]=[];g[co].push(u)});
  const s=Object.entries(g).sort((a,b)=>b[1].length-a[1].length);
  const cl=['#2563eb','#0d9488','#7c3aed','#ea580c','#16a34a','#4f46e5','#e11d48','#ca8a04','#0891b2','#7c3aed'];
  let h='';s.forEach(([co,cs],i)=>{
    const catS=new Set(cs.map(u=>u.primary_category));
    const ini=(co.replace(/[^A-Za-z\uAC00-\uD7A3]/g,'').charAt(0)||'?').toUpperCase();
    h+=`<div class="cv"><div style="display:flex;align-items:center;gap:10px"><div class="cv-a" style="background:${cl[i%cl.length]}">${ini}</div><div style="flex:1"><div class="cv-n">${esc(co)}</div><div class="cv-b">${C.map(c=>'<div class="cv-s" style="background:'+(catS.has(c.k)?c.c:'var(--bg3)')+'"></div>').join('')}</div></div><span style="font-size:.72rem;color:var(--text3)">${cs.length}</span></div><div style="margin-top:8px">${cs.sort((a,b)=>b.confidence-a.confidence).map(u=>{const c2=ci(u.primary_category);return`<div class="cv-r"><div class="sd" style="background:${c2.c};width:5px;height:5px"></div><span style="flex:1">${esc(u.title)}</span><span style="font-size:.68rem;font-weight:600;color:${cc(u.confidence)}">${u.confidence.toFixed(2)}</span></div>`}).join('')}</div></div>`;
  });document.getElementById('vco').innerHTML=h;
}

function renMx(){
  const co={};F.forEach(u=>{const c=typeof u.company==='string'?u.company:'Unknown';if(!co[c])co[c]={};co[c][u.primary_category]=u});
  const s=Object.keys(co).sort();
  let h='<div class="mx-w"><table class="mx"><thead><tr><th>Company</th>';
  C.forEach(c=>h+=`<th style="color:${c.c}">${c.s}</th>`);h+='</tr></thead><tbody>';
  s.forEach(c=>{h+='<tr><td>'+esc(c)+'</td>';C.forEach(cat=>{const u=co[c][cat.k];if(u){const v=u.confidence;const bg=v>=.5?'rgba(22,163,74,.1)':v>=.3?'rgba(202,138,4,.1)':'rgba(220,38,38,.1)';const fg=v>=.5?'var(--green)':v>=.3?'var(--yellow)':'var(--red)';h+=`<td><span class="mp" style="background:${bg};color:${fg}">${v.toFixed(2)}</span></td>`}else h+='<td></td>'});h+='</tr>'});
  h+='</tbody></table></div>';document.getElementById('vmx').innerHTML=h;
}

function ren(){if(ct==='cat')renCat();else if(ct==='co')renCo();else renMx()}
function init(){
  const inds=new Set();D.forEach(u=>(u.industry||[]).forEach(i=>inds.add(i)));
  const sel=document.getElementById('fI');[...inds].sort().forEach(i=>{const o=document.createElement('option');o.value=i;o.textContent=i;sel.appendChild(o)});
  const kc=D.filter(u=>(u.region||[]).includes('kr')).length;
  const cc2=new Set(D.map(u=>u.company).filter(Boolean)).size;
  document.getElementById('stats').textContent=D.length+' cases \u00b7 7 categories \u00b7 '+cc2+' companies \u00b7 '+kc+' Korean';
  document.getElementById('fn').textContent=D.length+' / '+D.length;
  document.getElementById('q').addEventListener('input',af);
  ren();
}
init();
"""

BODY = """
<header>
<div class="w">
  <div class="ht">
    <div><h1>HR AI Use Case Collection</h1><p class="hs" id="stats"></p></div>
    <div class="hr">
      <div class="si"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg><input type="text" id="q" placeholder="Search..."></div>
      <div class="ib" id="kb" onclick="tKR()">\U0001F1F0\U0001F1F7</div>
      <div class="ib" onclick="tDk()">\u263D</div>
    </div>
  </div>
  <div class="tabs">
    <div class="tab on" data-t="cat" onclick="sT('cat')">Category</div>
    <div class="tab" data-t="co" onclick="sT('co')">Company</div>
    <div class="tab" data-t="mx" onclick="sT('mx')">Matrix</div>
  </div>
</div>
</header>
<main class="w">
  <div class="fl">
    <select class="fs" id="fI" onchange="af()"><option value="">Industry</option></select>
    <select class="fs" id="fR" onchange="af()"><option value="">Region</option><option value="kr">Korea</option><option value="na">N. America</option><option value="eu">Europe</option><option value="apac">APAC</option><option value="global">Global</option></select>
    <select class="fs" id="fC" onchange="af()"><option value="0">Confidence</option><option value="0.5">&ge;0.50</option><option value="0.4">&ge;0.40</option><option value="0.3">&ge;0.30</option></select>
    <span class="fx" id="cA" style="display:none" onclick="cF()">Clear</span>
    <span class="fc" id="fn"></span>
  </div>
  <div id="vcat"></div>
  <div id="vco" style="display:none"></div>
  <div id="vmx" style="display:none"></div>
</main>
<footer><div class="w">HR AI Benchmark &middot; 81 Use Cases &middot; 2026-04-13</div></footer>
"""

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HR AI Use Case Collection</title>
<link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{BODY}
<script>
const D={data_js};
{JS}
</script>
</body>
</html>"""

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Done: {os.path.getsize(OUT_PATH)/1024:.0f}KB")
