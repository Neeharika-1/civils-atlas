import json,pathlib,csv,collections
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
N=load('data/notes.json');S=load('data/sources.json');J=load('data/linkages.json');D=load('research/magazine-review/vision-inventory.json');by={n['id']:n for n in N}
links={1:[7,9,10,11,12,13,14,15,16,31,32,33,34,35,64],3:[1,6,18,21,22,23,24,45,51,55,63],4:[25,26,27,28,29],6:[13,14,15,33,34,43],7:[8,17,25,49,57,58,59,60,61],8:[1,6,8,18,22,36,39,41,42,54,55,56,59,60,61,63,64],9:[2,3,4,5,6,7,12,16,33,45,46,47,48,53,54,62,63],10:[8,16,19,27,29,36,38,55,56,59],11:[17,38,39,40,41,42,43,44,60],12:[2,3,4,5,7,8,15,33,34,47,49,57,58,59,61,63],13:[10,11,30,31,32,44,45,49,50,56,57,59,63],14:[36,42,43,44],17:[6,13,14,15,16,33,34,42,43],18:[2,3,4,5,12,16,20,21,23,24,37,40,45,46,47,48,51,52,53,54,62,63]}
for i,ks in links.items():J[i-1]['notes']=list(dict.fromkeys(J[i-1]['notes']+[f'E12-2605-{k:03}' for k in ks]))
for n in N:
 n['journeys']=[j['id'] for j in J if n['id'] in j['notes']];n['related_notes']=list(dict.fromkeys(n.get('related_notes',[])+[k for j in J if n['id'] in j['notes'] for k in j['notes'] if k!=n['id']]))
for p,v in [('data/notes.json',N),('data/linkages.json',J)]: (R/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
lines=['# Civils Atlas · Cross-month reading journeys','','18 comparative reading paths across 2025 and January–May 2026. Reading order is not necessarily a legal timeline. Preserve data vintages, dates and legal stages.','']
for j in J:lines+=['## '+j['id']+' · '+j['title'],j['mechanism'],'']+['- **'+k+'** · '+by[k]['date'][:7]+' · '+by[k]['title'] for k in j['notes']]+['','**Avoid this shortcut:** '+j['caution'],'','**Mains synthesis:** '+j['prompt'],'']
(R/'volumes/Cross-Month-Reading-Journeys.md').write_text('\n'.join(lines)+'\n')
t=[]
for m,d in sorted(D.items()):
 for a in d['articles']:
  ks=[n['id'] for n in N if any(S[k][1]==a['url'] for k in n['sources'])];a['linked_notes']=ks;a['reconciliation']='Selected passages used; full-topic/primary audit open' if ks else 'Not incorporated; substantive reconciliation pending'
  if ks:a['retrieval']='Public body retrieved; selected lead/substantive passages inspected' if m=='2026-05' else a.get('retrieval','Not recorded')
  if ks:a['review']='Selected passages incorporated into original notes; not complete article/issue review'
  t.append([m,d['web_posting_date'],a['title'],a['url'],a.get('retrieval','Not recorded'),a.get('words',''),a['reconciliation'],'; '.join(ks)])
(R/'research/magazine-review/vision-inventory.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
with (R/'research/magazine-review/vision-reconciliation.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Coverage month','Web posting date','Title','Official URL','Retrieval status','Retrieved words','Editorial reconciliation','Linked notes']);w.writerows(t)
p=R/'template.html';s=p.read_text().replace('Research edition 11','Research edition 12').replace('January–April 2026 now blend','January–May 2026 now blend').replace("$('#month').value='2026-04';render()","$('#month').value='2026-05';render()").replace("$('#practiceMonth').value='2026-04';practice()","$('#practiceMonth').value='2026-05';practice()").replace('New: April 2026','April 2026')
if 'data-month="2026-05"' not in s:s=s.replace('<div class="jumpbar">','<div class="jumpbar"><button data-month="2026-05">New: May 2026 · 64 notes</button>',1)
p.write_text(s)
c=collections.Counter(n['date'][:7] for n in N);mag=sum(bool(x[-1]) for x in t);total=len(t);paths=sum(bool(n['journeys']) for n in N)
table='| Expanded period | Indexed notes | Original MCQs | Mains plans |\n|---|---:|---:|---:|\n'+'\n'.join(f'| {m} | {c[m]} | 30 | 8 |' for m in sorted(D))
guide=f'''# Civils Atlas · Edition 12

UPSC × Andhra Pradesh APPSC · English · Research cut-off: **7 November 2026**

## Open and study
Open **index.html**. Study and practice now open **May 2026**. Seventeen selected monthly volumes in **volumes/** provide PDF, editable Word and Markdown notes, original MCQs with explanations and eight tailored Mains frameworks each. Months in different years have distinct practice/document links. **Study-Notes.docx** contains the whole working archive. Eighteen comparative reading paths connect **{paths} notes**; reading order is not a single legal timeline. The app and note exports show eight direct related-note references, with wider sequences in Cross-Month Reading Journeys.

**{len(N)} notes / {len(S)} source-reference entries / 510 original MCQs / 136 original Mains frameworks.** This comprises 583 notes indexed to 2025, 45 each to January/February 2026, 48 each to March/April 2026, 64 to May 2026 and two later inherited seeds. Reference counts do not mean that many primary documents were fully read. These are original selected study aids, not official questions or exam predictions.

{table}

## May continuation
**64 newly authored May-indexed notes, 30 MCQs and eight tailored Mains frameworks.** Coverage includes courts/ordinances; four central labour-rule areas; rural-employment drafts; ECLGS; BHAVYA; insurance FDI; recovery and mutual-fund consultations; philanthropic CSR; MSP/FRP/cotton; PDS; surface gasification; demographic research; vehicle fitness; anti-doping; constitutionalism; panchayat indices; ECI appointments; sports institutions; US/Nordic/UAE and nuclear governance; oil coordination; DPI/UPI/IIP; rural/FPO/bank-capital evidence; naval strategy; laundering; circularity/hydro/ocean carbon/big cats/dam safety/ENSO; weather AI; examinations; SRS/care/health; R&D; drones; Bhojshala; Padma; school systems and child screening.

**Ten dedicated AP notes:** South Coast Railway notification; amended BharatNet agreement; deep-tech learner targets; AMCA infrastructure foundation; AI data-centre approval; solar-plus-storage units; manufacturing approvals; birth-incentive announcement; school-reform review; April inflation published in May. National notes add original AP analytical applications, not invented implementation claims. Exact APPSC paper mapping and comprehensive state-GO reconciliation remain unfinished.

## Evidence contract
The official public Vision IAS archive explicitly identifies **May 2026** at the **30 June 2026** web posting. **46 canonical article URLs inventoried; 38 public bodies retrieved; selected lead/substantive passages from 35 used in original notes**. PIL, Italy and PM POSHAN remain unincorporated; the latter's summary/body extension dates conflict. Eight news-in-shorts pages are not retrieved/incorporated in this batch. This is not a full-issue or complete primary audit. Across seventeen editions: **{total} URLs / {mag} linked / {total-mag} unincorporated**. No gated PDFs or magazine bodies redistributed.

Independent reading includes **all eight PRS review chunks**, **full two-page Supreme Court Ordinance**, selected English labour provisions from the 318-page OSH, 259-page Social Security and 69-page Wage Rules; full substantive PMO ECLGS and PIB CSR/MSP/coal/AP BharatNet/Padma releases; opening MoSPI CPI and later IIP chronology/methodology releases; contemporary AP AMCA, skills, Cabinet, birth-incentive and education reports. A large PDF being retrieved does **not** mean all its pages were read.

Actual access is recorded in **data/source-access.json**. WAM's substantive official search extract was read but direct fetch failed HTTP500. The AP railway Gazette was not independently read: a contemporary IANS extract supplies notification/operation reporting. ThePrint's substantive PTI body was available through both fetch chunks while separate direct requests failed403. APAC's opening fetch was navigation-heavy; direct public HTML extraction recovered the substantive Cabinet report. Full AP GOs, company filings, detailed land boundaries, most regulatory instruments and many original statistical tables remain unchecked.

## Essential distinctions and corrections
- **Supreme Court:** 37 judges **excluding** the CJI; **38 including**. The 16 May Ordinance commenced at once, but sanctioned posts do not mean immediate filled posts. Later replacement/lapse is not certified here.
- **Labour:** central-rule jurisdiction and the appropriate government matter. Inspected OSH rules specify 48 weekly hours and written-consent/transport/safety conditions for women's night work. Wage floor, appropriate-government minimum and CPI-IW adjustment are different decisions.
- **Gig eligibility:** 90 days with one aggregator or 120 cumulatively across aggregators in the preceding financial year, plus scheme-specific requirements. The rule explicitly permits three aggregators on one calendar day to count three days. Registration is not automatic receipt of every employee benefit.
- **VB–G RAM G:** May drafts and stated **1 July commencement** are distinct. Do not call a consultation final or extinguish old wage claims by assumption.
- **Credit:** ECLGS support uses peak **utilised** Q4 working capital; a lender guarantee is not debt forgiveness. **BHAVYA:** land readiness, SPV conditions and lower-of private-development caps remain relevant.
- **CSR:** ZCZP pays no coupon/principal redemption; the 10% ceiling uses **annual CSR expenditure**, not net profit. **Insurance:** the general 100% permission does not remove LIC's separate reviewed 20% cap or prudential rules.
- **Kharif MSP:** common paddy ₹2,441/quintal, Grade A ₹2,461. Highest absolute rise is sunflower ₹622. The primary cost description includes paid-out costs and imputed family labour; do not silently relabel as full C2 or universal procurement. FRP recovery adjustments concern another crop/price framework.
- **Coal:** surface facilities differ from April's underground extraction. The ₹9,000 crore product cap has **SNG/urea exceptions**. The scheme's 75 MT expectation differs from the national 100 MT goal. Coal-derived syngas is not automatically green hydrogen.
- **IIP chronology:** an earlier calendar scheduled 28 May, but the inspected later primary explicitly says **1 June initial new-series launch**, followed by **29 June PPI-based supersession**. These June facts are clearly labelled retrospective chronology checks in a May-indexed article, not known May outcomes. GDP provisional estimates scheduled for May were also located as June releases and are queued for June, not misdated into May.
- **UAE oil:** official announcement **28 April**, stated effect **1 May**. Exit from quota coordination is not cessation of exports or guaranteed immediate lower prices. Nordic/EU/EFTA memberships are not interchangeable; failed NPT review consensus does not terminate the treaty.
- **Measurement:** bank capital is not liquidity; RWA is not the amount of required capital. Attachment is not final confiscation. Care satellite valuations are not amounts already counted in GDP. Private-hospital rural/urban shares need weights for a combined estimate. Neonatal mortality concerns the first 28 completed days.
- **Environment:** “super” El Niño is informal; seasonal risk is probabilistic. UP's 1-km weather pilot is not verified AP deployment. Small capacity is not a no-impact exemption; marine carbon uptake requires net/permanence checks. IBCA eligibility/range countries are not actual membership.
- **Heritage and honours:** Bhojshala's full judgment, appeals/stays and inscription attribution remain unreviewed; no current-rights certification. Kurma means tortoise, not crocodile. Padma annual approval and 25 May investiture are not two awards; no exhaustive recipient list claimed.
- **AP:** railway notification is not 1 June operation; BharatNet GP scope is not activated homes; learner targets are not placements; AMCA infrastructure is not fighter induction. Data-centre/industrial approvals and prospective jobs are not realised investment/employment. MWAC/MWpDC/MWh are distinct. Birth-incentive operating rules/payments remain unverified; school enrolment targets are not achieved outcomes.
- **AP CPI:** 12 May reports **April provisional** AP headline/food **4.20%/5.64%**, national **3.48%/4.20%**, base2024. AP's headline gap is **0.72 percentage points**, not a72%price rise. March national3.40%is final in this release.

Earlier reviewed safeguards are retained: March Jan Vishwas count corrected to **79 Acts / 784 provisions** using the primary introduction release; April delimitation package defeated, not enacted; Amaravati assent6April with deemed effect2June2024; NZ signing27April distinct from FTA entry into force; IBC provision-specific commencement; gaming notification versus1Mayeffect; PLFS age/status/vintage distinctions; Phule199thanniversary; limestone at Amaravati; NDC capacity/intensity distinctions; AP Budget outlay/borrowing reconciliation and constitutional-rights distinctions. Historical Edition11 ZIP is not silently rewritten.

## Still unfinished
**Full January 2025–7 November 2026 coverage is NOT delivered.** June–November2026 comprises **six periods requiring substantial chronological backfill**. All **23 monthly audits**, **253 subject-month cells** and the **676-day daily-source reconciliation** remain open. Expanded does not mean exhaustive or fact-certified. Maps, awards/recipient lists, sports results and news-in-shorts remain uneven; many primary texts, judgments and AP GOs remain unread. Inventory or queued links are not completed substantive coverage.

## Daily discovery and rebuild
The supplied06:30IST workflow is **not activated on durable hosting**. The last recorded collector test remains205candidates,five responding and three blocked streams; no fresh collector run is claimed. Discovery is not automatic verified publication. The preview does not continue researching after the turn.

Install dependencies,then run `python scripts/validate.py && python scripts/reconcile.py && python scripts/build.py`. Authoritative JSON preserves reviewed content. Historical constructors can overwrite subsequent edits. App/schema/export/pagination checks do not independently certify facts,legal currency or completeness.
'''
# Readable guide spacing, without changing files, IDs or URL strings.
from importlib.util import spec_from_file_location,module_from_spec
# Use a standalone text-only formatter; do not import authoring/typography scripts with write side effects.
import re
guide=re.sub(r'(?<=[A-Za-z%])(?=\d|₹)',' ',guide);guide=re.sub(r'(?<=\d)(?=[A-Za-z])(?!st\b|nd\b|rd\b|th\b)',' ',guide);guide=re.sub(r',(?=[A-Za-z₹])',', ',guide)
for a,b in [('199 thanniversary','199th anniversary'),('Mayeffect','May effect'),('MWAC','MW AC'),('MWpDC','MWp DC'),('72%price','72% price')]:guide=guide.replace(a,b)
(R/'START-HERE.md').write_text(guide)
p=R/'README.md';old=p.read_text();keep=old[old.index('## Daily automation'):] if '## Daily automation' in old else '';p.write_text(guide+'\n'+keep)
(R/'research/Research-Status.md').write_text(guide.replace('# Civils Atlas · Edition 12','# Research status · Edition 12')+'''
## Next chronological work
June2026: actual1JuneIIPnewseries,29JunePPIrevision,5JuneGDPprovisionalestimates,railoperation and remaining primary-law queues. Read the public June magazine first,then independent national/APsources. Reconcile earlier omissions and daily-source audits instead of treating this monthly batch as complete.
''')
(R/'research/magazine-review/Integration-Report.md').write_text(f'''# Official public Vision IAS integration · Edition 12

Updated7November2026. Seventeen editorial coverage months,January–December2025 and January–May2026. **{total} canonical URLs / {mag} linked / {total-mag} unincorporated**. Counts are not completeness scores.

Official archive confirms May2026 at30June posting.46canonical article URLs;38public bodies retrieved;35selected lead/substantive passage sets used in original notes. PIL,Italy,PM POSHAN remain unincorporated; eight news-in-shorts pages not retrieved. Underlying primary instruments not all read. Linked notes preserve actual chronologies, legal stages and statistical denominators rather than reproduce magazine text.

Important safeguards include IIPJuneactual-release chronology versus Maycalendar date; SC37plusCJI; gig cumulative aggregator-day counting; coal-cap exceptions; MSPcost basis; correct bankRWAdefinition; care/health denominators; Bhojshala current-order limits and Kurma correction; IBCAfunding/range-member distinction; Padma announcement versus investiture. Source-access registry and reconciliation CSV retain actual access limits and pending items. No gated/full magazine bodies redistributed. The requested archive and daily-source audits remain unfinished.
''')
for name in ['check_exports.py','check_question_pagination.py']:
 p=R/'scripts'/name;p.write_text(p.read_text().replace('edition-11-','edition-12-'))
p=R/'scripts/build.py';p.write_text(p.read_text().replace('EDITION 11','EDITION 12'))
p=R/'scripts/validate.py';p.write_text(p.read_text().replace("'E10-','E11-'","'E10-','E11-','E12-'"))
p=R/'scripts/reconcile.py';p.write_text(p.read_text().replace("'2026-03','2026-04'}","'2026-03','2026-04','2026-05'}").replace('7 need substantial chronological backfill.','6 need substantial chronological backfill.'))
p=R/'.qa/check.cjs';s=p.read_text().replace("['2026-04',48]]","['2026-04',48],['2026-05',64]]").replace("length===48,'April 2026 initial'","length===64,'May 2026 initial'").replace('length===771','length===835').replace('notes:771','notes:835').replace('expanded_months:16,quizzes:16','expanded_months:17,quizzes:17').replace('edition-11-app-checks','edition-12-app-checks').replace('16 month filters/quizzes; 771 archive','17 month filters/quizzes; 835 archive')
s=s.replace("assert(errors.length===0,errors.join('\\n'));console.log", "d.querySelector('[data-month=\"2026-05\"]').click();assert(d.querySelectorAll('details.note').length===64,'May quick');input('#exam','ap');assert(d.querySelector('#E12-2605-056'),'May BharatNet');assert(d.querySelector('#E12-2605-064'),'May CPI');input('#exam','all');d.querySelector('#practiceMonth').value='2026-05';d.querySelector('#practiceMonth').dispatchEvent(new dom.window.Event('change'));assert(d.querySelector('#quiz').textContent.includes('MAY26-01'),'May practice');assert(d.querySelector('#volumeLinks').textContent.includes('May 2026'),'May documents');assert(errors.length===0,errors.join('\\n'));console.log")
p.write_text(s)
print('Integrated',len(N),'notes;',total,'Vision URLs;',mag,'linked;',paths,'notes in18journeys')
