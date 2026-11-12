"""Local showcase server (`curriculum serve`): serves the static site and adds a live "build your own"
form. A POST runs the full pipeline in a background thread, streaming stage progress to the page, then
redirects to the generated curriculum. Uses the models/keys in `.env` exactly like the CLI.

Stdlib only; no framework. This is a local demo tool, not a public service.
"""

from __future__ import annotations

import json
import re
import threading
import time
import traceback
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from . import html as site
from .models import Persona, UserContext

RUNS = Path("runs")
TEST_SET = Path("test_set")
CHATS: dict[str, dict] = {}
_LOCK = threading.Lock()

CT = {".html": "text/html; charset=utf-8", ".json": "application/json", ".md": "text/markdown; charset=utf-8",
      ".css": "text/css", ".js": "text/javascript"}


def _slug(goal: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", goal.lower()).strip("_")[:40] or "custom"
    return f"custom_{s}_{int(time.time()) % 100000}"


def _persona_from_testset(persona_id: str) -> Persona | None:
    """Load one of the 8 curated test-case personas by id. Its persona_id matches a saved fixture, so the
    agent loop runs over cached candidates/assessments — fast and free, ideal for 'curate for yourself'."""
    fp = TEST_SET / f"{persona_id}.json"
    if not (persona_id and persona_id.replace("_", "").isalnum() and fp.is_file()):
        return None
    d = json.loads(fp.read_text())
    return Persona(persona_id=d["persona_id"], goal=d["goal"], time_budget_minutes=d["time_budget_minutes"],
                   user_context=UserContext(**d["user_context"]))


def _persona_from_form(f: dict[str, list[str]]) -> Persona:
    def first(k: str) -> str:
        return (f.get(k, [""])[0] or "").strip()

    def items(k: str) -> list[str]:
        return [p.strip() for p in first(k).replace("\n", ",").split(",") if p.strip()]

    seeded = _persona_from_testset(first("persona_id"))
    if seeded:  # a test case chosen from the home page ("open" / "curate for yourself")
        return seeded
    goal = first("goal")
    if not goal:
        raise ValueError("a learning goal is required")
    budget = max(10, min(6000, int(first("budget") or "360")))
    return Persona(persona_id=_slug(goal), goal=goal, time_budget_minutes=budget,
                   user_context=UserContext(background=first("background"), known=items("known"),
                                            unknown=items("unknown"), constraints=first("constraints")))


def _do_chat(job_id: str, persona: Persona) -> None:
    """Build the curriculum with the agent loop, streaming each tool call into the chat's event list."""
    from .agent_loop import run_agent_loop
    try:
        out = RUNS / f"{persona.persona_id}__agent_loop"
        run_agent_loop(persona, out_dir=out, on_event=lambda e: CHATS[job_id]["events"].append(e))
        site.write_all(RUNS)  # so the result page is linkable and the comparison refreshes
    except Exception as ex:
        traceback.print_exc()
        CHATS[job_id]["events"].append({"kind": "error", "text": f"{type(ex).__name__}: {str(ex)[:300]}"})
    finally:
        CHATS[job_id]["building"] = False


def _do_followup(job_id: str, question: str) -> None:
    """Continue the saved conversation with a follow-up: the agent answers (and may revise the curriculum)."""
    from .agent_loop import continue_loop
    job = CHATS[job_id]
    try:
        _, changed, _ = continue_loop(Path(job["run_dir"]), question, on_event=lambda e: job["events"].append(e))
        if changed:
            site.write_all(RUNS)
    except Exception as ex:
        traceback.print_exc()
        job["events"].append({"kind": "answer", "text": f"(sorry — error: {type(ex).__name__})", "changed": False})
    finally:
        job["building"] = False


CHAT_CSS = """
main:has(.agent-shell){max-width:1180px}
.agent-shell{display:flex;gap:16px;align-items:stretch;margin-top:14px}
.agent-left{flex:1 1 440px;min-width:0;display:flex;flex-direction:column}
.agent-right{flex:1 1 460px;min-width:0;display:flex;flex-direction:column}
@media(max-width:900px){.agent-shell{flex-direction:column}.agent-right{order:-1}}
.chatpanel{background:var(--card);border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);display:flex;flex-direction:column;overflow:hidden;flex:1}
.chatbox{display:flex;flex-direction:column;gap:14px;padding:20px;min-height:52vh;max-height:66vh;overflow-y:auto}
/* right-hand curriculum artifact */
.artpanel{background:var(--card);border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);display:flex;flex-direction:column;overflow:hidden;flex:1;min-height:52vh;max-height:calc(66vh + 86px)}
.arthead{display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid var(--line);background:var(--card)}
.arthead .t{font-weight:600;font-size:14px;display:flex;align-items:center;gap:7px}
.arthead .sp{flex:1}
.arthead select{font:inherit;font-size:13px;padding:5px 9px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--ink);max-width:170px}
.arthead a.open{font-size:13px;font-weight:600;color:var(--accent)}
.artbody{padding:16px;overflow-y:auto;flex:1}
.art-empty{margin:auto;text-align:center;color:var(--muted);max-width:280px;padding:40px 16px;font-size:14px;line-height:1.5}
.art-empty .ico{font-size:28px;opacity:.5;display:block;margin-bottom:8px}
.art-meta{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}
.art-meta span{font-size:12px;background:var(--chip);color:var(--muted);border-radius:999px;padding:3px 10px}
.art-interp{font-size:13.5px;line-height:1.5;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:11px 13px;margin-bottom:14px}
.art-infeas{border-color:var(--warn-line,#e0b84d)}
.pick{border:1px solid var(--line);border-radius:12px;padding:12px 13px;margin-bottom:10px;background:var(--bg)}
.pick .ph{display:flex;gap:9px;align-items:baseline}
.pick .rk{flex:none;width:22px;height:22px;border-radius:6px;background:var(--accent-soft);color:var(--accent);font-size:12px;font-weight:700;display:grid;place-items:center}
.pick .pt{font-weight:600;font-size:14px;line-height:1.35}
.pick .pm{font-size:12px;color:var(--muted);margin:3px 0 0 31px}
.pick .pr{font-size:13px;line-height:1.5;color:var(--ink);margin:8px 0 0 31px}
.pick .pc{margin:8px 0 0 31px;display:flex;flex-wrap:wrap;gap:5px}
.pick .pc span{font-size:11px;background:var(--chip);color:var(--muted);border-radius:999px;padding:2px 8px}
.art-h{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);margin:16px 0 8px}
.art-warn{font-size:13px;line-height:1.5;color:var(--ink);background:#fff7e6;border:1px solid #f0d79a;border-radius:10px;padding:10px 12px;margin-bottom:8px}
@media (prefers-color-scheme:dark){:root:not([data-theme='light']) .art-warn{background:#2a2410;border-color:#5a4a1a}}
:root[data-theme='dark'] .art-warn{background:#2a2410;border-color:#5a4a1a}
.art-drop{font-size:12.5px;color:var(--muted);line-height:1.5;margin-bottom:6px}
.art-drop b{color:var(--ink);font-weight:600}
.art-flash{animation:artflash .9s ease}
@keyframes artflash{0%{background:var(--accent-soft)}100%{background:transparent}}
.chatbox-min{min-height:46vh;max-height:62vh}
.empty{margin:auto;text-align:center;color:var(--muted);max-width:420px;padding:20px}
.empty .spark{font-size:30px}.empty h3{margin:10px 0 4px;color:var(--ink);font-size:18px;font-weight:600}
.empty p{font-size:14px;line-height:1.5;margin:0 0 16px}
.examples{display:flex;flex-direction:column;gap:8px}
.ex{text-align:left;background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:10px 13px;font:inherit;font-size:14px;color:var(--ink);cursor:pointer;transition:border-color .12s}
.ex:hover{border-color:var(--accent)}
/* message thread: one full-width column per turn, no avatars (mirrors mcp-agent-ui) */
.chatbox{--teal:#137680}
@media (prefers-color-scheme:dark){:root:not([data-theme='light']) .chatbox{--teal:#61ccd8}}
:root[data-theme='dark'] .chatbox{--teal:#61ccd8}
.turn{display:flex;flex-direction:column;gap:9px;max-width:100%}
.u-msg{align-self:flex-end;max-width:85%;background:var(--chip);color:var(--ink);border-radius:14px;padding:9px 14px;font-size:14.5px;line-height:1.5;white-space:pre-wrap;word-break:break-word}
.a-text{font-size:14.5px;line-height:1.6;color:var(--ink);white-space:pre-wrap;word-break:break-word}
.a-status{font-size:13px;display:inline-flex;align-items:center;gap:6px}
.shimmer{background:linear-gradient(90deg,var(--muted) 30%,var(--ink) 50%,var(--muted) 70%);background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:sh 1.5s linear infinite}
@keyframes sh{to{background-position:-200% 0}}
/* tool invocation row (collapsible, teal) */
.tool{border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--bg)}
.tool-head{display:flex;align-items:center;gap:8px;width:100%;padding:8px 11px;background:none;border:0;font:inherit;font-size:12.5px;color:var(--teal);cursor:pointer;text-align:left}
.tool-head .ti{flex:none;font-size:13px}
.tool-head .tl{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:500}
.tool-head .tc{flex:none;color:var(--muted);font-size:11px;transition:transform .15s}
.tool[data-open='1'] .tool-head .tc{transform:rotate(180deg)}
.tool-body{display:none;border-top:1px solid var(--line);padding:10px 11px;font-size:12px;color:var(--ink)}
.tool[data-open='1'] .tool-body{display:block}
.tool-sec{margin-bottom:9px}.tool-sec:last-child{margin-bottom:0}
.tool-sec b{display:block;text-transform:uppercase;letter-spacing:.04em;font-size:10px;color:var(--muted);margin-bottom:4px;font-weight:700}
.tool-sec pre{margin:0;background:var(--chip);border-radius:7px;padding:7px 9px;font-size:11.5px;overflow-x:auto;white-space:pre-wrap;word-break:break-word}
.tool.err .tool-head{color:var(--bad)}
/* reasoning block (if the model streams it) */
.reason{font-size:12.5px}
.reason-h{color:var(--muted);cursor:pointer;display:inline-flex;gap:5px;align-items:center;font-weight:500}
.reason-b{display:none;border-left:2px solid var(--line);padding-left:11px;margin-top:6px;color:var(--muted);line-height:1.55;white-space:pre-wrap}
.reason[data-open='1'] .reason-b{display:block}
/* compact completion summary */
.donecard{font-size:12.5px;color:var(--muted);display:flex;flex-wrap:wrap;gap:8px;align-items:center;border-top:1px dashed var(--line);padding-top:10px}
.donecard b{color:var(--ink);font-weight:600}
.composer{border-top:1px solid var(--line);padding:12px;background:var(--card)}
.inbar{display:flex;align-items:flex-end;gap:8px;background:var(--bg);border:1px solid var(--line);border-radius:14px;padding:6px 6px 6px 14px;transition:border-color .12s}
.inbar:focus-within{border-color:var(--accent)}
.inbar textarea{flex:1;border:0;background:none;color:var(--ink);font:inherit;font-size:15px;resize:none;outline:none;padding:7px 0;max-height:160px;line-height:1.45}
.inbar button{flex:none;width:36px;height:36px;border-radius:50%;border:0;background:var(--accent);color:#fff;font-size:17px;cursor:pointer;display:grid;place-items:center}
.inbar button:disabled{opacity:.4;cursor:default}
.profile{margin-top:10px;font-size:13px}.profile summary{cursor:pointer;color:var(--muted);list-style:none;display:inline-flex;align-items:center;gap:6px}
.profile summary::before{content:'⚙';opacity:.7}
.profile .row{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}.profile label{flex:1;min-width:150px;display:grid;gap:4px;color:var(--muted)}
.profile input{font:inherit;padding:8px 11px;border:1px solid var(--line);border-radius:9px;background:var(--bg);color:var(--ink)}
.chatnote{text-align:center;font-size:12px;color:var(--muted);margin-top:10px}
"""

CHAT_JS = """
const chat=document.getElementById('chat'),form=document.getElementById('cf'),goalI=document.getElementById('goal'),sendB=document.getElementById('send');
const verSel=document.getElementById('ver'),artBody=document.getElementById('artifact'),openFull=document.getElementById('openfull');
let jobId=null,lastIdx=0,curUrl='#';
let versions=[],curTurn=null,curText=null;  // one assistant turn = one full-width column (no avatars)
function esc(s){return (s||'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
function scroll(){chat.scrollTop=chat.scrollHeight;}
function clearEmpty(){const e=chat.querySelector('.empty');if(e)e.remove();}
function endTurn(){curTurn=null;curText=null;}
function ensureTurn(){if(!curTurn){curTurn=document.createElement('div');curTurn.className='turn';chat.appendChild(curTurn);}return curTurn;}
function clearStatus(){const s=ensureTurn().querySelector('.a-status');if(s)s.remove();}
function userMsg(text){endTurn();const d=document.createElement('div');d.className='turn';d.innerHTML=`<div class='u-msg'>${esc(text)}</div>`;chat.appendChild(d);endTurn();scroll();}
function statusLine(text){ensureTurn();let s=curTurn.querySelector('.a-status');if(!s){s=document.createElement('div');s.className='a-status';curTurn.appendChild(s);}s.innerHTML=`<span class='shimmer'>${esc(text)}</span>`;scroll();}
function textDelta(t){ensureTurn();clearStatus();if(!curText){curText=document.createElement('div');curText.className='a-text';curTurn.appendChild(curText);}curText.textContent+=t;scroll();}
// a tool invocation renders as a collapsed teal row that expands to params + result
function toolRow(icon,label,params,result,err){ensureTurn();clearStatus();curText=null;
  const t=document.createElement('div');t.className='tool'+(err?' err':'');t.dataset.open='0';
  const body=(params?`<div class='tool-sec'><b>Parameters</b><pre>${esc(params)}</pre></div>`:'')
            +(result?`<div class='tool-sec'><b>${err?'Issue':'Result'}</b><div>${esc(result)}</div></div>`:'');
  t.innerHTML=`<button class='tool-head' type='button'><span class='ti'>${icon}</span><span class='tl'>${esc(label)}</span><span class='tc'>${body?'⌄':''}</span></button>`
    +(body?`<div class='tool-body'>${body}</div>`:'');
  curTurn.appendChild(t);scroll();}
chat.addEventListener('click',ev=>{const h=ev.target.closest('.tool-head');if(h){const t=h.parentElement;t.dataset.open=t.dataset.open==='1'?'0':'1';return;}
  const rh=ev.target.closest('.reason-h');if(rh){const r=rh.parentElement;r.dataset.open=r.dataset.open==='1'?'0':'1';}});
// ---- right-hand artifact (the curriculum, versioned) ----
function fmtMin(m){return (Math.round(m*10)/10).toString().replace(/\\.0$/,'');}
function renderArtifact(d){
  const picks=d.picks||[],subs=d.sub_topics||[],warns=d.warnings||[],drops=d.dropped||[];
  const sub=id=>{const s=subs.find(x=>x.id===id);return s?s.title:id;};
  let h=`<div class='art-meta'><span>${picks.length} video${picks.length===1?'':'s'}</span>`
    +`<span>${fmtMin(d.total_minutes)}/${d.budget_minutes} min</span>`
    +(d.feasible?'':`<span style='color:#c0392b'>flagged not fully feasible</span>`)+`</div>`;
  if(d.interpretation)h+=`<div class='art-interp${d.feasible?'':' art-infeas'}'>${esc(d.interpretation)}`
    +(d.feasible?'':' '+esc(d.feasibility_note||''))+`</div>`;
  picks.forEach(p=>{
    const rng=(p.watch_from||p.watch_until)?` · watch ${esc(p.watch_from||'0:00')}–${esc(p.watch_until||'end')}`:'';
    h+=`<div class='pick'><div class='ph'><div class='rk'>${p.rank}</div><div class='pt'>`
      +`<a href='${esc(p.url)}' target='_blank'>${esc(p.title)}</a></div></div>`
      +`<div class='pm'>${esc(p.channel)} · ${fmtMin(p.minutes_counted)} min${rng}</div>`
      +`<div class='pr'>${esc(p.reason)}</div>`
      +`<div class='pc'>`+(p.covers||[]).map(c=>`<span>${esc(sub(c))}</span>`).join('')
      +`<span>confidence ${Math.round((p.confidence||0)*100)}%</span></div></div>`;
  });
  if(warns.length){h+=`<div class='art-h'>Honest caveats</div>`+warns.map(w=>`<div class='art-warn'>${esc(w)}</div>`).join('');}
  if(drops.length){h+=`<div class='art-h'>Read but dropped</div>`+drops.map(x=>`<div class='art-drop'><b>${esc(x.title||x.video_id)}</b> — ${esc(x.reason)}</div>`).join('');}
  artBody.innerHTML=h;artBody.classList.remove('art-flash');void artBody.offsetWidth;artBody.classList.add('art-flash');
}
function pushVersion(d){
  versions.push(d);const i=versions.length-1;
  const o=document.createElement('option');o.value=i;o.textContent=i===0?'v1 · first build':('v'+(i+1)+' · revised');
  verSel.appendChild(o);verSel.style.display=versions.length>1?'':'none';verSel.value=i;
  openFull.style.display='';renderArtifact(d);
}
verSel.addEventListener('change',()=>renderArtifact(versions[+verSel.value]));
// ---- chat event stream: each event is a part stacked inside the current assistant turn ----
function render(e){
  switch(e.kind){
    case 'token': textDelta(e.text); break;
    case 'status': statusLine(e.text); break;
    case 'search': toolRow('🔍','Searched: "'+e.query+'"','query: '+e.query,(e.n||0)+' matching video(s) in the candidate pool'); break;
    case 'read': toolRow('📖','Read: '+e.title,'video_id: '+(e.video_id||''),'Read the transcript'+(e.level?' · level: '+e.level:'')); break;
    case 'submit': toolRow('📝','Assembled the curriculum','',(e.n_picks||0)+' pick(s) submitted for verification'); break;
    case 'retry': toolRow('⚠️','Fixed a validation issue','',(e.errors||[]).join('; '),true); break;
    case 'curriculum': pushVersion(e.data); break;
    case 'answer_done':
      if(curText){ if(e.changed) curText.innerHTML=esc(curText.textContent)+" <span style='color:var(--ok)'>· updated the curriculum ↗</span>"; }
      else if(e.text){ ensureTurn();clearStatus();const d=document.createElement('div');d.className='a-text';
        d.innerHTML=esc(e.text)+(e.changed?" <span style='color:var(--ok)'>· updated the curriculum ↗</span>":'');curTurn.appendChild(d); }
      endTurn(); break;
    case 'done':{ ensureTurn();clearStatus();curText=null;
      const c=document.createElement('div');c.className='donecard';
      c.innerHTML=`✓ <b>Curriculum ready</b> · ${e.n_videos} videos · ${e.minutes}/${e.budget} min · ${e.read} read · ${e.turns} turns · $${e.cost}`;
      curTurn.appendChild(c);
      const h=document.createElement('div');h.className='a-text';h.style.cssText='color:var(--muted);font-size:13px';
      h.textContent='It\\u2019s on the right ↗ — ask me why I chose something, or tell me to change it.';curTurn.appendChild(h);
      endTurn(); break; }
    case 'error':{ ensureTurn();clearStatus();const d=document.createElement('div');d.className='a-text';d.textContent='⚠️ '+e.text;curTurn.appendChild(d);endTurn(); break; }
  }
  scroll();
}
async function poll(){
  try{const r=await fetch('/chat-status/'+jobId);const j=await r.json();
    if(j.url)curUrl=j.url;openFull.href=curUrl;const evs=j.events||[];
    for(;lastIdx<evs.length;lastIdx++)render(evs[lastIdx]);
    if(j.building){setTimeout(poll,300);}
    else{endTurn();sendB.disabled=false;goalI.disabled=false;goalI.placeholder='Ask a follow-up, or ask for a change…';goalI.focus();}
  }catch(err){setTimeout(poll,500);}
}
function grow(){goalI.style.height='auto';goalI.style.height=Math.min(goalI.scrollHeight,160)+'px';}
goalI.addEventListener('input',grow);
goalI.addEventListener('keydown',ev=>{if(ev.key==='Enter'&&!ev.shiftKey){ev.preventDefault();form.requestSubmit();}});
document.querySelectorAll('.ex').forEach(b=>b.addEventListener('click',()=>{goalI.value=b.textContent;grow();goalI.focus();}));
// start a live build from a goal (composer or builder form)
async function startBuild(body,label){
  clearEmpty();userMsg(label);sendB.disabled=true;goalI.disabled=true;statusLine('Starting…');
  const pf=document.querySelector('.profile');if(pf)pf.open=false;
  const r=await fetch('/chat',{method:'POST',body});const j=await r.json();
  if(j.error){render({kind:'error',text:j.error});sendB.disabled=false;goalI.disabled=false;return;}
  jobId=j.job_id;poll();
}
form.addEventListener('submit',async ev=>{
  ev.preventDefault();const q=goalI.value.trim();if(!q||sendB.disabled)return;
  goalI.value='';grow();
  if(!jobId){
    const body=new URLSearchParams({goal:q,budget:(document.getElementById('budget').value||'60'),background:document.getElementById('background').value,known:document.getElementById('known').value,unknown:document.getElementById('unknown').value,constraints:document.getElementById('constraints').value});
    startBuild(body,q);
  }else{
    clearEmpty();userMsg(q);sendB.disabled=true;goalI.disabled=true;
    const r=await fetch('/chat-followup',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({job_id:jobId,question:q})});
    const j=await r.json();if(j.error){render({kind:'error',text:j.error});sendB.disabled=false;goalI.disabled=false;return;}
    poll();
  }
});
// auto-start the live build when opened from the builder form (?goal=...) or with a seeded
// test case (?persona_id=... — its saved fixture makes the pool cached, so the build is fast)
(function(){const p=new URLSearchParams(location.search);
  if(p.get('goal')||p.get('persona_id')){const body=new URLSearchParams();['persona_id','goal','budget','background','known','unknown','constraints'].forEach(k=>p.get(k)&&body.set(k,p.get(k)));startBuild(body,p.get('goal')||p.get('persona_id').replaceAll('_',' '));}
})();
"""

_EXAMPLES = ["Learn SQL window functions to rewrite my self-joins",
             "Build a small React habit tracker this weekend",
             "Understand Rust ownership and the borrow checker"]


def _chat_page() -> str:
    examples = "".join(f"<button class='ex' type='button'>{site.e(x)}</button>" for x in _EXAMPLES)
    empty = (f"<div class='empty'><div class='spark'>✦</div><h3>What do you want to learn?</h3>"
             f"<p>I'll search YouTube, read the transcripts, and build you an ordered curriculum — "
             f"then you can ask me why, or tell me to change it.</p><div class='examples'>{examples}</div></div>")
    art_empty = ("<div class='art-empty'><span class='ico'>📚</span>The curriculum will appear here as the agent "
                 "builds it — then every change you ask for adds a new version you can switch between.</div>")
    left = (
        "<div class='agent-left'>"
        "<div class='crumb'><a href='/'>Home</a> · agent</div>"
        "<h1 style='margin-bottom:4px'>Curriculum agent</h1>"
        "<div class='muted' style='font-size:14px;margin-bottom:4px'>Builds and defends a learning curriculum, grounded in what the videos actually teach.</div>"
        "<div class='chatpanel'>"
        f"<div id='chat' class='chatbox'>{empty}</div>"
        "<form id='cf' class='composer'>"
        "<div class='inbar'><textarea id='goal' rows='1' placeholder='Message the agent…'></textarea>"
        "<button id='send' type='submit' aria-label='Send'>↑</button></div>"
        "<details class='profile'><summary>About you (optional)</summary>"
        "<div class='row'><label>Time budget (min)<input id='budget' type='number' value='60' min='10' max='3000'></label>"
        "<label>Background<input id='background' placeholder='Data analyst, 3 years SQL'></label></div>"
        "<div class='row'><label>Already know<input id='known' placeholder='select, joins, group by'></label>"
        "<label>Want to learn<input id='unknown' placeholder='window functions, PARTITION BY'></label></div>"
        "<label>Constraints<input id='constraints' placeholder='Just a lunch break; practical examples'></label></details>"
        "</form></div>"
        "<div class='chatnote'>Runs the agent loop live with the models in <code>.env</code>. Test cases are instant; a brand-new goal takes 1–2 min.</div>"
        "</div>")
    right = (
        "<div class='agent-right'>"
        "<div class='artpanel'>"
        "<div class='arthead'><span class='t'>📄 Curriculum</span>"
        "<select id='ver' style='display:none'></select><span class='sp'></span>"
        "<a id='openfull' class='open' href='#' target='_blank' style='display:none'>Open full ↗</a></div>"
        f"<div id='artifact' class='artbody'>{art_empty}</div>"
        "</div></div>")
    body = ("<div class='agent-shell'>" + left + right + "</div>"
            + "<style>" + CHAT_CSS + "</style><script>" + CHAT_JS + "</script>")
    return site._page("Agent", body, active="chat")


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        pass

    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = urllib.parse.urlparse(self.path).path
        if path == "/chat":
            return self._send(200, _chat_page().encode(), CT[".html"])
        if path.startswith("/chat-status/"):
            job = CHATS.get(path[len("/chat-status/"):], {"error": "unknown job"})
            return self._send(200, json.dumps(job).encode(), CT[".json"])
        rel = "index.html" if path in ("", "/") else path.lstrip("/")
        target = (RUNS / rel).resolve()
        if RUNS.resolve() not in target.parents and target != RUNS.resolve() or not target.is_file():
            return self._send(404, b"not found", "text/plain")
        self._send(200, target.read_bytes(), CT.get(target.suffix, "application/octet-stream"))

    def do_POST(self) -> None:
        p = urllib.parse.urlparse(self.path).path
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode()
        if p == "/chat":
            try:
                persona = _persona_from_form(urllib.parse.parse_qs(body))
            except Exception as ex:
                return self._send(400, json.dumps({"error": str(ex)}).encode(), CT[".json"])
            job_id = f"chat_{int(time.time() * 1000) % 10_000_000}"
            CHATS[job_id] = {"events": [], "building": True, "error": None, "goal": persona.goal,
                             "run_dir": str(RUNS / f"{persona.persona_id}__agent_loop"),
                             "url": f"/{persona.persona_id}__agent_loop/curriculum.html"}
            threading.Thread(target=_do_chat, args=(job_id, persona), daemon=True).start()
            return self._send(200, json.dumps({"job_id": job_id}).encode(), CT[".json"])
        if p == "/chat-followup":
            try:
                data = json.loads(body)
                job = CHATS[data["job_id"]]
            except Exception:
                return self._send(400, json.dumps({"error": "unknown chat"}).encode(), CT[".json"])
            q = (data.get("question") or "").strip()
            if not q or job.get("building"):
                return self._send(400, json.dumps({"error": "empty or still building"}).encode(), CT[".json"])
            job["building"] = True  # the user bubble is rendered client-side; server streams the agent's reply
            threading.Thread(target=_do_followup, args=(data["job_id"], q), daemon=True).start()
            return self._send(200, json.dumps({"ok": True}).encode(), CT[".json"])
        return self._send(404, b"not found", "text/plain")


def serve(port: int = 8000) -> None:
    site.write_all(RUNS)  # make sure the static pages are current before serving
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"Curriculum showcase on http://localhost:{port}/  (Ctrl+C to stop)")
    print("The live agent runs with the models in .env "
          "(set OPENROUTER_API_KEY / *_MODEL there; transcripts need an open network or SUPADATA_API_KEY / GEMINI_MAX_USD).")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
