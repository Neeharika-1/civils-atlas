import pathlib,json,csv,re,collections
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
N=load('data/notes.json');S=load('data/sources.json');J=load('data/linkages.json');D=load('research/magazine-review/vision-inventory.json');by={n['id']:n for n in N};aliases=load('research/edition-09-id-map.json')
def ref(i):return aliases['E9-2602-'+str(i).zfill(3)]
links={1:[1,2,3,4,5,12,13,14,41],3:[9,30],4:[15,16,20,21,22,32],5:[7,18,26,27],6:[17,18,30,31,33],7:[21,27,28,45],8:[9,10,23,30,39,40,41,44],9:[31,42,43],10:[19,25,28,35],11:[11,37,45],12:[6,7,8,18,24,25,32,43],13:[26,27,34,35],14:[38],15:[11,36],17:[28,31,33,45],18:[29,31,42]}
for i,ks in links.items():J[i-1]['notes']=list(dict.fromkeys(J[i-1]['notes']+[ref(k) for k in ks]))
for n in N:
 n['journeys']=[j['id'] for j in J if n['id'] in j['notes']];n['related_notes']=list(dict.fromkeys(n.get('related_notes',[])+[k for j in J if n['id'] in j['notes'] for k in j['notes'] if k!=n['id']]))
for p,v in [('data/notes.json',N),('data/linkages.json',J)]: (R/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
lines=['# Civils Atlas · Cross-month reading journeys','','18 original comparative paths across2025 and January–February2026. Reading order is not necessarily a legal timeline. Preserve dates,revisions and status.','']
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
p=R/'template.html';s=p.read_text().replace('Research edition 08','Research edition 09').replace('January–December 2025 and January 2026 now blend','January–December 2025 and January–February 2026 now blend').replace("$('#month').value='2026-01';render()","$('#month').value='2026-02';render()").replace("$('#practiceMonth').value='2026-01';practice()","$('#practiceMonth').value='2026-02';practice()")
s=s.replace('<div class="jumpbar">','<div class="jumpbar"><button data-month="2026-02">New: February 2026 · 45 notes</button>',1).replace('New: January 2026','January 2026');p.write_text(s)
c=collections.Counter(n['date'][:7] for n in N);mag=sum(bool(x[-1]) for x in t);total=len(t);paths=sum(bool(n['journeys']) for n in N);months=sorted(D)
table='| Expanded period | Indexed notes | Original MCQs | Mains plans |\n|---|---:|---:|---:|\n'+'\n'.join(f'| {m} | {c[m]} | 30 | 8 |' for m in months)
guide=f'''# Civils Atlas · Edition 09

UPSC × Andhra Pradesh APPSC · English · Archive cut-off: **7 November 2026**

## Open and study
Open **index.html**. Study and practice initially open **February 2026**. Fourteen selected monthly volumes in **volumes/** contain PDF,editable Word and Markdown notes,questions/explanations and original Mains frameworks. January2025/January2026 and February2025/February2026 retain separate practice files and document links. **Study-Notes.docx** contains the whole working archive. Eighteen reading journeys now connect {paths} notes; reading order is not a single legal timeline.

**{len(N)} notes / {len(S)} source-reference entries / 420 original MCQs / 112 original Mains frameworks.** This comprises583 notes indexed to2025,45 toJanuary2026,45 toFebruary2026 and two later inherited seeds. Source-reference counts are not fully read primary-document counts. These are original study aids,not official questions or exam predictions.

{table}

## February continuation
**45 substantial February notes:38 newly added and seven inherited seeds rewritten/enriched under stable IDs.** Thirty new original MCQs and eight tailored Mains plans. Breadth: Union Budget,biopharma,semiconductors,MSMEs,GDP/CPI rebasing,monetary policy,Finance Commission,credit derivatives,trust finance,capital-market exposure,US/GCC trade,France/Brazil/Malaysia,startup funds/recognition,defence approvals,urban finance,labour transition,safety,AI summit/Pax Silica,offshore minerals,road-trauma care,rural decentralisation,SHGs,textiles,grain storage,counter-terrorism,border technology,LIGO,CCUS and retrospective dowry-law context.

AP material covers the total/net Budget perimeter,capital-outlay reconciliation,fiscal targets/receipt assumptions,welfare allocations,weaver power proposals,wealth-fund/guarantee risks and proposed rare-earth corridors. AP application also appears in national notes. Exact APPSC paper mapping and full state-GO reconciliation remain unfinished.

## Evidence contract
Public official Vision IAS February2026 web edition:posted **31March2026**. Thirty-eight URLs inventoried;twelve selected public bodies retrieved and lead/substantive passages inspected,not a complete article/issue review. Across fourteen editions:{total} URLs,{mag} linked,{total-mag} unincorporated. No magazine bodies or gated PDFs redistributed. A coverage month is an editorial index,not an event/publication date.

Independent February work:PRS policy PDF chunks0–4;AP Budget analysis chunks0–2;Union Budget speech chunks0–1;MoSPI GDP press-note opening;CPI release opening/substantive national results;**both chunks/full Finance Commission action-taken memorandum**;PIB startup-recognition,US-framework and PM RAHAT substantive releases. AP official AFS was read selectively:opening tables and PDF pages28,31,37,38,47,48. A contemporary newspaper search extract supplied corroboration,not a full article read. Access and failures are recorded in **data/source-access.json**. These are selective independent checks,not all linked primary documents.

## Corrections and essential distinctions
- **AP capital headline:**the official AFS shows about₹48,697.71crore capital outlay plus₹5,217.67crore loans/advances=₹53,915.38crore. Do not call the broader headline solely direct outlay. The tables are in lakhs; crore conversions were checked. Total expenditure₹3,32,205crore includes principal repayment; net expenditure is about₹3,10,058crore.
- **Finance Commission:**41% applies to net divisible taxes,not gross Union receipts. The Centre accepted devolution/local grants but not every reform recommendation outright. The primary memorandum gives₹7,91,493crore local-body grants and₹2,04,401crore state disaster-fund corpus,the latter including a state share; do not add the whole corpus as if all were Union grants.
- **GDP:**January7.4% is an old-series first advance estimate;February7.6% a new2022–23-base second advance estimate. Neither is a final outturn. Double deflation applies to specified sectors,not identically all sectors. Budget-day deficit ratios predate the rebase.
- **CPI:**12February’s release concerns January data,with provisional combined inflation2.75%;later final values need separate dated treatment. The February-data CPI release belongs in March. The January-volume CPI article remains explicitly labelled later context.
- **US trade:**7February’s18% framework statement is not a universal permanent month-end/current tariff schedule. PRS records subsequent US legal/tariff developments; the underlying judgment and new operative product schedules were not independently read here.
- Draft REIT/InvIT or credit-derivative proposals are not automatically final law;CME directions’ reviewed commencement is1April. A defence proposal is not delivered equipment;a grant corpus is not money already spent.
- **Magazine restraint:**no mandatory identical three-tier municipal hierarchy,no automatically established border-technology oversight authority,no guarantee every SHG member receives₹1lakh cash,no claim LIGO-India was operational from a construction contract. The dowry article cites a2025 case;it is a retrospective supplement,not an invented February2026 judgment.

## Still unfinished
**Full January2025–7November2026 coverage is NOT delivered.** March–November2026 spans nine periods needing substantial backfill. All23 monthly audits and the676-day source-by-source daily reconciliation remain open. Expanded does not mean exhaustive or fact-certified. February culture/sport/shorts/maps,most Gazette texts,court orders,bilateral annexes and AP operative GOs remain uneven or unread. Zero-subject cells remain visible instead of being padded with generic content.

## Daily updating and rebuild
The supplied06:30IST workflow is **not activated on durable hosting**. The last recorded collector test remains205 candidates,five responding and three blocked streams;no new live-collector test is claimed. Candidate discovery is not verified publication,and the preview does not research after a turn ends.

Install dependencies and run `python scripts/validate.py && python scripts/reconcile.py && python scripts/build.py`. JSON is authoritative;historical authoring scripts can overwrite later edits. The builder recognises year-specific **data/2026-02-mcqs.json** alongside legacy2025 names. Structural/app/export checks are not independent factual or completeness certification.
'''
# Keep typography readable around delimiters without touching numeric comma groups.
guide=re.sub(r',(?=[A-Za-z₹])',', ',guide);guide=re.sub(r';(?=[A-Za-z₹])','; ',guide);guide=re.sub(r'(?<=\d)(crore|lakh|notes|periods|years)',r' \1',guide)
(R/'START-HERE.md').write_text(guide);p=R/'README.md';old=p.read_text();keep=old[old.index('## Daily automation'):] if '## Daily automation' in old else '';p.write_text(guide+'\n'+keep)
(R/'research/Research-Status.md').write_text(guide.replace('# Civils Atlas · Edition 09','# Research status · Edition 09')+'''
## Primary-check queue / next chronological work
March2026 is next. Read final REIT/InvIT/CME amendments for current compliance,US post-judgment tariff instruments,the primary PRAHAAR text,defence contracting documents,the LIGO contract and the dowry judgment before treating detailed magazine statements as independently verified. State Budget publication is not evidence every proposal was operative;weaver benefits need implementation GOs. The official AP portal contains other summary figures whose vintage was not reconciled;the authored numerical reconciliation uses the actual2026–27 AFS columns,not the landing-page graphics. PRS AP’s earlier national-GDP comparison is not reused as the rebased national growth figure.
''')
(R/'research/magazine-review/Integration-Report.md').write_text(f'''# Public official Vision IAS integration · Edition09

Updated7November2026. Fourteen coverage months:January–December2025 plusJanuary–February2026. {total} URLs;{mag} linked,{total-mag} unincorporated. Not whole-issue review or a completeness measure.

February2026 adds twelve selected article integrations,posted31March2026. Bodies were retrieved;lead/substantive passages were inspected. Source references do not imply independent reading of every linked statute,order or annexure.

Independent corrections:use the Finance Ministry’s actual local-grant amount and Union-versus-state disaster contribution,not rounded magazine components that can be double-counted. Avoid copying a mandatory three-tier municipal claim or describing an author’s proposed border oversight body as officially created. CCUS is not the only decarbonisation option and utilisation is not necessarily permanent storage. Dowry-law context references a2025 case;no February judgment date is invented. No crime totals or purported mandatory arrest directions are reproduced from this secondary lead.

{table}

Open daily audits,unreviewed shorts/maps and incomplete AP/legal-primary checks remain recorded in the CSV and Research-Status.md. No original magazine bodies redistributed.
''')
print('Integrated',len(N),'notes;',paths,'in18journeys;',mag,'/',total,'magazine URLs linked')
