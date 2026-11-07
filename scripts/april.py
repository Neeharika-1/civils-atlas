"""April 2025 research batch. Historical snapshots; no daily completeness claim."""
import pathlib,json
R=pathlib.Path(__file__).resolve().parents[1];N=json.loads((R/'data/notes.json').read_text());S=json.loads((R/'data/sources.json').read_text());A=json.loads((R/'data/source-access.json').read_text());J=[]
def source(k,t,u,full=False):
 S[k]=[t,u];A[k]=dict(title=t,url=u,access='Substantive article/web synthesis read; linked documents not necessarily independently reviewed' if full else 'Search-result source extract inspected; full document review pending',checked_on='2026-11-06',method='Assistant-led web research; no independent human editorial certification')
def add(subject,block,day,title,why,facts,static,analysis,trap,mains,src='M-PRS',priority='P1',ap=False,precision='day'):
 keys=src.split(',');J.append(dict(id=f'APR25-{len(J)+1:03}',subject=subject,block=block,date=f'2025-04-{day:02}',date_precision=precision,title=title,why=why,facts=facts.split('|'),static_link=static,analysis=analysis.split('|'),trap=trap,mains=mains,sources=keys,priority=priority,ap=ap,status='April historical snapshot; later law and implementation require separate review',checked='2026-11-06',evidence_access='Full substantive synthesis/article read; independent primary-document checks may remain open' if any(k in ['A-PRS','A-RRB'] for k in keys) else 'Source extract(s) inspected; full-document review pending'))
source('A-PRS','PRS · April 2025 monthly review; all six chunks read','https://prsindia.org/policy/monthly-policy-review/april-2025',True)
source('A-RRB','PIB · RRB amalgamation, 8 April; substantive primary release read','https://pib.gov.in/PressReleasePage.aspx?PRID=2120016',True)
source('A-SC','The New Indian Express · AP SC sub-classification ordinance, 17 April','https://www.newindianexpress.com/states/andhra-pradesh/2025/Apr/17/andhra-pradesh-issues-ordinance-on-sc-sub-categorisation-classifying-into-three-groups')
source('A-SPORT','The New Indian Express · AP recruitment/sport quota implementation, 21 April','https://www.newindianexpress.com/states/andhra-pradesh/2025/Apr/21/ap-brings-sc-sub-classification-raises-sports-quota-to-3-under-new-governance-push')
source('A-FISH','The New Indian Express · Fishing-ban relief launch preview, 26 April','https://www.newindianexpress.com/states/andhra-pradesh/2025/Apr/26/andhra-cm-naidu-to-launch-matsyakara-sevalo-for-fishers-today')
source('A-FISHPOST','The New Indian Express · Post-launch minister statement, 28 April','https://www.newindianexpress.com/states/andhra-pradesh/2025/Apr/28/cm-naidu-fulfilled-another-poll-promise-with-matsyakarula-sevalo-minister-s-savitha')
source('A-CBG','The New Indian Express · Kanigiri CBG foundation ceremony on 2 April, report 3 April','https://www.newindianexpress.com/states/andhra-pradesh/2025/Apr/03/minister-nara-lokesh-lays-stone-for-first-of-500-cbg-units-in-kanigiri')
source('A-SPADEX','ISRO · Second docking on 20 April and power transfer on 21 April','https://www.isro.gov.in/Spadex_Successful_demonstration_of_Second_Docking_and_Power_Transfer.html')
source('A-BIOMASS','ESA · Biomass launch, 29 April','https://www.esa.int/ESA_Multimedia/Images/2025/04/ESA_s_forest_mission_lifts_off')
source('A-BIOMASS2','ESA · Biomass mission/instrument description; live page, use historical launch facts only','https://earth.esa.int/eogateway/missions/biomass')
source('A-LUCY','NASA · Donaldjohanson flyby on 20 April; post-event article 23 April','https://www.nasa.gov/image-article/nasas-lucy-spacecraft-images-asteroid-donaldjohanson/')
source('A-PANDEMIC','WHO · Draft pandemic agreement negotiations concluded, 16 April','https://www.who.int/news/item/16-04-2025-who-member-states-conclude-negotiations-and-make-significant-progress-on-draft-pandemic-agreement')
source('A-MATERNAL','WHO · UN maternal mortality report, 7 April','https://www.who.int/news/item/07-04-2025-aid-cuts-threaten-fragile-progress-in-ending-maternal-deaths-un-agencies-warn')
source('A-MEMORY','PIB · Gita/Natyashastra recognition, 18 April','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2122608&reg=48&lang=2')
source('A-CCS','MEA · CCS briefing after Pahalgam attack, 23 April','https://www.mea.gov.in/media-briefings.htm?dtl%2F39443%2FTranscript_of_Special_briefing_by_MEA_April_23_2025=')
source('A-RAFALE','PIB · Rafale naval-aircraft agreement, 28 April','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2124851&reg=3&lang=2')
source('A-BIMSTEC','MEA · India in BIMSTEC; retrospective verification of April summit outcomes','https://www.mea.gov.in/Portal/ForeignRelation/India_in_BIMSTEC.pdf')
source('A-SL','MEA · Sri Lanka visit briefing, 5 April','https://mea.gov.in/outoging-visit-detail.htm?39378%2FTranscript+of+Special+briefing+by+MEA+on+Prime+Ministers+visit+to+Sri+Lanka+April+05+2025=')
source('A-TARIFF','Rediff · US reciprocal tariff pause, 10 April; dated April snapshot','https://m.rediff.com/news/commentary/2025/apr/10/us-suspends-additional-26-tariff-on-india-till-july-9/664b84dd4e255990462f11b322a2e11b')
source('A-IMF','Fortune India · April WEO forecasts and fiscal/calendar-year interpretation, 22 April','https://www.fortuneindia.com/economy/imf-cuts-indias-fy26-growth-forecast-to-62-amid-trade-tensions-projects-global-growth-to-decline-to-28-in-2025/122375')
source('A-RANA','The Hindu · Tahawwur Rana extradition on 10 April, report 11 April','https://www.thehindu.com/news/national/tahawwur-hussain-rana-extradition-timeline-role-involvement-in-2008-mumbai-terror-attack/article69438562.ece')
source('A-SIMILIPAL','The New Indian Express · Similipal notification, 24 April; national-count discrepancy investigated 26 April','https://www.newindianexpress.com/states/odisha/2025/Apr/26/odisha-government-declares-similipal-as-107th-national-park-wii-lists-it-as-106th')
source('A-PAMBAN','PM India · New Pamban bridge inauguration, 6 April','https://www.pmindia.gov.in/en/news_updates/pm-lays-foundation-stone-inaugurates-development-works-worth-over-%E2%82%B98300-crore-in-rameswaram-tamil-nadu/')
add('Polity & Governance','01 · Federalism & constitutional institutions',8,'Tamil Nadu Governor case: the April judgment','The Court decided the assent dispute reserved in February.',
'The Court set aside the reservation of ten repassed Tamil Nadu Bills and treated them as having received assent in November 2023.|It held that a Governor could not withhold assent and then reserve an essentially unchanged repassed Bill for the President.|The judgment prescribed differentiated one-month/three-month timelines for specified gubernatorial decisions.|It also prescribed a three-month presidential decision timeline and recognised judicial review in specified circumstances.',
'Articles 200 and 201 govern gubernatorial and presidential consideration of state Bills; Article 142 concerns the Supreme Court’s power to do complete justice.',
'Indefinite delay can frustrate representative legislation and the federal balance.|Explain the specific holding, reasoning and remedy separately; later review, reference proceedings or subsequent judgments require their own dated notes.',
'This is the April ruling, not a timeless statement of current law. The February note correctly records only reservation of judgment.',
'Discuss constitutional accountability when assent procedures are used to delay elected legislatures.','A-PRS',ap=True)
add('Polity & Governance','03 · Religious institutions & property governance',4,'Waqf amendment: parliamentary passage snapshot','Parliament passed changes to the Waqf Act, 1995.',
'The passed framework changes requirements for declaring waqf and prospectively removes creation by waqf-by-user.|It changes the composition of the Central Waqf Council and state boards, including specified non-Muslim representation.|It changes the process relating to disputes over property claimed to be government property.|These provisions generated constitutional and property-rights questions; later court orders must be read separately.',
'A waqf is an endowment for recognised pious, religious or charitable purposes under Muslim law. Statutory administration and freedom of religion raise related but distinct legal questions.',
'Transparent records, fair hearings and independent dispute mechanisms matter in property governance.|Analyse administrative reform alongside religious freedom, equality and due process without assuming the existence of a dispute establishes either side’s title.',
'This note describes the passed legislation, not the later operative position after judicial proceedings. Do not turn a legislative proposal or interim hearing into a final judicial ruling.',
'How can reform of religious-endowment administration preserve transparency and procedural fairness?','A-PRS')
add('Economy','06 · Monetary policy & inflation',9,'RBI repo cut to 6%; stance turns accommodative','The April MPC followed February’s rate cut with further easing.',
'The repo rate fell from 6.25% to 6%.|The Standing Deposit Facility rate fell to 5.75%.|The MSF rate and Bank Rate were reduced to 6.25%.|The policy stance changed from neutral to accommodative.',
'The repo is a collateralised policy lending rate, SDF is an uncollateralised absorption facility and MSF is an overnight liquidity facility. Bank Rate should not be simplistically equated with all ordinary bank lending rates.',
'Lower inflation can create space to support demand, but transmission depends on bank funding, balance sheets and borrower conditions.|An accommodative stance communicates policy direction; it does not guarantee an immediate or identical reduction in every retail loan rate.',
'February’s stance was neutral and repo was 6.25%. These are April historical values, not the latest 2026 rates.',
'Explain why a policy-rate cut does not translate mechanically into stronger credit growth.','A-PRS')
add('Economy','06 · Price statistics & base effects',15,'Q4 inflation eases; CPI and WPI differ','March price releases allowed assessment of the January–March quarter.',
'Average CPI inflation in Q4 FY2024–25 was 3.7%, down from 5.6% in Q3.|Average food inflation fell from 9.4% in Q3 to 4.1% in Q4.|Average WPI inflation in Q4 was 2.3%, compared with 0.3% a year earlier.|The April release date does not change the reference period of the underlying March data.',
'CPI measures consumer-price movement; WPI concerns wholesale prices and has different coverage and weights. Disinflation is slower price growth, not necessarily falling price levels.',
'Lower food inflation may improve household purchasing power, but averages can conceal commodity and regional stress.|Policy should distinguish supply shocks, base effects and broader demand conditions before projecting the trend.',
'The 3.7% figure is a quarterly average, not necessarily the single-month March CPI rate.',
'How should policymakers interpret divergent consumer and wholesale inflation signals?','A-PRS')
add('Economy','08 · Rural banking institutions',8,'One State, One RRB: fourth amalgamation phase','The Department of Financial Services notified a new regional-rural-bank merger phase.',
'Twenty-six RRBs were involved across ten states and one Union Territory.|The national RRB count was to fall from 43 to 28 after the amalgamations.|The stated objectives were scale efficiency and cost rationalisation.|The primary release reports about 92% of branches in rural/semi-urban areas.',
'RRBs combine a development mandate with banking functions. A merger changes institutional structure; it does not guarantee branch expansion or credit inclusion.',
'Common technology, pooled capability and lower overhead may improve service delivery.|Monitor rural access, borrower relationships, staff integration and local-language support so efficiency does not mean withdrawal from difficult areas.',
'Twenty-six participating banks do not mean 26 newly created banks. Specific state structures and effective dates require the Gazette schedules.',
'Can consolidation strengthen rural banking without weakening its local development mandate?','A-RRB',ap=True)
add('Polity & Governance','04 · Census, data & social justice',30,'Cabinet approves caste enumeration in the next Census','The decision concerned the scope of the upcoming population census.',
'Cabinet approved including caste enumeration in the upcoming Census.|The previous completed decennial Census was in 2011.|The April decision did not itself provide final enumeration results or establish every methodological detail.',
'A census is an enumeration exercise; a sample survey and an administrative beneficiary database serve different purposes. Data categories require clear definitions and robust quality assurance.',
'Granular data may improve analysis of representation and deprivation if collection and interpretation are credible.|Privacy, training, classification consistency, public explanation and statistical safeguards are essential in a politically salient exercise.',
'Approval of caste enumeration is not publication of caste population totals or an automatic change to reservation quotas.',
'What methodological and governance safeguards are necessary for a credible caste enumeration?','A-PRS',ap=True)
add('Security','02 · Border development & internal security',4,'Vibrant Villages Programme-II approved','Cabinet approved a central-sector border-village development programme.',
'The approved outlay is ₹6,839 crore for FY2024–25 to FY2028–29.|It targets select strategic villages adjoining international land borders.|Objectives include improved living conditions, livelihoods, control of trans-border crime and stronger integration.|Support includes infrastructure, value chains, education and tourism circuits.',
'Border-area development links human security, services and territorial security. A central-sector scheme differs from a centrally sponsored cost-sharing programme.',
'Services and livelihoods can reduce distress outmigration and support resilient border communities.|Projects need ecological suitability and community participation; tourism or construction cannot substitute for basic education and health access.',
'This is VVP-II for selected land-border villages, not a universal scheme for every coastal settlement in AP.',
'Why is development of border communities an essential component of security policy?','A-PRS')
add('Polity & Governance','04 · Migration & legislative chronology',1,'Immigration framework: parliamentary passage advances','The April review records completion of parliamentary passage after March introduction and Lok Sabha action.',
'The framework consolidates four earlier laws on entry, registration, foreigners and carriers’ liability.|It provides for a Bureau of Immigration and registration of foreigners.|It adds information duties for specified educational and medical institutions.',
'Entry regulation, citizenship and international protection are distinct legal subjects. Parliamentary passage must be followed through assent, rules and commencement.',
'Unified systems can improve coordination, but information collection must have clear purpose, access controls and correction mechanisms.|Institutions need usable guidance so compliance does not arbitrarily obstruct treatment or education.',
'This month-level index records parliamentary progress, not independent verification that every implementing provision commenced immediately.',
'What administrative safeguards should accompany consolidated immigration regulation?','A-PRS',priority='P2',precision='month')
add('Economy','09 · Aircraft financing & international obligations',3,'Aircraft Objects Bill: parliamentary passage','Legislation advanced domestic implementation of the Cape Town aviation framework.',
'The framework gives legal effect to the 2001 Cape Town Convention and aircraft-specific Protocol, to which India acceded in 2008.|It addresses creditor rights in high-value aircraft equipment when debtors default.|Debtors must submit relevant dues records to DGCA; creditors must notify DGCA before exercising remedies.|The framework also recognises specified detention rights for unpaid public-service dues.',
'Aircraft leasing and secured finance depend on predictable creditor remedies; repossession law differs from aviation-safety certification.',
'Clear asset-recovery rules may reduce financing risk and leasing costs.|Reform must coordinate insolvency, operational safety, public dues and procedural fairness rather than assuming repossession alone solves airline viability.',
'February was introduction; April is later parliamentary progress. A financing law does not certify aircraft airworthiness or make leasing free of risk.',
'How can predictable creditor rights improve aviation finance while protecting the wider public interest?','A-PRS')
add('Society & Welfare','02 · Higher education & cooperatives',1,'Tribhuvan Sahkari University Bill passes','Parliament advanced the university legislation introduced in February.',
'The Bill establishes Tribhuvan Sahkari University through the IRMA institutional framework in Anand, Gujarat.|IRMA is placed as a school within the university.|The framework states that IRMA’s autonomous identity is to be preserved.',
'Cooperative education spans governance, professional management and member participation. A change in institutional status is not automatic improvement in learning outcomes.',
'Professional training can strengthen cooperative finance, dairy, procurement and rural enterprise.|Expansion should preserve academic standards, inclusion and useful field links instead of measuring success only by institutional scale.',
'The location is Gujarat, not AP. Passage and subsequent institutional operation require separate chronology.',
'What should professional cooperative education retain from member-led institutions?','A-PRS',priority='P2',precision='month')
add('Society & Welfare','02 · Higher-education flexibility',1,'UGC degree regulations: flexibility with standards','UGC notified minimum-standard regulations for undergraduate and postgraduate programmes.',
'The framework permits twice-yearly admissions and flexible UG/PG programme structures.|It recognises multiple entry/exit options and assessment of prior learning.|It provides for accelerated and extended undergraduate degree programmes.|At least 50% of total credits are required in a discipline for the specified undergraduate major.',
'Credit accumulation, programme duration and degree recognition are different elements of quality assurance. Flexibility needs institutional capability.',
'Flexible pathways may help learners with financial or family constraints return to study.|Students need clear information, transfer systems, adequate teaching and financial support to avoid flexibility becoming a low-quality exit route.',
'Permission does not mean every institution offers every option immediately, or that academic requirements disappear.',
'How can flexible degree pathways improve access without compromising academic standards?','A-PRS',precision='month')
add('Agriculture','05 · Crop prices & farm income',30,'Sugarcane FRP for 2025–26: ₹355 per quintal','CCEA approved the price for the October–September sugar season.',
'The basic FRP is ₹355 per quintal at 10.25% sugar recovery.|The previous season’s basic FRP was ₹340 per quintal.|FRP is the minimum price sugar mills must pay for sugarcane under the central framework.',
'FRP is specific to sugarcane and differs from MSP procurement arrangements for other crops; recovery links cane quality with sugar output.',
'Price support protects growers only when mills pay on time and production is financially viable.|Policy also needs to consider water stress, crop choice, cane arrears and the interaction of sugar and ethanol markets.',
'The price applies to the specified future sugar season and recovery base; it is not a universal price for every crop.',
'Explain the interaction between cane pricing, mill viability and sustainable water use.','A-PRS',ap=True)
add('Agriculture','06 · Irrigation delivery & water management',9,'M-CADWM: modernising irrigation’s last mile','Cabinet approved a PMKSY sub-scheme for FY2025–26.',
'Modernisation of Command Area Development and Water Management is a sub-scheme under PM Krishi Sinchayee Yojana.|The initial approved outlay is ₹1,600 crore for FY2025–26.|The scheme targets modern irrigation-water supply and micro-irrigation networks.',
'Command-area development links storage and main canals to actual farm delivery, drainage, distribution and water-use efficiency.',
'A dam or canal can underperform if field channels, scheduling, maintenance and farmer institutions are weak.|AP irrigation evaluation should include tail-end access, water accounting, crop suitability and delivered reliability, not just constructed capacity.',
'The initial outlay is not actual disbursement or proof that all command areas have been modernised.',
'Why is command-area management as important as creating new irrigation capacity?','A-PRS',ap=True)
add('Economy','10 · Electronics incentives & implementation',8,'Electronics Component Manufacturing Scheme notified','The April notification followed March Cabinet approval.',
'The scheme envisages ₹22,919 crore over six years.|Selected categories receive sales-linked support, capex support or both.|Eligibility includes thresholds for investment, incremental sales and employment.|Applications are to be appraised through a project-management agency and interministerial governance process.',
'Production-linked and capital-expenditure incentives reward different inputs/outcomes. Domestic sales do not automatically equal complete indigenous value addition.',
'Incentive design should reward capability, supplier depth and incremental outcomes.|Transparent selection, verification and monitoring are needed to control deadweight subsidy and overstated employment.',
'Not every electronics firm automatically qualifies; the category-specific notification and selection process matter.',
'How should manufacturing incentives be designed to reward genuine additional capability?','A-PRS',ap=True)
add('International Relations','05 · Diaspora welfare & migration governance',1,'Parliamentary committee on diaspora welfare','The External Affairs Committee recommended clearer policy and better support for returnees.',
'The committee called for a unified diaspora policy document.|It recommended lower remittance frictions and clearer investment/tax information.|It identified the need for reintegration policy for deportees and returned migrants, with Centre–state responsibilities.|It urged timely progress on the proposed Emigration Bill.',
'NRIs, PIOs, OCIs and migrant workers are not interchangeable legal categories. Immigration to India differs from emigration by Indians.',
'Returnees may need skills recognition, job matching, debt counselling and protection from recruitment fraud.|AP’s overseas-worker connections make coordination among consulates, state agencies and local services important, beyond celebrating remittance totals.',
'A committee recommendation is not an enacted law or a newly operational universal benefit.',
'Why should migrant-welfare policy include reintegration after return?','A-PRS',ap=True)
add('Environment','03 · Circular economy & urban waste',1,'Construction and Demolition Waste Rules 2025','The Environment Ministry notified a replacement framework under the Environment Protection Act.',
'The rules introduce extended producer responsibility for specified large construction/demolition waste generators.|The stated large-project threshold is built-up area of 20,000 square metres or more.|Registered recyclers and EPR certificates form part of compliance.|The framework specifies phased recycled-material utilisation targets from FY2026–27 onward.',
'C&D waste includes material from construction, renovation and demolition. Safe reuse needs sorting, processing, quality standards and accountable destination tracking.',
'Urban construction can reduce virgin-material demand when recycled products meet engineering standards and public procurement creates demand.|AP capital and urban projects can connect waste planning with works contracts, but targets must be verified against applicable dates and categories.',
'Notification is not the same as immediate commencement of all future targets. EPR is not satisfied merely by moving debris elsewhere.',
'How can urban construction move from debris disposal to a quality-assured circular material system?','A-PRS',ap=True,precision='month')
add('Environment','01 · Carbon markets & industrial transition',16,'Draft greenhouse-gas emission-intensity targets','Draft rules proposed entity-specific targets under India’s carbon-credit trading framework.',
'The April instrument was a draft, not final rules.|It covered obligated entities in sectors including cement, chemicals, metals and paper.|Targets concern greenhouse-gas emissions intensity under the prescribed methodology.|The proposal includes compliance obligations and environmental compensation for failure.',
'Emissions intensity is emissions per unit of output; it differs from an absolute cap on total emissions. Carbon-credit systems require measurement, reporting and verification.',
'Intensity targets can reward process improvement while allowing output growth.|Credible baselines, independent verification and market oversight are essential; intensity reductions need not imply lower total emissions.',
'Do not call the April draft final law, or describe an intensity target as a universal absolute emissions cap.',
'What safeguards make an industrial carbon-credit market environmentally credible?','A-PRS')
add('Science & Technology','06 · Telecom, IoT & critical infrastructure',22,'TRAI recommendations for critical M2M services','TRAI proposed an application-specific approach to reliability in machine-to-machine communications.',
'M2M enables direct electronic-device communication, often using embedded SIMs.|TRAI recommended identifying specific critical applications rather than entire sectors.|Criteria include ultra-reliable low-delay connectivity and the consequences of disruption for security, health, safety or the economy.|Recommendations include service-level agreements, phased device testing/certification and authorisation/SIM-transfer frameworks.',
'Latency, availability and reliability are distinct service characteristics. Criticality depends on what failure would do, not simply whether a device is connected.',
'Telemedicine and transport-control systems may require stronger safeguards than routine telemetry.|Technology-neutral standards can preserve innovation while assigning responsibility and measurable service expectations.',
'TRAI recommendations are not automatically binding final government rules. Not every IoT device is equally critical.',
'How should communications regulation distinguish critical applications from ordinary connected devices?','A-PRS',priority='P2')
add('Andhra Pradesh','01 · Social justice & reservation',17,'AP Scheduled Castes sub-classification ordinance','The state issued an ordinance after Cabinet approval on 15 April.',
'The 59 Scheduled Castes were divided into three groups within the existing 15% reservation.|Reported allocations were 1% for Group I, 6.5% for Group II and 7.5% for Group III.|The three groups contained 12, 18 and 29 listed castes respectively.|The instrument was an ordinance approved by the Governor, not a constitutional amendment.',
'Sub-classification within a reserved category differs from altering the Presidential Scheduled Castes list. An ordinance also has constitutional limits and requires legislative follow-through.',
'The policy question concerns distribution within a category, supported by credible evidence on disadvantage and representation.|Implementation requires clear rosters, transparent eligibility and grievance mechanisms; later legislative replacement and court proceedings must be tracked separately.',
'The percentages sum to the existing 15%, not a new additional 15%. This April note does not certify current operative law.',
'What evidence and safeguards should guide sub-classification within reserved categories?','A-SC',ap=True)
add('Andhra Pradesh','01 · Recruitment, sport & inclusion',19,'AP sportsperson recruitment quota raised to 3%','April orders and subsequent implementation reporting described a higher horizontal reservation.',
'The horizontal quota for eligible meritorious sportspersons rose from 2% to 3%.|The reported recognised-sport list expanded from 29 to 65 disciplines.|Selection involves screening and state-level evaluation under the applicable orders.|The report describes application across specified public recruitment bodies and services.',
'Horizontal reservation operates across vertical social categories; it must not be mechanically added as a separate vertical caste quota.',
'Sports recognition needs verifiable achievement standards, transparent scrutiny and safeguards against certificate fraud.|Recruitment preference should complement grassroots facilities, coaching, women’s participation and athlete support.',
'Check exact GO scope and eligibility. A 3% horizontal quota is not an additional 3 percentage points in every vertical reservation category.',
'Explain the distinction between horizontal and vertical reservations using sportsperson recruitment as an example.','A-SPORT',priority='P2',ap=True)
add('Andhra Pradesh','04 · Fisheries welfare & conservation',26,'Fishing-ban relief: from Budget promise to launch reporting','April coverage documented the move from the February Budget commitment toward implementation.',
'The annual conservation period was 15 April–14 June, a 61-day window.|The assistance announced for eligible fishers was ₹20,000, compared with the earlier ₹10,000.|The 26 April event was presented as the scheme launch; a 28 April minister statement described implementation.|Eligibility and actual receipt must still be checked against official lists and transaction evidence.',
'Seasonal restrictions protect breeding and recruitment in fish stocks; livelihood support can reduce the cost imposed on fishing households.',
'Timely and accurately targeted aid can strengthen compliance without treating conservation and welfare as opposing goals.|Women in sorting, processing and trade may face indirect income losses even when beneficiary lists focus on fishers; policy evaluation should examine the whole household/value chain.',
'Launch reporting does not prove every eligible household received payment. Do not infer identical vessel exemptions from inconsistent newspaper descriptions.',
'How should marine conservation measures be paired with inclusive livelihood protection?','A-FISH,A-FISHPOST',ap=True)
add('Andhra Pradesh','03 · Bioenergy, land & investment milestones',2,'Kanigiri CBG foundation: project start, not 500 working plants','A foundation ceremony took place for Reliance New Energy’s proposed programme.',
'The reported first plant site was Divakarapalli in Kanigiri constituency, Prakasam district.|The ceremony concerned a compressed-biogas project within a much larger proposed state programme.|The coverage mentions Napier grass as an intended feedstock.|Headline investment, land and employment figures were programme ambitions, not verified completed outcomes.',
'Biogas upgrading removes impurities and raises methane concentration for CBG use; feedstock choice affects land, water, logistics and emissions.',
'Assess lifecycle emissions, methane leakage, land rights, feedstock contracts, digestate quality and commercial offtake.|Dedicated energy crops should not be assumed to be equivalent to waste recovery; water and competing land uses require local assessment.',
'The 2 April event was foundation laying, not commissioning of 500 plants. Avoid reporting all promised jobs or land development as achieved.',
'What safeguards should accompany large compressed-biogas investment programmes?','A-CBG',ap=True)
add('Science & Technology','01 · Docking & orbital infrastructure',21,'SpaDeX re-docking and bidirectional power transfer','ISRO completed further experiments after January docking and March undocking.',
'The second docking took place on 20 April at 20:20 IST.|Power transfer in both directions between SDX-01 and SDX-02 was demonstrated on 21 April.|The experiment powered a heater element on one satellite from the other.|The reported transfer lasted approximately four minutes.',
'A mechanical docking link and electrical power transfer are distinct capabilities; both matter for multi-module orbital infrastructure.',
'Repeated autonomous operations and post-docking functions build confidence beyond a one-off contact event.|Mission readiness still requires qualification across safety, reliability and operational conditions, especially for human spaceflight.',
'April 21 was power transfer; second docking was April 20. Do not collapse these into March’s undocking milestone.',
'Why is post-docking resource transfer important for future orbital infrastructure?','A-SPADEX')
add('Science & Technology','05 · Earth observation & forest carbon',29,'ESA Biomass satellite launches','The European mission launched aboard Vega-C from French Guiana.',
'The launch occurred on 29 April.|The spacecraft is designed to measure forest biomass and changes over time.|Its principal instrument is a P-band synthetic-aperture radar.|Its data are intended to improve understanding of forests’ role in the carbon cycle.',
'SAR uses active radar rather than sunlight; longer radar wavelengths interact differently with vegetation structure. Biomass estimation is not identical to measuring forest area.',
'Better carbon-stock information can improve monitoring and climate analysis when calibrated with ground evidence.|Data interpretation must consider uncertainty, forest structure and validation; launch alone does not produce an immediately complete global carbon inventory.',
'Biomass is an ESA mission, not NISAR. A launch milestone is distinct from instrument commissioning and data-product release.',
'Why does reliable forest-carbon accounting need both remote sensing and ground measurements?','A-BIOMASS,A-BIOMASS2',priority='P2')
add('Science & Technology','03 · Planetary science & asteroids',20,'Lucy flies past Donaldjohanson','NASA released images following the main-belt asteroid encounter.',
'The flyby occurred on 20 April; NASA’s image article followed on 23 April.|Donaldjohanson is a main-belt asteroid, not one of Jupiter’s Trojan asteroids.|The images showed an elongated contact-binary form.|NASA reported closest approach at approximately 960 kilometres.',
'A contact binary comprises joined bodies; a flyby gathers observations without necessarily entering orbit or landing. Trojan asteroids share a planet’s orbital region around the Sun.',
'Smaller-body observations illuminate collision histories and the early solar system.|A spacecraft’s rehearsal/intermediate target may contribute valuable science while testing systems for later encounters.',
'Do not describe this as a Trojan encounter, landing or a sample return. Later changes to mission targets belong to later updates.',
'What can asteroid morphology reveal about the processes that shaped the early solar system?','A-LUCY',priority='P2')
add('Society & Welfare','04 · Global health cooperation',16,'Pandemic agreement draft negotiations conclude','WHO Member States finalised a proposal for consideration by the May World Health Assembly.',
'The April milestone was completion of negotiations on a draft proposal.|The text addresses prevention, preparedness, response and more equitable access to health products.|Proposals include pathogen access/benefit sharing, geographically diverse capacity and technology cooperation.|WHO explicitly stated that the draft does not authorise it to impose national lockdowns, vaccination mandates or domestic laws.',
'Negotiation, adoption, signature, ratification and entry into force are distinct treaty stages. National public-health powers and international cooperation should not be conflated.',
'Equitable access needs workable manufacturing, finance and supply-chain arrangements, not only statements of solidarity.|Sovereignty and cooperation can reinforce each other where information sharing and benefit sharing are credible.',
'April was not the May adoption milestone or proof of entry into force. Avoid claims that WHO gained power to dictate domestic restrictions.',
'How can pandemic cooperation improve equity while respecting national decision-making?','A-PANDEMIC')
add('Society & Welfare','04 · Maternal health & health-system equity',7,'UN maternal mortality report: progress slows','The World Health Day release updated estimates for 2000–2023.',
'UN agencies estimated around 260,000 maternal deaths globally in 2023.|The report describes a substantial decline since 2000 but slower improvement after 2016.|It highlights regional inequalities and preventable pregnancy/childbirth complications.|WHO, UNICEF, UNFPA, the World Bank Group and UNDESA’s Population Division contributed through the interagency estimation group.',
'Maternal mortality ratio uses maternal deaths per 100,000 live births; a death count and a ratio answer different questions.',
'Antenatal care must connect to skilled delivery, referral transport, blood, emergency obstetric care and respectful treatment.|AP evaluation should examine district and social-group gaps, not assume a better state average eliminates preventable deaths.',
'The 260,000 estimate concerns global 2023 deaths, not India-only deaths in April 2025. Revised estimation series can supersede older comparisons.',
'Why does reducing maternal mortality require a functioning referral system as well as institutional delivery?','A-MATERNAL',ap=True)
add('Culture & History','02 · Documentary heritage & preservation',18,'Gita and Natyashastra enter Memory of the World recognition','The April official statement welcomed inclusion in UNESCO’s documentary-heritage register.',
'The recognition concerned the Bhagavad Gita and Natyashastra.|Memory of the World addresses documentary heritage.|It is a different UNESCO framework from the World Heritage List of sites.|The Natyashastra is associated with performance, theatre and aesthetic traditions.',
'Documentary heritage, immovable World Heritage sites and intangible cultural heritage use different UNESCO programmes and procedures.',
'Recognition should support conservation, scholarly access, cataloguing and responsible digitisation.|Living performance traditions and manuscript preservation can reinforce each other, but inscription is not ownership of an entire cultural tradition.',
'Do not call these two new Indian World Heritage sites or confuse this register with Mudumal’s tentative-list status.',
'How can documentary-heritage conservation combine preservation with wider public access?','A-MEMORY',priority='P2',precision='reporting-day')
add('Security','01 · Terrorism & civilian protection',22,'Pahalgam terrorist attack','The 23 April official briefing described the attack and the government’s initial response.',
'The attack occurred in Pahalgam, Jammu and Kashmir, on 22 April.|MEA’s initial official account reported 25 Indian and one Nepali citizen killed.|The Cabinet Committee on Security reviewed the attack on 23 April.|Subsequent diplomatic measures are separately dated and do not establish the final status of investigations or prosecutions.',
'Terrorism prevention requires intelligence, local policing, civilian protection, evidence preservation and accountable prosecution.',
'Security responses should combine immediate protection with credible investigation and victim support.|Distinguish official attribution, investigative findings and adjudicated guilt; avoid communal generalisations or unverified claims about perpetrators.',
'Operation Sindoor began in May, not April. Do not present subsequent military action as part of the April chronology.',
'What institutional capabilities are necessary to protect civilians while preserving accountable counterterrorism?','A-CCS')
add('International Relations','01 · India–Pakistan & water diplomacy',23,'India holds Indus Waters Treaty in abeyance','The CCS decision was announced following the Pahalgam attack.',
'The official wording was that the 1960 treaty would be held in abeyance with immediate effect pending the specified condition on cross-border terrorism.|The same briefing announced closure of the Integrated Check Post Attari.|The treaty allocates eastern and western river uses through a detailed legal framework.|The April announcement was a policy decision; operational, legal and hydrological consequences require separate examination.',
'The eastern rivers are Ravi, Beas and Sutlej; the western rivers are Indus, Jhelum and Chenab, with treaty-specific rights and qualifications.',
'Transboundary water management combines security, international law, engineering constraints and downstream vulnerability.|A diplomatic announcement cannot instantaneously create storage or redirect an entire river system; distinguish rhetoric from physical capacity.',
'Do not rewrite the official term as proof that the treaty was mutually terminated, or claim that all flows stopped overnight.',
'Analyse why transboundary water disputes require legal and hydrological reasoning as well as diplomatic strategy.','A-CCS')
add('Security','04 · Naval aviation & defence procurement',28,'India–France agreement for 26 naval Rafale aircraft','An intergovernmental procurement agreement was signed.',
'The agreement covers 26 aircraft: 22 single-seat and four twin-seat aircraft.|The package includes training, simulators, weapons, associated equipment and performance-based logistics.|It also includes equipment for the existing Indian Air Force Rafale fleet.|The release describes technology cooperation for integration of indigenous weapons.',
'Contract signing, delivery, training, integration and operational deployment are distinct procurement stages. Land-based twin-seat trainers should not automatically be described as carrier-capable Rafale-M aircraft.',
'Capability depends on platform availability, weapons, maintenance, trained crews and carrier integration.|Evaluate lifecycle support and domestic integration capability alongside acquisition price and headline aircraft counts.',
'The agreement did not mean 26 aircraft had been delivered or were operational in April. Do not claim every aircraft in the package is an identical naval variant.',
'Why should defence procurement be assessed through lifecycle capability rather than platform counts alone?','A-RAFALE')
add('International Relations','02 · Bay of Bengal regionalism',4,'Sixth BIMSTEC Summit: Bangkok Vision 2030','The Bangkok summit advanced institutional and maritime cooperation.',
'The sixth summit was held in Bangkok on 4 April.|Members adopted the BIMSTEC Bangkok Vision 2030.|The outcomes included signing the Maritime Transport Cooperation Agreement.|BIMSTEC connects five South Asian and two South-East Asian members around a Bay of Bengal cooperation agenda.',
'Members are Bangladesh, Bhutan, India, Myanmar, Nepal, Sri Lanka and Thailand. BIMSTEC is distinct from SAARC and ASEAN.',
'Maritime connectivity can support trade, disaster response and blue-economy cooperation.|Implementation requires interoperable procedures, investment and political trust; agreement signing is not proof that all services or an FTA are operational.',
'Do not include Pakistan or Maldives as BIMSTEC members. An agreement and a vision document have different legal effects.',
'How can BIMSTEC convert geographic proximity into practical regional connectivity?','A-BIMSTEC',ap=True)
add('International Relations','03 · India–Sri Lanka cooperation',5,'Sri Lanka visit: defence and energy cooperation','The visit briefing described new bilateral and trilateral instruments.',
'India and Sri Lanka concluded an MoU on defence cooperation.|India, Sri Lanka and the UAE signed a trilateral MoU on developing Trincomalee as an energy hub.|The briefing connected cooperation with energy security, capacity building and regional stability.|Trincomalee is on Sri Lanka’s eastern coast.',
'An MoU outlines cooperation but is not identical to a completed project or mutual-defence alliance. Energy hubs combine storage, infrastructure, supply and markets.',
'Partner ownership, commercial feasibility and local benefit are essential to durable connectivity projects.|Maritime relations also involve fishing livelihoods and environmental concerns; cooperation should not obscure these unresolved challenges.',
'Do not treat the energy MoU as a commissioned hub or the defence MoU as an automatic alliance obligation.',
'How can neighbourhood infrastructure cooperation remain economically useful and politically sustainable?','A-SL')
add('Economy','11 · Trade policy & tariff uncertainty',9,'US reciprocal tariffs: announcement followed by a pause','April announcements created rapidly changing conditions for Indian exporters.',
'The 2 April announcement listed a 26% India-specific reciprocal tariff rate.|On 9 April the higher country-specific rates were paused for 90 days for most partners, including India.|A 10% baseline additional tariff continued for covered goods during the pause.|Product exclusions and separate sectoral tariffs require examination of the relevant instrument.',
'A tariff is levied at importation; its economic incidence can be shared across importers, consumers and exporters. A headline country rate does not describe every product.',
'Uncertainty can deter orders and investment before a tariff’s final economic impact is known.|AP export sectors such as seafood require product-specific exposure analysis, standards compliance and market diversification rather than a single blanket percentage.',
'This is the April policy sequence, not the latest US tariff regime. Do not add 26% and 10% indiscriminately or assume every export faces identical treatment.',
'How should an export-oriented economy respond to volatile and discriminatory trade barriers?','A-TARIFF',ap=True)
add('Economy','06 · Global growth forecasts',22,'IMF April WEO lowers growth outlook','The forecasts reflected trade tensions and heightened policy uncertainty.',
'Global growth was projected at 2.8% for 2025, down from the January projection.|India’s FY2025–26 projection was cut to 6.2% from 6.5%.|The India forecast for FY2026–27 was 6.3%.|These are forecasts, not realised national-account growth results.',
'The IMF uses calendar-year global figures and fiscal-year conventions for India’s reported forecasts; forecast revisions reflect assumptions and incoming information.',
'Tariffs can weaken demand, disrupt supply chains and affect investment through uncertainty.|Resilience requires domestic demand, competitive production and diversified trade, while avoiding the claim that relatively faster growth eliminates external vulnerability.',
'Do not compare a fiscal-year India forecast with a calendar-year global figure without labelling periods, or call April forecasts final outcomes.',
'Explain how trade-policy uncertainty can reduce growth even before all announced tariffs are implemented.','A-IMF')
add('Security','03 · Counterterrorism & legal cooperation',10,'Tahawwur Rana extradited from the United States','The accused in the Mumbai-attack conspiracy case was brought to India after US legal proceedings.',
'The transfer took place on 10 April.|The case relates to alleged involvement in the 2008 Mumbai attacks.|Extradition followed treaty-based and judicial processes in the United States.|Indian investigation, custody and trial are separate stages after transfer.',
'Extradition differs from deportation, expulsion and prisoner transfer. Cooperation depends on treaty conditions, judicial scrutiny and applicable safeguards.',
'Cross-border investigation needs durable evidence cooperation and compliance with conditions of surrender.|Extradition can enable prosecution but does not itself establish guilt in the receiving court.',
'Use accused/alleged for unresolved charges. Extradition is not a conviction or a substitute for a fair trial.',
'Why does effective counterterrorism require sustained legal cooperation across borders?','A-RANA',priority='P2')
add('Environment','04 · Protected areas & source verification',24,'Similipal national-park notification: avoid the ordinal trap','Odisha notified the specified national-park area; reporting exposed inconsistent national-count claims.',
'The notification concerned 845.70 square kilometres of Similipal in Odisha.|It was described as Odisha’s second national park after Bhitarkanika.|Similipal also has tiger-reserve and biosphere-reserve contexts, which are not identical designations.|A follow-up investigation contrasted the state’s 107th-national-park claim with a different WII count.',
'Distinguish legal designation, notified area and the wider landscape. A national ordinal depends on a dated, reconciled authoritative list.',
'Area-specific protection must be understood alongside habitat connectivity, community rights and existing management institutions.|Where credible sources conflict, prioritise uncontested location/area facts and flag the unresolved count rather than forcing a false precision.',
'Do not memorise 106th versus 107th as settled from a single headline. The discrepancy remains an explicit research gap.',
'How should conservation reporting distinguish notification milestones from actual ecological outcomes?','A-SIMILIPAL',priority='P2')
add('Economy','09 · Transport engineering & resilience',6,'New Pamban Rail Bridge inaugurated','The new link to Rameswaram opened in Tamil Nadu.',
'The inauguration took place on 6 April.|The official account identifies it as India’s first vertical-lift sea bridge.|It supports the rail connection between the mainland and Rameswaram.|The lift arrangement accommodates vessel movement while serving rail connectivity.',
'A vertical-lift span moves upward; it differs from the older bridge’s opening mechanism. Marine structures face corrosion, wind, wave and operational-safety challenges.',
'Connectivity infrastructure must be appraised through maintenance, climate resilience, safe operations and reliable access.|Inauguration confirms a milestone, not permanent freedom from closures, maintenance requirements or extreme-weather risk.',
'The location is Tamil Nadu, not AP. Do not confuse the new bridge’s mechanism with that of the old Pamban bridge.',
'Why should infrastructure evaluation combine engineering innovation with lifecycle resilience?','A-PAMBAN',priority='P2')
# Merge passage analysis into the existing assent seed instead of double-counting one reform.
waqf=next(n for n in J if n['id']=='APR25-002')
for n in N:
 if n['id']=='CA-044':
  n.update({k:v for k,v in waqf.items() if k not in ['id','date','title','sources','facts']})
  n.update(title='Waqf Amendment Act: passage and 5 April assent',sources=['LAW','A-PRS'],facts=['The Gazette records presidential assent on 5 April 2025, Act No. 14 of 2025.']+waqf['facts'])
J=[n for n in J if n['id']!='APR25-002']
N=[n for n in N if not n['id'].startswith('APR25-')]+J
for f,v in [('notes.json',N),('sources.json',S),('source-access.json',A)]: (R/'data'/f).write_text(json.dumps(v,ensure_ascii=False,indent=2))
print('April new',len(J),'April total',sum(n['date'].startswith('2025-04') for n in N),'archive',len(N),'sources',len(S))
