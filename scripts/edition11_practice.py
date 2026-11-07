import json,pathlib,random
R=pathlib.Path(__file__).resolve().parents[1];N={n['id']:n for n in json.loads((R/'data/notes.json').read_text())}
def ref(i):return f'E11-2604-{i:03}'
rows='''1~Adjournment sine die is best distinguished from dissolution because it:~Ends sittings without fixing a further sitting date, without itself ending the House’s existence.~Automatically ends the Lok Sabha’s legal existence.|Requires every pending bill to have passed.|Is identical to the President’s prorogation in every respect.
2~An Article 368 special majority in a House requires:~A majority of total membership and at least two-thirds of members present and voting.~Only two-thirds of the members who happen to attend, regardless of total membership.|A simple majority of members present and voting in every case.|Unanimity of all members including absentees.
2~After the Constitution amendment in April’s delimitation package was defeated, which inference is valid?~The proposed 850-seat ceiling did not thereby become the Constitution’s operative ceiling.~Lok Sabha automatically expanded to 850 elected seats.|Women’s reservation automatically commenced solely because the proposal was introduced.|Every dependent bill became law without further voting.
3~The 3.40% figure in MoSPI’s 13 April release denotes:~March 2026 provisional combined year-on-year CPI inflation.~April 2026 final inflation.|The CPI index level of 3.40.|The quarterly food-inflation average.
4~Consider: 1. Repo remained 5.25%. 2. Neutral stance promises a cut at the next meeting. 3. The 22 April document records the earlier 6–8 April meeting. Which are correct?~1 and 3 only.~1 and 2 only.|2 and 3 only.|1, 2 and 3.
5~The proposed ₹10,000 monthly full-KYC PPI cash-loading limit should be read as:~A draft limit on the specified wallet cash-loading activity, not every bank or UPI transfer.~An operative universal ceiling on all bank transactions.|A minimum wallet balance every user must maintain.|A cash grant to every verified wallet holder.
6~The ₹1,000 social-impact fund entry threshold discussed in April applies to:~The specified social-impact segment, not every AIF investment.~All AIF categories without distinction.|Only bank fixed deposits.|A guarantee of positive commercial returns.
7~An otherwise eligible SEZ unit’s highest annual FOB export value in the preceding three years is ₹120 crore. Under the reviewed 30% cap, the relevant ceiling is:~₹36 crore, subject to the other conditions.~₹12 crore, because only the current year matters.|₹120 crore irrespective of conditions.|₹30 crore for every unit irrespective of its exports.
7~Which additional check is central to the reviewed SEZ concession?~At least 20% value addition under the prescribed calculation, alongside other conditions.~Automatic refund of the same input taxes twice.|Unrestricted eligibility for every imported item passing through a warehousing zone.|Proof that domestic clearances are always entirely duty-free.
8~April’s RELIEF expansion added which pair to the reviewed geographic coverage?~Egypt and Jordan.~Norway and Iceland.|Brazil and Argentina.|Japan and Mongolia.
9~Which statement accurately compares the announced New Zealand FTA offers?~New Zealand’s offer covers 100% of India’s exports, while India’s tariff-line liberalisation is about 70%, subject to the agreement.~Both sides immediately abolish every tariff on signature alone.|India’s 70% tariff-line figure necessarily means exactly 70% of trade value.|The investment commitment is evidence all US$20 billion had already arrived.
10~A rule notified on 22 April with stated commencement on 1 May should be indexed as:~An April notification with a distinct later operative date.~Fully operative from 22 April solely because it was published.|A May parliamentary bill introduced by the regulator.|Proof no preparation was possible before 1 May.
11~Underground coal gasification differs from surface combustion chiefly because it:~Converts coal in situ into gas, creating distinct subsurface safety and closure concerns.~Eliminates every groundwater risk by definition.|Requires no mining-plan approval.|Necessarily leaves no cavity or well-closure liability.
13~Which PMGSY-III deadline pairing matches the April approval?~Plains roads/bridges and hill roads—March 2028; hill bridges—March 2029.~Every road and bridge—March 2028 without exception.|Every road—March 2029; all bridges—March 2027.|Only new airports—March 2028.
14~A toll provision levying no overload fee up to a specified excess-load level necessarily means:~Neither a general weight-law exemption nor proof the loading is safe.~All other motor-vehicle weight restrictions are repealed.|The vehicle is mechanically safe under every condition.|The goods vehicle needs no registration.
15~Tar balls are most accurately understood as:~Weathered oil residues that can arise from different spill/leakage or seepage sources.~A harmless form of clean beach sand.|Proof that every incident came from the same identified operator.|Only untreated household plastic pellets.
18~The IBC amendment’s provision for different notified commencement dates implies:~Assent does not by itself prove every new procedure was operational on 6 April.~All provisions must have commenced simultaneously on assent.|No provision can ever commence.|Every later rule can automatically be backdated by a textbook.
20~LFPR and unemployment rate differ because:~LFPR uses the population denominator, while unemployment rate uses the labour-force denominator.~Both use only people already employed as denominator.|LFPR necessarily equals the unemployment rate.|Neither depends on age or reference-status definitions.
20~A usual-status unemployment estimate for age 15+ should be compared directly with a youth current-weekly-status estimate only after:~Reconciling age, status, period and survey definitions.~Assuming every published unemployment number is the same concept.|Deleting the age labels to simplify revision.|Treating every non-worker as unemployed.
22~PLI-linked incremental sales alone cannot establish:~The same amount of additional domestic value added or technological capability.~That sector-specific eligibility matters.|That policy evaluation needs a baseline.|That approved claims and payments can differ.
27~A proposed cooling-off period in a fraud discussion paper is best evaluated as:~A possible trade-off between cancellation opportunity and genuine payment speed, not a universal current delay.~Proof that every transfer above ₹10,000 already waits one hour.|A substitute for all account-level fraud controls.|A guarantee users can never be deceived after authentication.
29~The ₹38,424 crore defence-export figure concerns:~FY2025–26 exports, distinct from total defence production and indigenous-content ratios.~April 2026 exports alone.|The entire defence budget.|A direct measure proving no exported product contains imported components.
30~Which comparison is dimensionally sound?~Installed capacity in GW versus electricity generated in TWh, with their different meanings retained.~GW treated as identical to annual TWh.|A capacity share used automatically as the generation share.|Non-fossil and renewable treated as identical because both exclude coal.
32~Artemis II’s April outcome was:~A completed crewed lunar flyby and Earth return, not a lunar surface landing.~A permanent crewed lunar base.|The first landing on Mars.|A mission that remained only an unlaunched proposal.
33~The One Health Quadripartite comprises:~WHO, FAO, UNEP and WOAH.~WHO, WTO, IMF and World Bank.|UNESCO, IAEA, ICAO and IMO.|FAO, NATO, OECD and OPEC.
34~With Jyotiba Phule’s birth on 11 April 1827, 11 April 2026 marks:~199 completed years; the 200th anniversary falls in 2027.~200 completed years.|100 completed years.|The founding date of Satyashodhak Samaj.
35~For the revised Jan Vishwas proposal, which measures should remain distinct?~79 Acts, 784 provisions, and the number of offences rationalised.~Acts and offences, because both always count the same thing.|Every proposal and every already commenced provision, because introduction implements both.|Civil penalties and absence of any enforceable duty, because they are identical.
41~The Amaravati amendment’s legal chronology is:~Assent on 6 April 2026 with deemed effect from 2 June 2024.~Assent on 2 June 2024 because that is the retrospective date.|Amendment of the central Act solely by March’s Assembly resolution.|A prohibition on any future parliamentary amendment.
43~In AP’s reported census schedule, the correct sequence is:~Self-enumeration 16–30 April, then field houselisting/housing census 1–30 May with validation.~Completed population enumeration by 16 April.|Mandatory smartphone-only counting without field visits.|All state-level field visits completed before self-enumeration began.
45~An increase in Polavaram OTS housing assistance supports which inference?~A revised assistance component, not proof all rehabilitation and livelihood obligations have been fulfilled.~All displaced families were fully paid on the Cabinet date.|Every family has identical losses and eligibility.|Cash assistance alone establishes adequate replacement services.'''
Q=[];rng=random.Random(11)
for row in rows.splitlines():
 i,q,right,wrong=row.split('~');n=N[ref(int(i))];opts=[right]+wrong.split('|');rng.shuffle(opts);Q.append(dict(id=f'APR26-{len(Q)+1:02}',question=q,options=opts,answer=opts.index(right),explanation=n['static_link']+' '+n['analysis'][0]+' Caution: '+n['trap'],ref=n['id']))
assert len(Q)==30
Q[7]['explanation']='30% × ₹120 crore = ₹36 crore. The base is the highest annual FOB export value in the immediately preceding three years, not present production. Minimum value addition, unit/product eligibility and other conditions still apply.'
(R/'data/2026-04-mcqs.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
F=[
(2,'Evaluate delimitation through population equality and federal fairness.',[
'Anchor the April package as defeated, not an enacted increase to850seats.',
'Explain constituency-population equality, inter-state allocation and the separate question of women’s representation.',
'Analyse concerns of states that achieved population stabilisation alongside the democratic case for updating representation.',
'Explain Article368majority requirements; distinguish constitutional proposal, ordinary legislation and implementation.',
'Recommend transparent data, public reasoning and institutionally credible consultation without inventing a single settled formula.']),
(7,'Can temporary SEZ–DTA concessions support manufacturing without distorting competition?',[
'Anchor1April2026–31March2027, the20%value-addition condition and the30%cap with its historical FOB-export denominator.',
'Explain the benefit: capacity utilisation, employment continuity and lower unit costs during external disruption.',
'Counterpoint: DTAproducers may face uneven conditions; export benefits must not be claimed twice.',
'Assess eligibility certification, audit, product exclusions and the difference between a concession and duty-free clearance.',
'Recommend transparent temporary review using additional production, jobs and genuine compliance, not only domestic sales volume.']),
(9,'How can India turn the New Zealand FTA’s announced access into export gains?',[
'Anchor27April signing; distinguish conclusion/signature from entry into force and applicable origin rules.',
'Explain asymmetry: NewZealand100%export access versus India’s roughly70%tariff-line liberalisation and sensitive exclusions.',
'Link opportunities to standards, logistics, services capability and professional-mobility eligibility.',
'ForAP, assess eligible food/seafood supply chains and certification; do not assume mirrored concessions for every farm product.',
'Treat US$20billion as a forward-looking commitment. Recommend utilisation monitoring and exporter assistance rather than counting promised flows as realised.']),
(18,'How should insolvency reform balance timely recovery and stakeholder fairness?',[
'Anchor the6AprilAct and its express provision-specific notified commencement.',
'Explain value preservation, admission discipline and the difference between rescue and liquidation.',
'Discuss creditor-led and cross-border/group frameworks as institutional designs needing operative rules and capacity.',
'Counterpoint: concentrating creditor power without transparency can disadvantage other claimants; deadlines alone cannot supply tribunal capacity.',
'Recommend reasoned decisions, professional quality, predictable implementation and recovery statistics with explicit denominators.']),
(20,'Why does a low unemployment rate not settle the question of employment quality?',[
'Anchor PLFS2025usual-status age15+: LFPR59.3%,WPR57.4%,UR3.1%; preserve27March release and2025reference year.',
'Explain population versus labour-force denominators and usual status versus current weekly status.',
'Analyse gender participation, informal/insecure work, hours and earnings; nominal wage gains do not prove real gains.',
'Use the23.6%regular-wage/salaried share as one composition measure, not proof all jobs are formal or protected.',
'Recommend matched data, skills, care infrastructure and productive-job creation. Avoid substituting older graduate subgroups for current national figures.']),
(30,'How should renewable-energy progress be measured beyond installed capacity?',[
'Define GWcapacity separately from period-specific electricity inTWh/billionunits.',
'Distinguish renewable from non-fossil and capacity share from generation share.',
'Map grid, storage, flexibility, forecasting and curtailment constraints that affect delivered energy.',
'ForAP, add land, transmission, distribution-company finances and household affordability without inventing local output figures.',
'Recommend reporting reliable generation, emissions, cost and service outcomes alongside capacity. Reject unverified51.5%demand claims derived from a capacity statistic.']),
(41,'Explain the significance and limits of Amaravati’s statutory recognition.',[
'Anchor theGazette:Act7/2026,assent6April,deemed effect2June2024,andAPCRDA-notified-area explanation.',
'Trace theMarchAssembly request to1AprilLokSabha and2AprilRajyaSabha passage without collapsing the stages.',
'Benefits: administrative clarity and a more stable legal reference for planning.',
'Limits: naming the capital does not complete works, settle every land/rehabilitation dispute or produce financing.',
'Recommend transparent project appraisal, land obligations, fiscal disclosure, service milestones and heritage safeguards. Parliament’s future amendment power is not extinguished.']),
(45,'What makes Polavaram rehabilitation adequate beyond increased cash assistance?',[
'Anchor30Aprilreported changes:house-construction assistance₹2.85lakh→₹3.57lakh;eligible outside-colony sitevalue₹1lakh→₹2lakh.',
'Distinguish Cabinet approval, notified eligibility, payment and actual rehabilitation.',
'Examine housing quality, land/livelihood restoration, community services, access and applicable rights.',
'Counterpoint: a standard unit cost may not reflect varying losses or local construction costs; informed choice and grievances matter.',
'Recommend transparent beneficiary records, timely support and independent post-relocation outcomes. Do not infer all obligations were fulfilled on approval day.'])]
lines=['# April 2026 · Eight original Mains frameworks','','Original answer-planning aids, not official model answers or predictions. Preserve legal stages, data vintages and source limitations.']
for i,title,plan in F:
 n=N[ref(i)];lines+=['','## '+title,'','**Study reference:** '+n['id'],'','**Dated anchor:** '+n['why'],'']+[f'{j}. {x}' for j,x in enumerate(plan,1)]+['','**Evidence caution:** '+n['trap'],'','**Conclusion test:** Identify the responsible institution, the financing/rights safeguard and a measurable outcome.']
(R/'volumes/April-2026-Mains-Frameworks.md').write_text('\n'.join(lines)+'\n')
print('Created30MCQs/eightMainsframeworks')
