"""One-time September integration. Do not rerun constructors on authoritative data."""
import json,pathlib,re,collections,math,csv
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
def save(p,x):(R/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
N=load('data/notes.json');S=load('data/sources.json');A=load('data/source-access.json');L=load('data/linkages.json');new=[n for n in N if n['id'].startswith('E16-')];assert len(new)==60
fix={'CFC s':'CFCs','HCFC s':'HCFCs','HFC s':'HFCs','MSP s':'MSPs','MoU s':'MoUs','Bank s':'Banks','Vice roy':'Viceroy','DILRMP3.0':'DILRMP 3.0','DDU–GKY2.0':'DDU–GKY 2.0','DDU–GKYwas':'DDU–GKY was','DDU–GKYis':'DDU–GKY is','CIIP costrevision':'CIIP cost revision','DAindexation':'DA indexation','APMSMEs':'AP MSMEs','EUFTA':'EU FTA','GECIIIapproval':'GEC III approval','GECIIIframework':'GEC III framework','GECIII':'GEC III','Augustopening':'August opening','AP-specific':'AP-specific','lowPUEmay':'low PUE may','1.5°Cdoes':'1.5°C does','1.5° Cdoes':'1.5°C does','KNMrice':'KNM rice','GWhBESS':'GWh BESS','FY 2032':'FY2032','FY 2026':'FY2026','C 2':'C2','2,610is':'2,610 is','₹ 2':'₹2'}
def proof(s):
 for a,b in fix.items():s=s.replace(a,b)
 s=re.sub(r',(\d+(?:\.\d+)?%)',r', \1',s)
 s=re.sub(r'(\d)\s?GW h',r'\1 GWh',s)
 return s
for n in new:
 for k in ['title','why','static_link','trap','mains']:n[k]=proof(n[k])
 for k in ['facts','analysis']:n[k]=[proof(x) for x in n[k]]
links={1:[1,6,28],2:[2,10,20,23,35,53],3:[3,4,5,7,9,19,20,21,43,52,53],4:[8,22,24,25,26,37,54,55,60],5:[40,41,44],6:[13,25,40,45,46,47,58],7:[8,17,29,31,32,33],8:[21,24,33,37,39,48,49,50,54,55,56,60],9:[18,23,45,48,49,51,56,59],10:[34,35,36,38,39],11:[15,16,34,38,41],12:[3,4,5,9,10,15,16,17,18,19,20,21,23,34,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60],13:[1,6,7,26,28,40,41,44,57],14:[10,16,17,18,27,35,43,52,53,59],15:[29,30,31,32,33,45,51],16:[42],17:[11,12,14,22,24,27,33,36,39,54,55,60],18:[8,21,24,29,33,37,48,49,50,51,54,55,56,60]}
for i,ks in links.items():L[i-1]['notes']=list(dict.fromkeys(L[i-1]['notes']+[f'E16-2609-{k:03}' for k in ks]))
stop=set('the and for with from this that into are not through july august september india indian policy new state national framework report review development original stage different'.split())
def words(n):return set(re.findall(r'[a-z]{4,}',(n['title']+' '+n['block']).lower()))-stop
old=[n for n in N if not n['id'].startswith('E16-')];df=collections.Counter(w for n in old for w in words(n))
for n in N:n['journeys']=[l['id']for l in L if n['id']in l['notes']]
for n in new:
 ranks=sorted(old,key=lambda x:sum(math.log(1+len(old)/(1+df[w]))for w in words(n)&words(x))+(1 if n['subject']==x['subject']else 0),reverse=True)
 companions=[k for l in L if n['id']in l['notes']for k in l['notes']if k!=n['id']]
 n['related_notes']=list(dict.fromkeys([x['id']for x in ranks[:6]]+companions))
save('data/notes.json',N);save('data/linkages.json',L)
# Readable, precise access registry; discovery links are not full-document evidence.
access={
'BOP':'Complete one-chunk RBI release and tables read. Preliminary April–June FY2026–27 data; reserve entry means US$8.1 billion depletion. Preserve gross/net and reserve-inclusive/nonreserve distinctions.',
'UPI':'All three FAQ chunks read. PDF dated 15 September, effective 15 October. Selective merchant MDR with exemptions; ordinary payer/P2P use remains free. No-surcharge rule does not prove indirect price effects impossible; credit-linked products separate.',
'EPFO':'Complete English/Hindi notification read. ₹25,000 monthly ceiling for Chapter III of Code on Social Security 2020; effective publication 17 September, superseding 29 May notification. Not a universal minimum wage or pension.',
'GEC':'Complete PIB body read. 30 September approval; headline ₹1,86,405 crore, central support ₹54,082 crore, 135 GW evacuation/50 GWh storage by FY2032–33. Primary component figures differ from total by ₹27 crore; unreconciled breakdown withheld.',
'MSP':'Complete substantive PIB body and cost footnote read. 30 September announcement for rabi marketing season 2027–28. Six crop rates verified; paid-out plus family-labour cost is not C2. Procurement is not universal.',
'DAC':'Complete substantive PIB release read. 7 September Acceptance of Necessity, about ₹1.10 lakh crore, 98% planned Indian-industry procurement. Not a signed contract, delivery or verified domestic content of every subsystem.',
'DIL':'Complete 9 September prelaunch PIB body read, announcing 10 September launch. Anticipated ₹565.50 crore, ULPIN and LandStack checked. PRS supplies later release account; complete guidelines and completed nationwide rollout not verified.',
'ECOM':'Opening chunk 0/3, including substantive Hindi amendments, read; complete later English duplication not read. Notification 9 September; commencement 1 January 2027. Lowest prior 30-day price definition checked.',
'FOOD':'Opening chunk 0/2, substantive Hindi provisions and English opening, read. Notification 14 September; commencement 1 April 2027. Specified 14-day regulatory/referral and five-day import reporting, with delay reasons.',
'ALLIED':'Opening chunk 0/11, definitions and commencement, read. Notification dated 31 August, September Gazette publication. Later five-year registration and CPD clauses rely on PRS, not a complete primary reading. Registration categories differ.',
'KYC':'Complete one-chunk RBI consultation release dated 11 September read; comments 2 October. Detailed 20/10/30-day procedures via PRS; full draft SOP and underlying court order not independently read. Not final directions.',
'WMA':'Complete one-chunk 29 September RBI release read: committee recommendations to be examined. Numerical proposals via PRS; complete advisory report not independently read. No implemented-limit claim.',
'IBBI':'Discussion-paper chunk 0/3 read, covering four proposals and opening related-party/avoidance discussion. Later valuation and recorded-deliberation details via PRS; not all primary pages. Comments 3 October; not final regulations.',
'IRDAI':'Page returned an 80-page viewer and download labels only, not substantive PDF text. No primary-paper reading claimed. Insurance details attributed to PRS.',
'AP3':'Complete substantive Telugu Cabinet-report body read. English notes are original summaries. Proposals/discussion distinguished from final approval; original GOs not read. Conflicting agenda counts withheld; linked 31 August Veligonda opening not redated.',
'AP23':'Both chunks, complete substantive body read. Original GOs not read. Four commissionerates, influencer policy, investment pipeline, CIIP and DA/DR stages preserved. Sector totals unreconciled; precise BNSS subsection withheld. Jobs are potential, not realised.',
'NELL':'Complete substantive 4 September report read on 3 September decision. 22.31 of 62.70 acres; active-canal/operational exclusions and 20-foot buffer. Original GO, survey and individual allotments not inspected.',
'PRICE':'Complete substantive 4 September report read on 3 September intervention. Onion ₹35/kg; 1.20 lakh tonnes tur dal is a request; 10,000 tonnes KNM rice is a procurement order. Original orders/delivery accounts not read.'}
for k,t in access.items():A['E16-'+k]['access']=t
for k in A:
 if k.startswith('E16-'):A[k]['title']=S[k][0]
save('data/source-access.json',A)
by={n['id']:n for n in N};lines=['# Civils Atlas · Cross-month reading journeys','','18 comparative paths across 2025 and January–September 2026. Preserve evidence vintages, draft status and commencement dates; reading order is not one continuous legal timeline.','']
for l in L:lines+=['## '+l['id']+' · '+l['title'],l['mechanism'],'']+['- **'+k+'** · '+by[k]['date'][:7]+' · '+by[k]['title']for k in l['notes']]+['','**Avoid this shortcut:** '+l['caution'],'','**Mains synthesis:** '+l['prompt'],'']
(R/'volumes/Cross-Month-Reading-Journeys.md').write_text('\n'.join(lines)+'\n')
linked=sum(bool(n['journeys'])for n in N);counts=collections.Counter(n['priority']for n in new)
p=R/'template.html';s=p.read_text().replace('Research edition 15','Research edition 16');a=s.index('January–December 2025 and January–August 2026');b=s.index(' <a href="research/magazine-review/Integration-Report.md">',a)
s=s[:a]+'''January–December 2025 and January–September 2026 have selected expanded volumes. September adds 60 original notes, 30 MCQs and eight Mains frameworks, including 16 AP notes/applications. Vision’s official archive was checked first; no public September monthly issue was independently verified. Selected Drishti September passages, PRS and independent official/newspaper checks provide breadth. Drishti’s filename says 2027 but its official link and internal cover verify September 2026 (25 August–24 September coverage). This is not a complete magazine or daily-source review. Historical/thematic revision and AP analytical applications are distinguished from new events.'''+s[b:]
s=s.replace('<div class="jumpbar">','<div class="jumpbar"><button data-month="2026-09">New: September 2026 · 60 notes</button>',1).replace('New: August 2026','August 2026').replace("$('#practiceMonth').value='2026-08'","$('#practiceMonth').value='2026-09'").replace("$('#month').value='2026-08';render()","$('#month').value='2026-09';render()")
p.write_text(s)
for fn in ['scripts/build.py','scripts/check_exports.py','scripts/check_question_pagination.py']:
 p=R/fn;p.write_text(p.read_text().replace('EDITION 15','EDITION 16').replace('edition-15-document','edition-16-document').replace('edition-15-question','edition-16-question'))
p=R/'scripts/validate.py';p.write_text(p.read_text().replace("'E14-','E15-'","'E14-','E15-','E16-'"))
text=f'''# CIVILS ATLAS · Edition 16
English · UPSC × Andhra Pradesh APPSC · Research cut-off: **7 November 2026**

## Start studying
- Open **index.html** for the offline app. It now opens **September 2026**; use month, subject, priority and AP filters, bookmarks, reading paths and monthly practice.
- September PDF: **volumes/September-2026-Study-Volume.pdf**; editable Word and Markdown alongside it.
- Original answer planning: **volumes/September-2026-Mains-Frameworks.md**.
- **Study-Notes.docx** contains the full working note archive; prior monthly volumes remain available.

## Current inventory — counts, not completeness
**{len(N):,} notes · {len(S)} source references · 630 original MCQs · 168 Mains frameworks · 21 selected monthly volumes · 18 reading paths linking {linked} notes.**

September adds **60 notes**, including **16 AP notes/applications**, **30 MCQs** and **eight Mains frameworks**. Priority distribution: **{counts['P1']} P1 / {counts['P2']} P2**. Historical editions remain preserved separately.

## September coverage
- Economy: Q1 balance of payments, selective UPI merchant MDR, insurance/insolvency consultations, mule-account safeguards, WMA recommendations, wage ceiling, renewable transmission/storage, petroleum draft, e-commerce rules, MSP and industrial safety.
- Governance and welfare: land-record integration, allied-health registration, food testing, advertising/telecom regulation, women farmers, adult disability support and rural skilling.
- Science/environment: ozone/Kigali, rhinos, climate overshoot, hanging glaciers, deep-sea minerals, stem cells, agentic AI, lunar radio astronomy, cooling, Salmonella and thermal protection.
- AP: cage-culture proposal, mango/tobacco support, Sangamam, Veligonda equipment, utility guarantees, Nellore land, commissionerates, influencer policy, investment/energy pipeline, CIIP, DA/DR and commodity intervention. Two clearly labelled applications connect national land/energy policy to AP, not new state announcements.
- International/history: BRICS, Belgium, Interim Government and party-symbol institutions. Selected thematic/historical notes are not silently converted into new September events.

## Magazine-first sourcing and actual access
Vision’s official monthly archive was checked first. No public September monthly issue was independently verified; the latest exposed issue remained June 2026, with a 31 July reader posting. Unofficial copies and daily entries were not substituted for an authenticated monthly edition.

Alternative: Drishti’s public **Saraansh September 2026**, **120 pages**, coverage **25 August–24 September**. Official archive label and internal cover confirm the issue even though the linked filename says “September 2027”. Contents and selected passages, many partial, were read — **not the complete issue**. Full magazine PDF/text is not redistributed.

Independent work includes PRS substantive chunks 0–5, complete selected RBI/PIB releases and official UPI FAQ, complete wage-ceiling Gazette, opening e-commerce/food/allied-health Gazette passages, opening IBBI discussion paper, and substantive AP newspaper reports. IRDAI’s viewer and MEA’s navigation shell are not counted as primary-body reading. Details: **research/edition16/Research-Log.md**, **research/magazine-review/edition16-selected.json**, **data/source-access.json**.

## Important distinctions and corrections
- BoP release is preliminary April–June data. US$8.1 billion is reserve depletion; personal-transfer receipts differ from net secondary income. Reserve-inclusive and nonreserve financial balances differ.
- UPI: selective merchant MDR effective **15 October**, not a consumer/P2P charge. Cap and exemptions matter; no-surcharge regulation does not prove indirect prices cannot change.
- E-commerce amendment: **1 January 2027** commencement. Food-laboratory amendment: **1 April 2027** commencement. Notification dates are not operative dates.
- GEC III: headline **₹1,86,405 crore**, central **₹54,082 crore**, **135 GW / 50 GWh**. Unreconciled component mismatch of ₹27 crore is documented; breakdown withheld.
- DAC approval is Acceptance of Necessity, not contract/delivery. WMA and multiple consultations remain recommendations/drafts, not verified final law.
- MSP uses the official paid-out plus family-labour cost footnote, not automatically C2; announcement is not universal procurement.
- AP proposals, guarantees, approvals, requested stocks, potential jobs and reported releases are not completed projects, audited spending or verified individual receipts. Original AP GOs remain a major follow-up gap.
- Hanging glaciers can form naturally; lunar far side is not permanently dark; typhoid and non-typhoidal Salmonella are not interchangeable. Unverified arrest holding, specific party-symbol freeze, first-state claims and exact study statistics are withheld.

## Still unfinished — do not mistake this for complete coverage
**The full requested January 2025–7 November 2026 archive remains incomplete. All 23 monthly daily-source audits remain open.** October and 1–7 November 2026 still need substantial expanded backfill. Earlier months retain newspaper/PIB/district, legal, implementation, sports, appointment and other gaps. No month has passed complete daily reconciliation. Reference and note counts are not coverage percentages.

**Daily automatic updating is NOT active.** The supplied collector/workflow has not been activated or freshly revalidated; its unreviewed discovery links are not researched notes. No unattended future research is promised.

## QA scope
Edition 16 structural, export, question-pagination and app checks are recorded in research/edition-16-* files. Such checks and sampled rendered pages do not establish independent factual accuracy,current law or completeness. See the final QA scope and package check.
'''
for f in ['START-HERE.md','README.md','research/Research-Status.md']:(R/f).write_text(text)
save('research/magazine-review/edition16-selected.json',dict(edition=16,month='2026-09',vision_issue_verified=False,alternative='Drishti public Saraansh September 2026',filename_year_discrepancy='Official September 2026 anchor and internal cover; filename says September 2027',pdf_pages=120,coverage='2026-08-25 to 2026-09-24',complete_issue_review=False,selected_pages=[2,3,4,5,8,30,31,32,33,34,35,38,39,40,64,65,69,71,76,77,78,79,80,84,85,87,88,89,94,95],selection_scope='Selected partial passages, not all pages/articles completely read',original_notes=60,ap_notes=16,mcqs=30,mains=8,limits='research/edition16/Research-Log.md; no full magazine redistribution'))
p=R/'research/magazine-review/Integration-Report.md';p.write_text(p.read_text()+'\n## Edition 16 · September 2026\nVision archive checked first; no verified public September monthly issue. Official Drishti anchor/internal cover verify September 2026 despite filename September 2027; 120 pages, 25 August–24 September, selected partial passages, not whole issue. PRS substantive chunks 0–5 and selected independent official/newspaper passages read. 60 original notes, 16 AP notes/applications, 30 MCQs, eight Mains frameworks. See edition16-selected.json and research/edition16/Research-Log.md. All daily audits remain open; historical/thematic material and analytical AP applications explicitly labelled.\n')
for f in ['data/coverage-ledger.csv','research/remaining-period-inventory.csv']:
 p=R/f
 with p.open(newline='')as h:r=csv.DictReader(h);fields=r.fieldnames;rows=list(r)
 for row in rows:
  if row.get('Month')=='2026-09':
   row['Indexed notes']=sum(n['date'].startswith('2026-09')and n['subject']==row['Subject']for n in N);row['Status']='Expanded / incomplete';row['PRS monthly synthesis']='Substantive chunks 0–5 read; primary follow-up partial';row['AP/specialist reconciliation']='Partial';row['Comments']='60 selected September notes;16 AP notes/applications. Magazine selected partial passages,not full issue. All daily audits open;counts not completeness percentages.'
  if row.get('Period')=='September 2026':
   row['Notes already indexed']='60';row['Editorial status']='Expanded volume; audit still open';row['PRS task']='Substantive sections read; complete primary reconciliation pending';row['Andhra Pradesh task']='16 notes/applications; ETV/South First/The Hindu bodies read; original GOs and daily audit pending'
 with p.open('w',newline='')as h:w=csv.DictWriter(h,fields);w.writeheader();w.writerows(rows)
M=load('Package-Manifest.json');M.update(edition='16',notes=len(N),source_references=len(S),monthly_volumes=21,original_mcqs=630,original_mains_frameworks=168,notes_linked_to_journeys=linked,substantial_backfill_periods=2,september_2026_notes=60,september_2026_new_notes=60,september_2026_ap_notes=16,september_2026_priority_counts=dict(counts),september_vision_issue_verified=False,september_alternative='Drishti 120 pages;25 August–24 September;selected partial passages;filename discrepancy verified internally',qa='Pending Edition16 export/app/layout checks;not factual/completeness certification.');M.pop('packaged_file_count',None);save('Package-Manifest.json',M)
print('Integrated',len(new),'September notes;',linked,'notes in18paths;',dict(counts))
