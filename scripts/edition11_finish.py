import json,pathlib,csv,collections
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
N=load('data/notes.json');S=load('data/sources.json');J=load('data/linkages.json');D=load('research/magazine-review/vision-inventory.json');by={n['id']:n for n in N}
links={1:[3,4,5,20,42],3:[1,2,36,41,43],4:[7,8,9,12,16,17],5:[32],6:[21,25,38],7:[22,29,46],8:[13,15,31,35,38,41,43,44,45,47,48],9:[19,20,24,33,38,39,45],10:[7,8,14,15,47],11:[11,30,31,48],12:[19,20,22,24,25,29,34,46],13:[5,10,26,27,28,36,43],14:[23,44],15:[32],17:[13,21,25,31,48],18:[19,24,33,38,39,45]}
for i,ks in links.items():J[i-1]['notes']=list(dict.fromkeys(J[i-1]['notes']+[f'E11-2604-{k:03}' for k in ks]))
for n in N:
 n['journeys']=[j['id'] for j in J if n['id'] in j['notes']];n['related_notes']=list(dict.fromkeys(n.get('related_notes',[])+[k for j in J if n['id'] in j['notes'] for k in j['notes'] if k!=n['id']]))
for p,v in [('data/notes.json',N),('data/linkages.json',J)]: (R/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
lines=['# Civils Atlas · Cross-month reading journeys','','18 comparative reading paths across 2025 and January–April 2026. Reading order is not necessarily a legal timeline. Preserve data vintages, dates and legal stages.','']
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
p=R/'template.html';s=p.read_text().replace('Research edition 10','Research edition 11').replace('January–March 2026 now blend','January–April 2026 now blend').replace("$('#month').value='2026-03';render()","$('#month').value='2026-04';render()").replace("$('#practiceMonth').value='2026-03';practice()","$('#practiceMonth').value='2026-04';practice()")
s=s.replace('New: March 2026','March 2026')
if 'data-month="2026-04"' not in s:s=s.replace('<div class="jumpbar">','<div class="jumpbar"><button data-month="2026-04">New: April 2026 · 48 notes</button>',1)
p.write_text(s)
c=collections.Counter(n['date'][:7] for n in N);mag=sum(bool(x[-1]) for x in t);total=len(t);paths=sum(bool(n['journeys']) for n in N)
table='| Expanded period | Indexed notes | Original MCQs | Mains plans |\n|---|---:|---:|---:|\n'+'\n'.join(f'| {m} | {c[m]} | 30 | 8 |' for m in sorted(D))
guide=f'''# Civils Atlas · Edition 11

UPSC × Andhra Pradesh APPSC · English · Research cut-off: **7 November 2026**

## Open and study
Open **index.html**. Study and practice now open **April 2026**. Sixteen selected monthly volumes in **volumes/** provide PDF, editable Word and Markdown notes, original MCQs with explanations and tailored Mains frameworks. Months in different years have separate practice/document links. **Study-Notes.docx** contains the whole working archive. Eighteen comparative reading paths connect **{paths} notes**; their reading order is not a single legal timeline. The app shows eight direct related-note links per note, with wider sequences in Linked reading paths.

**{len(N)} notes / {len(S)} source-reference entries / 480 original MCQs / 128 original Mains frameworks.** This comprises 583 notes indexed to 2025, 45 each to January/February 2026, 48 each to March/April 2026 and two later inherited seeds. Source-reference counts do not mean that many primary texts were fully read. These are selected original study aids, not official questions or exam predictions.

{table}

## April continuation
**48 newly authored April-indexed notes, 30 MCQs and eight tailored Mains plans.** Coverage includes Parliament, the defeated delimitation package, CPI/MPC, PPI consultation, social-impact finance, SEZ domestic sales, export-risk support, New Zealand FTA signing, online gaming, underground coal gasification, textile remission, rural roads, overload fees, tar-ball proposals, Austria/Korea, insolvency reform, gig work, annual PLFS, edible oils, PLI, road safety, labour protests, farm resilience, payments/fraud, AI security, defence exports, renewables, water systems, Artemis II, One Health, Phule, trust-based regulation, census, Amaravati heritage, rural housing, household vulnerability and business ethics.

Eight notes under Andhra Pradesh cover the capital amendment Act, state inflation evidence, census timetable, heat alerts, Polavaram rehabilitation, Puttaparthi DRDO land allotment, fishing-harbour approvals and Punganur canal modernisation. Amaravati heritage is an additional AP-linked culture note. National notes contain original AP applications, not invented state implementation claims. Exact APPSC paper mapping and full state-GO reconciliation remain unfinished.

## Evidence contract
Official public Vision IAS archive identifies the April edition at web posting **22 May 2026**. **34 canonical article URLs inventoried; 23 public bodies retrieved and selected lead/substantive passages inspected and used**. One hash-navigation duplicate was excluded, not counted as another article. This is not a full-issue audit. Across sixteen editions: **{total} URLs, {mag} linked, {total-mag} unincorporated**. Editorial month, publication date and event chronology remain distinct. No gated PDFs or magazine bodies redistributed.

Independent April research: all six PRS review chunks; RBI MPC minutes opening/resolution; MoSPI March CPI release and AP table; PIB SEZ, FTA, PMGSY, annual PLFS, defence-export and Jan Vishwas material; **full two-page AP amendment Gazette**; opening IBBI-hosted IBC amendment Gazette; NASA substantive mission recap; ASI official search extract; contemporary AP census, heat and Cabinet reports. The AP Cabinet fetch failed initially, but direct public HTML extraction recovered the substantive report. ASI’s old URL redirected to its homepage: only the substantive official search extract is claimed. Detailed gaming commencement uses an inspected legal-practice search extract, not a primary Gazette reading. **data/source-access.json** records actual scopes and failures.

## Corrections and essential distinctions
- **March correction:** Jan Vishwas’s earlier PRS-derived **80 Acts** is corrected to **79 Acts / 784 provisions** from the primary 27 March release. The archive and rebuilt March volume reflect the correction; historical Edition10 ZIP is not silently replaced. Acts, provisions and offences are distinct counts.
- **Delimitation:** April’s Constitution amendment was defeated. The proposed 850-seat ceiling and altered women’s-reservation trigger did not become operative changes. Article368 requires both a majority of total membership and two-thirds present and voting; do not omit the first limb.
- **Amaravati:** assent **6 April 2026**, deemed effect **2 June 2024**; section5 names Amaravati and defines the relevant capital-city area by APCRDA notifications. March’s Assembly resolution was an earlier request. Future parliamentary amendment is not constitutionally impossible.
- **CPI:** 13 April reports **March provisional3.40%**, not April inflation; AP’s corresponding provisional CPI/food rates are **4.05%/5.45%**. Quarterly averages and index levels differ. RBI’s **22 April minutes** record the **6–8 April meeting**, not a second rate change.
- **New Zealand:** the primary signing release is **27 April**, not PRS’s reference-list28April. Signature is not verified entry into force. Tariff-line and trade-value coverage, investment commitment and realised inflows are different measures.
- **IBC:** assent and provision-specific commencement are separate; do not backdate later operative procedures to6April. **Gaming:** April notification and **1 May commencement** are distinct. PPI, fraud, tar-ball and other consultations are not automatically final law.
- **PLFS:** released **27 March**, reference year **January–December2025**, carried forward in April’s magazine. Age/status/denominator labels matter. The primary hours-worked difference is not an unpaid-work measure. Older graduate/subgroup statistics are not substituted for the current national estimate.
- **Energy:** GWcapacity is not TWhgeneration; non-fossil is broader than renewable. The magazine’s51.5%demand statement is not adopted as a verified energy-share figure.
- **Phule:** April2026 marks **199 completed years** after1827; the200thanniversary is in2027. **Amaravati sculpture:** the inspected ASI account describes limestone, not blanket white-marble construction. Ancient monument geography is not the full statutory capital region.
- **AP census:** optional self-enumeration **16–30 April**, field houselisting **1–30 May**. No claim the population census was completed in April. Heat alerts distinguish forecasts from observed readings.
- **AP approvals:** revised Polavaram assistance does not prove all rehabilitation obligations fulfilled. Land allotment is not production; harbour/canal approval is not completed spending or realised beneficiary gains. Detailed GOs/DPRs remain unchecked.

Earlier safeguards remain in notes: GDP/CPI rebasing and vintage comparisons; AP Budget outlay/loans/repayment reconciliation; NDC intensity/capacity distinctions; SC/ST legal differences; adoption’s12weeks; FDI FEMA commencement; FHI reference-year/pillar labels; Mahad anniversary; NavIC navigation versus messaging; EIA scheduled thresholds and defence/launch/trade implementation stages.

## Still unfinished
**Full January 2025–7 November 2026 coverage is NOT delivered.** May–November2026 comprises **seven periods requiring substantial chronological backfill**. All **23 monthly audits**, **253 subject-month cells** and the **676-day daily-source reconciliation** remain open. Expanded does not mean exhaustive or fact-certified. Culture/sport/awards/maps/shorts remain uneven. Many underlying Gazette texts, judgments, bilateral annexes and AP implementing orders are unread. Remaining inventory links are not disguised as completed research.

## Daily updates and rebuild
The supplied06:30IST workflow is **not activated on durable hosting**. The last recorded collector test remains205candidates, five responding and three blocked streams; no fresh collector run is claimed. Discovery is not verified publication, and the preview does not research after a turn ends.

Install dependencies, then run `python scripts/validate.py && python scripts/reconcile.py && python scripts/build.py`. JSON is authoritative. Historical authoring constructors can overwrite later edits. App, schema, export and pagination checks do not independently certify facts, current law or comprehensive coverage.
'''
# Readability in narrative guides, preserving paths/IDs.
import re
guide=re.sub(r'(?<=[A-Za-z%])(?=\d|₹)',' ',guide);guide=re.sub(r'(?<=\d)(?=[A-Za-z])(?!st\b|nd\b|rd\b|th\b)',' ',guide);guide=re.sub(r'(?<=[%+])(?=[A-Za-z])',' ',guide);guide=re.sub(r',(?=[A-Za-z₹])',', ',guide)
(R/'START-HERE.md').write_text(guide)
p=R/'README.md';old=p.read_text();keep=old[old.index('## Daily automation'):] if '## Daily automation' in old else '';p.write_text(guide+'\n'+keep)
(R/'research/Research-Status.md').write_text(guide.replace('# Civils Atlas · Edition 11','# Research status · Edition 11')+'''
## Next chronological work and primary queue
May2026 is next. Independently inspect the actual gaming Gazette, IBC commencement/rules, detailed SEBI AIF instrument, tariff schedules/FTA entry-into-force instruments, Phalodi road-safety order, final digital-fraud/PPI directions and AP implementing GOs before describing April announcements as current operative law. Review earlier pending transgender/FDI/EIA and other primary queues. Complete remaining magazine topics and source-by-source daily audits; do not infer completeness from inventory counts.
''')
(R/'research/magazine-review/Integration-Report.md').write_text(f'''# Official public Vision IAS integration · Edition 11

Updated7November2026. Sixteen editorial coverage months: January–December2025 and January–April2026. **{total} canonical URLs; {mag} linked, {total-mag} unincorporated**. Inventory/link counts are not completeness scores.

The April edition is confirmed by the official public archive link to the22May2026 posting.34canonical article URLs; a hash-navigation duplicate excluded.23selected public bodies retrieved and lead/substantive passages inspected/used, not a whole-issue review. Original notes add primary/independent checks and qualify chronology, Phule anniversary, limestone, labour/statistical denominators, capacity/generation and current-law claims.

Source-access.json records full versus selective primary/secondary reading and access failures. Reconciliation CSV retains pending articles. January–April2025 were retrofitted before chronological continuation fromMay2025. All later editions remain unincorporated here; no gated or full magazine bodies are redistributed.
''')
for name in ['check_exports.py','check_question_pagination.py']:
 p=R/'scripts'/name;p.write_text(p.read_text().replace('edition-10-','edition-11-'))
p=R/'scripts/build.py';p.write_text(p.read_text().replace('EDITION 10','EDITION 11'))
p=R/'scripts/validate.py';p.write_text(p.read_text().replace("'E9-','E10-'","'E9-','E10-','E11-'"))
p=R/'scripts/reconcile.py';s=p.read_text().replace("'2026-02','2026-03'}","'2026-02','2026-03','2026-04'}").replace('8 need substantial chronological backfill.','7 need substantial chronological backfill.');p.write_text(s)
p=R/'.qa/check.cjs';s=p.read_text().replace("['2026-03',48]]","['2026-03',48],['2026-04',48]]").replace("'March 2026 initial'","'April 2026 initial'").replace('length===723','length===771').replace('notes:723','notes:771').replace('expanded_months:15,quizzes:15','expanded_months:16,quizzes:16').replace('edition-10-app-checks','edition-11-app-checks').replace('15 month filters/quizzes; 723 archive','16 month filters/quizzes; 771 archive')
s=s.replace("assert(errors.length===0,errors.join('\\n'));console.log", "d.querySelector('[data-month=\"2026-04\"]').click();assert(d.querySelectorAll('details.note').length===48,'April quick');input('#exam','ap');assert(d.querySelector('#E11-2604-041'),'April capital Act');assert(d.querySelector('#E11-2604-045'),'April rehabilitation');input('#exam','all');d.querySelector('#practiceMonth').value='2026-04';d.querySelector('#practiceMonth').dispatchEvent(new dom.window.Event('change'));assert(d.querySelector('#quiz').textContent.includes('APR26-01'),'April practice');assert(d.querySelector('#volumeLinks').textContent.includes('April 2026'),'April documents');assert(errors.length===0,errors.join('\\n'));console.log")
p.write_text(s)
print('Integrated',len(N),'notes;',total,'Vision URLs;',mag,'linked;',paths,'notes in18journeys')
