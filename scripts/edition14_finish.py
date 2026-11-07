import json,pathlib,re,collections,math
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
def save(p,o):(R/p).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
N=load('data/notes.json');S=load('data/sources.json');L=load('data/linkages.json');new=[n for n in N if n['id'].startswith('E14-')]
def prose(s):
 s=re.sub(r'(?<=[A-Za-z])(?=[0-9₹])|(?<=[0-9])(?=[A-Za-z₹])',' ',s)
 s=re.sub(r'(?<=[%₹])(?=[A-Za-z])',' ',s)
 s=re.sub(r'(?<=[A-Za-z])[,;](?=[A-Za-z])',lambda m:m.group()+' ',s)
 s=re.sub(r'(?<=[0-9])[,;](?=[A-Za-z])',lambda m:m.group()+' ',s)
 s=s.replace('MW×','MW × ').replace('OMquashed','OM quashed').replace('PVonly','PV only').replace('yearone','year one').replace('15July','15 July')
 return s
for n in new:
 for k in ['title','why','static_link','trap','mains']:n[k]=prose(n[k])
 for k in ['facts','analysis']:n[k]=[prose(x) for x in n[k]]
# Explicit editorial date notes override any temptation to use a magazine cover as event evidence.
links={1:[59,64],3:[11,35,36],4:[9,66,67,68,69],5:[48],6:[53,65],7:[8,42,66,67],8:[6,7,11,16,23,36,54,55,56,57,58,60,61,62,63],9:[19,21,53,54,55,56,59,62,65],10:[16,17,25,41,58,61,67,68,69],11:[18,24,25,26,43,50,60,61,66,68],12:[1,3,4,5,8,9,28,29,37,38,39,45,47,52,65,66,68,69],13:[1,12,13,15,33,35,36,39,44,48,54,57,64],14:[1,3,28,29,34,37,47,55],15:[45,46],16:[31],17:[18,19,20,21,22,49,50,60,62,69],18:[6,7,19,21,28,30,47,53,54,55,56,62,65]}
for i,ks in links.items():L[i-1]['notes']=list(dict.fromkeys(L[i-1]['notes']+[f'E14-2607-{k:03}' for k in ks]))
stop=set('the and for with from this that into are not through july india indian policy new state national framework report review development original stage different'.split())
def words(n):return set(re.findall(r'[a-z]{4,}',(n['title']+' '+n['block']).lower()))-stop
old=[n for n in N if not n['id'].startswith('E14')];df=collections.Counter(w for n in old for w in words(n))
for n in N:n['journeys']=[l['id'] for l in L if n['id'] in l['notes']]
for n in new:
 ranks=sorted(old,key=lambda x:sum(math.log(1+len(old)/(1+df[w])) for w in words(n)&words(x))+(1 if n['subject']==x['subject'] else 0),reverse=True)
 cross=[x['id'] for x in ranks[:6]]
 companions=[k for l in L if n['id'] in l['notes'] for k in l['notes'] if k!=n['id']]
 n['related_notes']=list(dict.fromkeys(cross+companions))
save('data/notes.json',N);save('data/linkages.json',L)
Q=load('data/2026-07-mcqs.json')
for q in Q:
 for k in ['question','explanation']:q[k]=prose(q[k])
 q['options']=[prose(x) for x in q['options']]
save('data/2026-07-mcqs.json',Q)
p=R/'volumes/July-2026-Mains-Frameworks.md';p.write_text('\n'.join(prose(x) for x in p.read_text().splitlines())+'\n')
by={n['id']:n for n in N};lines=['# Civils Atlas · Cross-month reading journeys','','18 comparative paths across 2025 and January–July 2026. Preserve evidence vintages, proposals and commencement dates; reading order is not one continuous legal timeline.','']
for l in L:lines+=['## '+l['id']+' · '+l['title'],l['mechanism'],'']+['- **'+k+'** · '+by[k]['date'][:7]+' · '+by[k]['title'] for k in l['notes']]+['','**Avoid this shortcut:** '+l['caution'],'','**Mains synthesis:** '+l['prompt'],'']
(R/'volumes/Cross-Month-Reading-Journeys.md').write_text('\n'.join(lines)+'\n')
# Current UI, preserving the previous June quick navigation.
p=R/'template.html';s=p.read_text().replace('Research edition 13','Research edition 14')
a=s.index('January–December 2025 and January–June 2026');b=s.index(' <a href="research/magazine-review/Integration-Report.md">',a)
s=s[:a]+"January–December 2025 and January–July 2026 have selected expanded volumes. July adds 69 original notes, 30 MCQs and eight Mains frameworks. No independently verified public July Vision edition was found: the latest exposed 31 July reader belongs to June. July therefore uses selected passages from Drishti’s public compilation (25 June–24 July), PRS and independent official/newspaper checks. This is not a complete issue review. June-reported material appearing in the July magazine is labelled as revision, not a new July event."+s[b:]
s=s.replace('<div class="jumpbar"><button data-month="2026-06">New: June 2026 · 62 notes</button>','<div class="jumpbar"><button data-month="2026-07">New: July 2026 · 69 notes</button><button data-month="2026-06">June 2026 · 62 notes</button>')
s=s.replace("$('#practiceMonth').value='2026-06'","$('#practiceMonth').value='2026-07'").replace("$('#month').value='2026-06';render()","$('#month').value='2026-07';render()")
p.write_text(s)
for fn in ['scripts/build.py','scripts/check_exports.py','scripts/check_question_pagination.py']:
 p=R/fn;s=p.read_text().replace('EDITION 13','EDITION 14').replace('edition-13-document','edition-14-document').replace('edition-13-question','edition-14-question');p.write_text(s)
p=R/'scripts/validate.py';p.write_text(p.read_text().replace("'E12-','E13-'","'E12-','E13-','E14-'"))
# Extend—not replace—the regression for older volumes.
p=R/'.qa/check.cjs';s=p.read_text().replace("['2026-06',62]]","['2026-06',62],['2026-07',69]]").replace("length===62,'June 2026 initial'","length===69,'July 2026 initial'").replace('length===896','length===965').replace('notes:896','notes:965').replace('expanded_months:18,quizzes:18','expanded_months:19,quizzes:19').replace('edition-13-app-checks','edition-14-app-checks').replace('18 month filters/quizzes; 896 archive','19 month filters/quizzes; 965 archive')
needle="assert(errors.length===0,errors.join('\\n'));console.log('PASS: 19"
s=s.replace(needle,"d.querySelector('[data-month=\"2026-07\"]').click();assert(d.querySelectorAll('details.note').length===69,'July quick');input('#exam','ap');assert(d.querySelector('#E14-2607-057'),'July NiVU');assert(d.querySelector('#E14-2607-055'),'July disability');input('#exam','all');d.querySelector('#practiceMonth').value='2026-07';d.querySelector('#practiceMonth').dispatchEvent(new dom.window.Event('change'));assert(d.querySelector('#quiz').textContent.includes('JUL26-01'),'July practice');assert(d.querySelector('#volumeLinks').textContent.includes('July 2026'),'July documents');assert(errors.length===0,errors.join('\\n'));console.log('PASS: 19")
p.write_text(s)
counts=collections.Counter(n['priority'] for n in new);linked=sum(bool(n['journeys']) for n in N)
text=f'''# Civils Atlas · Edition 14

**English · UPSC × Andhra Pradesh APPSC · Research cut-off: 7 November 2026**

## Open and study
Open **index.html**. Study and practice default to **July 2026**. Use **volumes/July-2026-Study-Volume.pdf** or editable **.docx**; original Markdown and eight Mains frameworks are alongside them. Earlier monthly volumes remain available.

**69 new July-indexed notes · 12 dedicated AP notes · 30 original MCQs · 8 Mains frameworks.** Four AP notes are explicit applications/revision rather than new state sanctions or events; month-level indexing does not assert an event occurred on31July. Priorities: {counts['P1']} P1 / {counts['P2']} P2 / {counts['P3']} P3.

Working archive: **965 notes / 583 reference entries / 570 MCQs / 152 Mains frameworks / 19 selected monthly volumes / 18 paths linking {linked} notes.** Reference entries are not a count of primary documents fully read. Counts do not certify complete coverage or current law.

## July study map
- **Governance:** public examinations, Supreme Court strength, Advocates draft, national song, births/deaths registration, fair trial, citizenship, internet restrictions and civil-registration evidence.
- **Economy/agriculture:** MSME/TReDS, foreign-investment draft, PMS consultation, insurance/securities regulation, ports/rail, urea, PM-KISAN, rice quality, steel/coal, new statistical series, CPI and skill finance.
- **Social/environment/science:** employment transition, food labels/PDS, medical/pharmacy/drug proposals, retrospective EC judgment, floating solar, offshore exploration, biogas, heron habitat, geothermal, helium, timing, Gaganyaan, oncology, neonatal trials and quantum error correction.
- **AP:** Hero parts centre, SHG fees, tribal Aadhaar access, disability reassessment, rare-disease consultation, NiVU, Pushkaralu planning, dated CPI and explicitly analytical reservoir/offshore/employment applications. Seshachalam is June-reported July revision, not a July discovery.
- **International/culture/sports:** four bilateral briefs attributed to PRS, Vivekananda and Khelo India. This is not an exhaustive awards/results/appointments list.

## Magazine and primary-source honesty
Vision official archive was checked first. Its newest exposed2026reader is **31July posting of the June editorial**, not a verified July edition. No independently verified public July issue was found; unofficial photocopies were not used. The existing Vision inventory remains760URLs /228linked /532pending—discovery counts, not coverage percentages.

Public alternative: **118-page Drishti Saraansh July2026**, covering **25June–24July**. Contents and selected substantive passages were read, not the whole issue. Several excerpts remain source-limited. The complete magazine and extracted text are not redistributed. Source-access registry specifies passages and limits.

PRS substantive July review chunks0–8were read. Independent checks include six Cabinet releases, MoSPI CPI, selected wage/transition/skill Gazette passages, opening FEMA draft and the final five pages of the80-page Supreme Court EC judgment. AP evidence includes actual substantive newspaper reports (English and Telugu), The Hindu disability reporting and an IORD participant account. Primary AP GOs, UIDAI order, bank circular and several sector instruments remain unread.

## Corrections that matter
- PM-KISAN primary outlay **₹3.15lakhcrore**, not rounded₹3.2lakhcroreas an exact figure; annual eligible-family benefit remains₹6,000.
- Khelo/ANSF period **2026–27to2030–31**, not the PRS typo2023–31. Funding approval is not Olympic hosting rights.
- **700MW means floating PV**, not all Indian solar.5000MW×2hours=10000MWh. Sanction and disbursement windows differ.
- **29July EC judgment:** limited2017notification upheld; perpetual2021OMquashed prospectively. Existing clearances are subject to individual challenge; pending cases need judgment-specific treatment, not automatic clearance. No fresh applications under the impugned instruments.
- **Birth Bill:** Lok Sabha passage is not both-House passage. **FEMA/PMS/Pharmacy/NMC/Advocates** proposals are not final operative reforms. Exam-Bill passage does not independently establish assent/commencement.
- **13July CPI refers to June**, provisional: India4.38%headline/5.32%food; AP5.39%/8.18%,2024base. Monthly figures and quarter averages differ.
- **Skill guarantee:**15%aggregate claim ceiling is not individual cover; upper loan limit was already part of the2024revision. Guarantee is not a borrower debt waiver.
- **AP NiVU:** contemporary newspaper names **Explurger**, not the coaching page’s Xplorer. Phased targets are not statewide completion; first-state claim remains promotional.
- **Hero:** Madanapalle in **Satyavedu mandal,Tirupati**, not the familiar town.₹750crorecentre and₹3200croreexpansion are not proved non-overlapping expenditure. Conflicting current-capacity figures withheld.
- **SHG:** fee relief is not interest/principal waiver; headline savings were not reconciled and are withheld. **Aadhaar:** headline cancellation versus officials’ temporary suspension distinguished; alleged irregularities are not adjudicated guilt.
- **Rare-disease conference:**24June event,7July publication. **Seshachalam:**23June news,31July1554epigraph date,July-magazine indexing. Neither is automatically a new July event.
- **Pushkaralu:** proposals,sanction/release language,state share and audited use differ; do not sum overlapping amounts.
- **Quantum:** superposition does not let users read every answer; entanglement does not transmit usable information faster than light. **NeoSep1:** up-to90-day trial scope does not redefine the neonatal period.
- Precise unverified CRS/UDISE/ICI/ISP/NIIF rankings, population totals, helicopter-style launch claims, helium export orders and sports lists are not certified. Indonesia’s Prabowo is **President**, not Prime Minister; Japan’s inconsistent exact visit dates are withheld.

## Unfinished work
**August–November2026 still need substantial backfill (November only1–7).** All23monthly source audits and the daily reconciliation remain open. January2025–7November2026 full coverage has NOT been achieved. Neither this edition nor earlier selected volumes certify every event, latest law or implementation.

**Daily scheduler remains NOT ACTIVATED.** Supplied code can collect candidate links after deployment/enabling; it does not autonomously author and verify daily notes. Last recorded collector result remains205candidates,5OK/3blocked, not retested in this edition. There is no hidden background researcher after the response.
'''
text='\n'.join(prose(x) for x in text.splitlines())+'\n'
(R/'START-HERE.md').write_text(text);(R/'README.md').write_text(text)
old=(R/'research/Research-Status.md').read_text();(R/'research/Edition-13-Research-Status.md').write_text(old)
(R/'research/Research-Status.md').write_text(text+'\n## Historical status through Edition 13\n\n'+old)
save('research/edition-14-research-decisions.json',dict(new_notes=69,ap_notes=12,primary_limits='See data/source-access.json; selected reading not whole instruments',vision_july_verified=False,alternative_pages=118,alternative_coverage='25 June–24 July 2026',alternative_complete_review=False,corrections=['PM-KISAN exact3.15lakhcrore','Khelo2030–31','700MWfloatingonly','EC prospective quashing and existing EC caveats','CPI June reference/July publication','APdateandlocationcorrections','Quantum/younginfantdefinitioncorrections'],open=['Complete July Vision access/verification','Drishti full reconciliation and original statistical tables','AP original orders and bank/UIDAI circulars','Primary bilateral outcomes/visit-date reconciliation','August–November substantial backfill','All23monthlydaily source audits','Daily automation deployment']))
save('research/magazine-review/edition14-selected.json',dict(vision_july_verified=False,archive_checked=S['E14-ARCHIVE'][1],public_alternative=S['E14-DRISHTI'][1],pages=118,coverage='25 June–24 July2026',review='Selected passages only; exact limits in source-access',incorporated=[n['id'] for n in new if 'E14-DRISHTI' in n['sources']],withheld=['Vikram1 mission status without primary verification','Unverified national report ranks and counts','Helium ban original order','Full anti-doping protected-person definition','Complete appointments/awards/sports lists']))
p=R/'research/magazine-review/Integration-Report.md';p.write_text(p.read_text()+'\n\n## Edition14 · July2026\nVision archive checked first; no verified public July issue identified. Newest exposed31Julyreader is June editorial. Public alternative Drishti Saraansh July has118pages and25June–24Julycoverage; selected passages only. See edition14-selected.json and source-access for scope and corrections. Vision URL inventory unchanged; counts do not imply completeness.\n')
M=load('Package-Manifest.json');M.update(edition='14',notes=965,source_references=583,monthly_volumes=19,original_mcqs=570,original_mains_frameworks=152,notes_linked_to_journeys=linked,substantial_backfill_periods=4,july_2026_notes=69,july_2026_new_notes=69,july_2026_ap_notes=12,july_2026_priority_counts=dict(counts),july_vision_complete_issue_inventory=False,july_vision_issue_verified=False,july_alternative='Drishti118pages,25June–24July,selectedpassagesonly',qa='Pending Edition14 checks; counts are not factual/completeness certification.');M.pop('packaged_file_count',None);save('Package-Manifest.json',M)
print('Integrated',len(new),'notes;',linked,'linked notes; priorities',dict(counts))
