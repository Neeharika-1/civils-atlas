"""February 2025 original notes and traceable evidence provenance. Not a completeness certificate."""
import pathlib,json
R=pathlib.Path(__file__).resolve().parents[1];N=json.loads((R/'data/notes.json').read_text());S=json.loads((R/'data/sources.json').read_text());A=json.loads((R/'data/source-access.json').read_text());J=[]
def source(k,t,u,full=False):
 S[k]=[t,u];A[k]=dict(title=t,url=u,access='Full substantive web text read; linked original documents not necessarily independently read' if full else 'Search-result source extract inspected; full document review pending',checked_on='2026-11-06',method='Assistant-led web research; no independent human editorial certification')
source('F-PRS','PRS · February 2025 monthly review; all five chunks read','https://prsindia.org/policy/monthly-policy-review/february-2025',True)
source('F-UB','PRS · Union Budget 2025–26 web analysis; both chunks read','https://prsindia.org/budgets/parliament/union-budget-2025-26-analysis',True)
source('F-APB','PRS · AP Budget 2025–26 web analysis; both chunks read','https://prsindia.org/budgets/states/andhra-pradesh-budget-analysis-2025-26',True)
source('F-SPEECH','Finance Ministry · Budget speech, 1 February; source extracts inspected','https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/feb/doc202521493201.pdf')
source('F-HIGHLIGHTS','PIB · Union Budget highlights, 1 February; PDF extracts','https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/feb/doc202521492701.pdf')
source('F-DETAIL','PIB · Budget sectoral releases, 1 February; PDF extracts','https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/feb/doc202521492801.pdf')
source('F-RBI','RBI · MPC resolution, 7 February; primary reference through PRS','https://rbidocs.rbi.org.in/rdocs/PressRelease/PDFs/PR2094189B0DF105514A28A2FA834330E94B26.PDF')
source('F-GDP','MoSPI · Second advance estimates and Q3 GDP, 28 February; reference through PRS','https://www.mospi.gov.in/sites/default/files/press_release/PRESS-NOTE-ON-SAE-2024-25-Q3-2024-25-FRE-2023-24-and-FE-2022-23-M.pdf')
source('F-SKILL','PIB · Skill India continuation, 7 February; reference through PRS','https://pib.gov.in/PressReleaseIframePage.aspx?PRID=2100845')
source('F-CBSE','CBSE · Draft Class X examination policy, 25 February; reference through PRS','https://www.cbse.gov.in/cbsenew/documents/SCHEME_BOARD_EXAMS_POLICY_25022025.pdf')
source('F-US','MEA · India–US joint statement, 13 February; through PRS','https://www.mea.gov.in/bilateral-documents.htm?dtl/39066')
source('F-FRANCE','MEA · India–France AI declaration, 12 February; through PRS','https://www.mea.gov.in/bilateral-documents.htm?dtl/39034/IndiaFrance_Declaration_on_Artificial_Intelligence_February_12_2025')
source('F-UK','ANI · India–UK FTA negotiations resume, 24 February','https://www.bignewsnetwork.com/news/278063349/india-uk-resume-negotiations-on-free-trade-agreement')
source('F-NAKSHA','PIB · NAKSHA launch preview, 17 February','https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2104028&reg=48&lang=2')
source('F-NAKSHA2','The Hindu · NAKSHA launch, 18 February','https://www.thehindu.com/news/national/karnataka/naksha-project-for-urban-properties-launched-in-mysuru/article69234375.ece')
source('F-CEC','CNBC-TV18 · Gyanesh Kumar assumes charge, 19 February','https://www.cnbctv18.com/india/gyanesh-kumar-takes-charge-as-chief-election-commissioner-amid-supreme-court-review-19561123.htm')
source('F-CEC2','PTI / The Print · CEC and EC appointments, 17 February','https://theprint.in/india/gyanesh-kumar-is-the-new-chief-election-commissioner-vivek-joshi-appointed-election-commissioner/2499603/')
source('F-MANIPUR','PTI / BusinessLine · President’s Rule, 13 February','https://www.thehindubusinessline.com/news/national/presidents-rule-imposed-in-manipur/article69215938.ece')
source('F-LOKPAL','The Hindu · Interim stay of Lokpal order, 20 February','https://www.thehindu.com/news/national/supreme-court-stays-lokpals-order-that-it-has-jurisdiction-over-high-court-judges/article69241461.ece')
source('F-TNGOV','Supreme Court Observer · Judgment reserved on 10 February; dated account 11 February','https://www.scobserver.in/reports/pendency-of-bills-in-tamil-nadu-day-10-supreme-court-reserves-judgement/')
source('F-DELHI','Times Now · ECI results reporting, 8 February','https://www.timesnownews.com/india/election-commission-of-india-delhi-results-2025-live-arvind-kejriwal-eci-delhi-bjp-aap-congress-results-eci-gov-in-latest-news-today-liveblog-118044259')
source('F-DELHI2','Wikiwand · Delhi election/20 February oath; secondary cross-check','https://www.wikiwand.com/en/articles/2025_Delhi_Legislative_Assembly_election')
source('F-CBD','Down To Earth · Rome biodiversity agreement, 28 February','https://www.downtoearth.org.in/wildlife-biodiversity/cbd-cop16-secures-landmark-biodiversity-funding-agreement')
source('F-CBD2','FAO · Resumed COP16 outcomes; retrospective corroboration','https://www.fao.org/biodiversity/news/detail/achievements-for-biodiversity-at-resumed-meeting-of-cop16/en')
source('F-WETLAND','PIB · World Wetlands Day, 2 February','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2098981&reg=48&lang=2')
source('F-EUAI','European Commission · AI Act application timeline; live page may contain later amendments','https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai')
source('F-EUAI2','Mayer Brown · First AI Act requirements; February 2025 account','https://www.mayerbrown.com/en/insights/publications/2025/01/eu-ai-act-ban-on-certain-ai-practices-and-requirements-for-ai-literacy-come-into-effect')
source('F-CE20','ISRO · 7 February CE20 vacuum ignition test; posted 8 February','https://www.isro.gov.in/LVM3_CE20_vacuum_ignition_trial_cryogenic_engine_successful.html')
source('F-EUCLID','ESA · Euclid Einstein ring around NGC6505, 10 February','https://www.esa.int/ESA_Multimedia/Images/2025/02/Close-up_of_the_Einstein_ring_around_galaxy_NGC_6505')
source('F-NEUTRINO','KM3NeT · 12 February ultra-high-energy neutrino announcement','https://www.km3net.org/km3net-detects-the-highest-energy-neutrino-ever-observed/')
source('F-ASTEROID','NASA · 2024 YR4 risk update, 24 February','https://science.nasa.gov/blogs/planetary-defense/2025/02/24/latest-calculations-conclude-asteroid-2024-yr4-now-poses-no-significant-threat-to-earth-in-2032-and-beyond/')
source('F-EBOLA','WHO · Sudan-virus vaccine efficacy trial, 3 February, corrected 4 February','https://www.who.int/news/item/03-02-2025-groundbreaking-ebola-vaccination-trial-launches-today-in-uganda')
source('F-ENERGY','PIB · India Energy Week conclusion, 14 February','https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2103188&reg=3&lang=2')
source('F-AERO','PIB · Aero India preview, 9 February','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2101170&reg=48&lang=2')
source('F-TROPEX','PIB · TROPEX operational update, 7 February','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2100813&reg=48&lang=2')
source('F-APCAB','The New Indian Express · AP Cabinet decisions of 6 February, reported 7 February','https://www.newindianexpress.com/states/andhra-pradesh/2025/Feb/07/ap-cabinet-approves-enhanced-subsidies-for-sc-st-bc-minority-women-entrepreneurs')
source('F-APFLU','The New Indian Express · Confirmed poultry H5N1, 11 February','https://www.newindianexpress.com/states/andhra-pradesh/2025/Feb/11/public-urged-not-to-eat-chicken-as-bird-flu-confirmed-in-east-godavari-district')
source('F-APSESSION','The New Indian Express · AP legislature session preview, 23 February','https://www.newindianexpress.com/states/andhra-pradesh/2025/Feb/23/andhra-pradesh-budget-session-begins-as-ysrcp-reconsiders-boycott')
source('F-APNEWS','The Hindu · AP Budget live reporting, 28 February','https://www.thehindu.com/news/national/andhra-pradesh/andhra-pradesh-budget-for-2025-2026-live-updates-february-28-2025/article69273299.ece')
source('F-SLBC','BusinessLine · SLBC tunnel collapse, 22 February; updated 24 February','https://www.thehindubusinessline.com/news/slbc-tunnel-mishap-live-8-workers-trapped-13-injured-rescue-operations-underway/article69250594.ece')
source('F-GAMES','The Bridge · National Games results, 14 February','https://thebridge.in/national-games/38th-national-games-services-reign-supreme-tops-medal-tally-52059')
source('F-SCIENCEDAY','PIB · National Science Day 2025, 27 February','https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2106574&reg=48&lang=2')
source('F-JHUMOIR','PIB · Jhumoir Binandini, 24 February','https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2105906&reg=3&lang=2')
source('F-GERMANY','The Telegraph · German election, 23 February; provisional results account','https://www.telegraph.co.uk/world-news/2025/02/23/germany-election-conservatives-projected-win-afd-second/')
source('F-CRICKET','Olympics.com · Champions Trophy schedule and venues, 17 February','https://www.olympics.com/en/news/icc-men-champions-trophy-2025-schedule-fixtures-matches-teams-dates')
def add(subject,block,day,title,why,facts,static,analysis,trap,mains,src,priority='P1',ap=False,precision='day'):
 J.append(dict(id=f'FEB25-{len(J)+1:03}',subject=subject,block=block,date=f'2025-02-{day:02}',date_precision=precision,title=title,why=why,facts=facts.split('|'),static_link=static,analysis=analysis.split('|'),trap=trap,mains=mains,sources=src.split(','),priority=priority,ap=ap,status='February historical snapshot; later legal/operational changes need separate review',checked='2026-11-06',evidence_access='Full PRS web synthesis read; linked primary texts not necessarily independently read' if any(k in src.split(',') for k in ['F-PRS','F-UB','F-APB']) else 'Supporting source extract(s) inspected; full-document review pending'))
add('Economy','06 · Growth, inflation & statistics',7,'RBI cuts the repo rate to 6.25%','The February MPC reduced the policy rate by 25 basis points while retaining a neutral stance.',
'Repo moved from 6.50% to 6.25%.|Standing Deposit Facility moved to 6.00%.|MSF and Bank Rate moved to 6.50%.|The MPC maintained the 4% inflation-target focus while supporting growth.',
'The repo rate is a policy instrument, not every borrower’s contracted loan rate. Transmission depends on funding costs, loan benchmarks and bank balance sheets.',
'A cut can support demand and reduce some debt-service costs, but transmission is uneven and not instantaneous.|A neutral stance is not a promise of uninterrupted future cuts; incoming inflation and growth evidence remains relevant.',
'25 basis points is 0.25 percentage point, not a 25% rate cut. These are February rates, not current rates.',
'Why may a repo-rate cut fail to translate into an equally large immediate reduction in all lending rates?','F-PRS,F-RBI')
add('Economy','06 · Growth, inflation & statistics',28,'GDP: Q3 growth and the second advance estimate','MoSPI’s release revised both current-year projections and earlier-year estimates.',
'Real Q3 FY2024–25 GDP growth was 6.2%, versus 9.5% in the corresponding prior-year quarter at this vintage.|The second advance FY2024–25 growth estimate was 6.5%, versus January’s 6.4%.|FY2023–24 growth was revised from 8.2% to 9.2%.|Q3 agriculture GVA grew 5.6%; manufacturing 3.5%.',
'A statistical vintage matters: revisions alter historical comparisons. Quarterly year-on-year growth, annual growth and sequential growth are distinct.',
'Use this note to understand why January’s and February’s prior-year numbers differ without assuming one was fabricated.|Sector differences suggest targeted productivity and investment questions, rather than treating aggregate recovery as uniform prosperity.',
'Do not mix January’s unrevised 8.2% prior-year figure with February’s revised series without disclosure. These are not certified latest-series values.',
'How should statistical revisions change economic analysis and public communication?','F-PRS,F-GDP')
add('Economy','06 · Growth, inflation & statistics',12,'Industrial production: December and Q3 readings','The monthly release completed the October–December industrial picture.',
'December 2024 IIP growth was 3.2%.|PRS computed Q3 growth at 3.9%, compared with 6.1% a year earlier.|Q3 manufacturing grew 4.3%, mining 1.8%, electricity 4.1%.|Manufacturing carries about 78% of the IIP weight.',
'IIP measures physical output movements in selected industries. It is not identical to manufacturing GVA or the whole economy’s GDP.',
'Compare broad groups and use categories to examine whether capital-goods and consumer demand are strengthening.|A positive but slower growth rate means expansion at a reduced pace, not necessarily contraction.',
'3.2% is the December monthly reading; 3.9% is the quarterly average growth described by PRS. Do not substitute one for the other.',
'Why should policymakers use IIP alongside GDP, employment and business surveys rather than as a standalone verdict?','F-PRS',priority='P2')
add('Economy','02 · Taxation',13,'Income-Tax Bill 2025: introduction, not enactment','A new Bill sought to replace the Income-Tax Act, 1961 and was referred to a Select Committee.',
'The February Bill retained most substantive provisions and did not itself recast individual/corporate tax rates.|It proposed a 1 April 2026 commencement.|It addressed virtual digital assets in undisclosed income and access to virtual digital space during search proceedings.|New scheme-making powers and parliamentary laying requirements were described by PRS.',
'A tax-code replacement Bill and the annual Finance Bill are different instruments. Introduction, passage, assent and commencement are separate stages.',
'Simpler drafting can reduce compliance uncertainty but must be tested against actual taxpayer experience.|Expanded digital-search powers raise necessity, scope, privacy and remedy questions beyond the goal of language simplification.',
'Do not attribute February’s tax slabs to this replacement Bill rather than the Budget/Finance Bill. Later withdrawal or replacement versions must be traced separately.',
'How can tax simplification preserve enforceability while limiting discretionary intrusion?','F-PRS')
add('Economy','08 · Financial inclusion & markets',21,'Draft foreclosure-charge protections','RBI consulted on switching costs for floating-rate business loans.',
'The draft addressed loans to individuals and micro/small enterprises.|It proposed no foreclosure/prepayment penalty on specified floating-rate business loans.|For MSEs, the described aggregate sanctioned limit was ₹7.5 crore per borrower.|Comments were invited until 21 March; no minimum lock-in was proposed for covered prepayment.',
'Floating-rate loans differ from fixed-rate contracts. Lower exit costs can increase lender competition but do not erase the outstanding principal.',
'Restrictive exit clauses can prevent borrowers accessing lower rates or better service.|Final rules need clear scope and disclosures so fees are not simply relabelled elsewhere.',
'This was a draft, not a February universal ban on every charge for every loan. Micro/small is not automatically all medium enterprises.',
'How can borrower mobility improve credit-market competition?','F-PRS',priority='P2',ap=True)
add('Society & Welfare','02 · Education & skills',7,'Skill India continuation and restructuring','Cabinet continued a three-component skills programme.',
'The package includes PM Kaushal Vikas Yojana, PM National Apprenticeship Promotion Scheme and Jan Shikshan Sansthan.|The outlay was ₹8,800 crore for FY2022–23 to FY2025–26.|PMKVY covers short-term/on-job training; apprenticeship support links learners and establishments.|JSS focuses on accessible vocational training for disadvantaged groups.',
'Training enrolment, certification, employment and sustained wage gains are different outcome levels. Apprenticeship combines workplace learning with a formal arrangement.',
'Demand-linked training needs employer participation and credible assessment.|For AP, monitor placement quality, retention, inclusion and regional access rather than only numbers trained.',
'₹8,800 crore is a multi-year total, not a fresh annual grant. The three schemes are not interchangeable names.',
'What indicators would demonstrate that skills spending improves productive employment?','F-PRS,F-SKILL',ap=True)
add('Society & Welfare','03 · Education evidence & learning',25,'CBSE draft: two Class X examination opportunities','The consultation proposed a second annual opportunity from 2026.',
'The draft envisaged examinations in February–March and May.|Both examinations would use the same syllabus and centres.|First-exam results could support Class XI admission through DigiLocker.|Final passing-document arrangements and conditional admissions were described in the draft.',
'An additional opportunity can change high-stakes assessment incentives. CBSE policy is not automatically every state board’s policy.',
'A second chance may reduce one-shot pressure, but can also increase coaching and administrative load.|Schools need counselling, scheduling and equitable access so disadvantaged pupils can benefit.',
'The February text was a draft; do not assert final 2026 dates or identical rules for the AP board from it.',
'How can board-exam reform reduce stress without weakening assessment credibility?','F-PRS,F-CBSE',ap=True)
add('Polity & Governance','12 · Cooperatives & institutions',3,'Tribhuvan Sahkari University Bill','The proposed university sought specialised education for the cooperative sector.',
'The Bill proposed establishing IRMA, Anand, within the university framework.|Objectives include cooperative education, training, research and capacity building.|PRS describes a VC, executive council and governing board with central appointment roles.|IRMA’s autonomous identity was to be preserved within the proposed structure.',
'Cooperative capability depends on member governance, accounts, professional management and market access—not institutional naming alone.',
'Sector-specific education can strengthen audit, logistics and digital skills.|The design should preserve member-centred values and academic quality rather than substitute centralised administration for cooperative autonomy.',
'A Bill introduced on 3 February is not proof the university was fully operational or every programme accredited that month.',
'How can professionalisation strengthen cooperatives without weakening democratic member control?','F-PRS',priority='P2',ap=True)
add('Economy','11 · Transport & infrastructure',10,'Aircraft Objects Bill and the Cape Town framework','The Rajya Sabha introduction addressed rights over high-value aviation assets.',
'The Bill sought legal effect for the Cape Town Convention and Aircraft Protocol.|India had acceded to those agreements in 2008.|It described creditor remedies after default, DGCA notification and specified asset-detention rights.|Aircraft, helicopters and engines fall within the relevant asset framework.',
'Predictable repossession/security rights can affect leasing cost and financing risk. Treaty accession and effective domestic implementation are distinct.',
'Clear remedies may improve access to aircraft finance and reduce uncertainty.|The policy must reconcile creditor rights, public-service dues and orderly resolution when an airline fails.',
'This was introduction, not completed enactment. It was not a blanket cancellation of every airline debt or a passenger-compensation law.',
'Why does legal certainty in asset leasing matter for affordable and reliable aviation?','F-PRS')
add('International Relations','04 · India–US & technology diplomacy',13,'India–US talks: trade, defence and technology intent','The joint statement outlined a programme for deeper bilateral cooperation.',
'The two sides targeted bilateral trade of US$500 billion by 2030.|They sought a first tranche of a bilateral trade agreement in 2025.|A new ten-year defence framework and expanded technology cooperation were envisaged.|Energy trade and possible localised US-designed nuclear-reactor cooperation were discussed.',
'A joint statement expresses agreed intent; procurement, treaty commitments, commercial contracts and operational projects require distinct follow-up.',
'India can pursue market access and technology while diversifying strategic options.|Evaluate local capability, commercial viability and regulatory conditions rather than assume promised trade is already achieved.',
'The US$500 billion figure is a target, not February realised trade. A procurement discussion is not a signed purchase contract.',
'What makes a strategic partnership translate into durable domestic capability?','F-PRS,F-US')
add('International Relations','03 · Indo-Pacific & bilateral relations',12,'France visit and the AI declaration','India and France linked AI cooperation with privacy, diversity and scientific collaboration.',
'The countries signed an AI declaration on 12 February.|PRS records principles of global benefit, human rights/privacy and linguistic/cultural diversity.|Intent included an Indo-French Centre of Digital Sciences and work on advanced/SMR technology.|Defence R&D cooperation was also discussed.',
'AI governance includes access, safety, data, compute and market structure. A bilateral declaration is not a binding global AI treaty.',
'Public-interest AI requires affordable compute and meaningful participation by under-represented languages.|Research collaboration should be assessed by interoperable standards and shared capability, not diplomatic vocabulary alone.',
'Do not treat intent on reactors or research centres as proof of completed facilities. France’s bilateral declaration differs from the wider summit outcome.',
'How can international AI cooperation balance innovation, inclusion and rights?','F-PRS,F-FRANCE')
add('International Relations','08 · Trade negotiations',24,'India–UK FTA negotiations resume','The two governments restarted negotiations after a pause.',
'Piyush Goyal and Jonathan Reynolds announced resumption.|The aim was a balanced, mutually beneficial agreement.|Goods, services and investment issues were among the negotiating concerns.|Parallel investment/social-contribution discussions were reported separately.',
'Negotiation, political conclusion, signature, ratification and entry into force are different trade-agreement stages.',
'Potential gains depend on actual tariff schedules, rules of origin and services access.|AP exporters need product-level opportunities and standards capacity rather than a generic assumption that every export becomes duty-free.',
'The February restart is not the date a final FTA entered into force. Later milestones must be indexed separately.',
'How should India evaluate a trade agreement beyond the number of tariff lines liberalised?','F-UK',ap=True)
add('Polity & Governance','13 · Land records & spatial governance',18,'NAKSHA: urban land-record pilot','The pilot launched with aerial mapping and field validation.',
'NAKSHA stands for National Geospatial Knowledge-based Land Survey of Urban Habitations.|The announced pilot covered 152 ULBs across 26 states and three UTs.|The launch was at Raisen, Madhya Pradesh; the approximate central cost was ₹194 crore.|Survey of India provides technical support; states undertake ground verification.',
'Urban record mapping is distinct from rural abadi mapping under SVAMITVA. Geometry, possession and legally established ownership are not automatically the same.',
'Mapping can support planning, taxation and transparent transactions.|Public objections, correction procedures and safeguards for tenants/informal residents are necessary to avoid digitising existing inequities.',
'A pilot is not nationwide completed coverage. A high-resolution map does not by itself finally adjudicate every title dispute.',
'How can urban land digitisation improve governance without increasing exclusion?','F-NAKSHA,F-NAKSHA2',ap=True)
add('Culture & History','03 · Manuscripts & knowledge heritage',1,'Gyan Bharatam Mission proposed','The Budget proposed a large manuscript-survey and conservation effort.',
'The stated coverage ambition was more than one crore manuscripts.|Academic institutions, museums, libraries and private collectors were identified as partners.|Survey, documentation and conservation were core tasks.|The speech also envisaged wider digital access to knowledge heritage.',
'Cataloguing, physical conservation, digitisation, transcription and translation are distinct stages. A digital image is not necessarily searchable or understood text.',
'Preservation requires suitable storage and trained conservators alongside scanning.|Access should respect provenance, linguistic diversity and legitimate community/owner interests.',
'One crore is a proposed coverage target, not manuscripts already conserved in February. A new mission does not erase earlier manuscript initiatives.',
'What would a credible national manuscript-preservation strategy require beyond digitisation?','F-SPEECH,F-DETAIL',priority='P2',ap=True)
add('Economy','03 · Industry & MSMEs',1,'MSME credit package: guarantees and micro credit cards','The Budget proposed distinct credit tools for different enterprise segments.',
'Guarantee cover was proposed to rise from ₹5 crore to ₹10 crore for micro/small enterprises.|For start-ups, the proposed cover rose from ₹10 crore to ₹20 crore.|Exporter MSMEs were assigned a separate proposed cover up to ₹20 crore.|Ten lakh Udyam-registered micro-enterprise credit cards with ₹5 lakh limits were envisaged in the first year.',
'A credit-card limit, guaranteed-loan cover and an investment-classification threshold are different numbers. None is an unconditional cash transfer.',
'Different instruments address working-capital, collateral and export-finance constraints.|Evaluation needs additional viable lending, borrower cost, defaults and access by truly small firms.',
'Do not mix this Budget package with January’s separate machinery guarantee scheme or treat ten lakh cards as already issued.',
'How can enterprise-finance policy improve access without hiding contingent public liabilities?','F-UB',ap=True)
add('Economy','11 · Transport & infrastructure',1,'Maritime Development Fund and shipbuilding ecosystem','The Budget proposed long-term maritime finance and supporting industrial measures.',
'The proposed fund corpus was ₹25,000 crore.|Government contribution was up to 49%, with the balance from ports/private investors.|Shipbuilding clusters and changes to shipbuilding assistance were proposed.|Large ships above a specified size were to receive infrastructure-list treatment.',
'A corpus is not necessarily annual expenditure or disbursal. Maritime industrial policy includes vessels, repair, finance, skills and supporting suppliers.',
'AP’s ports and shipbuilding base offer opportunities if financing is linked to credible demand and competitiveness.|Commercial appraisal, environmental standards and domestic supplier development determine whether public support creates durable value.',
'₹25,000 crore is not wholly a direct government grant. Announcement is not proof the fund had already financed projects.',
'How can maritime policy connect trade logistics with domestic manufacturing capability?','F-UB,F-HIGHLIGHTS',ap=True)
add('Economy','09 · Logistics & manufacturing',1,'Manufacturing Mission and clean-technology value chains','The Budget proposed policy support for small, medium and large industries.',
'The mission covered ease/cost of business, workforce, MSMEs, technology and quality.|Clean-tech priorities included solar cells, batteries, electrolyzers, wind turbines and transmission equipment.|Domestic value addition and execution/monitoring were emphasised.|This was a mission proposal, not completed factories.',
'Assembly, component manufacture and upstream material capability provide different levels of value addition. Clean end-use does not remove upstream environmental costs.',
'Industrial strategy should address scale, learning, power quality and market demand together.|For AP, pair clean-energy investment with supplier skills and credible emissions/water accounting.',
'Do not equate every listed technology with an individually approved production incentive or a commissioned plant.',
'What conditions turn clean-technology demand into competitive domestic manufacturing?','F-SPEECH,F-DETAIL',ap=True)
add('Economy','12 · Housing finance & urban livelihoods',1,'SWAMIH Fund 2: completion finance','The Budget proposed a second blended-finance facility for stalled housing.',
'The proposed fund was ₹15,000 crore.|Contributors were to include government, banks and private investors.|The target was completion of another one lakh dwelling units.|The objective addressed households facing both rent and loan instalments on delayed homes.',
'Completion finance is different from a universal home-purchase subsidy or forgiveness of every developer debt. Project selection and cash-flow assessment matter.',
'Finishing viable stalled projects can unlock sunk investment and relieve households.|Transparent eligibility, escrow discipline and accountability are needed so rescue does not reward misconduct.',
'A target of one lakh units is not completed February output. Fund size and annual budget release differ.',
'How should a stressed-housing completion fund protect buyers while limiting moral hazard?','F-UB,F-HIGHLIGHTS',priority='P2')
add('Agriculture','06 · Seeds, cotton & value chains',1,'Seed mission, gene bank and cotton productivity','The Budget linked research capability with climate-resilient farm productivity.',
'A High Yielding Seeds Mission was proposed for research and targeted propagation.|The speech proposed a second gene bank with ten lakh germplasm lines.|A five-year Cotton Productivity Mission would support sustainability and extra-long staple varieties.|These were announced objectives, not completed research outputs.',
'Conserving germplasm, breeding a variety, regulatory assessment and farmer adoption are separate steps. High yield alone does not guarantee local resilience or profitability.',
'AP relevance includes seed systems, cotton quality, water stress and market linkages.|Public research, seed quality assurance and accessible extension are necessary to turn laboratory potential into reliable farmer benefit.',
'Ten lakh germplasm lines is not ten lakh newly released crop varieties. Cotton and pulses missions have different durations.',
'How should seed policy balance productivity, genetic diversity and farmer choice?','F-SPEECH,F-DETAIL',ap=True)
add('Agriculture','05 · High-value crops & institutions',1,'Makhana Board: a Bihar value-chain proposal','The Budget proposed commodity-focused support for makhana producers.',
'The Board was proposed for Bihar.|Functions covered production, processing, value addition and marketing.|Producers were to be organised into FPOs.|Training and convergence with existing schemes were emphasised.',
'A commodity board is a coordination mechanism, not a guaranteed procurement price. Makhana is associated with aquatic cultivation and specialised processing.',
'Producer aggregation can improve access to technology and bargaining power.|Success depends on market access, processing quality and ecological sustainability, not institution creation alone.',
'Budget proposal is not proof that a functioning board or universal benefits existed that day. Do not confuse this with January’s Turmeric Board launch.',
'How can a specialised value-chain institution avoid becoming an additional administrative layer?','F-SPEECH,F-HIGHLIGHTS',priority='P2')
add('Economy','12 · Housing finance & urban livelihoods',1,'PM SVANidhi revamp and first-time entrepreneurs','The Budget proposed expanded small-credit support for underserved urban workers.',
'PM SVANidhi revamp included enhanced loans and UPI-linked credit cards with ₹30,000 limits.|Capacity-building support was proposed for street vendors.|A separate first-time entrepreneur proposal covered five lakh women/SC/ST entrepreneurs.|The separate entrepreneur loan ceiling announced was up to ₹2 crore.',
'Working-capital credit, digital payments and enterprise-development lending have different purposes. Credit access is not proof of profitable self-employment.',
'Low-friction credit can reduce informal dependence when repayment terms suit volatile incomes.|Vendor recognition, legal vending space and grievance mechanisms remain important beyond payment digitisation.',
'Do not merge the ₹30,000 vendor card with the separate ₹2 crore entrepreneur loan ceiling or describe either as a free grant.',
'What should inclusive enterprise support provide besides a loan?','F-UB',priority='P2',ap=True)
add('Society & Welfare','01 · Health & social protection',1,'Health Budget: seats and service capacity','The Budget linked workforce expansion and health-system access.',
'Ten thousand additional medical seats were proposed for the next year.|The five-year ambition was 75,000 additional seats.|The proposals require institutional and clinical training capacity.|Separate Budget proposals addressed gig-worker healthcare; that is not the same as seat expansion.',
'A sanctioned educational seat is not a trained doctor available immediately. Teaching faculty, hospitals, caseload and accreditation determine training quality.',
'Quantity expansion should address regional imbalance and retention in underserved areas.|Workforce planning needs nurses, technicians, public-health staff and primary care, not doctors alone.',
'Do not describe all 75,000 seats as added in FY2025–26 or as doctors already graduating in February.',
'How can medical-education expansion improve service access without compromising quality?','F-UB',ap=True)
add('Economy','08 · Financial inclusion & markets',1,'Insurance FDI: conditional Budget proposal','The Budget proposed increasing the foreign-investment limit.',
'The proposed limit was 100%, up from 74%.|The proposal referred to companies investing their entire premium in India.|Implementation required legal/regulatory follow-up.|The aim was increased capital and participation, not automatic universal insurance.',
'FDI ownership limits, prudential solvency, insurance distribution and policyholder protection are different policy dimensions.',
'More capital can support competition and product development.|Coverage depends on affordability, claims conduct and distribution; higher FDI alone does not ensure trustworthy protection.',
'An announced 100% limit is not evidence every necessary amendment had already commenced in February.',
'How can insurance liberalisation improve protection rather than merely expand premium collection?','F-PRS,F-UB')
add('Polity & Governance','13 · Land records & spatial governance',1,'National Geospatial Mission proposed','The Budget proposed foundational spatial infrastructure and data.',
'The mission was intended to support land-record modernisation.|Urban planning and infrastructure design were identified uses.|The speech linked the work with PM Gati Shakti.|This proposal is broader than one urban land-survey pilot.',
'Geospatial data combine location with attributes. Mapping accuracy, interoperability, privacy and legal validity are distinct concerns.',
'Shared spatial evidence can reduce planning duplication and improve network decisions.|Accountable access, current datasets and transparent correction are essential when maps influence property and public investment.',
'The National Geospatial Mission, NAKSHA and SVAMITVA are related but not interchangeable names.',
'How can spatial-data infrastructure improve public investment while protecting citizens’ rights?','F-SPEECH,F-UB',ap=True)
add('Polity & Governance','11 · Electoral participation',19,'CEC transition under the 2023 appointment law','Gyanesh Kumar assumed charge after the February appointment notification.',
'Gyanesh Kumar succeeded Rajiv Kumar as CEC.|The appointment notification was dated 17 February; assumption was on 19 February.|Vivek Joshi was appointed Election Commissioner.|The appointments occurred amid pending legal debate over the selection framework.',
'Article 324 establishes the constitutional election institution. The 2023 selection law and judicial challenges to it are distinct from an assumption-of-office event.',
'Credible appointments require transparency, institutional independence and public confidence.|Explain the legal framework and contested issues without equating an allegation with a judicial finding.',
'Appointment date and charge-taking date differ. Do not describe the Chief Justice as a member of the statutory 2023 selection panel.',
'What institutional safeguards strengthen both the independence and accountability of an election commission?','F-CEC,F-CEC2')
add('Polity & Governance','14 · Federalism & constitutional safeguards',13,'President’s Rule in Manipur','The proclamation followed the Chief Minister’s resignation during a prolonged crisis.',
'President’s Rule was imposed on 13 February.|N. Biren Singh had resigned four days earlier.|The Assembly was placed under suspended animation.|The notification invoked Article 356.',
'Article 356 concerns failure of constitutional machinery. Suspended animation differs from dissolution; parliamentary approval and constitutional limits remain relevant.',
'Union administration may be justified as a temporary response but is not a substitute for restoring representative government.|Peace-building requires security, relief, rehabilitation, accountability and trust across communities.',
'Do not call this a national emergency under Article 352 or assume the Assembly was automatically dissolved.',
'How should constitutional intervention be combined with a credible path back to representative government?','F-MANIPUR')
add('Polity & Governance','09 · Judicial capacity',20,'Supreme Court stays Lokpal’s HC-judge order','An interim intervention raised the balance between accountability and judicial independence.',
'The Lokpal order asserting jurisdiction was dated 27 January.|The Supreme Court stayed it on 20 February in suo motu proceedings.|Notices and further consideration followed.|The February milestone was interim, not a fully reasoned final determination of all issues.',
'Statutory anti-corruption jurisdiction and constitutional judicial status must be read together. Independence does not mean immunity from every accountability mechanism.',
'Legitimate scrutiny needs procedures protecting both public confidence and judges from harassment.|A balanced answer should identify proper investigation, disciplinary and removal routes rather than infer total impunity from one stay.',
'A stay suspends operation; it is not automatically final quashing or a declaration that no judge can ever face criminal process.',
'How can judicial accountability be strengthened without weakening independent adjudication?','F-LOKPAL')
add('Polity & Governance','14 · Federalism & constitutional safeguards',10,'Tamil Nadu Governor case: judgment reserved','The Court completed February hearings over delayed assent to Bills.',
'The bench reserved judgment on 10 February, as reported the next day.|The dispute concerned Governor action under Article 200.|Repassed Bills and later reservation for the President were central issues.|The later April judgment is not a February holding.',
'Article 200 concerns assent, withholding, return and reservation in the constitutional framework. Oral arguments, judicial questions and a final ratio are different.',
'Indefinite delay can frustrate elected lawmaking and invite constitutional deadlock.|Study institutional role and remedy without treating a party’s courtroom argument as settled law.',
'Do not backdate April’s timelines or deemed-assent relief to February; later references and rulings also need current-law review.',
'Why do constitutional offices require both formal powers and conventions of timely action?','F-TNGOV')
add('Polity & Governance','11 · Electoral participation',8,'Delhi election: results and government formation','The Assembly result produced a change in government.',
'BJP won 48 of 70 seats; AAP won 22.|The results were declared on 8 February.|Rekha Gupta took oath as Chief Minister on 20 February.|Seat outcomes and the later appointment are distinct stages.',
'Delhi’s constitutional framework under Article 239AA differs from an ordinary state. A seat majority does not mean the same percentage of total votes.',
'Use the event to revise electoral representation and Delhi’s institutional structure.|Policy accountability should focus on service outcomes and lawful division of functions rather than partisan campaign claims.',
'Do not confuse these Assembly results with municipal elections; one source’s live narrative contained that imprecise wording.',
'How does Delhi’s special constitutional arrangement affect democratic accountability?','F-DELHI,F-DELHI2',priority='P2')
add('Environment','07 · Global biodiversity governance',27,'Resumed CBD COP16: Rome finance agreement and Cali Fund','The resumed session addressed business unfinished in Cali in 2024.',
'The resumed talks were held in Rome on 25–27 February.|Parties agreed a resource-mobilisation strategy linked to at least US$200 billion annually by 2030.|Monitoring, reporting and review arrangements were among the outcomes.|The Cali Fund for benefit-sharing from digital sequence information was launched; its establishment had been agreed earlier.',
'CBD COP16 is not UNFCCC COP16. Digital sequence information concerns genetic-resource information; benefit sharing differs from physical access permission.',
'Finance strategies need actual contributions and transparent delivery to close implementation gaps.|The Fund connects biotechnology value creation with biodiversity stewardship and Indigenous/local-community interests.',
'US$200 billion is a mobilisation goal, not cash already collected in Rome. Do not misdate the earlier decision establishing the Cali Fund.',
'What would make biodiversity finance both adequate and equitable?','F-CBD,F-CBD2')
add('Environment','02 · Wetlands',2,'World Wetlands Day at Parvati Arga','The national event highlighted management as well as recognition.',
'The venue was Parvati Arga Ramsar Site in Gonda, Uttar Pradesh.|The theme was Protecting Wetlands for our Common Future.|An integrated management plan was among the publications launched.|Tourism-corridor intentions were announced separately.',
'2 February commemorates adoption of the Ramsar Convention. A management plan, site designation and wetland-city accreditation are different processes.',
'Integrated management needs hydrology, catchment pollution control and compatible livelihoods.|For AP, apply this lens to wetland pressures rather than simply adding another site-name flashcard.',
'A publication titled Factbook of India’s 85 Ramsar Sites is not proof the February national total remained 85. Publication scope and current count differ.',
'Why should wetland policy be evaluated through ecological condition rather than designation counts alone?','F-WETLAND',priority='P2',ap=True)
add('Science & Technology','08 · AI governance',2,'EU AI Act: first requirements apply','Selected prohibitions and literacy duties began before the wider framework’s later phases.',
'Prohibited-practice provisions and AI-literacy obligations applied from 2 February.|The framework follows a risk-based approach.|Covered practices include specified manipulation, social scoring and certain biometric/emotion-recognition uses, with legal qualifications.|Other provisions had different implementation dates.',
'Entry into force and phased application are distinct. Risk categories and prohibited practices should be studied from the operative legal text, not simplified slogans.',
'AI literacy is an organisational governance requirement, not merely teaching users to write prompts.|India can draw comparative lessons while choosing a context-appropriate mix of safeguards and innovation support.',
'Do not claim the entire EU AI Act first became law on 2 February. The Commission’s live page includes later changes that must not be projected backward.',
'What are the strengths and limitations of risk-based AI regulation?','F-EUAI,F-EUAI2')
add('Science & Technology','01 · Space',7,'CE20 vacuum-ignition trial','ISRO tested a multi-element igniter in simulated space-vacuum conditions.',
'The test was at IPRC Mahendragiri, Tamil Nadu.|CE20 powers LVM3’s cryogenic upper stage.|The trial formed part of work toward restart capability.|ISRO described further testing, including bootstrap-start studies.',
'Cryogenic propulsion uses very low-temperature propellants. A ground vacuum-ignition trial differs from demonstrated repeated in-flight restart.',
'Restart capability can enable more flexible orbital operations when qualified across the full mission envelope.|Reliable ignition, thermal behaviour and propellant management require staged validation.',
'This was not a new satellite launch or proof that all flight-restart tests were complete. The test was 7 February; the web announcement was 8 February.',
'Why do propulsion programmes use ground simulations before flight demonstration?','F-CE20')
add('Science & Technology','09 · Astronomy & fundamental science',10,'Euclid reveals an Einstein ring','ESA published the gravitational-lensing discovery around NGC6505.',
'NGC6505 is the foreground lens galaxy, about 590 million light-years away.|Its mass bends and magnifies light from a more distant background galaxy.|Near alignment creates the ring appearance.|The February milestone was publication/announcement, not necessarily the original observation date.',
'Gravitational lensing follows the curvature of spacetime. It is not an ordinary ring of material physically orbiting the foreground galaxy.',
'Lensing can probe mass distributions and distant objects, including matter not directly luminous.|Geometry and modelling matter; a striking image is not by itself a complete dark-matter explanation.',
'Do not identify the ring as a planetary ring or claim the galaxy was first discovered in 2025.',
'How can gravitational lensing act as both a natural telescope and a tool for studying mass?','F-EUCLID',priority='P2',precision='reporting-day')
add('Science & Technology','09 · Astronomy & fundamental science',12,'KM3NeT’s ultra-high-energy neutrino announcement','The collaboration reported an event with an estimated neutrino energy around 220 PeV.',
'The result used an underwater Mediterranean detector.|A muon crossing the detector supplied the signal used to infer the neutrino event.|The February announcement followed analysis of an earlier detected event.|The team described it as the highest-energy neutrino observed at that time.',
'Neutrinos interact weakly; detectors infer them from secondary signals. A petaelectronvolt is an energy unit, not a distance or luminosity.',
'Extreme-energy neutrinos can open a window onto violent cosmic processes.|One event’s interpretation involves substantial uncertainty; energy estimates and source attribution are different questions.',
'Do not say the event was physically detected for the first time on its publication date or that its source was conclusively located.',
'Why do weakly interacting particles offer information unavailable from ordinary light alone?','F-NEUTRINO',priority='P2',precision='reporting-day')
add('Science & Technology','01 · Space',24,'Asteroid 2024 YR4: risk sharply downgraded','More observations narrowed orbit uncertainty after earlier public concern.',
'NASA’s 24 February update placed Earth-impact probability for December 2032 at 0.004%.|It described no significant Earth threat over the next century on that evidence.|Further observations had refined the predicted trajectory.|The agency separately discussed a small lunar-impact probability, not an Earth impact.',
'Impact probability changes as an uncertain orbit is constrained. A temporarily rising probability can reflect changing uncertainty, not an asteroid deliberately changing course.',
'The episode tests observation networks, international notification and risk communication.|Communicate both probability and uncertainty rather than repeat the month’s most alarming headline after it has been superseded.',
'The 0.004% is a dated estimate, not a permanent current lunar or Earth probability. Avoid confusing the two targets.',
'How should agencies communicate a low-probability high-consequence risk as evidence changes?','F-ASTEROID')
add('Society & Welfare','01 · Public health',3,'Uganda: Sudan-virus vaccine efficacy trial','WHO described rapid research mobilisation after the outbreak declaration.',
'The trial launched four days after the 30 January outbreak confirmation.|It tested clinical efficacy of a candidate vaccine against Sudan virus disease.|Contacts and contacts-of-contacts were organised into rings.|WHO clarified the wording on 4 February: earlier safety/immunogenicity trials had occurred.',
'A clinical efficacy trial is not licensing or proof of efficacy. Ebola viruses of different species cannot be assumed to share identical vaccine protection.',
'Pre-positioned doses and pre-agreed ethical/regulatory procedures can accelerate outbreak research.|Speed must retain consent, community engagement and reliable endpoint assessment.',
'Do not call it the first-ever testing of any Ebola vaccine or claim an already licensed Sudan-virus vaccine existed from the trial launch.',
'How can outbreak preparedness make clinical research both faster and ethically sound?','F-EBOLA')
add('Economy','13 · Energy security',14,'India Energy Week 2025','The third edition combined energy-transition discussions with hydrocarbon investment.',
'The event ran 11–14 February at Yashobhoomi, New Delhi.|The concluding account highlighted exploration licensing and partnerships.|Biofuels, hydrogen, LNG and renewable technologies featured.|A conference announcement is not an independently audited delivery outcome.',
'Energy security balances availability, affordability and sustainability. Expanding a domestic resource does not automatically eliminate import exposure.',
'India’s transition must manage growing demand and the reliability of existing supply.|Evaluate partnerships through realised investment, emissions and technology capability rather than exhibition size or promotional global rankings.',
'Do not treat every displayed technology as commercially deployed or use unverified superlatives as core exam facts.',
'How should India reconcile near-term energy security with long-term decarbonisation?','F-ENERGY',priority='P2',ap=True)
add('Security','01 · Defence & strategy',10,'Aero India 2025: industrial partnerships','The fifteenth edition took place at Yelahanka, Bengaluru.',
'The dates were 10–14 February.|The theme was The Runway to a Billion Opportunities.|Business and public days were distinguished.|The exhibition included foreign aircraft and domestic-industry participation.',
'An air-show appearance, a memorandum, a procurement decision and an inducted operational platform are different stages.',
'Aerospace capability requires engines, components, certification, maintenance and supplier learning.|Assess partnerships by technology depth and sustainable production rather than the number of display aircraft.',
'F-35 or Su-57 participation at an exhibition does not establish an Indian purchase contract.',
'How can defence exhibitions support capability rather than remain announcement-driven events?','F-AERO',priority='P2')
add('Security','02 · Military exercises',7,'TROPEX-25: operational update','The Navy reported its capstone biennial readiness exercise underway.',
'The exercise spanned January–March 2025 in the Indian Ocean Region.|It integrated naval units with Army, Air Force and Coast Guard assets.|Phases included harbour/sea activity, cyber/electronic warfare and amphibious operations.|The release described approximately 65 ships, nine submarines and over 80 aircraft.',
'Jointness means coordinated operations across services; interoperability includes communications, procedures and logistics. A domestic exercise differs from a bilateral drill.',
'Realistic scenarios can reveal gaps in sustainment and coordinated response.|Readiness should be assessed through validated lessons and corrective action, not platform counts alone.',
'7 February is the reporting date, not the exercise’s entire duration. TROPEX was not a one-day India–US exercise.',
'What makes a joint exercise useful for operational readiness?','F-TROPEX',precision='reporting-day')
add('Andhra Pradesh','05 · Inclusive industry & administration',6,'AP Cabinet: targeted enterprise incentives','The Cabinet approved policy amendments for specified under-represented entrepreneurs.',
'Reporting described investment subsidy rising from 35% to 45% for the identified categories.|Land-support changes for SC/ST entrepreneurs and power-incentive changes were also reported.|The package covered amendments to multiple sectoral policies.|Transport/logistics support and GST reimbursement were among the decisions described.',
'Cabinet approval, operative GO, eligibility determination and reimbursement are distinct. Percentages often have caps and conditions that cannot be omitted in an application.',
'Targeted support can address unequal access to capital and business networks.|Evaluate additional viable enterprises, survival, payment delays and inclusion—not just sanctioned subsidy amounts.',
'This note is not a complete eligibility guide; verify the applicable GO, category, cap, duration and investment base before using a percentage.',
'How can AP design targeted enterprise incentives that expand opportunity without creating rent-seeking?','F-APCAB',ap=True)
add('Andhra Pradesh','11 · One Health & agricultural livelihoods',11,'Poultry H5N1 confirmation and One Health','February reports moved from suspected poultry mortality to laboratory-confirmed avian influenza.',
'The report concerned Kanuru/Peravali in East Godavari.|Samples were sent to specialised laboratories including NIHSAD, Bhopal.|Authorities described culling zones, rapid-response teams and carcass-disposal precautions.|Poultry cases do not establish confirmed human cases.',
'One Health connects animal, human and environmental health. Suspicion, laboratory confirmation and demonstrated transmission pathway are different evidence stages.',
'Biosecurity, veterinary surveillance, safe disposal, worker protection and fair compensation should operate together.|Communication must distinguish official current food-safety advice from broad alarming newspaper headlines; do not improvise dietary guidance from this note.',
'Do not assert migratory birds caused the outbreak without evidence, confuse H5N1 with Newcastle disease, or treat all poultry deaths as individually confirmed.',
'How should AP coordinate veterinary, public-health and livelihood responses to an animal-disease outbreak?','F-APFLU',ap=True)
add('Andhra Pradesh','12 · Legislature & budget accountability',24,'AP legislature’s Budget Session','The session calendar linked the Governor’s address with the state budget.',
'The preview placed the session opening on 24 February.|Governor S. Abdul Nazeer was to address the Assembly and Council.|The Budget was subsequently presented on 28 February.|Political participation and any final sitting schedule require the official proceedings for confirmation.',
'Article 176 concerns a Governor’s special address. Legislative absence and disqualification require the precise constitutional conditions, not an oversimplified count of calendar days.',
'Attendance matters because scrutiny of spending and executive claims is a representative responsibility.|Study the role of the Business Advisory Committee and committee/demand scrutiny alongside floor debate.',
'The opening detail relies on a pre-event report; it is labelled accordingly. Do not treat a preview’s likely sitting count as a verified final total.',
'What would improve substantive budget scrutiny in a state legislature?','F-APSESSION,F-APB',priority='P2',ap=True)
add('Andhra Pradesh','01 · State economy & budget',28,'AP receipts and the BE–RE credibility gap','The Budget analysis showed why a larger planned outlay needs a credible revenue base.',
'FY2025–26 non-borrowing receipts were estimated at ₹2,18,002 crore, 24% above FY2024–25 RE.|FY2024–25 non-borrowing receipts were revised 12% below BE.|The FY2024–25 revenue deficit was revised to 3.0% of GSDP, versus 2.1% BE.|Net expenditure was also revised lower, yet the deficit ratio rose.',
'Budget Estimates are plans; Revised Estimates update expectations; Actuals record realised outcomes. Deficit is affected by both revenue and spending.',
'Under-realised revenue can widen deficits despite spending compression.|AP should stress-test assumptions, improve collection and protect high-value services from abrupt cash rationing.',
'A 24% projected receipts increase is not realised growth or proof of a comparable real economic expansion.',
'How can a state strengthen fiscal credibility when receipts repeatedly undershoot targets?','F-APB',ap=True)
add('Andhra Pradesh','01 · State economy & budget',28,'Central capex loans and AP borrowing','PRS separated special long-term Union loans from other borrowing.',
'AP budgeted ₹10,200 crore of central capex loans for FY2025–26.|FY2024–25 RE for these loans was ₹11,750 crore.|PRS describes the Union’s 50-year interest-free capital-expenditure loan arrangement.|It notes their exclusion from the state borrowing-ceiling calculation under that arrangement.',
'Interest-free is not repayment-free. Fiscal-deficit accounting, debt stocks and an administratively permitted borrowing ceiling are separate concepts.',
'Long-tenor finance can support productive assets if appraisal and execution are strong.|AP must budget maintenance and contingent obligations so cheaper finance does not substitute for project quality.',
'Exclusion from a borrowing-ceiling calculation does not mean the loan vanishes from all debt/fiscal analysis.',
'How should states assess concessional borrowing for infrastructure?','F-APB',ap=True)
add('Andhra Pradesh','04 · Innovation & infrastructure',28,'Amaravati and Polavaram: budgeted capital priorities','The Budget made provisions for two major state development priorities.',
'The Hindu reported ₹6,000 crore for Amaravati.|It reported ₹6,705 crore for Polavaram.|These are FY2025–26 budget provisions, not February expenditure certificates.|The projects have distinct financing, clearance and execution structures.',
'A budget allocation, funding agreement, loan drawdown, work award and certified physical progress are different milestones.',
'Capital-city works need climate-resilient planning, service delivery and transparent procurement.|Irrigation development also needs safety, rehabilitation and environmental compliance.|Compare physical milestones and outcomes with spending rather than use allocation size as the only success measure.',
'Do not add previously announced external financing to an annual provision as though both were new cash expenditure in February.',
'How can AP reconcile accelerated infrastructure delivery with fiscal and social safeguards?','F-APNEWS',ap=True)
add('Andhra Pradesh','09 · Irrigation & disaster resilience',6,'Polavaram rehabilitation: fresh-tender decision','The Cabinet’s February account included unfinished rehabilitation-colony works.',
'Fresh tenders were to be invited for remaining R&R housing-colony works.|Basic amenities as well as houses were included in the reported commitment.|The decision was part of the 6 February Cabinet meeting.|It did not certify that every affected family had been rehabilitated.',
'Resettlement moves people; rehabilitation restores livelihoods and social functioning. A completed house alone does not establish adequate rehabilitation.',
'Independent verification should cover land/entitlements, water, schools, health, transport and livelihood access.|Participation and usable grievance channels are essential when displacement is involuntary.',
'Approval to tender is not completed construction or proof of consent/settlement of all claims.',
'What should an outcome-based rehabilitation audit of a large irrigation project examine?','F-APCAB',ap=True)
add('Security','06 · Mass-gathering safety',22,'SLBC tunnel collapse: construction and rescue risk','A tunnel section collapsed near Domalapenta in Telangana.',
'The incident was on 22 February in Nagarkurnool district.|Eight workers were reported trapped in contemporary accounts.|Rescue involved multiple technical and emergency agencies.|February reports do not establish the eventual outcome for every missing person.',
'The Srisailam Left Bank Canal tunnel is not the Polavaram project. Underground safety depends on geology, water ingress, support systems and worker access.',
'Prevention requires updated geotechnical assessment, instrumentation and enforceable safety protocols.|Rescue requires specialist coordination, air/water management and protection of rescuers against secondary failure.',
'Do not relocate the incident to AP merely because Srisailam is linked to an interstate river project. Final casualty outcomes need later sources.',
'What should a major underground-project safety and rescue framework contain?','F-SLBC',ap=True)
add('Awards & Sports','03 · Competitions',14,'National Games conclude: Services lead the gold tally','The event that opened in January produced its final results in February.',
'Services Sports Control Board led with 68 gold medals.|Its reported total was 121 medals.|Maharashtra had a larger overall medal count but fewer golds.|The host was Uttarakhand and the closing date 14 February.',
'Medal-table ordering commonly prioritises gold, then silver and bronze, not simply total medals.',
'The opening and the results are separate monthly milestones, not duplicate descriptions of the same development.|Use results for concise factual recall; evaluate broader sporting policy through participation and athlete pathways.',
'The team with most total medals need not top the gold-ordered table. Do not put February results into January’s as-of record.',
'Explain how medal-table order can differ from total-medal order.','F-GAMES',priority='P3')
add('Science & Technology','07 · Scientific administration',28,'National Science Day: Raman effect and research culture','The annual observance highlighted youth leadership in science and innovation.',
'The 2025 theme concerned empowering Indian youth for global science/innovation leadership for Viksit Bharat.|28 February commemorates discovery of the Raman effect.|C.V. Raman received the Nobel Prize in Physics in 1930.|The first National Science Day observance was in 1987.',
'Raman scattering is inelastic scattering of light, involving an energy/frequency change. It differs from elastic Rayleigh scattering.',
'An anniversary is a useful entry point to spectroscopy and scientific temper.|Research opportunity needs laboratories, mentorship, merit-based access and stable support beyond ceremonial events.',
'Discovery year, Nobel year and start of the annual observance are distinct. A theme is not proof of achieved global leadership.',
'What institutional conditions help young researchers contribute to public-interest innovation?','F-SCIENCEDAY',priority='P3')
add('Culture & History','04 · Communities & performing traditions',24,'Jhumoir Binandini and Assam’s tea communities','The Guwahati event foregrounded a living performing tradition.',
'The programme took place on 24 February.|Jhumoir was described as a folk dance of Assam’s Tea Tribe and Adivasi communities.|PIB described around 8,000 performers.|The event was linked to commemoration of 200 years of the tea industry in Assam.',
'Living heritage belongs to communities and includes language, practice and social context; a large stage event is only one expression.',
'Cultural recognition should be connected to community dignity, education and livelihoods.|Avoid assuming that visibility at a national event settles longstanding socio-economic disadvantage.',
'Do not confuse Jhumoir with Bihu or claim this event itself granted UNESCO inscription.',
'How can cultural promotion support the communities sustaining the tradition?','F-JHUMOIR',priority='P3')
add('International Relations','09 · Political transitions & Europe',23,'Germany votes: coalition formation still ahead','The election made the CDU/CSU bloc the largest grouping.',
'Provisional contemporary reporting placed CDU/CSU first and AfD second.|Friedrich Merz led the CDU campaign.|The election was on 23 February.|A parliamentary election result precedes coalition agreement and formal election of a chancellor.',
'Germany’s Bundestag elects the chancellor within its constitutional framework. Winning the largest vote share does not equal an immediate direct popular mandate to take office.',
'Coalition politics and economic/security priorities matter for India–Europe relations.|Use official final results for exact percentages; provisional rounded figures can differ from final accounts.',
'Do not label Merz an already sworn-in chancellor on election night. Do not equate vote share with seat share.',
'Why is government formation a separate analytical stage after a parliamentary election?','F-GERMANY',priority='P2')
# Enrich the 17 pre-existing February topics rather than duplicate Budget headlines.
ENRICH={
'CA-001':('The Union Budget was presented on 1 February.', 'Fiscal deficit measures the borrowing gap; revenue deficit concerns the revenue account. Capital expenditure is not automatically high-quality investment.', 'Interest payments absorb a substantial share of spending and limit room for other priorities.|Assess capex through project quality, execution and maintenance, not only its share of GDP.', ['F-PRS','F-UB']),
'CA-003':('Budget tax proposals changed the new-regime slabs and rebate.', 'A nil slab, rebate, deduction and special-rate income have different legal effects.', 'Tax relief can support disposable income but affects only households within its scope.|Judge distribution, consumption response and revenue cost; check operative law before using thresholds as personal tax advice.', ['F-UB']),
'CA-004':('The Budget announced a district-focused agriculture programme.', 'District convergence combines complementary interventions; district selection and individual beneficiary eligibility are different.', 'Local diagnosis should integrate water, credit, extension and markets.|For AP, targets need district evidence and transparent monitoring rather than assuming every district is covered.', ['F-SPEECH','F-UB']),
'CA-005':('The Budget announced a six-year pulses mission.', 'Procurement assurance can influence cropping choices, but seed, agronomy and market infrastructure affect the response.', 'Credible buying arrangements may reduce risk in diversification.|Water use, local suitability and storage should guide implementation; avoid assuming universal procurement without registration/conditions.', ['F-SPEECH','F-UB']),
'CA-006':('The Budget proposed a higher subvention-linked KCC loan limit.', 'Credit limits and subsidised-interest eligibility are not cash entitlements or proof of loan approval.', 'Formal credit helps when timely and matched to crop cash flows.|Tenant farmers, small borrowers and disaster-affected households need usable documentation and repayment support.', ['F-UB']),
'CA-007':('The Budget proposed a sustainable EEZ/high-seas fisheries framework.', 'An EEZ gives specified sovereign resource rights; the high seas operate under a different international legal framework.', 'AP marine exports require stock sustainability, traceability, cold chains and crew safety.|Industrial expansion should not displace small-scale fishers without fair safeguards.', ['F-SPEECH']),
'CA-008':('Budget proposed revised MSME classification thresholds.', 'Investment and turnover tests are separate; classification affects access to selected schemes but does not remove every lending condition.', 'Higher thresholds can reduce the incentive to remain artificially small.|Support must still reach micro firms with weaker collateral and bargaining power.', ['F-SPEECH','F-UB']),
'CA-009':('The Budget proposed an SMR research mission and nuclear-law changes.', 'SMRs are reactor designs with modular/smaller-unit characteristics, not automatically risk-free or commercially mature.', 'Evaluate licensing, waste, liability, fuel and cost alongside decarbonisation potential.|A research allocation and a 2033 target do not establish deployed generation in February.', ['F-UB']),
'CA-010':('The Budget proposed healthcare/social-security linkage for online-platform workers.', 'Registration, eligibility, enrolment and successful access to benefits are distinct.', 'Portable benefits should accommodate multi-platform work and variable earnings.|Worker voice, contribution design and usable grievance systems matter beyond identity cards.', ['F-UB']),
'CA-011':('Budget proposed school/PHC connectivity, labs and an AI education centre.', 'Connectivity, functional equipment, trained teachers and improved learning are separate outcome stages.', 'Digital investments require maintenance, accessible content and teacher support.|Evaluate inclusion and educational gains rather than count devices alone.', ['F-SPEECH','F-UB']),
'CA-012':('Budget proposed extending water coverage and new urban finance.', 'A multi-year corpus, annual allocation, sanction and release differ. A tap connection is not proof of continuous safe supply.', 'Water services need source protection, quality testing and affordable O&M.|Urban projects need credible finance and local capacity; announced funds are not automatic municipal revenue.', ['F-UB']),
'CA-016':('AP’s Finance Minister presented the state Budget on 28 February.', 'Gross expenditure includes debt repayment; net expenditure excludes it. Ratios use the relevant nominal GSDP denominator.', 'Compare BE, RE and actuals consistently when discussing fiscal consolidation.|Borrowing for productive assets differs economically from financing persistent revenue gaps.', ['F-APB']),
'CA-017':('The Budget projected nominal GSDP for FY2025–26.', 'Current-price growth includes price changes; constant-price growth seeks to remove them. Per-capita GSDP is not household disposable income.', 'Diversification and productivity matter alongside aggregate growth.|Avoid using a higher state average as proof that every district or household is better off.', ['F-APB']),
'CA-018':('AP’s Budget proposed education-linked support for FY2025–26.', 'A budget policy description is distinct from beneficiary GOs, payment conditions and actual disbursal.', 'Assess attendance, retention and learning as well as financial coverage.|Reliable eligibility and appeals help avoid excluding vulnerable children.', ['F-APB']),
'CA-019':('The Budget proposed doubling fishing-ban relief.', 'Closed-season compensation can protect income while supporting stock recovery.', 'Timely, accessible support improves compliance incentives.|Check beneficiary definitions, coverage, payment timing and ecological evidence rather than assume all fisher households received it.', ['F-APB']),
'CA-020':('The Budget proposed a hub-and-zonal-centre innovation network.', 'An innovation ecosystem needs institutions, finance, mentors, skills and market access, not just a building.', 'AP should connect district universities and MSMEs to opportunity.|Measure viable firms, technology adoption and jobs rather than only event attendance or MoUs.', ['F-APB'])}
N=[n for n in N if not n['id'].startswith('FEB25-')]
for n in N:
 if n['id'] in ENRICH:
  why,static,analysis,src=ENRICH[n['id']];n.update(why=why,static_link=static,analysis=analysis.split('|'),sources=src,evidence_access='Full PRS web analysis read; additional Budget-speech claims use inspected source extracts',status='February Budget proposal/snapshot; operative rules and actual outcomes require follow-up')
  # Retain the factual content but not misleading universal eligibility.
N+=J
(R/'data/notes.json').write_text(json.dumps(N,ensure_ascii=False,indent=2));(R/'data/sources.json').write_text(json.dumps(S,ensure_ascii=False,indent=2));(R/'data/source-access.json').write_text(json.dumps(A,ensure_ascii=False,indent=2))
print('February new',len(J),'total',sum(n['date'].startswith('2025-02') for n in N),'archive',len(N),'sources',len(S))
