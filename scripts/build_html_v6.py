#!/usr/bin/env python3
"""
v6: Enhanced Company View with companies.json, headline cards, innerHTML rendering,
    wider process steps, specific System/Data/Model keys.
"""
import json, os
from datetime import date

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
UC_PATH = os.path.join(SCRIPT_DIR, '..', 'wiki', 'exports', 'usecases.json')
CO_PATH = os.path.join(SCRIPT_DIR, '..', 'wiki', 'exports', 'companies.json')
OUT_PATH = os.path.join(SCRIPT_DIR, '..', 'wiki', 'exports', 'hr-ai-usecase-collection.html')

with open(UC_PATH, 'r', encoding='utf-8') as f:
    uc_data = json.load(f)
with open(CO_PATH, 'r', encoding='utf-8') as f:
    co_data = json.load(f)

uc_js = json.dumps(uc_data, ensure_ascii=False, separators=(',', ':'))
co_js = json.dumps(co_data, ensure_ascii=False, separators=(',', ':'))
today = date.today().isoformat()
uc_count = len(uc_data)
co_count = len(set(u.get('company','') for u in uc_data if u.get('company')))

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
  --tech-gen:#a855f7;--tech-pred:#f59e0b;--tech-rec:#06b6d4;
  --tech-dec:#64748b;--tech-auto:#ec4899;
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

/* Card — v6 new layout with headline */
.uc{background:var(--bg);padding:14px 20px;cursor:pointer;transition:background .12s}
.uc:hover{background:var(--bg2)}
.uc-row1{display:flex;align-items:center;gap:8px}
.uc-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0}
.uc-co{font-size:.82rem;font-weight:600;flex:1}
.uc-conf{font-size:.72rem;font-weight:700;font-variant-numeric:tabular-nums;flex-shrink:0}
.uc-hl{font-size:.78rem;font-weight:500;color:var(--text);line-height:1.45;margin-top:5px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.uc-tags{display:flex;gap:4px;margin-top:6px;flex-wrap:wrap}
.tg{font-size:.6rem;padding:1px 6px;border-radius:3px;background:var(--bg3);color:var(--text3)}
.tg.kr{background:#fef3c7;color:#92400e}.dark .tg.kr{background:#422006;color:#fbbf24}
.tg.tech-gen{background:color-mix(in srgb,var(--tech-gen) 15%,transparent);color:var(--tech-gen)}
.tg.tech-pred{background:color-mix(in srgb,var(--tech-pred) 15%,transparent);color:var(--tech-pred)}
.tg.tech-rec{background:color-mix(in srgb,var(--tech-rec) 15%,transparent);color:var(--tech-rec)}
.tg.tech-dec{background:color-mix(in srgb,var(--tech-dec) 15%,transparent);color:var(--tech-dec)}
.tg.tech-auto{background:color-mix(in srgb,var(--tech-auto) 15%,transparent);color:var(--tech-auto)}
.uc-imp{font-size:.7rem;color:var(--text3);margin-top:5px;line-height:1.45;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}

/* Detail */
.det{display:none;margin-top:14px;padding-top:14px;border-top:1px solid var(--border)}
.det.open{display:block;animation:fi .15s ease}
@keyframes fi{from{opacity:0}to{opacity:1}}

.tpl-sec{padding:12px 16px;background:var(--bg2);border-radius:8px;margin-top:10px}
.tpl-hd{font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--text3);margin-bottom:6px;display:flex;align-items:center;gap:5px}
.tpl-hd i{font-style:normal;font-size:.7rem}
.tpl-bd{font-size:.72rem;color:var(--text2);line-height:1.65}
.tpl-bd ul{margin:0;padding-left:16px}.tpl-bd li{margin-bottom:2px}

/* Process flow — v6 wider steps */
.flow-wrap{padding:16px;background:var(--bg2);border-radius:8px;margin-top:10px;overflow-x:auto;width:100%}
.flow{display:flex;align-items:center;gap:0;padding:8px 0;min-width:min-content}
.flow-step{
  padding:8px 16px;
  background:var(--bg);border:1px solid var(--border);border-radius:7px;
  font-size:.72rem;font-weight:500;color:var(--text);
  white-space:normal;flex-shrink:0;
  max-width:220px;line-height:1.35;
}
.flow-step.hl{background:var(--accent-bg);border-color:var(--accent);color:var(--accent)}
.flow-arr{color:var(--text3);font-size:.85rem;padding:0 8px;flex-shrink:0}

/* Before → After */
.flow-before-after{display:flex;gap:0;align-items:stretch;margin-top:8px}
.flow-ba-box{flex:1;padding:10px 14px;font-size:.7rem;line-height:1.5}
.flow-ba-before{background:#fef2f2;color:#991b1b;border-radius:7px 0 0 7px;border:1px solid #fecaca}
.dark .flow-ba-before{background:#2c1111;color:#fca5a5;border-color:#5c2222}
.flow-ba-after{background:#f0fdf4;color:#166534;border-radius:0 7px 7px 0;border:1px solid #bbf7d0;border-left:0}
.dark .flow-ba-after{background:#0c2a14;color:#86efac;border-color:#1a5c2e}
.flow-ba-mid{display:flex;align-items:center;padding:0 4px;background:var(--bg3);font-size:.9rem;color:var(--text3)}
.flow-ba-label{font-size:.55rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;opacity:.6;margin-bottom:2px}

/* 3-col grid: System | Data | Model */
.three{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:10px}
@media(max-width:700px){.three{grid-template-columns:1fr}}
.info-block{padding:12px 14px;background:var(--bg2);border-radius:8px}
.info-row{display:flex;gap:6px;font-size:.68rem;padding:3px 0;border-bottom:1px solid var(--border)}
.info-row:last-child{border-bottom:none}
.info-key{font-weight:600;color:var(--text3);min-width:70px;flex-shrink:0;font-size:.62rem}
.info-val{color:var(--text2);word-break:break-word}

/* Consulting */
.cbox{padding:10px 14px;border-left:2px solid var(--accent);background:var(--accent-bg);border-radius:0 7px 7px 0;font-size:.7rem;line-height:1.6;color:var(--text2);margin-top:10px}
.cbox ul{margin:0;padding-left:16px}.cbox li{margin-bottom:2px}

/* ===== Company View — v6 enhanced ===== */
.cv{background:var(--bg);border:1px solid var(--border);border-radius:var(--r);padding:20px 24px;margin-bottom:12px}
.cv-head{display:flex;align-items:center;gap:12px}
.cv-a{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.78rem;font-weight:700;color:#fff;flex-shrink:0}
.cv-n{font-size:.95rem;font-weight:700}
.cv-desc{font-size:.74rem;color:var(--text2);line-height:1.55;margin-top:8px}
.cv-desc strong{color:var(--text);font-weight:600}
.cv-strat{font-size:.72rem;color:var(--text2);line-height:1.55;margin-top:8px;padding:10px 14px;background:var(--bg2);border-radius:8px;border-left:3px solid var(--accent)}
.cv-strat-label{font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--text3);margin-bottom:4px}
.cv-b{display:flex;gap:2px;height:6px;margin-top:10px;border-radius:3px;overflow:hidden}
.cv-s{flex:1;border-radius:1px;position:relative}
.cv-s[title]:hover{opacity:.8}
.cv-meta{display:flex;gap:12px;margin-top:6px;font-size:.65rem;color:var(--text3)}
.cv-uc-sec{margin-top:16px;border-top:1px solid var(--border);padding-top:12px}
.cv-uc{padding:14px 0;border-bottom:1px solid var(--border)}
.cv-uc:last-child{border-bottom:none}
.cv-uc-head{display:flex;align-items:baseline;gap:8px}
.cv-uc-title{font-size:.78rem;font-weight:600;flex:1}
.cv-uc-hl{font-size:.72rem;color:var(--text2);margin-top:3px;line-height:1.45}
.cv-cons{margin-top:14px}

/* Company simple (no companies.json entry) */
.cv-simple .cv-r{display:flex;align-items:center;gap:6px;padding:4px 0;font-size:.72rem;border-bottom:1px solid var(--border)}
.cv-simple .cv-r:last-child{border-bottom:none}

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
.dark .cv-strat{background:var(--bg3)}
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

// Company lookup by slug or name
const COL={};
CO.forEach(c=>{COL[c.slug]=c;COL[c.name]=c});

const ci=c=>C.find(x=>x.k===c)||{s:'?',c:'#888'};
const cc=v=>v>=.5?'var(--green)':v>=.3?'var(--yellow)':'var(--red)';
const esc=s=>s?(s+'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'):'';
// For fields already containing HTML tags — pass through safely (strips dangerous tags)
const htm=s=>s||'';
const nd='<span style="color:var(--text3);font-size:.68rem">Not disclosed</span>';

// AI 기술 분류 라벨·CSS class 매핑
const TECH_LABEL={generative:'생성형',predictive:'판별·예측',recognition:'인식','decision-optimization':'의사결정·최적화',automation:'자동화'};
const TECH_CLASS={generative:'tech-gen',predictive:'tech-pred',recognition:'tech-rec','decision-optimization':'tech-dec',automation:'tech-auto'};
const SUB_LABEL={'text-generation':'텍스트 생성','summarization-qa':'요약·재작성·QA','multimodal':'멀티모달','information-extraction':'정보 추출','prediction':'예측','clustering-classification':'군집·분류','recommendation-ranking':'추천·랭킹','ocr':'OCR','speech-recognition':'음성 인식','optimization':'최적화','rpa':'RPA'};
const SUB_PARENT={'text-generation':'generative','summarization-qa':'generative','multimodal':'generative','information-extraction':'generative','prediction':'predictive','clustering-classification':'predictive','recommendation-ranking':'predictive','ocr':'recognition','speech-recognition':'recognition','optimization':'decision-optimization','rpa':'automation'};
let dk=0,kr=0,ct='cat',F=[...D];

function tDk(){dk=!dk;document.documentElement.classList.toggle('dark',dk)}
function tKR(){kr=!kr;document.getElementById('kb').classList.toggle('on',kr);af()}
function sT(t){ct=t;document.querySelectorAll('.tab').forEach(e=>e.classList.toggle('on',e.dataset.t===t));['cat','co','mx'].forEach(v=>document.getElementById('v'+v).style.display=v===t?'':'none');ren()}
function cF(){document.getElementById('fI').value='';document.getElementById('fR').value='';document.getElementById('fT').value='';document.getElementById('fC').value='0';document.getElementById('q').value='';kr=0;document.getElementById('kb').classList.remove('on');af()}

function af(){
  const q=document.getElementById('q').value.toLowerCase(),
    i=document.getElementById('fI').value,
    r=document.getElementById('fR').value,
    t=document.getElementById('fT').value,
    c=parseFloat(document.getElementById('fC').value)||0;
  F=D.filter(u=>{
    if(kr&&!(u.region||[]).includes('kr'))return 0;
    if(q&&!JSON.stringify(u).toLowerCase().includes(q))return 0;
    if(i&&!(u.industry||[]).includes(i))return 0;
    if(r&&!(u.region||[]).includes(r))return 0;
    if(t&&!(u.ai_tech_type||[]).includes(t))return 0;
    return u.confidence>=c;
  });
  document.getElementById('cA').style.display=(q||i||r||c>0||kr)?'':'none';
  document.getElementById('fn').textContent=F.length+' / '+D.length;
  ren();
}

/* ---- Rendering helpers ---- */

const SYS_KEYS=['Core HRIS','AI \uc2dc\uc2a4\ud15c \ubc30\uce58','\ubc30\ud3ec \ud658\uacbd','\uc5f0\ub3d9\xb7\ud1b5\ud569','\uc0ac\uc6a9\uc790 \uc811\uc810'];
const DAT_KEYS=['\uc785\ub825 \ub370\uc774\ud130 \uc18c\uc2a4','\ub370\uc774\ud130 \uaddc\ubaa8','\uc804\ucc98\ub9ac\xb7\uc815\uc81c','\ud559\uc2b5 vs RAG','\ub370\uc774\ud130 \uac70\ubc84\ub10c\uc2a4'];
const MOD_KEYS=['Foundation model','\ubaa8\ub378 \uc720\ud615','\uc81c\uacf5 \ubc29\uc2dd','\ucee4\uc2a4\ud130\ub9c8\uc774\uc9d5 \uae30\ubc95','\ud3c9\uac00\xb7\uac00\ub4dc\ub808\uc77c'];

function renderInfoBlock(title,icon,obj,keys){
  if(!obj||!Object.keys(obj).length)return '<div class="info-block"><div class="tpl-hd"><i>'+icon+'</i> '+title+'</div>'+nd+'</div>';
  let h='<div class="info-block"><div class="tpl-hd"><i>'+icon+'</i> '+title+'</div>';
  // Show keys in order if provided, then remaining
  const shown=new Set();
  if(keys){
    keys.forEach(k=>{
      if(obj[k]!==undefined){
        shown.add(k);
        h+='<div class="info-row"><span class="info-key">'+esc(k)+'</span><span class="info-val">'+htm(obj[k])+'</span></div>';
      }
    });
  }
  for(const[k,v] of Object.entries(obj)){
    if(!shown.has(k)){
      h+='<div class="info-row"><span class="info-key">'+esc(k)+'</span><span class="info-val">'+htm(v)+'</span></div>';
    }
  }
  return h+'</div>';
}

function renderFlow(steps){
  if(!steps||!steps.length)return nd;
  return '<div class="flow">'+steps.map((s,i)=>{
    const hl=/(AI|GPT|Agent|Olivia|Ava|LLM|watsonx|Joule|Skye|Copilot|inAIR|AICT|Gloat|Paradox|Eightfold|Claude|Gemini|NLP|ML\b|machine.?learn)/i.test(s);
    return(i>0?'<span class="flow-arr">\u2192</span>':'')+
      '<div class="flow-step'+(hl?' hl':'')+'" title="'+esc(s)+'">'+esc(s)+'</div>';
  }).join('')+'</div>';
}

function renderBA(u){
  const b=u.process_before,a=u.process_after,imp=u.impact_summary;
  if(b||a){
    return '<div class="flow-before-after">'+
      '<div class="flow-ba-box flow-ba-before"><div class="flow-ba-label">Before</div>'+(htm(b)||'Not disclosed')+'</div>'+
      '<div class="flow-ba-mid">\u2192</div>'+
      '<div class="flow-ba-box flow-ba-after"><div class="flow-ba-label">After</div>'+(htm(a)||'Not disclosed')+'</div>'+
      '</div>'+(imp?'<div style="margin-top:8px;font-size:.7rem;color:var(--text2);line-height:1.5">'+htm(imp)+'</div>':'');
  }
  if(imp)return '<div style="font-size:.7rem;color:var(--text2);line-height:1.5">'+htm(imp)+'</div>';
  return nd;
}

/* ---- Category View card ---- */

function card(u,idx){
  const c=ci(u.primary_category),cn=u.confidence||0;
  const tags=[];
  if(u.vendor&&u.vendor.length)u.vendor.forEach(v=>tags.push(v));
  if(u.industry&&u.industry.length)tags.push(u.industry[0]);
  if((u.region||[]).includes('kr'))tags.push('KR');

  let h='<div class="uc" onclick="tog('+idx+')" id="u'+idx+'">';
  // Row 1: dot + company + confidence
  h+='<div class="uc-row1">';
  h+='<div class="uc-dot" style="background:'+c.c+'"></div>';
  h+='<div class="uc-co">'+esc(typeof u.company==='string'?u.company:'')+'</div>';
  h+='<div class="uc-conf" style="color:'+cc(cn)+'">'+cn.toFixed(2)+'</div>';
  h+='</div>';
  // Row 2: Headline
  if(u.headline){
    h+='<div class="uc-hl">'+htm(u.headline)+'</div>';
  }
  // Row 3: Tags
  h+='<div class="uc-tags">'+tags.map(t=>'<span class="tg'+(t==='KR'?' kr':'')+'">'+esc(t)+'</span>').join('')
    +(u.ai_tech_type||[]).map(t=>'<span class="tg '+(TECH_CLASS[t]||'')+'">'+esc(TECH_LABEL[t]||t)+'</span>').join('')
    +'</div>';
  // Row 4: Impact summary (muted, truncated)
  if(u.impact_summary){
    h+='<div class="uc-imp">'+htm(u.impact_summary)+'</div>';
  }

  // Detail panel
  h+='<div class="det" id="d'+idx+'">';

  // 1. Pain Point
  if(u.problem){
    h+='<div class="tpl-sec"><div class="tpl-hd"><i>\ud83d\udccb</i> Pain Point</div><div class="tpl-bd">'+htm(u.problem)+'</div></div>';
  }

  // 2. Process Flow (full width)
  h+='<div class="flow-wrap"><div class="tpl-hd"><i>\ud83d\udd35</i> Process Flow</div>'+renderFlow(u.process_steps)+'</div>';

  // 3. System | Data | Model (3-col with specific keys)
  h+='<div class="three">';
  h+=renderInfoBlock('System','\ud83d\udfe2',u.system,SYS_KEYS);
  h+=renderInfoBlock('Data','\ud83d\udfe1',u.data,DAT_KEYS);
  h+=renderInfoBlock('Model','\ud83d\udfe3',u.model,MOD_KEYS);
  h+='</div>';

  // 3.5. Output (\uc2dc\uc2a4\ud15c\uc774 \uc0b0\ucd9c\ud558\ub294 \uac83)
  if(u.output){
    h+='<div class="tpl-sec"><div class="tpl-hd"><i>\ud83d\udce4</i> Output (\uc0b0\ucd9c\ubb3c)</div><div class="tpl-bd" style="font-size:.72rem;line-height:1.55">'+esc(u.output)+'</div></div>';
  }

  // 4. Impact Before→After
  h+='<div class="tpl-sec"><div class="tpl-hd"><i>\ud83d\udcca</i> Impact (Before \u2192 After)</div><div class="tpl-bd">'+renderBA(u)+'</div></div>';

  // 4.5. AI \uae30\uc220 \ubd84\ub958
  if((u.ai_tech_type||[]).length){
    const typeChips=(u.ai_tech_type||[]).map(t=>'<span class="tg '+(TECH_CLASS[t]||'')+'">'+esc(TECH_LABEL[t]||t)+'</span>').join(' ');
    const subBy={};
    (u.ai_tech_subtype||[]).forEach(s=>{const p=SUB_PARENT[s]||'';(subBy[p]=subBy[p]||[]).push(SUB_LABEL[s]||s)});
    let subText='';
    (u.ai_tech_type||[]).forEach(t=>{if(subBy[t])subText+='<div style="font-size:.68rem;color:var(--text2);margin-top:3px"><strong>'+esc(TECH_LABEL[t])+'</strong>: '+subBy[t].map(esc).join(' / ')+'</div>'});
    h+='<div class="tpl-sec"><div class="tpl-hd"><i>\ud83e\udde0</i> AI \uae30\uc220 \ubd84\ub958</div><div class="tpl-bd"><div style="display:flex;gap:4px;flex-wrap:wrap">'+typeChips+'</div>'+subText+'</div></div>';
  }

  // 5. Consulting
  if(u.consulting){h+='<div class="cbox">\ud83d\udca1 '+htm(u.consulting)+'</div>'}

  // All tags
  if(u.tags&&u.tags.length){h+='<div style="display:flex;gap:3px;flex-wrap:wrap;margin-top:10px">'+u.tags.map(t=>'<span class="tg">'+esc(t)+'</span>').join('')+'</div>'}

  h+='</div></div>';
  return h;
}

function tog(i){const d=document.getElementById('d'+i);if(d)d.classList.toggle('open')}

/* ---- Category View ---- */

function renCat(){
  let h='';C.forEach(cat=>{
    const cs=F.filter(u=>u.primary_category===cat.k).sort((a,b)=>b.confidence-a.confidence);
    if(!cs.length)return;
    h+='<div class="sec"><div class="sh" onclick="const g=this.nextElementSibling;g.style.display=g.style.display===\'none\'?\'\':\'none\';this.querySelector(\'.sv\').classList.toggle(\'open\')"><div class="sd" style="background:'+cat.c+'"></div><span class="sn">'+cat.k+'</span><span class="sc">'+cs.length+'</span><svg class="sv" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></div><div class="gr">';
    cs.forEach(u=>h+=card(u,D.indexOf(u)));
    h+='</div></div>';
  });
  document.getElementById('vcat').innerHTML=h;
}

/* ---- Company View — v6 rich ---- */

function renderCompanyRich(co,coInfo,cs){
  const cl=['#2563eb','#0d9488','#7c3aed','#ea580c','#16a34a','#4f46e5','#e11d48','#ca8a04','#0891b2','#7c3aed'];
  const ini=(co.replace(/[^A-Za-z\uAC00-\uD7A3]/g,'').charAt(0)||'?').toUpperCase();
  const catS=new Set(cs.map(u=>u.primary_category));
  const cIdx=Object.keys(COL).indexOf(co)%cl.length;
  const bgc=cl[Math.abs(cIdx)%cl.length];

  let h='<div class="cv">';
  // Header: avatar + name
  h+='<div class="cv-head"><div class="cv-a" style="background:'+bgc+'">'+ini+'</div><div style="flex:1"><div class="cv-n">'+esc(co)+'</div>';
  // Meta
  if(coInfo.industry||coInfo.size){
    h+='<div class="cv-meta">';
    if(coInfo.size)h+='<span>'+esc(''+coInfo.size)+' employees</span>';
    if(coInfo.industry)h+='<span>'+coInfo.industry.map(i=>esc(i)).join(', ')+'</span>';
    if(coInfo.region)h+='<span>'+coInfo.region.map(r=>esc(r)).join(', ')+'</span>';
    h+='</div>';
  }
  h+='</div></div>';

  // Description
  if(coInfo.description){
    h+='<div class="cv-desc">'+htm(coInfo.description)+'</div>';
  }

  // Strategy (skip Dataview TABLE queries, extract readable text before TABLE if mixed)
  if(coInfo.strategy){
    let strat=coInfo.strategy;
    const tIdx=strat.indexOf('TABLE WITHOUT ID');
    if(tIdx>0)strat=strat.substring(0,tIdx).trim();
    else if(tIdx===0)strat='';
    if(strat){
      h+='<div class="cv-strat"><div class="cv-strat-label">HR AI Strategy</div>'+htm(strat)+'</div>';
    }
  }

  // Category coverage bar
  h+='<div class="cv-b">';
  C.forEach(c=>{
    const has=catS.has(c.k);
    h+='<div class="cv-s" style="background:'+(has?c.c:'var(--bg3)')+'" title="'+c.k+(has?' \u2714':'')+'"></div>';
  });
  h+='</div>';

  // Use cases — full detail
  h+='<div class="cv-uc-sec">';
  cs.sort((a,b)=>b.confidence-a.confidence).forEach(u=>{
    const c2=ci(u.primary_category),cn=u.confidence||0;
    h+='<div class="cv-uc">';
    // Title + headline
    h+='<div class="cv-uc-head"><div class="uc-dot" style="background:'+c2.c+'"></div><div class="cv-uc-title">'+esc(u.title)+'</div><span class="uc-conf" style="color:'+cc(cn)+'">'+cn.toFixed(2)+'</span></div>';
    if(u.headline){h+='<div class="cv-uc-hl">'+htm(u.headline)+'</div>';}

    // Process flow
    if(u.process_steps&&u.process_steps.length){
      h+='<div class="flow-wrap" style="margin-top:8px">'+renderFlow(u.process_steps)+'</div>';
    }

    // System | Data | Model compact 3-col
    h+='<div class="three">';
    h+=renderInfoBlock('System','\ud83d\udfe2',u.system,SYS_KEYS);
    h+=renderInfoBlock('Data','\ud83d\udfe1',u.data,DAT_KEYS);
    h+=renderInfoBlock('Model','\ud83d\udfe3',u.model,MOD_KEYS);
    h+='</div>';

    // Impact Before→After
    if(u.process_before||u.process_after||u.impact_summary){
      h+='<div class="tpl-sec" style="margin-top:8px"><div class="tpl-hd"><i>\ud83d\udcca</i> Impact</div><div class="tpl-bd">'+renderBA(u)+'</div></div>';
    }

    h+='</div>';
  });
  h+='</div>';

  // Consulting Angle (from companies.json)
  if(coInfo.consulting){
    h+='<div class="cv-cons"><div class="cbox">\ud83d\udca1 <strong>Consulting Angle</strong><br>'+htm(coInfo.consulting)+'</div></div>';
  }

  h+='</div>';
  return h;
}

function renderCompanySimple(co,cs){
  const cl=['#2563eb','#0d9488','#7c3aed','#ea580c','#16a34a','#4f46e5','#e11d48','#ca8a04','#0891b2','#7c3aed'];
  const ini=(co.replace(/[^A-Za-z\uAC00-\uD7A3]/g,'').charAt(0)||'?').toUpperCase();
  const catS=new Set(cs.map(u=>u.primary_category));

  let h='<div class="cv cv-simple">';
  h+='<div class="cv-head"><div class="cv-a" style="background:#71717a">'+ini+'</div><div style="flex:1"><div class="cv-n">'+esc(co)+'</div>';
  h+='<div class="cv-b">';
  C.forEach(c=>{
    const has=catS.has(c.k);
    h+='<div class="cv-s" style="background:'+(has?c.c:'var(--bg3)')+'" title="'+c.k+(has?' \u2714':'')+'"></div>';
  });
  h+='</div></div><span style="font-size:.72rem;color:var(--text3)">'+cs.length+'</span></div>';
  h+='<div style="margin-top:8px">';
  cs.sort((a,b)=>b.confidence-a.confidence).forEach(u=>{
    const c2=ci(u.primary_category);
    h+='<div class="cv-r"><div class="sd" style="background:'+c2.c+';width:5px;height:5px"></div><span style="flex:1">'+esc(u.title)+'</span><span style="font-size:.68rem;font-weight:600;color:'+cc(u.confidence)+'">'+u.confidence.toFixed(2)+'</span></div>';
  });
  h+='</div></div>';
  return h;
}

function renCo(){
  const g={};F.forEach(u=>{const co=typeof u.company==='string'?u.company:'Unknown';if(!g[co])g[co]=[];g[co].push(u)});
  // Sort: companies with entries first (by use case count desc), then simple ones
  const withInfo=[];const withoutInfo=[];
  Object.entries(g).forEach(([co,cs])=>{
    // Try to find company info by name
    const info=findCompanyInfo(co);
    if(info)withInfo.push([co,cs,info]);
    else withoutInfo.push([co,cs]);
  });
  withInfo.sort((a,b)=>b[1].length-a[1].length);
  withoutInfo.sort((a,b)=>b[1].length-a[1].length);

  let h='';
  withInfo.forEach(([co,cs,info])=>{h+=renderCompanyRich(co,info,cs)});
  if(withoutInfo.length){
    h+='<div style="margin-top:16px;padding-top:12px;border-top:1px solid var(--border)"><div style="font-size:.72rem;color:var(--text3);margin-bottom:8px">Other companies</div>';
    withoutInfo.forEach(([co,cs])=>{h+=renderCompanySimple(co,cs)});
    h+='</div>';
  }
  document.getElementById('vco').innerHTML=h;
}

function findCompanyInfo(name){
  // Try exact slug match, then name match
  for(const c of CO){
    if(c.name===name)return c;
    if(c.slug===name.toLowerCase().replace(/\s+/g,'-'))return c;
    // Partial: company name contains the slug or vice versa
    if(name.toLowerCase().includes(c.slug.replace(/-/g,' ')))return c;
    if(c.name.toLowerCase().includes(name.toLowerCase()))return c;
  }
  return null;
}

/* ---- Matrix View ---- */

function renMx(){
  const co={};F.forEach(u=>{const c=typeof u.company==='string'?u.company:'Unknown';if(!co[c])co[c]={};if(!co[c][u.primary_category]||u.confidence>co[c][u.primary_category].confidence)co[c][u.primary_category]=u});
  const s=Object.keys(co).sort();
  let h='<div class="mx-w"><table class="mx"><thead><tr><th>Company</th>';
  C.forEach(c=>h+='<th style="color:'+c.c+'">'+c.s+'</th>');
  h+='</tr></thead><tbody>';
  s.forEach(c=>{
    h+='<tr><td>'+esc(c)+'</td>';
    C.forEach(cat=>{
      const u=co[c][cat.k];
      if(u){
        const v=u.confidence;
        const bg=v>=.5?'rgba(22,163,74,.1)':v>=.3?'rgba(202,138,4,.1)':'rgba(220,38,38,.1)';
        const fg=v>=.5?'var(--green)':v>=.3?'var(--yellow)':'var(--red)';
        h+='<td><span class="mp" style="background:'+bg+';color:'+fg+'">'+v.toFixed(2)+'</span></td>';
      }else h+='<td></td>';
    });
    h+='</tr>';
  });
  h+='</tbody></table></div>';
  document.getElementById('vmx').innerHTML=h;
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

BODY = f"""
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
    <select class="fs" id="fT" onchange="af()"><option value="">AI 기술</option><option value="generative">생성형</option><option value="predictive">판별·예측</option><option value="recognition">인식</option><option value="decision-optimization">의사결정·최적화</option><option value="automation">자동화</option></select>
    <select class="fs" id="fC" onchange="af()"><option value="0">Confidence</option><option value="0.5">&ge;0.50</option><option value="0.4">&ge;0.40</option><option value="0.3">&ge;0.30</option></select>
    <span class="fx" id="cA" style="display:none" onclick="cF()">Clear</span>
    <span class="fc" id="fn"></span>
  </div>
  <div id="vcat"></div>
  <div id="vco" style="display:none"></div>
  <div id="vmx" style="display:none"></div>
</main>
<footer><div class="w">HR AI Benchmark &middot; {uc_count} Use Cases &middot; {co_count} Companies &middot; {today}</div></footer>
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
const D={uc_js};
const CO={co_js};
{JS}
</script>
</body>
</html>"""

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"v6 Done: {os.path.getsize(OUT_PATH)/1024:.0f}KB - {uc_count} use cases, {co_count} companies")
