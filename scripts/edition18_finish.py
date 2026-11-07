"""Integrate first-week selection and honest deployment health. Run once."""
import json,pathlib,re,collections,math,csv
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
def save(p,x):(R/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
N=load('data/notes.json');S=load('data/sources.json');A=load('data/source-access.json');L=load('data/linkages.json');new=[n for n in N if n['date'].startswith('2026-11')];assert len(new)==25
# State sharing and local implementation are comparative, not identical fiscal instruments.
links={3:[1],7:[3,16],8:[5,14,20,22],9:[2,15,24],10:[12,18,19,21,22,23],11:[3,4,16],12:[11,16,17],13:[1,6,7,8,10,17],14:[2],15:[21,22,23,24],17:[9,10,14,21,24],18:[2,7,15,22,24]}
for i,ks in links.items():L[i-1]['notes']=list(dict.fromkeys(L[i-1]['notes']+[f'E18-2611-{k:03}'for k in ks]))
L[7]['notes']=list(dict.fromkeys(L[7]['notes']+['CA-043']))
stop=set('the and for with from this that into are not through january february march april may june july august september october november india indian policy new state national framework report review development original stage different'.split())
def words(n):return set(re.findall(r'[a-z]{4,}',(n['title']+' '+n['block']).lower()))-stop
old=[n for n in N if not n['date'].startswith('2026-11')];df=collections.Counter(w for n in old for w in words(n))
for n in N:n['journeys']=[l['id']for l in L if n['id']in l['notes']]
for n in new:
 ranks=sorted(old,key=lambda x:sum(math.log(1+len(old)/(1+df[w]))for w in words(n)&words(x))+(1 if n['subject']==x['subject']else 0),reverse=True)
 companions=[k for l in L if n['id']in l['notes']for k in l['notes']if k!=n['id']]
 n['related_notes']=list(dict.fromkeys([x['id']for x in ranks[:6]]+companions))
A['NOV']['url']=S['NOV'][1];A['NOV']['title']=S['NOV'][0];save('data/source-access.json',A)
save('data/notes.json',N);save('data/linkages.json',L)
by={n['id']:n for n in N};lines=['# Civils Atlas · Cross-month reading journeys','','18 comparative paths across 2025, January–October 2026 and a selected 1–7 November 2026 batch. Preserve evidence vintages, draft status and commencement dates; reading order is not one continuous legal timeline.','']
for l in L:lines+=['## '+l['id']+' · '+l['title'],l['mechanism'],'']+['- **'+k+'** · '+by[k]['date'][:7]+' · '+by[k]['title']for k in l['notes']]+['','**Avoid this shortcut:** '+l['caution'],'','**Mains synthesis:** '+l['prompt'],'']
(R/'volumes/Cross-Month-Reading-Journeys.md').write_text('\n'.join(lines)+'\n')
linked=sum(bool(n['journeys'])for n in N);counts=collections.Counter(n['priority']for n in new)
p=R/'template.html';s=p.read_text().replace('Research edition 17','Research edition 18');a=s.index('January–December 2025 and January–October 2026');b=s.index(' <a href="research/magazine-review/Integration-Report.md">',a)
s=s[:a]+'''January–December 2025 and January–October 2026 have selected expanded volumes; November covers only 1–7 November 2026. This first-week batch has 25 notes (24 new plus expanded CA-043), 30 original MCQs and eight Mains frameworks, including eight AP-linked notes. Vision’s archive was checked first; no authenticated full November magazine review is claimed. Independent official releases and AP reporting anchor this selection. All daily-source audits remain incomplete. The daily-discovery workflow has been locally retested, not deployed to your GitHub account. It collects unreviewed links, not automatically researched notes; see live health below and DAILY-UPDATES-SETUP.md.'''+s[b:]
s=s.replace('<div class="jumpbar">','<div class="jumpbar"><button data-month="2026-11">New: 1–7 November 2026 · 25 notes</button>',1).replace('New: October 2026','October 2026').replace("$('#practiceMonth').value='2026-10'","$('#practiceMonth').value='2026-11'").replace("$('#month').value='2026-10';render()","$('#month').value='2026-11';render()")
s=s.replace('<b>not activated</b>','<b id="automationLabel">deployment pending</b>')
s=s.replace('The included scheduled workflow must be enabled on an always-on host. It is <b>not running daily for you yet</b>. Some sources blocked the first collection attempt; failures are shown rather than bypassed.','<span id="automationDetail">Repository deployment is pending.</span> <a href="DAILY-UPDATES-SETUP.md">Daily activation guide ↗</a>. A scheduled run and successful retrieval of every source are different checks; failures are shown rather than bypassed.')
s=s.replace("const N=DATA.notes,S=DATA.sources;","const N=DATA.notes,S=DATA.sources;const AUTO=DATA.automation||{};")
needle="$('#total').textContent=N.length;"
s=s.replace(needle,needle+"$('#automationLabel').textContent=AUTO.scheduler_active?'scheduled run observed — check latest health':'not activated — repository setup pending';$('#automationDetail').textContent=(AUTO.deployment_status||'Repository deployment pending')+'. Last collection: '+(AUTO.sources_ok??0)+'/'+(AUTO.sources_tested??0)+' sources returned links; '+(AUTO.last_run||'no run recorded')+'. Link discovery does not create verified notes.';")
p.write_text(s)
p=R/'scripts/build.py';s=p.read_text().replace('EDITION 17','EDITION 18');s=s.replace("expanded=sorted(QS)","expanded=sorted(QS)\nAUTO=load('automation-status.json',{})\nAUTO_TEXT=('A scheduled discovery run has been observed; inspect current source health.' if AUTO.get('scheduler_active') else 'Daily discovery is NOT activated: GitHub repository deployment or first scheduled execution is pending.')+' Automation collects unreviewed source links, not researched study notes.'")
s=s.replace("linkages=load('linkages.json',[]))","linkages=load('linkages.json',[]),automation=AUTO)")
s=s.replace("'Daily discovery is NOT activated. The supplied scheduler collects unreviewed links, not automatically verified notes.'","AUTO_TEXT")
s=s.replace("'Daily scheduler: NOT ACTIVATED. Source discovery, review and factual publication are different stages. The tested inbox has '","AUTO_TEXT+' The inbox has '")
s=s.replace("p('Daily automation is NOT activated. Source extracts are not whole-document reviews. Review research/Research-Status.md before using this as a complete month.')","p(AUTO_TEXT);p('Source extracts are not whole-document reviews. November covers only 1–7 November. Review research/Research-Status.md before treating any month as complete.')")
s=s.replace("slug=MONTH.replace(' ','-');ns=", "slug=MONTH.replace(' ','-')\n if m=='2026-11':MONTH='1–7 November 2026'\n ns=")
p.write_text(s)
for fn in ['scripts/check_exports.py','scripts/check_question_pagination.py']:
 p=R/fn;p.write_text(p.read_text().replace('edition-17-document','edition-18-document').replace('edition-17-question','edition-18-question'))
p=R/'scripts/validate.py';s=p.read_text().replace("'E16-','E17-'","'E16-','E17-','E18-'");p.write_text(s)
text=f'''# CIVILS ATLAS · Edition 18
English · UPSC × Andhra Pradesh APPSC · Research cut-off: **7 November 2026**

## Start studying
- **index.html** is the offline study app; it opens **1–7 November 2026**. Use subject → block → date, priority/AP filters, bookmarks, cross-month journeys and practice.
- **volumes/November-2026-Study-Volume.pdf**, editable DOCX and Markdown cover **only 1–7 November**, not the full month.
- **volumes/November-2026-Mains-Frameworks.md** has eight original answer plans.
- **DAILY-UPDATES-SETUP.md** explains account-side GitHub Actions activation and optional website publication.
- **Study-Notes.docx** contains the working archive. Earlier selected monthly volumes remain available.

## Inventory — not coverage percentages
**1,178 notes · 678 source references · 690 original MCQs · 184 Mains frameworks · 23 selected period volumes · 18 reading paths linking {linked} notes.**

November first week has **25 notes**: **24 new** plus an expanded, stable **CA-043**. There are **eight AP-linked notes**, **30 original MCQs**, **eight frameworks**, and priorities **{counts['P1']} P1 / {counts['P2']} P2**. This does not claim every event of the seven days was reconciled.

## First-week coverage
- Statistics, industry and energy: VISTAR, Economic Census distinctions, lithium/nickel processing, storage VGF, Semicon portal/ECMS and tax-devolution timing.
- Governance/welfare: FTSC continuation, PAC resolution, telecom quality/grievances, Digi Yatra trials and medicine-price revision with future 9 November effect.
- Security/IR/science: Agniveer pathway, signed corvette contracts, Pralay evaluation, IndiaAI models, BIMSTEC maritime exercise and Tiger Triumph.
- Agriculture/environment: FMD SAT-1 preparedness, SUVIKALP mine repurposing and I-OECMs, including Srisailam–Cumbum.
- AP: regular devolution, OECM landscape, Visakhapatnam exercise/RINL land bids, Murasu chronology, emergency funding, lifeline restoration and source-specific livelihood-loss assessments.

## Magazine-first and independent research
Vision’s official archive was checked first on 7 November. Latest exposed reader remains June 2026, posted 31 July; no authenticated full November issue is claimed. A complete November monthly review is not assumed available during the first week. Selected Blackbook excerpts were used for discovery/breadth, not as independently verified primary evidence or a full magazine review.

The batch uses independently inspected official release bodies and AP reporting. PIB listing chunks 0, 2–6 and 13 were inspected for discovery; not all 323 releases were read. Twenty selected substantive PIB release bodies were inspected, with a recorded partial tail for Semicon; the existing devolution release/table was re-read. Three AP newspaper/wire report bodies were read. Full guidelines, orders, model cards, contracts and final loss audits remain follow-up tasks. See **research/edition18/Research-Log.md** and **data/source-access.json**.

## Important distinctions
- Devolution is a regular instalment advanced from 10 to 5 November; not an extra grant. CA-043 retained, not duplicated.
- Scheme support, total investment, GW/GWh, targets and commissioned output differ. Critical-mineral capex and storage approval are not completed plants/assets.
- FTSC 850 target differs from 779 existing courts. PAC resolution is not automatic amendment of all legislative rules.
- Telecom release describes 24-hour support but at least 16 hours of human assistance. Network Anubhav’s stated exceedance convention and user-test sampling limits are retained.
- Agniveer pathway retains willingness/selection conditions. Corvette contracts are not delivery. Pralay induction is described as imminent, not independently confirmed complete.
- Anti-cancer revised prices are stated to take effect **9 November**, after this cut-off. Original NPPA order not read; projected savings are not realised outcomes.
- OECM recognition does not change ownership or create a national park. A demonstration landscape is not blanket parcel-level recognition.
- Murasu loss estimates are preliminary and differ between source snapshots; horticulture figures are not silently averaged or combined. Regular devolution, state ₹37 crore emergency allocation and requested central assistance are distinct. RINL bids are not independently verified settled cash.
- Three September corrections remain incorporated in working exports. **Historical Edition 16 and Edition 17 ZIPs remain unchanged.** See **research/edition17/Corrections-to-September.md**.

## Daily updating — exact current state
**User selected GitHub Actions. Configuration is revised and locally tested; repository URL/deployment and first hosted scheduled execution are still pending. Daily automatic execution is NOT active for the user yet.** No supported GitHub connector is available in this session; no account-side setup is claimed.

Prepared schedule: **06:30 IST** daily. It adds deduplicated **unreviewed links**, records source health/history and rebuilds the app; **it does not automatically research or verify new study notes**. Optional Pages publication is separately configured. Local live test: **5/8 collectors retrieved links**; PIB returned 403 and Indian Express robots retrieval returned 403. Blocks are not bypassed. Five offline unit checks and reconciliation idempotence passed. Source failures persist to the queue/logs and remain visible.

The old reconciliation script’s stale month list could overwrite newer evidence disclosures; it was replaced with a count-only, disclosure-preserving version. A separate status file tracks manual versus actual scheduled GitHub runs. See **DAILY-UPDATES-SETUP.md**, **data/automation-status.json**, and **research/edition-18-automation-checks.json**. A configured cron line is not proof of activation or guaranteed future delivery.

## Still incomplete
**All 23 monthly daily-source audits remain open.** Chronological selected volumes now reach 7 November, but no month/first-week batch is certified complete. Newspaper/PIB/AP/district, legal, implementation, appointment, culture, sports and other omission reconciliation remains necessary. No November events after 7 November are represented as observed outcomes. Historical notes do not certify latest law or statistics.

## QA scope
Edition 18 technical results are recorded under **research/edition-18-***. Schema, pagination, document integrity, app regressions, source-health tests and sampled visual proof are not independent factual/current-law/completeness certification. Hosted GitHub/Pages activation has not been tested.
'''
for f in ['START-HERE.md','README.md','research/Research-Status.md']:(R/f).write_text(text)
for f in ['data/coverage-ledger.csv','research/remaining-period-inventory.csv']:
 p=R/f
 with p.open(newline='')as h:r=csv.DictReader(h);fields=r.fieldnames;rows=list(r)
 for row in rows:
  if row.get('Month')=='2026-11':
   row['Indexed notes']=sum(n['date'].startswith('2026-11')and n['subject']==row['Subject']for n in N);row['Status']='Expanded first-week selection / incomplete';row['PRS monthly synthesis']='No full November review claimed at 7 November cut-off';row['AP/specialist reconciliation']='Partial';row['Comments']='25 selected first-week notes, eight AP-linked; primary release bodies/newspaper checks, not complete daily reconciliation. No post-7-November observed events.'
  if row.get('Period','').startswith('November 2026'):
   row['Notes already indexed']='25';row['Editorial status']='Expanded first-week selection; audit still open';row['PRS task']='Full November issue not assumed available by 7 November; later review reconciliation pending';row['Andhra Pradesh task']='Eight AP-linked notes; original GOs/treasury/contract/final cyclone evidence and daily reconciliation pending'
 with p.open('w',newline='')as h:w=csv.DictWriter(h,fields);w.writeheader();w.writerows(rows)
M=load('Package-Manifest.json');M.update(edition='18',notes=len(N),source_references=len(S),monthly_volumes=23,original_mcqs=690,original_mains_frameworks=184,notes_linked_to_journeys=linked,substantial_backfill_periods=0,november_2026_notes=25,november_2026_new_notes=24,november_2026_expanded_existing_ids=['CA-043'],november_2026_scope='1–7 November only; selected first-week batch, not full month or daily audit',november_2026_ap_notes=8,november_2026_priority_counts=dict(counts),daily_scheduler_active=False,daily_scheduler_configuration='Revised/local-tested GitHub Actions 06:30 IST; repository deployment and first scheduled hosted run pending',daily_live_sources_ok=5,daily_live_sources_tested=8,qa='Pending Edition18 document/app/package checks. Hosted automation not activated.');M.pop('packaged_file_count',None);save('Package-Manifest.json',M)
save('research/magazine-review/edition18-selected.json',dict(edition=18,period='2026-11-01 to 2026-11-07',vision_archive_checked=True,vision_full_november_issue_verified=False,complete_issue_review=False,alternative_scope='Blackbook opening and chunk2 excerpts for discovery; independent official releases and AP reporting used for notes',new_notes=24,expanded_existing_note='CA-043',period_notes=25,ap_linked_notes=8,mcqs=30,mains=8))
p=R/'research/magazine-review/Integration-Report.md';p.write_text(p.read_text()+'\n## Edition 18 · 1–7 November 2026 only\nVision archive checked first; no verified full November issue. Selected Blackbook excerpts supply discovery, not primary verification. Independent PIB and AP report bodies anchor 24 new notes plus expanded stable CA-043, 30 MCQs and eight Mains frameworks. First-week selection only; all daily audits open. Revised daily-discovery workflow locally retested, not deployed/activated for the user. See research/edition18/Research-Log.md and DAILY-UPDATES-SETUP.md.\n')
print('Integrated',len(new),'first-week notes;',linked,'notes linked;',dict(counts))
