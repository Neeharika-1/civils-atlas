import json,pathlib,csv,collections
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
N=load('data/notes.json');S=load('data/sources.json');J=load('data/linkages.json');D=load('research/magazine-review/vision-inventory.json');by={n['id']:n for n in N}
links={1:[2,3,15,16,33],3:[1,4,41,47],4:[2,9,10,11,12,40],5:[37],6:[21,22,46],7:[24,25,44,46],8:[26,33,41,42,48],9:[5,6,26,45],10:[19,20,40],11:[27,28,29,44,45],12:[14,21,22,23,31,43],13:[6,16,17,30,32],14:[43],15:[38],17:[21,22,26,35,36],18:[5,6,23,26,45,47]}
for i,ks in links.items():J[i-1]['notes']=list(dict.fromkeys(J[i-1]['notes']+[f'E10-2603-{k:03}' for k in ks]))
for n in N:
 n['journeys']=[j['id'] for j in J if n['id'] in j['notes']];n['related_notes']=list(dict.fromkeys(n.get('related_notes',[])+[k for j in J if n['id'] in j['notes'] for k in j['notes'] if k!=n['id']]))
for p,v in [('data/notes.json',N),('data/linkages.json',J)]: (R/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
lines=['# Civils Atlas · Cross-month reading journeys','','18 comparative reading paths across 2025 and January–March 2026. Reading order is not necessarily a legal timeline. Preserve data vintages, dates and legal stages.','']
for j in J:lines+=['## '+j['id']+' · '+j['title'],j['mechanism'],'']+['- **'+k+'** · '+by[k]['date'][:7]+' · '+by[k]['title'] for k in j['notes']]+['','**Avoid this shortcut:** '+j['caution'],'','**Mains synthesis:** '+j['prompt'],'']
(R/'volumes/Cross-Month-Reading-Journeys.md').write_text('\n'.join(lines)+'\n')
t=[]
for m,d in sorted(D.items()):
 for a in d['articles']:
  ks=[n['id'] for n in N if any(S[k][1]==a['url'] for k in n['sources'])];a['linked_notes']=ks;a['reconciliation']='Selected passages used; full-topic/primary audit open' if ks else 'Not incorporated; substantive reconciliation pending'
  if ks:a['review']='Selected passages incorporated into original notes; not complete article/issue review'
  t.append([m,d['web_posting_date'],a['title'],a['url'],a.get('retrieval','Not recorded'),a.get('words',''),a['reconciliation'],'; '.join(ks)])
(R/'research/magazine-review/vision-inventory.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
with (R/'research/magazine-review/vision-reconciliation.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Coverage month','Web posting date','Title','Official URL','Retrieval status','Retrieved words','Editorial reconciliation','Linked notes']);w.writerows(t)
p=R/'template.html';s=p.read_text().replace('Research edition 09','Research edition 10').replace('January–February 2026 now blend','January–March 2026 now blend').replace("$('#month').value='2026-02';render()","$('#month').value='2026-03';render()").replace("$('#practiceMonth').value='2026-02';practice()","$('#practiceMonth').value='2026-03';practice()")
s=s.replace('New: February 2026','February 2026')
if 'data-month="2026-03"' not in s:s=s.replace('<div class="jumpbar">','<div class="jumpbar"><button data-month="2026-03">New: March 2026 · 48 notes</button>',1)
p.write_text(s)
c=collections.Counter(n['date'][:7] for n in N);mag=sum(bool(x[-1]) for x in t);total=len(t);paths=sum(bool(n['journeys']) for n in N)
table='| Expanded period | Indexed notes | Original MCQs | Mains plans |\n|---|---:|---:|---:|\n'+'\n'.join(f'| {m} | {c[m]} | 30 | 8 |' for m in sorted(D))
guide=f'''# Civils Atlas · Edition 10

UPSC × Andhra Pradesh APPSC · English · Research cut-off: **7 November 2026**

## Open and study
Open **index.html**. Study and practice now open **March 2026**. Fifteen selected monthly volumes in **volumes/** provide PDF, editable Word and Markdown notes, original MCQs with explanations and tailored Mains frameworks. Same-name months in different years retain separate practice/document links. **Study-Notes.docx** contains the whole working archive. Eighteen cross-month reading paths connect **{paths} notes**; their reading order is not a single legal timeline.

**{len(N)} notes / {len(S)} source-reference entries / 450 original MCQs / 120 original Mains frameworks.** This comprises 583 notes indexed to 2025, 45 each to January and February 2026, 48 to March 2026 and two later inherited seeds. These are selected original study aids, not official questions, predictions or fully read-primary counts.

{table}

## March continuation
**48 newly authored March-indexed notes, 30 original MCQs and eight Mains plans.** Includes parliamentary scrutiny, transgender amendment, adoptive maternity, cyber safety, Jan Vishwas/FCRA proposals, FDI review, export remission, digital-trade carry-forward, Canada negotiations, CAPF leadership, company/CSR reform, bank dividends, draft fraud compensation, regulatory ethics, aviation/tolls, farm seeds, AIIMS, mineral governance, JJM, NDCs, electricity/RECs, AI/intermediary rules, BHAVYA, DPI, fiscal health, EIA, CBD/Nagoya, LHCb, NavIC, Mahad and West Asian energy risks.

AP-focused notes cover Amaravati’s Assembly resolution, court expansion, coaching draft, Kadapa/Nandyal renewable manufacturing, PNG/Deepam support, Vaddera quarry concessions, SC-status litigation, municipal interest relief and AP’s fiscal-health diagnosis. National notes also contain original AP applications; these are analytical connections, not claims that new state projects were implemented. Exact APPSC paper mapping remains unfinished.

## Evidence contract
Public official Vision IAS March web edition: posted **30 April 2026**. **37 URLs inventoried; 12 selected public bodies retrieved and lead/substantive passages inspected**, not a complete issue review. Across fifteen editions: **{total} URLs, {mag} linked, {total-mag} unincorporated**. These counts measure inventory/linkage, not completeness. No gated magazine PDFs or full bodies redistributed. Editorial month, website posting and event date are distinct.

Independent March checks include PRS review chunks 0–11/13 plus targeted substantive HTML paragraphs; full RBI BoP release; full DPIIT three-page FDI note; opening DGFT draft/notice; substantive PIB BHAVYA, NDC, UDAN, aviation and JJM announcements; selected Supreme Court judgment passages and the FHI ranking/AP tables; CERN’s substantive LHCb announcement and ISRO’s short statement. Contemporary AP newspaper and IANS reporting support state decisions; primary implementing GOs were not read. **data/source-access.json** records exact access scopes and limitations. A linked source is not proof of full-text review.

## Important corrections and chronology
- **FDI:** the press note says effect begins with the FEMA notification. The note is not itself proof of commencement. Greater-than-10% is not the only test: entity-specific PML rules, aggregated interests and effective control matter; sectoral conditions remain.
- **Digital trade:** the primary consultation notice is **9 February**, carried forward in the March review. No March first-publication date is invented; the draft is not an enacted Act.
- **Adoption:** the specified entitlement is **12 weeks**, with the child’s three-month age restriction struck down. The paternity-leave observation is not a universal new law.
- **SC status:** the AP-linked ruling applies the SC Order and expressly distinguishes ST status. Ordinary criminal allegations were separately examined. It does not say conversion eliminates discrimination or ordinary criminal-law protection. The challenged HC order is **30 April 2025**, not 2024.
- **NDC:** **47% GDP emissions-intensity reduction** versus 2005 is not an absolute emissions cut. **60% non-fossil installed capacity** is not renewable generation. Cabinet approval is not a verified UNFCCC submission date.
- **FHI:** 2026 publication, **FY2023–24** data. AP is **17/18 major states, score 23.1, overall Aspirational**. Its **43.1/Front Runner** label concerns only expenditure quality.
- **EIA:** reject a universal ₹50-crore threshold; applicable scheduled projects/categories/thresholds control. Standing-body changes discussed here are draft proposals.
- **AI:** the committee **submitted its report** on 30 March; it was not newly constituted that day. Recommendations and separate draft intermediary rules are not automatically operative duties.
- **Mahad:** March 2026 is **99 completed years** after March 1927; the 100th anniversary is in 2027. Mesons are quark–antiquark states, not simply two quarks; LHCb’s discovery is composite, not a new elementary particle.
- **NavIC:** IRNSS-1F’s clock failure did not end its one-way messaging service. No live constellation-wide operating count is certified.
- **Aviation:** the 60% direction concerns seat allocation, not zero airfare. UDAN/BHAVYA approval does not mean all assets are built. JJM’s ₹8.69 lakh crore is total outlay; ₹3.59 lakh crore is total central assistance.
- **AP:** March’s capital resolution is not itself Parliament’s amendment; April developments belong to April. Court/post approvals do not prove functioning courts or appointments. Coaching/PNG/quarry/energy decisions need operative instruments. Property-tax relief concerns **50% of interest**, not half the principal tax.

Earlier corrections remain in their notes: AP Budget capital outlay versus loans/repayment; GDP/CPI rebase vintages; Finance Commission acceptance versus proposals; trade-agreement stages; stayed UGC rules and cautious launch/defence claims.

## Still unfinished — do not read the counts as completion
**Full January 2025–7 November 2026 coverage is NOT delivered.** April–November 2026 contains eight periods requiring substantial chronological backfill. All **23 monthly audits**, **253 subject-month cells** and the **676-day daily-source reconciliation** remain open. Expanded does not mean exhaustive or fact-certified. Culture, sport, awards, maps and short developments remain uneven; many underlying Gazette texts, primary judgments, annexes and AP GOs are unread. Zero-subject cells are visible rather than padded.

## Daily updates and rebuild
The supplied 06:30 IST workflow is **not activated on durable hosting**. The last recorded collector test remains 205 candidates, five responding and three blocked streams; this edition does not claim a fresh collector run. Discovery is not verified publication. The live preview does not continue research after a turn ends.

Install dependencies, then run `python scripts/validate.py && python scripts/reconcile.py && python scripts/build.py`. JSON is authoritative; historical constructors can overwrite later edits. Structural, app, file-integrity and pagination tests do not certify factual accuracy or comprehensive coverage.
'''
(R/'START-HERE.md').write_text(guide)
p=R/'README.md';old=p.read_text();keep=old[old.index('## Daily automation'):] if '## Daily automation' in old else '';p.write_text(guide+'\n'+keep)
(R/'research/Research-Status.md').write_text(guide.replace('# Civils Atlas · Edition 10','# Research status · Edition 10')+'''
## Next chronological work and primary-check queue
April 2026 is next. Check Amaravati’s later parliamentary amendment from the actual enacted text; retain the March resolution’s earlier stage. Independently inspect final transgender Gazette/commencement, FEMA FDI notification, final digital-fraud/intermediary/electricity rules, detailed mineral amendments, and AP implementing GOs before treating March announcements as current operative law. Read the underlying CBD/Nagoya national reports and EIA draft primary text; their magazine accounts are selective secondary evidence. Earlier monthly primary-check and daily-source queues remain open.
''')
(R/'research/magazine-review/Integration-Report.md').write_text(f'''# Public official Vision IAS integration · Edition 10

Updated 7 November 2026. Fifteen coverage months, January–December 2025 and January–March 2026: **{total} URLs, {mag} linked, {total-mag} unincorporated**. No whole-issue or completeness certification.

March adds 37 inventoried URLs, 12 selected public article bodies retrieved, and 12 selected integrations. Website posting is 30 April 2026. Lead/substantive passages were inspected, not all linked primary references. Original notes add independent checks and correct/qualify EIA threshold, meson composition, Mahad anniversary, NDC measures, FHI pillar labels and NavIC service claims.

Independent March source scopes are in data/source-access.json. The reconciliation CSV records linked and pending topics honestly. January–April2025 were retrofitted before chronological continuation from May2025. Remaining integration is still unfinished, including most March article URLs and all later editions. Inventory volume is not an audit score; no proprietary magazine bodies are redistributed.
''')
# Update ongoing scripts, not historical authoring constructors.
p=R/'scripts/reconcile.py';s=p.read_text().replace("'2026-01','2026-02'}","'2026-01','2026-02','2026-03'}").replace('9 need substantial chronological backfill.','8 need substantial chronological backfill.');p.write_text(s)
p=R/'scripts/validate.py';s=p.read_text().replace("'E8-','E9-'","'E8-','E9-','E10-'");p.write_text(s)
for name in ['check_exports.py','check_question_pagination.py']:
 p=R/'scripts'/name;p.write_text(p.read_text().replace('edition-09-','edition-10-'))
# Extend the established app regression suite.
p=R/'.qa/check.cjs';s=p.read_text().replace("['2026-02',45]]","['2026-02',45],['2026-03',48]]").replace("length===45,'February 2026 initial'","length===48,'March 2026 initial'").replace('length===675','length===723').replace('notes:675','notes:723').replace('expanded_months:14,quizzes:14','expanded_months:15,quizzes:15').replace('edition-09-app-checks','edition-10-app-checks').replace('14 month filters/quizzes; 675 archive','15 month filters/quizzes; 723 archive')
s=s.replace("assert(errors.length===0,errors.join('\\n'));console.log", "d.querySelector('[data-month=\"2026-03\"]').click();assert(d.querySelectorAll('details.note').length===48,'March quick');input('#exam','ap');assert(d.querySelector('#E10-2603-044'),'Kadapa manufacturing');assert(d.querySelector('#E10-2603-033'),'AP fiscal health');input('#exam','all');d.querySelector('#practiceMonth').value='2026-03';d.querySelector('#practiceMonth').dispatchEvent(new dom.window.Event('change'));assert(d.querySelector('#quiz').textContent.includes('MAR26-01'),'March practice');assert(d.querySelector('#volumeLinks').textContent.includes('March 2026'),'March documents');assert(errors.length===0,errors.join('\\n'));console.log")
p.write_text(s)
print('Integrated',len(N),'notes;',total,'Vision URLs;',mag,'linked;',paths,'notes in journeys')
