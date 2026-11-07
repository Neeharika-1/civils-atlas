"""One-time Edition 15 integration; no broad typography replacements."""
import pathlib,json,collections,re,math,csv,shutil
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
def save(p,x):(R/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
N=load('data/notes.json');S=load('data/sources.json');L=load('data/linkages.json');new=[n for n in N if n['id'].startswith('E15-')]
assert len(new)==63
links={1:[1,2,3,12],2:[10,12],3:[4,5,16,17,25,26],4:[8,9,30,34],5:[44,45],6:[18],7:[5,8,19,20],8:[24,25,26,28,31,33,38,50,52,54,55,56,61,62],9:[29,48,49,57,58,59],10:[28,37,54,60],11:[13,14,15,35,63],12:[6,7,11,17,18,19,20,22,23,34,40,41,42,44,45,48,55,57,58,60,63],13:[1,2,21,26,33,40,41,44,63],14:[4,16,17,21,23,48,51,55,56,59],15:[28,32,36,37,41,43,61,62],16:[],17:[14,18,23,27,29,32,36,38,39,49,53,57,58,61,62],18:[6,15,23,24,29,31,48,49,53,57,58,59]}
for i,ks in links.items():L[i-1]['notes']=list(dict.fromkeys(L[i-1]['notes']+[f'E15-2608-{k:03}' for k in ks]))
stop=set('the and for with from this that into are not through july august india indian policy new state national framework report review development original stage different'.split())
def words(n):return set(re.findall(r'[a-z]{4,}',(n['title']+' '+n['block']).lower()))-stop
old=[n for n in N if not n['id'].startswith('E15-')];df=collections.Counter(w for n in old for w in words(n))
for n in N:n['journeys']=[l['id']for l in L if n['id']in l['notes']]
for n in new:
 ranks=sorted(old,key=lambda x:sum(math.log(1+len(old)/(1+df[w]))for w in words(n)&words(x))+(1 if n['subject']==x['subject']else 0),reverse=True)
 companions=[k for l in L if n['id']in l['notes']for k in l['notes']if k!=n['id']]
 n['related_notes']=list(dict.fromkeys([x['id']for x in ranks[:6]]+companions))
save('data/notes.json',N);save('data/linkages.json',L)
by={n['id']:n for n in N};lines=['# Civils Atlas · Cross-month reading journeys','','18 comparative paths across 2025 and January–August 2026. Preserve evidence vintages, draft status and commencement dates; reading order is not one continuous legal timeline.','']
for l in L:lines+=['## '+l['id']+' · '+l['title'],l['mechanism'],'']+['- **'+k+'** · '+by[k]['date'][:7]+' · '+by[k]['title']for k in l['notes']]+['','**Avoid this shortcut:** '+l['caution'],'','**Mains synthesis:** '+l['prompt'],'']
(R/'volumes/Cross-Month-Reading-Journeys.md').write_text('\n'.join(lines)+'\n')
p=R/'template.html';s=p.read_text().replace('Research edition 14','Research edition 15');a=s.index('January–December 2025 and January–July 2026');b=s.index(' <a href="research/magazine-review/Integration-Report.md">',a)
s=s[:a]+"January–December 2025 and January–August 2026 have selected expanded volumes. August adds 63 original notes, 30 MCQs and eight Mains frameworks, including 14 AP notes. No independently verified public August Vision monthly edition was found; the newest exposed 31 July reader belongs to June. August uses selected Drishti passages (25 July–24 August coverage), PRS and independent official/newspaper checks. This is not a complete magazine or daily-source review. Historical and thematic magazine items are explicitly distinguished from new August events."+s[b:]
s=s.replace('<div class="jumpbar">','<div class="jumpbar"><button data-month="2026-08">New: August 2026 · 63 notes</button>',1).replace('New: July 2026','July 2026').replace("$('#practiceMonth').value='2026-07'","$('#practiceMonth').value='2026-08'").replace("$('#month').value='2026-07';render()","$('#month').value='2026-08';render()")
p.write_text(s)
for fn in ['scripts/build.py','scripts/check_exports.py','scripts/check_question_pagination.py']:
 p=R/fn;p.write_text(p.read_text().replace('EDITION 14','EDITION 15').replace('edition-14-document','edition-15-document').replace('edition-14-question','edition-15-question'))
p=R/'scripts/validate.py';p.write_text(p.read_text().replace("'E13-','E14-'","'E13-','E14-','E15-'"))
p=R/'.qa/check.cjs';s=p.read_text().replace("['2026-07',69]]","['2026-07',69],['2026-08',63]]").replace("length===69,'July 2026 initial'","length===63,'August 2026 initial'").replace('length===965','length===1028').replace('notes:965','notes:1028').replace('expanded_months:19,quizzes:19','expanded_months:20,quizzes:20').replace('edition-14-app-checks','edition-15-app-checks').replace('19 month filters/quizzes; 965 archive','20 month filters/quizzes; 1028 archive')
needle="assert(errors.length===0,errors.join('\\n'));console.log('PASS: 20"
s=s.replace(needle,"d.querySelector('[data-month=\"2026-08\"]').click();assert(d.querySelectorAll('details.note').length===63,'August26 quick');input('#exam','ap');assert(d.querySelectorAll('details.note').length===14,'August26 AP count');assert(d.querySelector('#E15-2608-057'),'August26 Netanna');assert(d.querySelector('#E15-2608-061'),'August26 elephant');input('#exam','all');d.querySelector('#practiceMonth').value='2026-08';d.querySelector('#practiceMonth').dispatchEvent(new dom.window.Event('change'));assert(d.querySelector('#quiz').textContent.includes('AUG26-01'),'August26 practice');assert(d.querySelector('#volumeLinks').textContent.includes('August 2026'),'August26 documents');assert(errors.length===0,errors.join('\\n'));console.log('PASS: 20")
p.write_text(s)
# Preserve the immediately preceding research status as a historical audit.
shutil.copyfile(R/'research/Research-Status.md',R/'research/Edition-14-Research-Status.md')
linked=sum(bool(n['journeys'])for n in N);counts=collections.Counter(n['priority']for n in new)
text=f'''# Civils Atlas · Edition 15

**English · UPSC × Andhra Pradesh APPSC · Research cut-off: 7 November 2026**

## Open and study
Open **index.html**. Study and practice default to **August 2026**. The printable volume is **volumes/August-2026-Study-Volume.pdf**; editable Word and original Markdown are beside it. Eight Mains frameworks are included and also supplied separately. All earlier volumes remain available.

**63 new August-indexed notes · 14 dedicated AP notes · 30 original MCQs · 8 Mains frameworks.** Priority: {counts['P1']} P1 / {counts['P2']} P2. AP and national thematic revision is labelled; a month-level index does not assert an event happened on 31 August.

Working archive: **1,028 notes / 599 reference entries / 600 MCQs / 160 Mains frameworks / 20 selected monthly volumes / 18 reading paths linking {linked} notes.** References include repeated publisher entries and an explicitly failed MEA access attempt: this is NOT a count of unique primary documents fully read. Counts do not certify completeness, current law or implementation.

## August study map
- **Polity:** session scrutiny, mineral federalism, corporate committee recommendations, tribunals, ISI proposal, telecom identification, employment audit draft, Panchayat devolution and digital land records.
- **Economy/agriculture:** Q1 GDP, four-sector IIP, unchanged MPC rates, MSME receivables, chemical parks, e-commerce exports, banking evidence, tax/disclosure stage checks, NCDC, GOBARdhan, PNG, road concessions, professional services, greenium and soil management.
- **Social/environment/science:** healthcare recommendations, medicines regulation, SC development finance, AMRUT/NRW, forest fires, Zanskar glaciers, cloudbursts, Western Ghats thematic revision, AI biology, space ecosystem, detonation engines, eclipses, Dirac Medal, lab-grown diamonds, care and nutrition.
- **AP:** draft PPP fund, Disha Bill withdrawal, Amaravati financing, aqua power support, Pushkaralu ghat preparation, education/urban institutions, pedestrian safety, Netanna Sevalo, differentiated electricity support, BC/insurance announcements, Chirala coastal tourism, regional elephant plan, HANUMAN and data-centre resource governance.
- **International/culture:** Uzbekistan partnership, RIN uprising revision and conditional Hoysala epigraph interpretation. Geopolitical events, sports, appointments and daily district reporting remain incompletely covered.

## Magazine-first sourcing, without invented access
Vision's official monthly archive was checked first. No independently verified public August monthly issue was identified. Its newest exposed 2026 reader is the **31 July posting of the June editorial edition**, not an August issue. Daily posts and unofficial photocopies were not substituted for a verified monthly issue.

Alternative: Drishti's **112-page public Saraansh August 2026**, coverage **25 July–24 August**. Contents and selected passages were inspected, many only partly. This is NOT a full-issue review. Historical/thematic items and July overlap are not silently redated as August events. Full copyrighted magazine PDF/text is not redistributed. Vision discovery inventory remains **760 URLs / 228 linked / 532 pending**, not a coverage percentage.

## Independent checks and material corrections
PRS substantive August chunks 0–10 were read. Selected independent checks: MoSPI GDP and IIP opening sections/tables, RBI policy decision, three energy/defence PIB releases, opening telecom and audit Gazette passages, ICTP award body, PIB elephant programme, full substantive PTI Cabinet and New Indian Express Chirala reporting. The MEA outcomes URL returned a navigation shell: Uzbekistan remains PRS-attributed, not claimed primary-verified.

- IIP has **four** sectors in the 2022–23 series. Water/sewerage/waste has **2.020%** weight; all weights sum to 100. July quick growth **6.7%**. June earlier quick **7.3%** differs from final table **8.8%**; April–July cumulative is **6.3%**. Do not mix dates or vintages.
- GDP real **7.8%**, nominal **10.3%**, real GVA **8.2%** refer to **April–June**, released 31 August. Charts differ from some prose levels; notes use primary prose rather than chart approximations.
- RBI repo **5.25%**, SDF **5%**, MSF/Bank Rate **5.5%**, neutral. Disputed prose/chart forecast series are not taught as settled observations.
- GOBARdhan **₹23,731 crore**, FY2026–27 to FY2035–36; **₹2,110/MMBTU** pricing differs from capital assistance up to **₹2 crore/TPD**. Approval is not achieved ten-fold production.
- PNG **200 SCM** goes to eligible CGD entities per incremental billed connection above a GA threshold, not free household gas; effective **1 September** after 18 August approval.
- Rural employment audit is **DRAFT**; a proposed commencement clause inside it does not establish final rules. Parliamentary passage elsewhere is not automatically assent or commencement.
- AP **Disha Bill withdrawal** is not automatically repeal of a commenced Act. **₹500 crore elephant plan** covers four southern states, not AP alone. PIB posting is **13 August**, used as reporting date rather than an inferred event date.
- Netanna **71,536 × ₹25,000 = ₹178.84 crore**, rounded to ₹179 crore. Release is not independent proof of every credit; electricity-support counts use different categories.
- Lab-grown diamond is real diamond, not identical natural geological rarity. NRW is not all leakage. A slower glacier may be thinning. Hazard labels require hourly rainfall evidence. AI design is not an approved therapy.

## Evidence and omissions
See **research/edition15/Research-Log.md**, **data/source-access.json** and **research/magazine-review/edition15-selected.json**. Primary AP GOs, project clearances, bank receipts, several Bills/reports and complete datasets remain unread. Many magazine themes are secondary-source consolidation, not independent primary confirmation. Tax-law and foreign-disclosure notes are limited stage/concept primers pending fuller instrument inspection.

**The full requested January 2025–7 November 2026 archive is not complete.** All **23 monthly daily-source audits remain open**. September–7 November 2026 still needs substantial backfill; earlier months also retain omissions. No month has passed complete PIB/newspaper/AP daily reconciliation. Sports/appointments/obituaries, district news and multiple legal/implementation checks remain outstanding.

**Daily automatic updating is NOT active.** A collector script/workflow exists but has not been activated or freshly verified in this edition. Its unreviewed links are not researched notes. This delivery does not promise unattended future research.

## QA scope
Edition 15 automated checks and sampled rendered pages are recorded separately after build. Structural/export/app checks are not independent factual review or completeness certification. Historical ZIP editions remain unchanged; current working exports share the latest typography and archive links.
'''
for f in ['START-HERE.md','README.md','research/Research-Status.md']:(R/f).write_text(text)
save('research/magazine-review/edition15-selected.json',dict(edition=15,month='2026-08',vision_issue_verified=False,alternative='Drishti public Saraansh August 2026',pdf_pages=112,coverage='2026-07-25 to 2026-08-24',complete_issue_review=False,selected_pages=[8,12,13,21,22,41,42,56,65,66,67,68,69,70,71,72,74,75,77,78,79,80,81,82,83,84,85,86,87,90,91,92],selection_scope='Many pages partial; opening article also sampled. No claim all passages/pages fully read.',original_notes=63,ap_notes=14,mcqs=30,mains=8,limits='research/edition15/Research-Log.md; no full magazine redistribution'))
p=R/'research/magazine-review/Integration-Report.md';p.write_text(p.read_text()+'\n## Edition 15 · August 2026\nVision archive checked first; no verified public August monthly edition found. Selected Drishti 112-page public issue passages used, 25 July–24 August coverage, not whole-issue review. PRS substantive sections and independent official/newspaper passages read. See edition15-selected.json and research/edition15/Research-Log.md for corrections, overlap and access limits. 63 original notes/30 MCQs/8 Mains; full daily reconciliation remains open.\n')
for f in ['data/coverage-ledger.csv','research/remaining-period-inventory.csv']:
 p=R/f
 with p.open(newline='')as h:r=csv.DictReader(h);fields=r.fieldnames;rows=list(r)
 for row in rows:
  if row.get('Month')=='2026-08':
   row['Indexed notes']=sum(n['date'].startswith('2026-08')and n['subject']==row['Subject']for n in N);row['Status']='Expanded / incomplete';row['PRS monthly synthesis']='Substantive sections read; primary follow-up partial';row['AP/specialist reconciliation']='Partial';row['Comments']='63 selected August notes; 14 AP. Magazine passages selected, not full issue. All daily audits open; counts are not completeness percentages.'
  if row.get('Period')=='August 2026':
   row['Notes already indexed']='63';row['Editorial status']='Expanded volume; audit still open';row['PRS task']='Substantive review read; complete primary reconciliation pending';row['Andhra Pradesh task']='14 selected notes; PTI/TNIE/PIB bodies read; original GOs and daily audit pending'
 with p.open('w',newline='')as h:w=csv.DictWriter(h,fields);w.writeheader();w.writerows(rows)
M=load('Package-Manifest.json');M.update(edition='15',notes=len(N),source_references=len(S),monthly_volumes=20,original_mcqs=600,original_mains_frameworks=160,notes_linked_to_journeys=linked,substantial_backfill_periods=3,august_2026_notes=63,august_2026_new_notes=63,august_2026_ap_notes=14,august_2026_priority_counts=dict(counts),august_vision_complete_issue_inventory=False,august_vision_issue_verified=False,august_alternative='Drishti 112 pages, 25 July–24 August, selected passages only',qa='Pending Edition 15 export/app/layout checks; not factual/completeness certification.');M.pop('packaged_file_count',None);save('Package-Manifest.json',M)
print('Integrated',len(new),'notes;',linked,'notes in 18 paths; priorities',dict(counts))
