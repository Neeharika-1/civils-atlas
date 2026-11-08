/* Daily home is embedded, works offline, and never promotes feed items to researched notes. */
(()=>{
const registry=DATA.registry||[],logs=new Map((DATA.logs||[]).map(x=>[x.source_id||x.source,x])),coverage=new Map((DATA.source_coverage?.sources||[]).map(x=>[x.source_id,x]));
const compilations=DATA.compilation_registry||[],allRegistry=[...registry,...compilations],compilationHealth=DATA.compilation_health||{};
const today=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Kolkata',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
let readIds=new Set(),checked=new Set();
try{readIds=new Set(JSON.parse(localStorage.getItem('atlas-read-links')||'[]'));checked=new Set(JSON.parse(localStorage.getItem('atlas-source-check-'+today)||'[]'));}catch(e){}
const safe=u=>{try{const x=new URL(u);return ['https:','http:'].includes(x.protocol)&&!x.username&&!x.password?x.href:'#';}catch(e){return '#';}};
const time=s=>s&&Number.isFinite(Date.parse(s))?new Date(s).toLocaleString('en-IN',{timeZone:'Asia/Kolkata',dateStyle:'medium',timeStyle:'short'})+' IST':'Not recorded';
const persist=(k,v)=>{try{localStorage.setItem(k,JSON.stringify([...v]));}catch(e){}};
const ok=(DATA.logs||[]).filter(x=>x.status==='ok').length,required=registry.length,unresolved=required-ok;
const hosted=AUTO.last_run_environment==='github-actions';
$('#automationLabel').textContent=AUTO.last_observed_scheduled_run?'scheduled run observed':hosted?'installed · scheduled run awaiting verification':'local preview · hosted run not verified';
$('#homeStatus').innerHTML=`<div class="daily-metrics"><div><strong>${N.length.toLocaleString()}</strong><span>researched archive notes</span></div><div><strong>${DATA.inbox.length.toLocaleString()}</strong><span>discovered links · not notes</span></div><div><strong>${ok}/${required}</strong><span>primary streams returned links</span></div><div><strong>${unresolved}</strong><span>streams need attention</span></div></div><p class="small">Latest sweep: <b>${esc(time(AUTO.last_run))}</b> · ${hosted?'GitHub Actions':'local test, not hosted proof'} · schedule: 6:30 a.m. IST (may be delayed).</p>${AUTO.last_run&&Date.now()-Date.parse(AUTO.last_run)>36*3600000?'<div class="notice">This snapshot is over 36 hours old. Check the Actions run; refreshing this page alone does not collect new articles.</div>':''}<p class="small">${AUTO.last_observed_scheduled_run?'Last scheduled execution: '+esc(time(AUTO.last_observed_scheduled_run)):'First scheduled execution has not yet been observed.'} A successful pipeline does not mean every source was read.</p>`;
$('#compilationSummary').textContent=(compilationHealth.working||0)+'/'+compilations.length+' compilation streams returned links. Checked: '+time(compilationHealth.updated_at)+'. These are secondary reading sources; primary-source access gaps remain separately visible.';
$('#compilationCards').innerHTML=compilations.map(r=>{const l=(compilationHealth.results||[]).find(x=>x.source_id===r.id)||{};return `<article class="tile"><span class="source-state ${l.status==='ok'?'ready':'attention'}">${l.status==='ok'?(l.discovered||0)+' links collected':'Access needs checking'}</span><h3>${esc(r.name)}</h3><p class="small">${esc(r.coverage_note||'Secondary compilation; check article and edition dates.')}</p><a class="action" href="${esc(safe(r.url))}" target="_blank" rel="noopener noreferrer">Open compilation source ↗</a><p><button class="action" data-compilation-filter="${esc(r.id)}">Show collected links →</button></p></article>`;}).join('');
const batches=DATA.research_updates||[],recent=batches.flatMap(b=>b.note_ids||[]).map(id=>N.find(n=>n.id===id)).filter(Boolean);
$('#researchSummary').textContent=recent.length+' notes researched in-session by the assistant; not automatically written by the daily collector. Earlier event dates remain backfills, not new November events.';
$('#recentResearch').innerHTML=recent.map(n=>`<div class="tile"><span class="eyebrow">${esc(n.date)} · ${esc(n.priority)}${n.ap?' · AP-linked':''}</span><h3>${esc(n.title)}</h3><button class="action" data-note="${esc(n.id)}">Read researched note →</button></div>`).join('')||'<p>No editorial research update in this snapshot.</p>';
$('#researchQuiz').innerHTML=(DATA.research_practice||[]).map(q=>`<article class="tile"><h3>${esc(q.id)}. ${esc(q.question)}</h3><ol type="A">${q.options.map(o=>`<li>${esc(o)}</li>`).join('')}</ol><details><summary>Answer &amp; explanation</summary><p><b>${String.fromCharCode(65+q.answer)}.</b> ${esc(q.explanation)}</p><button class="action" data-note="${esc(q.ref)}">Study reference →</button></details></article>`).join('');
const intake=DATA.document_intake||{};
$('#documentSummary').textContent=(intake.extracted||0)+'/'+(intake.attempted||0)+' AP Finance PDFs extracted in the latest intake · '+(intake.pending||0)+' pending. Machine extraction/OCR is not human verification. Date candidates are not certified legal commencement. '+(intake.updated_at?'Checked: '+time(intake.updated_at):'No intake run recorded.');
$('#documentIntake').innerHTML=(intake.documents||[]).map(d=>`<article class="tile"><span class="source-state ${d.status==='machine_text_extracted'?'ready':'attention'}">${esc(d.status.replaceAll('_',' '))}</span><h3>${esc(decodeURIComponent(new URL(safe(d.url)).pathname.split('/').at(-1)).replaceAll('_',' '))}</h3><p class="small">${d.pages||'?'} pages · ${d.pages_with_text||0} with text · OCR pages: ${esc((d.ocr_pages||[]).join(', ')||'none')}${d.document_date_candidate?' · Candidate document date: '+esc(d.document_date_candidate):''}</p>${d.cited_version_changed?'<div class="notice">Document differs from the version cited in the researched note. Recheck before relying on it.</div>':''}<p class="small">${esc(d.error||d.reading_limit||'Review required')}</p><a class="action" href="${esc(safe(d.url))}" target="_blank" rel="noopener noreferrer">Open original PDF ↗</a></article>`).join('');
$('#dailySource').innerHTML='<option value="all">Every source</option>'+allRegistry.map(r=>`<option value="${esc(r.id)}">${esc(r.name)}</option>`).join('');
function dailyQueue(){
 const q=$('#dailySearch').value.toLowerCase(),source=$('#dailySource').value,period=$('#dailyPeriod').value,hide=$('#dailyUnread').checked;
 const now=Date.now();let list=[...DATA.inbox].filter(x=>{
  const sid=x.source_id||allRegistry.find(r=>r.name===x.source)?.id;
  if(source!=='all'&&sid!==source&&!(x.discovered_by||[]).includes(allRegistry.find(r=>r.id===source)?.name))return false;
  if(q&&!((x.title||'')+' '+(x.source||'')).toLowerCase().includes(q))return false;
  if(hide&&readIds.has(x.id))return false;
  // This filter explicitly uses discovery time, not a verified publication date.
  const d=Date.parse(x.discovered_at||'');return period==='all'||(Number.isFinite(d)&&now-d<=Number(period)*86400000&&now-d>=-3600000);
 }).sort((a,b)=>String(b.discovered_at||'').localeCompare(String(a.discovered_at||'')));
 $('#dailyCount').textContent=list.length+' matching source links · showing up to 80 · discovery dates are not publication verification';
 $('#dailyArticles').innerHTML=list.slice(0,80).map(x=>`<article class="daily-article"><div><span class="eyebrow">${esc((x.discovered_by||[x.source||'Source']).join(' · '))}</span><h3><a href="${esc(safe(x.url))}" target="_blank" rel="noopener noreferrer">${esc(x.title)} ↗</a></h3><p class="small">Discovered: ${esc(time(x.discovered_at))}${x.published_raw?' · Publisher date (unverified): '+esc(x.published_raw):' · Publication date not verified'}</p><span class="pill">Unreviewed discovery · not a study fact</span></div><button type="button" data-read-link="${esc(x.id)}" aria-pressed="${readIds.has(x.id)}">${readIds.has(x.id)?'✓ Read':'Mark read'}</button></article>`).join('')||'<div class="empty">No links in this view. Try “All discovered links”. This does not prove there was no relevant news.</div>';
}
function sourceCards(){
 const problems=$('#onlyProblems').checked;
 $('#dailySources').innerHTML=registry.filter(r=>!problems||logs.get(r.id)?.status!=='ok').map(r=>{
  const l=logs.get(r.id)||logs.get(r.name)||{},c=coverage.get(r.id)||{},good=l.status==='ok';
  return `<article class="tile source-card"><div class="source-state ${good?'ready':'attention'}">${good?'Links collected · not yet reviewed':l.status==='review_required'?'Manual review required':'Access unresolved'}</div><h3>${esc(r.name)}</h3><p class="small">${esc(r.category)} · Required, never silently dropped</p><p class="small">${good?esc((l.discovered||0)+' links in latest sweep'):esc(l.error||'Not checked in this snapshot')}${l.fallback_used?' · Official fallback used':''}</p><a class="action" href="${esc(safe(r.url))}" target="_blank" rel="noopener noreferrer">Open source ↗</a>${r.fallbacks?.length?`<details><summary>Official-host candidate routes (${r.fallbacks.length})</summary>${r.fallbacks.map((f,i)=>`<p><a href="${esc(safe(f.url))}" target="_blank" rel="noopener noreferrer">Official route ${i+2} ↗</a></p>`).join('')}<p class="small">Each route is checked independently. An alternative address is not a confirmed fix.</p></details>`:''}${r.manual_recovery?`<p><a href="${esc(safe(r.manual_recovery.search_url))}" target="_blank" rel="noopener noreferrer">Find this source’s indexed pages ↗</a></p><p class="small">Manual search only—not a successful automatic collection or verified source reading.</p>`:''}<p class="small">Archive notes referencing this domain: ${Number(c.archive_notes_referencing_domain||0)}. Historical references do not verify today’s coverage.</p><label class="small"><input type="checkbox" data-check-source="${esc(r.id)}" ${checked.has(r.id)?'checked':''}> Reviewed by me today · this device only</label></article>`;
 }).join('');
}
$('#compilationCards').addEventListener('click',e=>{const b=e.target.closest('[data-compilation-filter]');if(!b)return;$('#dailySource').value=b.dataset.compilationFilter;$('#dailySearch').value='';$('#dailyPeriod').value='all';dailyQueue();$('#dailyArticles').scrollIntoView?.({block:'start'});});
for(const id of ['dailySearch','dailySource','dailyPeriod','dailyUnread'])$('#'+id).addEventListener('input',dailyQueue);
$('#onlyProblems').addEventListener('change',sourceCards);
$('#dailyRefresh').onclick=()=>location.reload();
$('#dailyAllNotes').onclick=()=>goStudy('all');
$('#dailyAP').onclick=()=>{goStudy('all');$('#exam').value='ap';render();};
$('#dailyLatest').onclick=()=>goStudy([...new Set(N.map(n=>n.date.slice(0,7)))].sort().at(-1));
document.addEventListener('click',e=>{
 const read=e.target.closest('[data-read-link]');if(read){const id=read.dataset.readLink;readIds.has(id)?readIds.delete(id):readIds.add(id);persist('atlas-read-links',readIds);dailyQueue();}
 const check=e.target.closest('[data-check-source]');if(check){check.checked?checked.add(check.dataset.checkSource):checked.delete(check.dataset.checkSource);persist('atlas-source-check-'+today,checked);}
});
const hashTabs={daily:'daily',study:'study',practice:'practice',sources:'daily',updates:'updates'};
function showDaily(){document.querySelectorAll('.panel').forEach(p=>p.classList.toggle('show',p.id==='daily'));document.querySelectorAll('[data-tab]').forEach(b=>b.classList.toggle('active',b.dataset.tab==='daily'));}
function route(){const key=location.hash.slice(1);const tab=hashTabs[key];if(!key||tab==='daily')showDaily();else if(tab)document.querySelector('[data-tab="'+tab+'"]').click();if(key==='sources')$('#dailySources').scrollIntoView?.({block:'start'});}
document.addEventListener('click',e=>{const b=e.target.closest('[data-tab]');if(b){const key=b.dataset.tab;if(['daily','study','practice','updates'].includes(key)){try{history.replaceState(null,'','#'+key);}catch(e){}}}});
window.addEventListener('hashchange',route);dailyQueue();sourceCards();route();
})();
