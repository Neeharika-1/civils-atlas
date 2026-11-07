import json,pathlib,collections,csv
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
N=load('data/notes.json');S=load('data/sources.json');J=load('data/linkages.json');D=load('research/magazine-review/vision-inventory.json');new=[n for n in N if n['id'].startswith('E13-')]
links={1:[4,5,6,7,8,9,10,11,12,13,14,15,46,49,55,56,61],2:[7],4:[6,8,13,21,22,23,24,25,26,27],5:[35,38,51],7:[59,61],8:[1,2,3,30,32,45,47,48,49,50,53,54,55,56,57,58,60],9:[2,9,10,11,16,17,18,19,20,42,44,45,57],10:[13,22,23,24,27,29,36,39,40,46,58],11:[20,28,29,30,31,34,52,61],12:[21,25,31,35,37,38,41,42,43,45,46,51,60],13:[3,9,10,11,14,15,19,31,35,36,38,40,49,51],14:[17,18,19,42,45,50],15:[31,35],17:[1,16,28,30,32,37,47,52,57,59],18:[2,3,9,10,11,16,17,18,19,20,33,34,36,41,44,50,54,57]}
for i,ks in links.items():J[i-1]['notes']=list(dict.fromkeys(J[i-1]['notes']+[f'E13-2606-{k:03}' for k in ks]))
for n in N:
 n['journeys']=[j['id'] for j in J if n['id'] in j['notes']]
 n['related_notes']=list(dict.fromkeys(n.get('related_notes',[])+[k for j in J if n['id'] in j['notes'] for k in j['notes'] if k!=n['id']]))
for p,v in [('data/notes.json',N),('data/linkages.json',J)]: (R/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
by={n['id']:n for n in N};paths=sum(bool(n['journeys']) for n in N)
lines=['# Civils Atlas · Cross-month reading journeys','','18 comparative paths across2025andJanuary–June2026. Reading order is not a single legal timeline; preserve vintages and legal stages.','']
for j in J:lines+=['## '+j['id']+' · '+j['title'],j['mechanism'],'']+['- **'+k+'** · '+by[k]['date'][:7]+' · '+by[k]['title'] for k in j['notes']]+['','**Avoid this shortcut:** '+j['caution'],'','**Mains synthesis:** '+j['prompt'],'']
(R/'volumes/Cross-Month-Reading-Journeys.md').write_text('\n'.join(lines)+'\n')
u=S['E13-VISION'][1]
D['2026-06']=dict(coverage_month='2026-06',web_posting_date='2026-07-31',entry_url=u,inventory_scope='Only one article exposed in public reader; not complete June issue inventory. Download requires authentication.',articles=[dict(title='Inter-States River Disputes',url=u,retrieval='Both public fetch chunks read',review='Substantive public article read; legal recommendations not treated as enactment',linked_notes=['E13-2606-001'],reconciliation='Incorporated with legal-stage cautions; underlying event/report date remains unresolved')])
(R/'research/magazine-review/vision-inventory.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
t=[]
for m,d in sorted(D.items()):
 for a in d['articles']:
  ks=[n['id'] for n in N if any(S[k][1]==a['url'] for k in n['sources'])]
  t.append([m,d['web_posting_date'],a['title'],a['url'],a.get('retrieval','Not recorded'),a.get('words',''),a.get('reconciliation','Unreconciled'),'; '.join(ks)])
with (R/'research/magazine-review/vision-reconciliation.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Coverage month','Web posting date','Title','Official URL','Retrieval status','Retrieved words','Editorial reconciliation','Linked notes']);w.writerows(t)
(R/'research/magazine-review/edition13-selected.json').write_text(json.dumps(dict(vision_public_urls=[u],vision_complete_issue_inventory=False,alternative_compilation=S['E13-DRISHTI'][1],alternative_coverage='25May–24June2026',selected_note_ids=[n['id'] for n in new if 'E13-DRISHTI'in n['sources']],not_incorporated=['NFHS6figures pending original fact sheet verification','Ramsar100thsite claim pending primary verification','precise2026themes/hosts/participationcounts','complete news-in-shorts and award/sports lists']),indent=2)+'\n')
# Preserve previous editorial guide as historical, then provide a current, concise entry point.
old=(R/'START-HERE.md').read_text();(R/'research/Edition-12-Coverage-Contract.md').write_text(old)
c=collections.Counter(n['subject'] for n in new);p=collections.Counter(n['priority'] for n in new)
guide=f'''# Civils Atlas · Edition 13

**UPSC × Andhra Pradesh APPSC · English · Research cut-off: 7 November 2026**

## Open and study
Open **index.html**. Study and practice now open **June 2026**. Download **volumes/June-2026-Study-Volume.pdf** or the editable **.docx**; Markdown and eight original Mains frameworks are beside them. The volume contains **62 June-indexed notes: 61 newly authored notes plus one inherited CETA seed**, **30 original MCQs with explanations** and **eight Mains frameworks**. The inherited CETA note has not been independently revalidated in this batch.

The working archive now has **{len(N)} notes / {len(S)} source-reference entries / 540 original MCQs / 144 Mains frameworks / 18 selected monthly volumes / 18 comparative reading paths linking {paths} notes**. Reference counts do not mean that many primary documents were fully read. **Study-Notes.docx** covers the whole working archive. Older months and year-specific practice remain available; previous edition ZIPs are preserved.

## June study map
- **Polity:** Tungabhadra/federal river governance, DISHA 2.0, FCRA compliance.
- **Economy:** new-base GDP, June MPC, external accounts, G-sec tax ordinance, foreign individual investment, financial mis-selling, digital-fraud liability and limited compensation, liquidation, ATF stabilisation, both June IIP milestones, mining adjudication and coal exchanges.
- **Agriculture/social:** draft AAY formula, mustard breeding, medical-device/drug consultations, ambulance systems, climate costs, prisons and language policy.
- **International relations:** France, Myanmar, Mauritius, Seychelles, Slovakia, Antarctic governance and logistics cooperation.
- **Environment/science/security/culture:** biochar, corals, watersheds, climate instruments, sand mining, species evidence, plantation outcomes, jet quenching, Bundibugyo surveillance, technology ecosystems, drones, infrastructure cyber-resilience, heritage, Yoga and V. V. S. Aiyar.
- **14 dedicated AP notes:** aviation policy; Polavaram canal packages; High Court external works; FiberNet guarantee; transplantation regulation; Quantum Valley land-related exemptions; Chittoor solar lease; Amaravati Eye PPP; Agri Gold court staffing; Union office and residential projects; rural-employment transition; beach-shack pilot; reorganisation anniversary. Most June Cabinet details rely on a fully inspected contemporary PTI report, not underlying GOs.

New-note priorities: **{p['P1']} P1 / {p['P2']} P2 / {p['P3']} P3**. Some topics are thematic magazine-indexed supplements, not separately verified June event dates. There is **no new exhaustive awards/sports/results list** in this batch; the subject gap remains visible.

## Magazine access: no invented completeness
The official Vision archive confirms **June 2026** at the **31 July 2026** posting. Its public reader exposes **one article**, which was read in both chunks. The archive’s full-PDF action requires sign-in; no access restrictions were bypassed. **One exposed URL is not a complete issue inventory.** Across all reviewed periods the registry now holds **760 discovered URLs / 228 linked URLs / 532 unincorporated URLs**; these are discovery counts, not coverage scores.

The alternative is Drishti’s public **128-page Saraansh June 2026**, expressly covering **25 May–24 June**. The contents and selected substantive passages were inspected, **not all 128 pages**. May overlap, unspecified event dates, questionable NFHS figures, changing species/Ramsar totals and theme/count claims remain separately flagged. No complete magazine PDF or extracted magazine text is redistributed. The notes and practice are original, referenced study aids.

## Independent checks and corrections
- PRS June review: all six chunks read. Selected primary evidence includes MoSPI GDP/IIP; RBI MPC minutes, BoP and conduct directions; the tax Ordinance; selected FEMA, IBBI and coal provisions; DFPD's complete draft; PIB DISHA/NAS/ATF; an official retrospective capital-project account; WHO and ATLAS. **data/source-access.json** records actual reading and limits.
- **MPC:** 3–5 June meeting; **5 June decision**, **19 June minutes**. GDP PE release **5 June**, real annual growth **7.7%**, real GVA **7.9%**, base **2022–23**. IIP actual new-series release **1 June**, PPI-based supersession **29 June**.
- **BoP:** Q4 surplus **US$7.1bn** does not erase the full-year **US$25.2bn deficit**. Net secondary income **+US$41.3bn**, net primary **−US$11.1bn**, gross personal transfers **US$43.5bn**; PRS's transfer shorthand is not repeated. Rounded components need not exactly sum.
- **RBI consumer directions:** issued in June, applicable from **1 January 2027**, not already operative in June. Suitability can fail despite consent. Fraud reporting uses **five calendar days from occurrence**. Small-fraud relief uses **gross loss≤₹50,000**, **min(85% net loss,₹25,000)**, reporting to both bank and1930/portal, **once in a lifetime**, and the **specified one-year loss window**. It is not blanket reimbursement.
- **Draft NFSA:** **7 kg/person, maximum35 kg/AAY household**. Three persons imply21 kg; seven persons remain capped at35 kg. Consultation is not enactment. The wrong PRS Food Safety Act footnote was excluded.
- **Legal dates:** the tax Ordinance is deemed effective1April. IBBI/coal signature, publication and website-upload dates are not interchangeable. FCRA's primary PDF failed retrieval; its details remain PRS-based. Medical/drug/mining drafts and later final dispositions are not certified.
- **AP:** Polavaram₹796/₹797crore difference is unresolved, so exact sanction recall is withheld. The transplantation framework began in **1994** and was amended in **2011**; the reported AP ordinance text is unread. A guarantee is not a grant, a bid invitation is not an award, land concessions are not a working quantum computer, capacity targets are not traffic, and July employment commencement is not June work delivered.
- **Capital:** office₹1,299.08crore and housing₹1,234.91crore are different10June approvals, inspected through a July official account. Each estimated seven lakh construction **man-days/year** is not seven lakh permanent jobs.
- **WHO:** June surveillance update differs from the **17 May PHEIC**; testing backlogs can increase reported cases without representing same-day infections. **ATLAS:** June2026 publication uses2025 collisions. Mutation breeding is not automatically risk-free; bleaching is not inevitable immediate coral death.
- Prior editions' substantive safeguards remain in their authoritative notes, source registry and historical coverage contracts; do not rerun old constructors over later edits.

## What remains unfinished
**Full January 2025–7 November 2026 coverage is NOT delivered.** July–November2026 comprises **five periods requiring substantial chronological backfill**. All **23 monthly source audits**, **253 subject-month cells** and **676-day daily reconciliation** remain open. Expanded monthly volumes are selected batches, not exhaustive coverage or current-law certification. Full Vision June access, earlier magazine omissions, original judgments, many statistical tables, AP GOs/DPRs and implementation audits remain pending.

## Daily discovery and reproducibility
The supplied06:30IST workflow remains **inactive on durable hosting**. The last recorded collector test is205 candidates/five responding/three blocked streams; no new collector test is claimed. Discovery does not automatically publish verified notes. The preview does not continue researching after this turn.

Install **requirements.txt** and optional **pymupdf**, then run `python scripts/validate.py && python scripts/reconcile.py && python scripts/build.py`. App regression uses `.qa/package.json` with jsdom24. Schema, export and pagination tests are integrity checks, **not independent factual/completeness certification**.
'''
# Explicit spacing only; keep paths and URLs untouched.
for a,b in [('1April','1 April'),('June2026','June 2026'),('2025 collisions','2025 collisions'),('10June','10 June'),('06:30IST','06:30 IST'),('June access','June access'),('maximum35','maximum 35'),('imply21','imply 21'),('at35','at 35'),('bank and1930','bank and 1930'),('July–November2026','July–November 2026'),('is205','is 205'),('24 June','24 June')]:guide=guide.replace(a,b)
(R/'START-HERE.md').write_text(guide);(R/'README.md').write_text(guide);(R/'research/Research-Status.md').write_text(guide.replace('# Civils Atlas · Edition 13','# Research status · Edition 13')+'\n## Next chronological work\nJuly 2026: locate the public official magazine, then independent national/AP primary evidence; continue omissions and daily-source audits. No unattended background research is running.\n')
(R/'research/magazine-review/Integration-Report.md').write_text('# Magazine integration · Edition 13\n\n'+guide[guide.index('## Magazine access'):guide.index('## Independent checks')])
# Default controls and structural checks.
p=R/'template.html';s=p.read_text().replace('Research edition 12','Research edition 13').replace('January–May 2026 now blend','January–June 2026 now blend').replace("$('#month').value='2026-05';render()","$('#month').value='2026-06';render()").replace("$('#practiceMonth').value='2026-05';practice()","$('#practiceMonth').value='2026-06';practice()").replace('New: May 2026','May 2026')
s=s.replace('<div class="jumpbar">','<div class="jumpbar"><button data-month="2026-06">New: June 2026 · 62 notes</button>',1);p.write_text(s)
for name in ['build.py','check_exports.py','check_question_pagination.py']:
 p=R/'scripts'/name;s=p.read_text().replace('EDITION 12','EDITION 13').replace('edition-12-','edition-13-');p.write_text(s)
p=R/'scripts/validate.py';p.write_text(p.read_text().replace("'E11-','E12-'","'E11-','E12-','E13-'"))
p=R/'scripts/reconcile.py';s=p.read_text().replace("'2026-04','2026-05'}","'2026-04','2026-05','2026-06'}").replace('6 need substantial chronological backfill.','5 need substantial chronological backfill.')
s=s.replace("('Full substantive synthesis read' if m<'2025-06'", "('Full substantive synthesis read' if m<'2025-06' or m=='2026-06'")
s=s.replace("('Synthesis read; independent primary checks remain' if m<'2025-06'", "('Synthesis read; independent primary checks remain' if m<'2025-06' or m=='2026-06'")
p.write_text(s)
p=R/'.qa/check.cjs';s=p.read_text().replace("['2026-05',64]]","['2026-05',64],['2026-06',62]]").replace("length===64,'May 2026 initial'","length===62,'June 2026 initial'").replace('length===835','length===896').replace('notes:835','notes:896').replace('expanded_months:17,quizzes:17','expanded_months:18,quizzes:18').replace('edition-12-app-checks','edition-13-app-checks').replace('17 month filters/quizzes; 835 archive','18 month filters/quizzes; 896 archive')
s=s.replace("assert(errors.length===0,errors.join('\\n'));console.log('PASS: 18", "d.querySelector('[data-month=\"2026-06\"]').click();assert(d.querySelectorAll('details.note').length===62,'June quick');input('#exam','ap');assert(d.querySelector('#E13-2606-049'),'June guarantee');assert(d.querySelector('#E13-2606-060'),'June reorganisation');input('#exam','all');d.querySelector('#practiceMonth').value='2026-06';d.querySelector('#practiceMonth').dispatchEvent(new dom.window.Event('change'));assert(d.querySelector('#quiz').textContent.includes('JUN26-01'),'June practice');assert(d.querySelector('#volumeLinks').textContent.includes('June 2026'),'June documents');assert(errors.length===0,errors.join('\\n'));console.log('PASS: 18")
p.write_text(s)
# Do not retain a copied magazine body in the delivered package.
p=R/'research/edition13/drishti-june-extract.txt'
if p.exists():p.unlink()
print('Edition13 integrated:',len(N),'notes;',len(S),'references;',paths,'linked notes;',len(t),'discovered Vision URLs')
