import json,pathlib,csv,collections,re
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
N=load('data/notes.json');S=load('data/sources.json');J=load('data/linkages.json');D=load('research/magazine-review/vision-inventory.json');by={n['id']:n for n in N}
# Extend existing thematic paths rather than invent legal continuity.
links={1:['E6-2510-001','E6-2510-002'],4:['E6-2509-019','E6-2509-020','E6-2510-020','E6-2510-022'],5:['E6-2510-029'],7:['E6-2509-018','E6-2510-015'],9:['E6-2509-027'],10:['E6-2509-010','E6-2509-025','E6-2510-028'],11:['E6-2509-013','E6-2509-014','E6-2510-008','E6-2510-017'],12:['E6-2509-023','E6-2510-027','E6-2510-033'],13:['E6-2509-011','E6-2509-012','E6-2510-013','E6-2510-014','E6-2510-023'],17:['E6-2510-009','E6-2510-010','E6-2510-011'],18:['E6-2509-003','E6-2509-031','E6-2509-032']}
for i,ks in links.items():
 j=J[i-1];j['notes']=list(dict.fromkeys(j['notes']+ks))
 j['caution']+=' September/October entries are historical snapshots; comparisons do not establish one legal programme.' if 'September/October' not in j['caution'] else ''
for n in N:
 n['journeys']=[j['id'] for j in J if n['id'] in j['notes']];n['related_notes']=list(dict.fromkeys(k for j in J if n['id'] in j['notes'] for k in j['notes'] if k!=n['id']))
for p,v in [('data/notes.json',N),('data/linkages.json',J)]: (R/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
lines=['# Civils Atlas · Cross-month reading journeys','','18 original comparative reading paths. Editorial order is not necessarily a legal timeline. Current status requires separate checking.','']
for j in J:
 lines+=['## '+j['id']+' · '+j['title'],j['mechanism'],'']+['- **'+k+'** · '+by[k]['date'][:7]+' · '+by[k]['title'] for k in j['notes']]+['','**Avoid this shortcut:** '+j['caution'],'','**Mains synthesis:** '+j['prompt'],'']
(R/'volumes/Cross-Month-Reading-Journeys.md').write_text('\n'.join(lines))
t=[]
for m,d in sorted(D.items()):
 for a in d['articles']:
  linked=[n['id'] for n in N if any(S[k][1]==a['url'] for k in n['sources'])];a['linked_notes']=linked;a['reconciliation']='Selected passages used; full-topic/primary audit open' if linked else 'Not incorporated; substantive reconciliation pending'
  if linked:a['review']='Selected passages incorporated into original notes; not complete article/issue review'
  t.append([m,d['web_posting_date'],a['title'],a['url'],a.get('retrieval','Not recorded'),a.get('words',''),a['reconciliation'],'; '.join(linked)])
(R/'research/magazine-review/vision-inventory.json').write_text(json.dumps(D,ensure_ascii=False,indent=2))
with (R/'research/magazine-review/vision-reconciliation.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Coverage month','Web posting date','Title','Official URL','Retrieval status','Retrieved words','Editorial reconciliation','Linked notes']);w.writerows(t)
# The renderer already discovers every monthly MCQ file dynamically.
p=R/'template.html';s=p.read_text().replace('Research edition 05','Research edition 06').replace('January–August','January–October')
s=s.replace('<div class="jumpbar">','<div class="jumpbar"><button data-month="2025-09">New: September 2025 · 32 new notes</button><button data-month="2025-10">October 2025 · 33 new notes</button>')
# Keep June’s initial state to preserve saved usage; new buttons make additions explicit.
p.write_text(s)
p=R/'scripts/build.py';p.write_text(p.read_text().replace('EDITION 05','EDITION 06'))
p=R/'scripts/reconcile.py';s=p.read_text().replace("'2025-07','2025-08'}","'2025-07','2025-08','2025-09','2025-10'}").replace('15 need substantial','13 need substantial');p.write_text(s)
p=R/'scripts/check_exports.py';s=p.read_text().replace('range(1,9)','range(1,11)').replace('archive_notes=462','archive_notes=len(N)').replace('edition-05-document','edition-06-document');p.write_text(s)
# Complete guides reflect actual data, not inventory-count claims.
c=collections.Counter(n['date'][:7] for n in N);linked=sum(bool(a['linked_notes']) for d in D.values() for a in d['articles']);total=sum(len(d['articles']) for d in D.values());counttable='| Month | Indexed notes | Original MCQs | Frameworks |\n|---|---:|---:|---:|\n'+'\n'.join(f'| 2025-{i:02} | {c[f"2025-{i:02}"]} | 30 | 8 |' for i in range(1,11))
guide=f'''# Civils Atlas · Edition 06

UPSC × Andhra Pradesh APPSC · English · Updated 7 November 2026

Open **index.html** for the offline study library. September/October quick buttons open the new material. The initial June view is retained; the month selector reaches the complete working archive. Monthly practice has a separate selector and PDF/Word links.

## What is included
**{len(N)} study notes / {len(S)} source-reference entries / 300 original MCQs / 80 original Mains frameworks.** Ten selected monthly volumes, January–October 2025, are in **volumes/** as PDF, editable DOCX and Markdown. **Study-Notes.docx** contains the full working archive. The 18 reading journeys now connect {sum(bool(n['journeys']) for n in N)} notes and include the new research.

{counttable}

## This continuation: 65 new notes
September: 32 additions on GST, finance, courts/electoral identity, labour/drones/telecom, shipping, energy, medical education, minerals, social reform and AP health/medical PPPs. October: 33 additions on monetary policy, agriculture, energy/carbon rules, digital governance, prisons, trade, factory statistics, hunger, biosphere geography, Nobel discoveries and AP AI investment/cyclone risk.

60 new original questions and 16 original answer plans accompany the notes. These are study aids, not official previous-year questions or predicted papers. Some inherited later seeds remain in the month counts and have not been represented as new research.

## Magazine breadth with independent checks
18 selected public official Vision IAS September/October article bodies were retrieved; selected passages, not complete issues, were inspected and integrated into original notes. Total inventory: {total} URLs, {linked} linked to notes, {total-linked} unincorporated. A URL count is not a topic-completeness percentage. Primary/independent evidence includes PRS substantive review sections, PIB’s GST announcement, Google’s original release, UNESCO’s profile and Nobel’s official aggregate. Source access is separately labelled; article bodies are not redistributed.

Corrections preserve the GST tobacco transition exceptions; identify the designated Cold Desert reserve in Himachal Pradesh; distinguish TEPA effectiveness from investment realised; record Google’s USD 15 billion as a proposed 2026–30 investment, not a commissioned hub; and separate Montha landfall-start reporting from final audited losses. AP insurance limits are not universalised from conflicting secondary accounts. Narayana Guru’s unsupported 2025 death-centenary claim is omitted. Biofoundry’s August launch and fisheries agreement’s September entry remain explicit despite later magazine coverage.

## Still unfinished
**The full January 2025–7 November 2026 archive is NOT complete.** November 2025–November 2026 spans 13 periods needing substantial backfill. All 23 monthly daily-source audits remain open, including the ten expanded months. Magazine shorts/maps, primary legal texts, district-level AP GOs, newspaper/PIB day-by-day reconciliation and exact APPSC paper mapping remain uneven. Counts are not completeness certificates.

**Daily updating is supplied, not activated.** The workflow needs an enabled durable hosting repository or always-on machine. Discovery creates unreviewed candidates, not publishable facts. The latest recorded collector test has 205 candidates, five responding streams and three blocked streams; it was not rerun for this edition. No access-control bypass or hidden background research is claimed.

## Rebuild
Install requirements, then run `python scripts/validate.py && python scripts/reconcile.py && python scripts/build.py`. The JSON dataset is authoritative. Historical authoring/report constructors can overwrite edits: do not rerun them as updaters. QA checks structural/rendering integrity, not independent factual or completeness certification.
'''
(R/'START-HERE.md').write_text(guide)
p=R/'README.md';old=p.read_text();keep=old[old.index('## Daily automation'):] if '## Daily automation' in old else '';p.write_text(guide+'\n'+keep)
(R/'research/Research-Status.md').write_text(guide.replace('# Civils Atlas · Edition 06','# Research status · Edition 06')+'''
## Evidence boundaries and review queue
- PRS September chunks 0–3 and October chunks 0–6 were inspected, not all linked primary PDFs or reference tails.
- PIB GST: substantive announcement chunk inspected, not all annexures. Category-specific notifications remain essential.
- Google’s full issuer release was read; investment and commissioned economic projections are issuer claims, not measured results.
- UNESCO Cold Desert and both chunks of Nobel’s official aggregate were read. Individual Nobel summary pages were blocked; the accessible official aggregate supplies the direct evidence.
- AP September Cabinet and Montha evidence used substantive search excerpts, not final official GOs/IMD reports. Coverage limits, final wind and losses remain unverified and are not invented.
- Vision selected passages support breadth, not complete issue review. Moral-integrity inspection was limited to the lead. Verify detailed legal/historical claims against primary texts before high-stakes use.
- Existing edition05 correction/provenance records and dated QA are historical evidence, not fresh certification of this edition.

## Next chronological work
November 2025 first; then December 2025 and each 2026 month through 7 November. In parallel close source-specific gaps in already-expanded months rather than increasing counts alone. No scheduler or automatic factual-publication process was activated here.
''')
(R/'research/magazine-review/Integration-Report.md').write_text(f'''# Official public Vision IAS integration · Edition 06

Updated 7 November 2026. Original summaries and analytical guidance, not reproductions. {total} official inventory URLs across January–October; {linked} link to authored notes and {total-linked} remain unincorporated. Not a completeness percentage.

The September/October pass adds 18 selected article integrations (10 + 8). Retrieved bodies were inspected selectively, not fully reviewed or redistributed. Independent PRS/PIB/Google/UNESCO/Nobel evidence checks chronology, geography and announcement-versus-delivery claims. See ../Research-Status.md and data/source-access.json for actual access scopes and unresolved primary checks.

Coverage month, posting date and event date are distinct. Biofoundry launched in August despite September coverage; WTO fisheries entry was in September despite October coverage. Source reconciliation CSV records every inventoried URL, including untouched shorts/maps and pending items.

{counttable}

All monthly daily-source audits remain open. A linked article can contain many unincorporated topics; multiple references can inform one note. Do not equate a linked URL with a completely reviewed article or magazine.
''')
print('Integrated sources, paths, renderer and current guides:',len(N),'notes;',linked,'/',total,'magazine URLs linked')
