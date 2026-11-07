import json,pathlib,random
R=pathlib.Path(__file__).resolve().parents[1];N={n['id']:n for n in json.loads((R/'data/notes.json').read_text())}
def ref(i):return f'E10-2603-{i:03}'
rows='''2~Consider the March BoP release: 1. Its quarterly reference period is October–December 2025. 2. The US$13.2 billion figure is the merchandise deficit. 3. Reserve depletion is stated on a BoP basis. Which are correct?~1 and 3 only.~1 and 2 only.|2 and 3 only.|1, 2 and 3.
3~A report quotes manufacturing growth of 6.3% alongside overall IIP growth of 5.3%. In this note, these describe:~Year-on-year changes for October–December 2025, not March monthly output.~Final March 2026 GDP growth.|Services output within IIP.|The same growth rate for every industrial sector.
4~Which statement is supported by the transgender amendment research recorded here?~Parliamentary passage dates are checked, while Gazette assent and commencement were not independently inspected.~Rajya Sabha passage alone proves every provision was operative that day.|Gender identity and sexual orientation are identical legal concepts.|A later constitutional challenge is presumed already decided.
5~The adoptive-maternity ruling reviewed here removed which restriction?~The adopted child’s three-month age limit for the specified 12-week leave entitlement.~All employment-related coverage conditions for every person.|Every distinction between adoption and childbirth leave.|All limits on the duration of maternity leave.
5~Which inference about paternity leave is justified by Hamsaanandini Nanduri?~The Court urged consideration of a provision; this is not itself a universal enacted entitlement.~All fathers received an automatic statutory 26-week leave entitlement.|The Court prohibited Parliament from legislating on paternity leave.|The observation applies only to biological mothers.
7~Decriminalisation in regulatory reform necessarily means:~None of the alternatives: duties and administrative or monetary enforcement may remain.~Repeal of every underlying Act.|Removal of all penalties for every covered activity.|Conversion of every violation into a constitutional right.
8~A proposal for administration of specified foreign-contribution assets should be treated as:~A proposed mechanism whose triggers and safeguards require the text and eventual legal stage.~Immediate confiscation of all domestic NGO property.|A completed repeal of foreign-contribution registration.|Proof all charitable work has ceased.
9~Under the March FDI press note, a third-country investor has a land-border-linked interest below a company ownership threshold but effective control exists. Which is the sound approach?~Examine control, aggregation, sector conditions and commencement; do not rely on the percentage alone.~Treat the investment as unconditionally exempt from every approval.|Ignore indirect interests because the immediate investor is elsewhere.|Assume a press note automatically overrides every sectoral cap.
9~What does the primary FDI note state about commencement?~The decision takes effect from the FEMA notification.~The publication date alone makes every change effective.|Each foreign investor chooses its own effective date.|The note abolishes all future reporting requirements.
10~Restoration of RoDTEP rates and value caps means:~Restoring the applicable remission framework, not granting 50% of every export invoice.~A uniform cash subsidy equal to half of every invoice.|Automatic compensation for every freight increase.|A guarantee no exporter can suffer losses.
11~The Digital Trade Facilitation draft’s chronology is best stated as:~A 9 February DGFT consultation carried forward in the March review.~A bill first published on 31 March solely because that is the index date.|An already commenced Act from the 2025 Budget speech.|A March parliamentary amendment verified from the Gazette.
12~India–Canada CEPA terms of reference signed in March establish:~A basis for negotiations, not an implemented tariff-elimination schedule.~Automatic entry into force of a final agreement.|A binding zero-tariff rate for every product immediately.|Completion of every domestic ratification process.
14~The proposed ₹10 crore CSR threshold should not be interpreted as:~A mandatory ₹10 crore CSR payment by every company.~A proposal concerning an applicability test.|A subject for legislative scrutiny.|Distinct from the percentage spending requirement.
16~Under the reviewed draft compensation formula, an otherwise eligible net loss of ₹20,000 would give what proposed amount before any other condition is applied?~₹17,000, because 85% is below the ₹25,000 cap.~₹25,000 regardless of the loss.|₹50,000 because that is the reviewed loss ceiling.|₹20,000 because all eligible losses are fully refunded.
17~A SEBI board announcement accepting conflict reforms is best distinguished from:~A separately operative notified instrument implementing each recommendation.~A policy-level decision.|An expression of institutional intent.|A subject for governance analysis.
18~The aviation direction on 60% free seat allocation concerns:~The seat-allocation charge, not a promise that 60% of passengers fly without paying airfare.~Abolition of 60% of ticket fares and taxes.|Reservation of all seats for the government.|An unconditional right to business-class travel.
19~Which pair matches Modified UDAN’s approved design?~FY2026–27 to FY2035–36; ₹28,840 crore support.~Calendar 2026 alone; ₹28,840 lakh support.|100 already commissioned new greenfield airports; no operating support.|200 operational helipads certified on approval day; no VGF.
24~A draft mineral-exchange framework can improve price discovery, but does not itself:~Create mineral deposits or replace mining and other applicable permissions.~Require attention to assaying.|Raise questions about delivery risk.|Need transparent governance.
26~Which JJM 2.0 comparison is correct?~₹8.69 lakh crore is total outlay; ₹3.59 lakh crore is total central assistance.~Both amounts are the same measure with different spellings.|₹8.69 lakh crore is already-spent Union assistance.|₹1.51 lakh crore is the entire original and revised mission cost combined.
27~Consider the 2035 NDC targets: 1. The 47% target concerns GDP emissions intensity versus 2005. 2. The 60% target concerns non-fossil installed electricity capacity. 3. They guarantee a 47% absolute emissions cut and 60% renewable generation. Which are correct?~1 and 2 only.~1 and 3 only.|2 and 3 only.|1, 2 and 3.
31~Approval of BHAVYA establishes:~A programme design for industrial parks, not proof that 100 parks are complete and occupied.~Completed production in 100 selected AP parks.|An unconditional grant to every industrial landowner.|Automatic demand for every tenant’s output.
33~AP’s FHI 2026 profile is correctly described as:~17th of 18 major states overall, with a different Front Runner classification for expenditure quality.~An overall Front Runner because one pillar is 43.1.|A live audit of March2026 accounts.|First nationally across a single combined major/NE/Himalayan cohort.
34~Which EIA claim should be rejected?~Every project above ₹50 crore is subject to one identical universal EIA test.~Project category and scheduled thresholds matter.|Appraisal institutions require qualified capacity.|A draft amendment needs a separate final-law check.
35~A seventh CBD national report is best used as:~An official reporting input to assess against indicators, not independent proof every target has been achieved.~A replacement for all ecological field evidence.|Proof forest-and-tree cover equals undisturbed natural forest.|A guarantee all invasive-species risks are resolved.
37~Which pairing is correct for the LHCb discovery?~Xi-cc-plus—ccd composite baryon; meson—quark–antiquark pair.~Xi-cc-plus—new fundamental quark; meson—two identical quarks only.|Xi-cc-plus—chemical element; meson—atomic nucleus.|Xi-cc-plus—ordinary electron; meson—three valence quarks.
38~ISRO’s short statement on IRNSS-1F supports which conclusion?~Navigation-clock failure can coexist with continued one-way broadcast messaging.~Every payload and function of the satellite permanently stopped.|Every NavIC satellite lost its clock on the same day.|The page independently certifies a live constellation-wide operating count.
39~20 March 2026 is correctly related to Mahad’s 20 March1927 action as:~99 completed years; the 100th anniversary falls in 2027.~The completed 100th anniversary.|The first anniversary of the event.|The date of the December1927 Manusmriti-burning action.
41~The March AP Assembly resolution on Amaravati was:~A request for statutory amendment, not itself Parliament’s amendment of the central Act.~An automatic amendment of section 5 by the Assembly.|Proof that the Act can never be amended again.|A completed record of every capital project’s construction.
47~Which distinction is important in Chinthada Anand?~The SC Order’s religion-based rule must not be mechanically applied as an identical ST exclusion, and ordinary criminal allegations need separate legal/evidentiary analysis.~All ST status automatically ends on any conversion.|Statutory SC eligibility decides whether social discrimination can ever occur.|Loss of a particular status makes violence against the person lawful.
48~AP’s reported 50% municipal property-tax interest relief means:~A concession concerning the interest component, not automatic halving of principal property tax.~Half of every household’s entire tax liability is extinguished.|Every municipal arrear has been collected.|No implementing conditions or deadlines can apply.'''
Q=[];rng=random.Random(10)
for line in rows.splitlines():
 i,q,right,wrong=line.split('~');n=N[ref(int(i))];opts=[right]+wrong.split('|');rng.shuffle(opts)
 Q.append(dict(id=f'MAR26-{len(Q)+1:02}',question=q,options=opts,answer=opts.index(right),explanation=n['static_link']+' '+n['analysis'][0]+' Caution: '+n['trap'],ref=n['id']))
assert len(Q)==30
# Tailor the two calculations/status questions rather than rely only on a shared note excerpt.
Q[13]['explanation']='85% × ₹20,000 = ₹17,000, below the ₹25,000 cap. The calculation is conditional on draft eligibility; it is not a statement that the scheme was already operative.'
(R/'data/2026-03-mcqs.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
F=[
(2,'How should India manage external vulnerability during an energy shock?',[
'Anchor the 2 March release: Q3 CAD US$13.2 billion/1.3% of GDP; identify the reference quarter as October–December2025.',
'Map transmission: import bill, freight/insurance, input costs, inflation, exchange-rate pressure and external financing.',
'Explain cushions: services, remittances, reserves and diversified supply; each has different limits and time horizons.',
'Counterpoint: suppressing all price signals can shift costs to budgets, while abrupt pass-through can harm vulnerable households.',
'Recommend targeted support, transparent contingency planning, efficiency and stable external-financing policy. Distinguish BoP-basis reserve flows from valuation-driven stock changes.']),
(5,'Examine adoptive-maternity protection through substantive equality.',[
'Use the 17 March ruling’s removal of the adopted child’s three-month age restriction; preserve the specified 12-week entitlement.',
'Explain why caregiving and attachment needs are not confined to infancy or biological childbirth.',
'Link Articles14/21 to dignity and non-arbitrary classification without assuming every statutory coverage condition was struck down.',
'Address implementation: employer awareness, accessible claims and protection against adverse workplace treatment.',
'Propose a wider shared-care framework, while distinguishing the Court’s paternity-leave suggestion from an enacted universal entitlement.']),
(9,'Can transparent investment screening reconcile capital access and economic security?',[
'Anchor DPIIT Press Note2, 15 March, and its explicit dependence on a FEMA notification for effect.',
'Explain indirect ownership, entity-specific thresholds, aggregated interests and ultimate effective control.',
'Benefits: predictable rules can reduce uncertainty for diversified funds while preserving review of controlled investments.',
'Risks: layered entities, information asymmetry, discretionary delay and weak enforcement can defeat both investment and security aims.',
'Recommend clear reporting, auditable beneficial-ownership information, reasoned decisions and timelines; retain sectoral caps and do not use a percentage as the sole test.']),
(26,'How can JJM move from counting connections to assuring rural water services?',[
'Anchor the December2028 extension and separate total outlay ₹8.69 lakh crore from central assistance ₹3.59 lakh crore.',
'Map source sustainability, treatment, distribution, household availability, quality testing and repair response.',
'Use Sujalam Bharat mapping, Jal Arpan and GP/O&M certification as accountability mechanisms rather than outcomes already proved.',
'In AP, connect water-stressed sources, local maintenance finance and village capacity; avoid treating a tap as proof of year-round safe supply.',
'Recommend service-level disclosure, inclusive community oversight and maintenance support. Measure downtime, quality and household reliability, not only assets built.']),
(27,'Assess the implementation challenge in India’s 2035 climate commitments.',[
'State the targets accurately: 47% GDP-intensity reduction versus2005, 60% non-fossil installed capacity, and the specified forest/tree carbon sink.',
'Explain intensity versus absolute emissions and capacity versus generation; non-fossil includes more than renewables.',
'Map implementation needs across power networks/storage, industrial efficiency, finance, livelihoods and ecological restoration.',
'Counterpoint: nominal capacity additions may underdeliver without grid integration; forest quantity can hide ecological-quality problems.',
'Recommend sectoral milestones and transparent monitoring. Cabinet approval is not independently verified UNFCCC submission, and the 2070 net-zero goal is distinct.']),
(33,'What does AP’s Fiscal Health Index profile imply for fiscal reform?',[
'Identify the data vintage: FHI2026 assesses FY2023–24; AP ranks17/18 major states with23.1 overall.',
'Distinguish the expenditure-quality pillar43.1/Front Runner from the overall Aspirational classification.',
'Diagnose revenue mobilisation, fiscal prudence, debt index and debt sustainability alongside productive-spending quality.',
'Discuss trade-offs: abrupt expenditure cuts can damage services, while weak project appraisal and contingent liabilities can compound debt risk.',
'Recommend better own-revenue administration, credible medium-term planning, transparent guarantees and outcome-based capital selection; do not invent March2026 audited conclusions.']),
(34,'How can environmental clearance be timely without weakening scrutiny?',[
'Anchor the draft standing-state-body proposal as a response to institutional vacancies and delays, not verified final law.',
'Explain the scheduled-project/category framework; explicitly reject a universal ₹50-crore EIA test.',
'Benefits: continuity, digital routing and clear appraisal responsibilities can reduce avoidable uncertainty.',
'Risks: poor expertise, rushed public consultation, conflicts and deadline-driven rubber-stamping can undermine environmental legitimacy.',
'Recommend adequate capacity, transparent reasons, participation and compliance monitoring. Institutional delay should not be treated as automatic environmental approval.']),
(47,'Explain notified social status, legal protection and evidence in the AP-linked SC-status ruling.',[
'Anchor Chinthada Anand, 24 March, and paragraph3 of the SC Order1950; distinguish the challenged HC order’s 30 April2025 date.',
'Explain that SC-status-dependent benefits must follow the notified legal framework and the Court’s treatment of the claimant’s facts.',
'Preserve the explicit ST distinction: no equivalent religion-based exclusion; the Court describes a fact-sensitive tribal-identity assessment.',
'Analyse ordinary IPC allegations separately; case-specific evidentiary findings do not extinguish universal criminal-law protection or deny persistent social discrimination.',
'Conclude with careful status verification, due process and avoidance of sweeping generalisations. This is an answer framework, not individual legal advice.'])]
lines=['# March 2026 · Eight original Mains frameworks','','Original planning aids, not official model answers or predictions. Facts, static connections and proposed reforms remain distinct.']
for i,title,plan in F:
 n=N[ref(i)];lines+=['','## '+title,'','**Study reference:** '+n['id'],'','**Dated anchor:** '+n['why'],'']+[f'{j}. {x}' for j,x in enumerate(plan,1)]+['','**Evidence caution:** '+n['trap'],'','**Conclusion test:** Identify the institution, financing/rights safeguard and measurable outcome rather than merely restating the proposal.']
(R/'volumes/March-2026-Mains-Frameworks.md').write_text('\n'.join(lines)+'\n')
print('Created 30 MCQs and eight Mains plans')
