"""One-time October integration, preserving earlier content and September corrections."""
import json,pathlib,re,collections,math,csv
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
def save(p,x):(R/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
N=load('data/notes.json');S=load('data/sources.json');A=load('data/source-access.json');L=load('data/linkages.json');new=[n for n in N if n['id'].startswith('E17-')];assert len(new)==66
# Remove obsolete CIIP agricultural/social associations after the factual correction.
for l in L:l['notes']=[x for x in l['notes']if x!='E16-2609-056']
L[7]['notes'].append('E16-2609-056');L[10]['notes']=list(dict.fromkeys(L[10]['notes']+['E16-2609-055']));L[17]['notes']=list(dict.fromkeys(L[17]['notes']+['E16-2609-057']))
links={1:[1,2,3,6,7,41],2:[4,5,8,9,10],3:[32,33,50,51],4:[7,11,12,13,34,35],5:[49],6:[10,26,36,52,58],7:[19,20,25,26,30,31],8:[12,18,23,24,32,33,50,54,61,62],9:[16,55,56,57,59],10:[11,13,47,63,64,65],11:[14,15,19,21,22,23,24,44,48,66],12:[26,28,29,30,38,39,40,41,43,49,51,53,54,55,56,57,60],13:[6,24,26,27,28,29,32,49,50,58],14:[28,29,37,53,54,56,57],15:[38,44,45,46,47,63,64,65],16:[30],17:[14,16,18,19,20,21,31,36,44,45,47,52,58,63,65],18:[16,28,33,46,55,56,57,59,60,65]}
for i,ks in links.items():L[i-1]['notes']=list(dict.fromkeys(L[i-1]['notes']+[f'E17-2610-{k:03}'for k in ks]))
stop=set('the and for with from this that into are not through january february march april may june july august september october india indian policy new state national framework report review development original stage different'.split())
def words(n):return set(re.findall(r'[a-z]{4,}',(n['title']+' '+n['block']).lower()))-stop
old=[n for n in N if not n['id'].startswith('E17-')];df=collections.Counter(w for n in old for w in words(n))
for n in N:n['journeys']=[l['id']for l in L if n['id']in l['notes']]
for n in new:
 ranks=sorted(old,key=lambda x:sum(math.log(1+len(old)/(1+df[w]))for w in words(n)&words(x))+(1 if n['subject']==x['subject']else 0),reverse=True)
 companions=[k for l in L if n['id']in l['notes']for k in l['notes']if k!=n['id']]
 n['related_notes']=list(dict.fromkeys([x['id']for x in ranks[:6]]+companions))
save('data/notes.json',N);save('data/linkages.json',L)
# Independent access accounts: fluent prose, with exact reading limits retained.
access={
'FX':'Complete operative release body read. The underlying-exposure threshold falls from US$100 million to US$5 million. FERR is 20% of INR-equivalent notional for specified purchases above US$2 million. Rebooking of cancelled contracts and permitted rollovers differ. Linked circulars not separately read; an unrelated PSL PDF was not counted as FX evidence.',
'ADS':'Opening Hindi notification and definitions, chunk 0/5, read. Notification 8 October, publication 9 October; commencement is the 180th day from publication, broadly April 2027. Detailed code clauses rely on PRS; not a complete primary reading.',
'IDBI':'Complete unique English body read despite the Hindi interface parameter. 14 October approval: 60.72% comprises 30.48% government and 30.24% LIC; residual stakes 15% and 19%. Fairfax subsidiary is selected buyer; consideration ₹52,878.08 crore. Conditional approval is not completed transfer.',
'BANK':'Complete unique body read. Committee constituted 30 October under Suresh N. Patel for six months. Remit and recommendations are not implemented banking law.',
'CMPS':'Complete unique body read. 28 October approval of ₹10,000 crore through 2039–40. Listed components sum to ₹9,900 crore: unresolved ₹100 crore difference, so the rupee breakdown is withheld. The 7.5 lakh TEU figure is a capacity target, not realised output.',
'ITLA':'Complete unique body read. SPV approved 6 October. Technical appraisal covers ₹500 crore or more; monitoring is described for projects above ₹500 crore. Existing financial appraisal mechanisms continue. PRS loses the exact boundary distinction.',
'VGSY':'Unique prose except the final implementation tail in chunk 0/4 read. 28 October approval: ₹7,395.55 crore = central ₹4,869.48 crore + state ₹2,526.07 crore; centrally sponsored, 2026–31; no permanent posts. Annual plans, GPDP and AuditOnline are not completed universal implementation.',
'SPORT':'Complete unique prose read. 28 October approval: ₹1,856.67 crore, 2026–2033–34; ₹1,130 crore investment/turnover support and ₹105 crore certification. Scheme approval is not a confirmed AP zone or athlete scholarship.',
'DAC':'Complete unique prose read. 26 October estimated ₹2,12,000 crore Acceptance of Necessity, with 82% planned procurement from Indian industry. Not signed contracts, deliveries or uniform domestic content in every subsystem.',
'NSAP':'Complete three-page, one-chunk DoRD-hosted PIB release read. 14 October approval, ₹53,428 crore for 2026–31. Disability eligibility/rate changes require guidelines and implementation within three months; immediate universal payment not verified. State top-ups are distinct.',
'H2':'Chunk 0/13 read: scope, definitions, 5% by-volume ceiling, explicit non-authorisation and network-specific qualification. Trials, billing, consumer notice and later clauses rely on PRS, not a complete primary reading.',
'ROW':'Chunks 0–1/10 read, completing operative guidelines and starting annexures. 6 October; specified 66 kV-and-above ISTS scope and state-policy conditions. Three valuers normalised within ±20% of median; 200% tower-base compensation, corridor rates 30%/45%/60%, and 30-day administrative appeal. Administrative finality is not a blanket bar on constitutional judicial review. Remaining annexures not fully read.',
'UNEP':'Opening chunk 0/2 read, including main findings and carbon-removal discussion. Published 21 October; full technical report not read. Current policies 2.8°C, pledges 2.6°C, additional net-zero commitments 2.1°C. Return-to-1.5°C pathway is conditional, with 50% probability and uncertain 320 Gt CO2 removals; cuts without reference baselines are withheld.',
'APNIE':'Complete unique report body in chunk 0/2 read. 8 October report on 7 October Cabinet: distinct Thalliki beneficiary groups and sanctions, diet, tribal coaching and APHIMS. Original GOs, bank payments and campus permissions not read. Government claims about financial burden are not independently proven zero cost.',
'APTOI':'Complete unique report and other decisions in chunk 0/3 read. 7 October Cabinet clears proposed ordinance promulgation, not independently verified Governor promulgation. Diet effect reported from 1 October. Original rules, GOs and individual permissions not read.',
'APHANS':'Complete unique body in chunk 0/2 read. APHIMS ₹20.62 crore over 72 months; ASHA gratuity explicitly concerns eligible death-in-service cases; Repalle ₹58.42 crore and 66 posts; distinct land allocations. Original GOs not read. Reported approval is not verified disbursement or commissioning.',
'IMD':'Opening chunk 0/5 read. Bulletin issued 0130 IST on 28 October, based on 2330 IST 27 October observations. Narrative forecasts 125–135 km/h, gusting 150, near early-28-October landfall. Forecast is not final observed wind/track. Table category/wind inconsistencies are not reused as settled facts; remaining maps/warnings not fully read.',
'ARNAB':'Liveblog opening chunk 0/11 read: reported completed 28 October landfall and weakening, flash-flood risk, power restoration and Telangana support. Not the entire liveblog or a final damage audit; final casualty/loss totals withheld.'}
for k,v in access.items():A['E17-'+k]['access']=v
for k in A:
 if k.startswith('E17-'):A[k]['title']=S[k][0]
save('data/source-access.json',A)
# Correct the September arithmetic question's context without altering its answer.
Q=load('data/2026-09-mcqs.json');Q[28]['question']='What is the increase from ₹904 crore to ₹1,548.98 crore in Amaravati’s reported Critical Infrastructure and Investment Plan (CIIP) estimate?';Q[28]['explanation']='The increase is ₹644.98 crore, approximately 71.35% of ₹904 crore. CIIP here concerns Amaravati capital-area panchayat infrastructure, not an irrigation project. Arithmetic does not establish the causes of escalation or completed spending; original revised estimates remain unread.';save('data/2026-09-mcqs.json',Q)
by={n['id']:n for n in N};lines=['# Civils Atlas · Cross-month reading journeys','','18 comparative paths across 2025 and January–October 2026. Preserve evidence vintages, draft status and commencement dates; reading order is not one continuous legal timeline.','']
for l in L:lines+=['## '+l['id']+' · '+l['title'],l['mechanism'],'']+['- **'+k+'** · '+by[k]['date'][:7]+' · '+by[k]['title']for k in l['notes']]+['','**Avoid this shortcut:** '+l['caution'],'','**Mains synthesis:** '+l['prompt'],'']
(R/'volumes/Cross-Month-Reading-Journeys.md').write_text('\n'.join(lines)+'\n')
linked=sum(bool(n['journeys'])for n in N);counts=collections.Counter(n['priority']for n in new)
p=R/'template.html';s=p.read_text().replace('Research edition 16','Research edition 17');a=s.index('January–December 2025 and January–September 2026');b=s.index(' <a href="research/magazine-review/Integration-Report.md">',a)
s=s[:a]+'''January–December 2025 and January–October 2026 have selected expanded volumes. October adds 66 original notes, 30 MCQs and eight Mains frameworks, including 14 AP notes/applications. Vision’s official archive was checked first; no public October monthly issue was independently verified. Selected Drishti October passages (25 September–24 October), PRS and independent official/newspaper checks provide breadth, not a complete magazine or daily-source review. October RBI forecast conflicts, deferred law/draft stages and cyclone forecast-versus-observation limits are recorded. Three September corrections are now incorporated in working exports; historical Edition 16 ZIP is unchanged. Analytical applications are labelled, not presented as new announcements.'''+s[b:]
s=s.replace('<div class="jumpbar">','<div class="jumpbar"><button data-month="2026-10">New: October 2026 · 66 notes</button>',1).replace('New: September 2026','September 2026').replace("$('#practiceMonth').value='2026-09'","$('#practiceMonth').value='2026-10'").replace("$('#month').value='2026-09';render()","$('#month').value='2026-10';render()")
p.write_text(s)
for fn in ['scripts/build.py','scripts/check_exports.py','scripts/check_question_pagination.py']:
 p=R/fn;p.write_text(p.read_text().replace('EDITION 16','EDITION 17').replace('edition-16-document','edition-17-document').replace('edition-16-question','edition-17-question').replace('most months remain thin or empty','monthly selections and daily-source audits remain incomplete'))
p=R/'scripts/validate.py';p.write_text(p.read_text().replace("'E15-','E16-'","'E15-','E16-','E17-'"))
text=f'''# CIVILS ATLAS · Edition 17
English · UPSC × Andhra Pradesh APPSC · Research cut-off: **7 November 2026**

## Start studying
- **index.html** is the offline app; it opens **October 2026**. Use subject → topic block → date, priority/AP filters, bookmarks, reading paths and practice.
- **volumes/October-2026-Study-Volume.pdf** is the new study volume; editable DOCX and Markdown sit alongside it.
- **volumes/October-2026-Mains-Frameworks.md** contains eight original answer plans.
- **Study-Notes.docx** is the working full-archive export. Prior monthly volumes are preserved and rebuilt with corrected working data.

## Inventory — counts, not coverage percentages
**1,154 notes · 653 source references · 660 original MCQs · 176 Mains frameworks · 22 selected monthly volumes · 18 reading paths linking {linked} notes.**

October adds **66 original notes**, including **14 AP notes/applications**, **30 MCQs** and **eight Mains frameworks**. Priorities: **{counts['P1']} P1 / {counts['P2']} P2 / {counts.get('P3',0)} P3**.

## October coverage
- Economy: MPC, daily CRR, inflation vintages, IDBI, GST recommendations, banking review, forex/FERR, securities advertising, SME capital, containers, transport, steel, minerals and digital DISCOMs.
- Governance/welfare: social assistance, tribunals, panchayats, AI accountability, allied-health boards, NTA recommendations, Census, urban classification, RTI and recruitment institutions.
- Science/environment: six Nobel categories, climate pathways, biodiversity-index interpretation, risk finance, coasts, pumped storage, QKD and ethical animal research.
- AP: foreign universities, private-school permission proposal, Thalliki expansion, diet charges, tribal coaching, APHIMS, eligible ASHA death-in-service gratuity, Repalle hospital, land administration, Arnab forecast/landfall/restoration. Two explicitly labelled AP applications cover risk finance and hydrogen; they are not new state schemes.
- International relations: Switzerland and Poland cooperation. Magazine thematic/historical selections are labelled rather than silently dated as fresh discoveries.

## Magazine-first sourcing and access limits
Vision’s official archive was checked first; no verified public October monthly issue was located. Latest exposed June reader was posted 31 July. Public Drishti **Saraansh October 2026**, **115 pages**, coverage **25 September–24 October**, supplies selected breadth. Contents and selected passages, often partial, were read — not the complete issue. No full magazine text/PDF is redistributed.

Independent work includes substantive PRS chunks 0–7, complete selected RBI/PIB/PMIndia bodies, six official Nobel announcements, the hosted NSAP release, opening PNGRB/Gazette passages, the operative transmission guidelines, UNEP’s explainer, IMD’s opening bulletin and substantive AP newspaper reports. MoSPI access returned 403; linked/discovered documents are not automatically counted as read. See **research/edition17/Research-Log.md**, **research/magazine-review/edition17-selected.json**, **data/source-access.json**.

## Corrections and essential distinctions
- RBI primary narrative projects FY2026–27 growth **7.1%** and CPI **5.2%**, conflicting with PRS **6.7% / 5%** and some charts. Primary prose is used; no fabricated average or inferred statistical revision.
- CRR daily **99% of the required balance** is not a 99% CRR on deposits. FX underlying-exposure and FERR thresholds are different.
- GST recommendations/drafts need operative instruments. Securities advertising has **180th-day** commencement; aviation rules **1 January 2027**; BS-VII draft **1 April 2029**. Notification is not immediate operation.
- NSAP approval needs follow-through and remains distinct from AP top-ups. Container components sum to ₹9,900 crore versus ₹10,000 crore headline; the unresolved rupee breakdown is withheld.
- ITLA technical appraisal is **₹500 crore or more**; monitoring is described **above ₹500 crore**. DAC AoN is not a signed contract or delivery.
- ASHA report specifies **death in service**, ₹5,000 per completed year, **₹1.50 lakh cap**. Thalliki new inclusions and second-phase beneficiaries have different denominators. Approval/sanction is not verified payment or commissioning.
- IMD forecast wind/track differs from later confirmed landfall reporting. Final casualty/loss totals were not audited; weakening does not end flood/electrical risk. Yanam belongs to Puducherry.
- **Three September note corrections** now appear in rebuilt working exports: CBG in the energy package; CIIP as Amaravati’s Critical Infrastructure and Investment Plan, not irrigation; two DA/DR instalments tied to July 2024/January 2025. September MCQ29 now names the correct CIIP context. **Historical Edition 16 ZIP remains unchanged.** Full notice: **research/edition17/Corrections-to-September.md**.

## Still unfinished
**The January 2025–7 November 2026 archive remains incomplete. All 23 monthly daily-source audits remain open.** The **1–7 November 2026** expanded batch is still pending. Earlier months, including October, need full dated newspaper/PIB/AP/district, legal, implementation, sport, appointment and omission reconciliation. No month has passed a complete daily-source audit. Indexing dates for month-precision notes are organisational, not invented event dates.

**Daily automatic updating is NOT active.** Collector/workflow files have not been activated or freshly revalidated. Discovery links are not researched notes. No unattended future research is promised.

## QA scope
Edition 17 schema, export, pagination and app/layout checks are recorded under **research/edition-17-***. These are technical and sampled editorial checks, not independent factual, current-law or completeness certification.
'''
for f in ['START-HERE.md','README.md','research/Research-Status.md']:(R/f).write_text(text)
save('research/magazine-review/edition17-selected.json',dict(edition=17,month='2026-10',vision_issue_verified=False,alternative='Drishti public Saraansh October 2026',pdf_pages=115,coverage='2026-09-25 to 2026-10-24',complete_issue_review=False,selected_pages=[5,12,13,17,18,22,36,37,41,52,58,61,63,64,65,66,68,71,72,73,75,76,78,79,80,81,82,83],selection_scope='Contents and selected partial excerpts, many opening 1750–2300 characters; page 80 QKD tail separately read. Not all pages/articles completely read.',original_notes=66,ap_notes=14,mcqs=30,mains=8,limits='research/edition17/Research-Log.md; no full magazine redistribution'))
p=R/'research/magazine-review/Integration-Report.md';p.write_text(p.read_text()+'\n## Edition 17 · October 2026\nVision archive checked first; no verified public October monthly issue. Drishti official anchor and internal cover verify Saraansh October 2026, 115 pages, coverage 25 September–24 October. Contents/selected partial excerpts only, not whole issue. PRS substantive chunks 0–7 and selected independent official/newspaper bodies provide original research. 66 original notes, 14 AP notes/applications, 30 MCQs, eight Mains frameworks. Access/discrepancy log: research/edition17/Research-Log.md; selected review: edition17-selected.json. Three September corrections incorporated in working exports; historical ZIP unchanged. All daily audits remain open.\n')
for f in ['data/coverage-ledger.csv','research/remaining-period-inventory.csv']:
 p=R/f
 with p.open(newline='')as h:r=csv.DictReader(h);fields=r.fieldnames;rows=list(r)
 for row in rows:
  if row.get('Month')=='2026-10':
   row['Indexed notes']=sum(n['date'].startswith('2026-10')and n['subject']==row['Subject']for n in N);row['Status']='Expanded / incomplete';row['PRS monthly synthesis']='Substantive chunks 0–7 read; primary follow-up partial';row['AP/specialist reconciliation']='Partial';row['Comments']='66 selected October notes; 14 AP notes/applications. Selected partial magazine passages, not whole issue. All daily audits open; counts not completeness percentages.'
  if row.get('Period')=='October 2026':
   row['Notes already indexed']='66';row['Editorial status']='Expanded volume; audit still open';row['PRS task']='Substantive sections read; complete primary reconciliation pending';row['Andhra Pradesh task']='14 notes/applications; TNIE/TOI/Hans/IE bodies read; original GOs and daily audit pending'
 with p.open('w',newline='')as h:w=csv.DictWriter(h,fields);w.writeheader();w.writerows(rows)
M=load('Package-Manifest.json');M.update(edition='17',notes=len(N),source_references=len(S),monthly_volumes=22,original_mcqs=660,original_mains_frameworks=176,notes_linked_to_journeys=linked,substantial_backfill_periods=1,october_2026_notes=66,october_2026_new_notes=66,october_2026_ap_notes=14,october_2026_priority_counts=dict(counts),october_vision_issue_verified=False,october_alternative='Drishti 115 pages; 25 September–24 October; selected partial passages, not whole issue',september_correction='E16-2609-055 energy CBG; 056 Amaravati CIIP; 057 two dated DA/DR instalments. Working exports rebuilt; historical Edition16 ZIP unchanged. September MCQ29 context clarified.',qa='Pending Edition17 export/app/layout checks; not factual/completeness certification.');M.pop('packaged_file_count',None);save('Package-Manifest.json',M)
print('Integrated',len(new),'October notes;',linked,'notes in 18 paths;',dict(counts))
