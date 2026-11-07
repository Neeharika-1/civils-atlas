import pathlib,json,csv,collections
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
N=load('data/notes.json');S=load('data/sources.json');J=load('data/linkages.json');D=load('research/magazine-review/vision-inventory.json');by={n['id']:n for n in N}
links={1:['E7-2511-001','E7-2512-001','E7-2512-002'],4:['CA-035','E7-2511-011','E7-2511-012','E7-2512-021','E7-2512-022'],7:['E7-2511-009'],8:['E7-2512-028','E7-2512-031','E7-2512-035'],10:['E7-2511-028'],11:['E7-2511-019','E7-2511-022','E7-2512-005','E7-2512-008','E7-2512-009'],12:['E7-2511-023','E7-2511-024','E7-2512-018','E7-2512-019','E7-2512-025'],13:['E7-2511-006','E7-2511-007','E7-2511-026','E7-2512-027','E7-2512-033'],14:['E7-2512-029','E7-2512-032'],17:['E7-2511-016','E7-2511-027','E7-2512-030','E7-2512-036'],18:['E7-2511-003','E7-2511-004','E7-2512-011','E7-2512-014','E7-2512-024']}
for i,ks in links.items():
 j=J[i-1];j['notes']=list(dict.fromkeys(j['notes']+ks));j['caution']=j['caution'].replace('September/October entries','Later 2025 entries')
for n in N:
 n['journeys']=[j['id'] for j in J if n['id'] in j['notes']];n['related_notes']=list(dict.fromkeys(k for j in J if n['id'] in j['notes'] for k in j['notes'] if k!=n['id']))
# Explicit correction trails beyond the broad thematic paths.
for earlier,later in [('E6-2509-001','E7-2512-002'),('E6-2509-008','E7-2511-003'),('E6-2509-008','E7-2512-023')]:
 for a,b in [(earlier,later),(later,earlier)]:by[a]['related_notes']=list(dict.fromkeys(by[a]['related_notes']+[b]))
for title,ref in [('assent','E7-2511-013'),('retrospective','E7-2511-015')]:
 for n in N:
  if n['date']<'2025-11' and title in n['title'].lower():
   for a,b in [(n['id'],ref),(ref,n['id'])]:by[a]['related_notes']=list(dict.fromkeys(by[a]['related_notes']+[b]))
for p,v in [('data/notes.json',N),('data/linkages.json',J)]: (R/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
lines=['# Civils Atlas · Cross-month reading journeys','','18 original comparative paths. Reading order is editorial, not necessarily one legal timeline. Date/status checks remain essential.','']
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
p=R/'template.html';s=p.read_text().replace('Research edition 06','Research edition 07').replace('January–October','January–December').replace("$('#month').value='2025-06';render()","$('#month').value='2025-11';render()")
s=s.replace('<div class="jumpbar">','<div class="jumpbar"><button data-month="2025-11">New: November 2025 · 30 notes</button><button data-month="2025-12">December 2025 · 44 notes</button>').replace('New: September','September').replace('New: June','June');p.write_text(s)
p=R/'scripts/build.py';p.write_text(p.read_text().replace('EDITION 06','EDITION 07'))
p=R/'scripts/reconcile.py';s=p.read_text().replace("'2025-09','2025-10'}","'2025-09','2025-10','2025-11','2025-12'}").replace('13 need substantial','11 need substantial');p.write_text(s)
p=R/'scripts/check_exports.py';p.write_text(p.read_text().replace('range(1,11)','range(1,13)').replace('edition-06-document','edition-07-document'))
p=R/'scripts/validate.py';p.write_text(p.read_text().replace("n['id'].startswith('E6-')","n['id'].startswith(('E6-','E7-'))"))
c=collections.Counter(n['date'][:7] for n in N);mag=sum(bool(x[-1]) for x in t);total=len(t);paths=sum(bool(n['journeys']) for n in N)
table='| Month | Notes | MCQs | Mains plans |\n|---|---:|---:|---:|\n'+'\n'.join(f'| 2025-{i:02} | {c[f"2025-{i:02}"]} | 30 | 8 |' for i in range(1,13))
guide=f'''# Civils Atlas · Edition 07

UPSC × Andhra Pradesh APPSC · English · Updated / archive cut-off: **7 November 2026**

## Open and study
Open **index.html**. The initial study view now opens **November 2025**. New November/December quick buttons and the month selector reach all working notes. **Monthly practice** has a separate selector and document links. Twelve selected monthly PDF/DOCX/Markdown volumes, January–December 2025, are in **volumes/**. **Study-Notes.docx** contains the full working archive. The 18 cross-month reading journeys now connect {paths} notes; they are comparative guidance, not necessarily one legal timeline.

**{len(N)} notes / {len(S)} source-reference entries / 360 original MCQs / 96 original Mains frameworks.** 583 notes are in 2025; 9 inherited 2026 seeds do not substitute for 2026 coverage. Sources are reference entries, not fully reviewed primary-document counts.

{table}

## New substance
**65 net new notes plus one enriched seed: November 30 substantial notes, December 36 new notes plus 8 retained seeds**, with 60 new MCQs and 16 tailored Mains plans. These are original study aids, not previous-year questions or official/predicted answers.

November adds GDP, QCOs, Labour Code commencement, EPF regularisation, DPDP phase-in, export support, rare-earth magnets, governor assent, tribunal independence, retrospective EC, seed rights/quality, G20/COP30, One Health/AMR, Birsa Munda and neuroethics. AP coverage includes the CII summit’s proposed investment and MSME-park geography.

December adds monetary/external accounts, nuclear reform/liability, hydrocarbon rules, VPPAs, solar/electrification audit, rural-employment redesign, land safeguards, insurance/securities/IBC scrutiny, education, Russia/Oman/NZ trade, labour drafts, platform social protection, skilling audit, groundwater/local DRR, living heritage and digital/workplace rights. AP coverage includes final district-reorganisation reporting and Rayalaseema horticulture funding requests.

## Evidence and magazine contract
Public official Vision IAS November/December editions supply breadth. **16 selected article bodies were retrieved; lead/substantive passages were inspected and integrated, not complete articles/issues certified.** Inventory now {total} URLs across twelve months; {mag} link to notes and {total-mag} remain unincorporated. No magazine bodies or gated PDFs are redistributed. Coverage month differs from posting/event dates (November issue posted 23 December; December issue posted 28 January 2026).

Independent evidence: PRS substantive sections, primary PIB labour/export/magnet/NZ announcements, UNESCO’s official Deepavali profile, UNU-EHS COP30 analysis and substantive AP news bodies. Actual access scope is registered in **data/source-access.json**. Many linked primary legal instruments, committee reports and official GOs remain independently unread.

## Important chronology and corrections
- Labour Codes were made effective in November; December draft rules are a separate implementation stage. Neither announcement proves every benefit was delivered.
- DPDP Rules have staggered commencement; not every processing obligation began immediately.
- December’s Q1 current-account comparator revises September’s initial estimate. Both retain their release vintage and are cross-linked.
- November’s assent opinion and environmental-clearance review qualify earlier 2025 positions. Do not read an earlier historical note as an unchanged present legal rule.
- The primary NZ conclusion release is dated **22 December**. Its 70% Indian tariff-line liberalisation measure differs from about 95% trade coverage; the PRS reference date/summary wording must not be copied uncritically. Conclusion is not entry into force.
- AP’s final reported arrangement adds **Markapuram and Polavaram**, total **28**, effective 31 December. Madanapalle becomes Annamayya headquarters, not an assumed third extra district. Gazette boundary schedules still need primary review.
- Summit MoUs/job forecasts, 175 MSME parks, rare-earth capacity and the requested Rayalaseema package are not already delivered outcomes.
- PESA’s 1996–2025 and PPV&FR’s 2001–2025 anniversary arithmetic is not repeated as completed thirty/twenty-five years. Groundwater extraction stage uses extractable resources, not total recharge.

## Still unfinished
**Full January 2025–7 November 2026 coverage is NOT delivered.** January–November 2026 spans eleven periods needing substantial chronological backfill. All **23 monthly audits** and the **676-day daily-source reconciliation** remain open. Twelve expanded 2025 volumes are selective, not complete magazine/newspaper/PIB coverage. Shorts/maps, primary texts, culture/sport miscellany, exact APPSC paper mapping, district GOs and daily two-paper reconciliation remain uneven.

## Daily updating and rebuilding
The 06:30 IST workflow is provided, **not activated on durable hosting**. Discovery creates unreviewed links, not publishable facts. The last recorded test remains 205 candidates, five responding streams and three blocked streams; no new collection run is claimed. A browser preview is not an autonomous researcher.

Install requirements, then run `python scripts/validate.py && python scripts/reconcile.py && python scripts/build.py`. Delivered JSON is authoritative. Historical constructors can overwrite edits and are not automatic updaters. Checks verify structural/rendering integrity, not independent factual or completeness certification.
'''
(R/'START-HERE.md').write_text(guide)
p=R/'README.md';old=p.read_text();keep=old[old.index('## Daily automation'):] if '## Daily automation' in old else '';p.write_text(guide+'\n'+keep)
(R/'research/Research-Status.md').write_text(guide.replace('# Civils Atlas · Edition 07','# Research status · Edition 07')+'''
## Specific source limits
PRS November chunks 0–4 and December 0–6 inspected; tails and all linked primary texts not certified read. PIB labour chunk 0 of 5; export and magnet full substantive announcements in chunk 0; NZ chunk 0 of 3; UNESCO inscription/profile chunk 0; UNU substantive analysis chunk 0. AP summit and district full substantive news bodies read; horticulture primary memorandum, official district gazette schedules and final project permissions pending. Vision bodies retrieved with selected passages inspected, not whole-issue review.

## Next chronological work
January 2026, then each subsequent month through 7 November, while closing primary-text and daily-source gaps in the twelve selected 2025 volumes. Earlier edition QA reports are historical, not new certification. No background completion or activated scheduler is implied.
''')
(R/'research/magazine-review/Integration-Report.md').write_text(f'''# Official public Vision IAS integration · Edition 07

Updated 7 November 2026. Original summaries, not reproductions. January–December 2025 inventory: {total} URLs, {mag} linked to authored notes, {total-mag} unincorporated. This is not a completeness percentage: an article can contain unincorporated topics and a short page can contain many items.

November/December add 16 selected article integrations (8 each). Retrieved bodies were inspected selectively, not fully reviewed or redistributed. Coverage/posting chronology is explicit: November posted 23 December; December posted 28 January 2026. World Inequality Report 2026 and other unselected links remain inventory leads, not authored evidence.

Independent PRS, PIB, UNESCO, UNU and AP news checks qualify magazine assertions. Unsupported anniversary shorthand, groundwater denominator ambiguity, overbroad benefit claims and proposal-versus-delivery confusion are excluded or corrected. See ../Research-Status.md and the source-access registry for actual scope.

{table}

All daily source audits remain open. The reconciliation CSV records untouched shorts/maps and pending URLs; a link to a note is not certification of a complete article or issue.
''')
print('Integrated',len(N),'notes;',mag,'/',total,'magazine URLs linked;',paths,'notes in paths')
