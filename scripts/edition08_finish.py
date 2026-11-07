import pathlib,json,csv,re,collections,datetime
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
N=load('data/notes.json');S=load('data/sources.json');J=load('data/linkages.json');D=load('research/magazine-review/vision-inventory.json');by={n['id']:n for n in N}
links={1:[2,3,4,33],4:[6,7,8,9,32,38],7:[14,15],8:[28,31,39,40],10:[39],11:[17,18,19,20,21,22,44],12:[11,12,35,41,42],13:[29,37],14:[11,12,37],15:[34,45],16:[26,27],17:[13,44],18:[24,25]}
for i,ks in links.items():J[i-1]['notes']=list(dict.fromkeys(J[i-1]['notes']+['E8-2601-'+str(k).zfill(3) for k in ks]));J[i-1]['caution']=J[i-1]['caution'].replace('Later 2025 entries','Later entries')
for n in N:
 n['journeys']=[j['id'] for j in J if n['id'] in j['notes']];n['related_notes']=list(dict.fromkeys(n.get('related_notes',[])+[k for j in J if n['id'] in j['notes'] for k in j['notes'] if k!=n['id']]))
for p,v in [('data/notes.json',N),('data/linkages.json',J)]: (R/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
lines=['# Civils Atlas · Cross-month reading journeys','','18 original comparative paths across 2025 and January2026. Reading order is not necessarily a legal timeline. Preserve dates, revisions and status.','']
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
p=R/'template.html';s=p.read_text().replace('Research edition 07','Research edition 08').replace('January–December now blend','January–December 2025 and January 2026 now blend').replace("$('#month').value='2025-11';render()","$('#month').value='2026-01';render()")
bar='<div class="jumpbar"><button data-month="2026-01">New: January 2026 · 45 notes</button><button data-month="2025-12">December 2025 · 44 notes</button><button data-month="2025-11">November 2025 · 30 notes</button><button data-month="2025-10">October 2025 · 33 notes</button><button data-month="2025-08">August 2025 · 45 notes</button></div>'
s=re.sub(r'<div class="jumpbar">.*?</div>',bar,s,count=1);s=s.replace("$('#practiceMonth').onchange=practice;practice();", "$('#practiceMonth').onchange=practice;$('#practiceMonth').value='2026-01';practice();");p.write_text(s)
c=collections.Counter(n['date'][:7] for n in N);mag=sum(bool(x[-1]) for x in t);total=len(t);paths=sum(bool(n['journeys']) for n in N);months=sorted(D)
table='| Expanded period | Indexed notes | Original MCQs | Mains plans |\n|---|---:|---:|---:|\n'+'\n'.join(f'| {m} | {c[m]} | 30 | 8 |' for m in months)
guide=f'''# Civils Atlas · Edition 08

UPSC × Andhra Pradesh APPSC · English · Updated / archive cut-off: **7 November 2026**

## Open and study
Open **index.html**. Study and practice now initially open **January 2026**. Month filters retain the twelve selected 2025 volumes. Thirteen monthly volumes are in **volumes/** as PDF, editable DOCX and Markdown, including questions/explanations and original Mains frameworks. **Study-Notes.docx** holds the complete working dataset. The eighteen reading journeys connect {paths} notes across dates and mechanisms; the order does not imply one legal programme.

**{len(N)} notes / {len(S)} source-reference entries / 390 original MCQs / 104 original Mains frameworks.** 583 notes are indexed to 2025, 45 to January2026, and nine inherited later seeds remain. Counts are not coverage percentages; source references are not fully read primary-document counts. Questions/frameworks are original study aids, not official previous-year questions or predictions.

{table}

## This continuation: January 2026
**45 new substantial notes, 30 MCQs and eight tailored Mains plans.** Breadth includes Parliament/Survey/advance GDP estimates, inflation/fiscal analysis, EU/UAE/Germany trade and cooperation, design protection, UGC equity stay and mental-health systems, pesticide/mining drafts, waste/environmental-consent/carbon rules, drug research, cooperative banking, pensions, sports governance, delimitation, anti-corruption, urban water, state finances, EPI, GLOFs, scramjet technology, Somnath and AI ethics.

AP material includes the official EPI ranking, APLINC/AIF, MSME common facilities, Kadapa electrical-steel/wind-mast proposal, Tirupati/Chittoor aerospace land allotments, water-loan guarantee, Kamalapadu pumped-storage DPR approval and the Sriharikota PSLV anomaly. Approvals and project proposals are not reported as completed assets, disbursed expenditure or jobs already created.

## Magazine and independent-evidence contract
The public official January2026 Vision IAS web edition was posted **28 February2026**. Ten selected public article bodies were retrieved; lead/substantive passages inspected, not complete issue/article review. Total inventory: {total} URLs over thirteen coverage months, {mag} linked to authored notes, {total-mag} unincorporated. No magazine bodies or gated PDFs are redistributed. Coverage month, reference data period, web posting and event/publication dates differ.

Independent evidence: substantive PRS January sections (chunks0–6), PIB EU/APY/scramjet releases, targeted official NITI report passages and MoSPI’s seven-page CPI FAQ; a full substantive specialist-news AP Cabinet body and corroborating newspaper extracts. The SWM Gazette fetch failed; the rule notes use PRS and do not claim primary-text review. Several court orders, state GOs, project DPRs and treaty schedules remain independently unread. **data/source-access.json** records actual scope.

## Important study distinctions
- The Economic Survey’s FY2026–27 growth projection differs from the FY2025–26 first advance estimate and later revised/rebased outcomes.
- January’s quarterly inflation figures concern October–December2025. The magazine’s CPI-2024-base supplement uses **later February** evidence and is not backdated as a January release. MoSPI specifies elementary Jevons and higher-level Young/modified-Laspeyres methods; classification changes require like-for-like weight comparisons.
- EU negotiations concluded in January; entry into force, tariff schedules, product standards, mobility and CBAM compliance remain separate. Trade-value coverage is not tariff-line share.
- UGC equity regulations were notified and then stayed in the reviewed January position; this is not final invalidation or unconditional implementation.
- SWM January notification differs from 1 April2026 commencement; an environmental-consent reform is not immunity from pollution duties.
- Scramjet ground testing is not an operational missile flight. PSLV’s anomaly report is not a final root-cause finding.
- AP ranks fifth with score60.65 in EPI2024’s inspected official tables; preparedness is not a rank in export volume. Forty-five CFCs are not the earlier plan for 175 finished industrial parks.

## Still unfinished
**Full January2025–7 November2026 coverage is NOT delivered.** February–November2026 spans ten periods needing substantial chronological backfill. All **23 monthly audits** and the **676-day daily-source reconciliation** remain open. Expanded months are selective, not complete PIB/newspaper/magazine coverage. Shorts/maps, primary legal texts, exact APPSC paper mapping, local GOs and culture/sport/P3 gaps remain uneven.

## Daily updating and rebuild
The 06:30IST workflow is supplied, **not activated on durable hosting**. The last recorded discovery test remains205 candidates, five responding and three blocked streams; no fresh collector test is claimed. Discovery is not verified publication and the preview does not research in the background.

Install requirements and run `python scripts/validate.py && python scripts/reconcile.py && python scripts/build.py`. JSON is authoritative; historical constructors can overwrite edits and are not automatic updaters. The builder now recognises year-specific practice files such as **data/2026-01-mcqs.json**, keeping January2025 separate. Structural/rendering checks are not independent factual or completeness certification.
'''
(R/'START-HERE.md').write_text(guide)
p=R/'README.md';old=p.read_text();keep=old[old.index('## Daily automation'):] if '## Daily automation' in old else '';p.write_text(guide+'\n'+keep)
(R/'research/Research-Status.md').write_text(guide.replace('# Civils Atlas · Edition 08','# Research status · Edition 08')+'''
## Next work and primary-check queue
February2026 is next chronologically. Before current-law use, read operative UGC/Section17A orders, the SWM/consent Gazette texts, final pesticides/mining/UCB instruments, treaty schedules and AP Cabinet GOs/DPRs. The NITI report was selectively inspected, not all 54 chunks; AP’s profile introduction contains older geography/statistical vintages not certified as current. The CPI FAQ is later February corroboration and both text chunks were read. The PSLV account is a contemporary newspaper extract, not final technical investigation. Earlier edition QA remains historical, not fresh certification.
''')
(R/'research/magazine-review/Integration-Report.md').write_text(f'''# Public official Vision IAS integration · Edition 08

Updated 7 November2026. Thirteen coverage months: January–December2025 plus January2026. {total} inventory URLs; {mag} linked, {total-mag} unincorporated. Not a completeness percentage or a whole-issue review claim.

January2026 adds ten selected article integrations. Public bodies were retrieved; lead/substantive passages inspected. The issue was posted28 February2026. Its CPI article includes later-released January-reference data; that is labelled later corroboration. MoSPI’s primary FAQ qualifies the article’s simplified index-method statement, and NITI’s official ranking/framework supports the EPI note and AP application.

Other restraint: no absolute delimitation non-reviewability assertion, no invented majority outcome from a Section17A split verdict, no final causation from a launch-anomaly extract, no operational projects from AP approvals, no unsupported Somnath attack count. No source bodies redistributed.

{table}

All daily source audits remain open. Read ../Research-Status.md and the access registry for independently unread primary texts and the Gazette fetch failure. CSV inventory retains unincorporated shorts/maps and articles as pending, not authored coverage.
''')
print('Finished integration',len(N),'notes;',paths,'in journeys;',mag,'/',total,'magazine URLs linked')
