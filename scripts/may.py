"""May 2025: independently researched policy/AP batch plus selected official magazine themes."""
import json,pathlib
R=pathlib.Path(__file__).resolve().parents[1];N=json.loads((R/'data/notes.json').read_text());S=json.loads((R/'data/sources.json').read_text());A=json.loads((R/'data/source-access.json').read_text());D=json.loads((R/'research/magazine-review/vision-inventory.json').read_text());J=[]
def source(k,t,u,access):
 S[k]=[t,u];A[k]=dict(title=t,url=u,access=access,checked_on='2026-11-06')
source('MY-PRS','PRS · May 2025 monthly policy review, all six chunks read','https://prsindia.org/policy/monthly-policy-review/may-2025','Full public synthesis read; linked primaries not necessarily independently read')
source('MY-MISS','PIB · MISS continuation, 28 May 2025','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2131988','Substantive primary release read')
source('MY-IBM','IBM · Amaravati quantum plans, 2 May 2025','https://newsroom.ibm.com/2025-05-02-ibm,-tata-consultancy-services-and-government-of-andhra-pradesh-unveil-plans-to-deploy-indias-largest-quantum-computer-in-the-countrys-first-quantum-valley-tech-park','Substantive primary announcement read; issuer claims not independent performance certification')
source('MY-AP','PMIndia · Amaravati development, 2 May 2025','https://www.pmindia.gov.in/en/news_updates/pm-lays-foundation-stone-inaugurates-development-works-worth-over-rs-58000-crore-in-amaravati-andhra-pradesh/','Selected substantive primary passages read, not all web chunks')
source('MY-DRDO','PIB · Nagayalanka foundation stone, 2 May 2025','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2126248&reg=48&lang=2','Primary search excerpt inspected; full-document review pending')
source('MY-YOGA','Yo! Vizag · YogAndhra curtain raiser, 21 May; report 22 May','https://www.yovizag.com/visakhapatnam-kicks-off-month-long-yogandhra-campaign-ahead-of-international-yoga-day/','Local reporting search excerpt inspected')
source('MY-PSLV','The New Indian Express · PSLV-C61 setback, 18 May 2025','https://www.newindianexpress.com/nation/2025/May/18/pslv-c61-mission-could-not-be-accomplished-isro','Substantive search excerpt inspected; distinguishes initial statement from root-cause determination')
source('MY-RICE','ICAR/IARI · Genome-edited rice, 4 May 2025','https://www.iari.res.in/files/Latest-News/ICAR_Genome_Edited_Rice_04052025.pdf','Primary press-note excerpt inspected')
source('MY-WHO','WHO · Pandemic Agreement legal sequence','https://www.who.int/news-room/questions-and-answers/item/pandemic-prevention--preparedness-and-response-accord','Official Q&A search excerpts inspected; May adoption distinguished from later legal steps')
source('MY-HDI','UNDP India · HDR release announcement, 6 May 2025','https://x.com/UNDP_India/status/1919645822192697523','Official institutional social-post excerpt inspected; not full statistical annex')
source('MY-PLFS','MoSPI · First monthly PLFS bulletin, 15 May 2025','https://mospi.gov.in/sites/default/files/press_release/Press_note_MB01_Monthly_bulletin_Final.pdf','Primary bulletin search excerpts inspected')
source('MY-SINDOOR','PIB · Initial Operation Sindoor statement, 7 May 2025','https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2127370&reg=3&lang=1','Primary release search excerpt inspected; battlefield claims attributed to issuing authority')
source('MY-EC-REVIEW','Supreme Court Observer · Later Vanashakti litigation (2026 contextual warning)','https://www.scobserver.in/journal/vanashakti-iii-restores-rule-and-exception/','Later legal-reporting excerpt inspected; not a full current-law certification')
def add(subject,block,day,title,why,facts,static,analysis,trap,mains,ap=False,priority='P1',sources=None,slug=None):
 keys=sources or ['MY-PRS'];mag={}
 if slug:
  a=next(a for a in D['2025-05']['articles'] if a['url'].endswith('/'+slug));k='V2505-'+str(D['2025-05']['articles'].index(a)+1).zfill(2)
  source(k,'Vision IAS · May edition · '+a['title'].removeprefix('Next Article '),a['url'],'Lead and selected substantive public passages inspected; full topic/primary audit pending');keys=[k]+(sources or []);a['review']='Selected passages incorporated into original May note';mag=dict(magazine_edition='2025-05',magazine_posted='2025-06-17',content_type='magazine-supplement')
 J.append(dict(id=f'MY25-{len(J)+1:03}',date=f'2025-05-{day:02}' if day and not slug else '2025-05-31',date_precision='day' if day and not slug else 'month',subject=subject,block=block,title=title,why=why+(' Editorial coverage month is not an event date.' if slug else ''),facts=facts.split('|'),static_link=static,analysis=analysis.split('|'),trap=trap,mains=mains,ap=ap,priority=priority,sources=keys,status='Historical May snapshot; subsequent implementation, law and statistics require re-checking',checked='2026-11-06',evidence_access='Original synthesis from listed access levels; source-backed essentials distinguished from original analytical guidance',**mag))
add('Economy','01 · National accounts & growth',30,'FY2024–25 provisional GDP: 6.5% real growth','NSO released provisional annual and fourth-quarter estimates.',
'Real GDP growth was estimated at 6.5% for FY2024–25, using the 2011–12 price base.|Q4 growth was estimated at 7.4% year-on-year.|FY2024–25 GVA growth was estimated at 6.4%; construction grew 9.4% in this vintage.',
'GDP equals GVA plus product taxes minus product subsidies; real growth removes the chosen price effect rather than measuring nominal rupee expansion.',
'Sectoral growth helps identify investment and employment patterns but does not directly measure distribution or job quality.|Use the release vintage: subsequent revisions can change historical values without making the original release misreported.',
'FY2024–25 is not calendar year 2025, and a high quarterly rate is not the annual growth rate.',
'How should growth estimates be assessed alongside employment and household welfare?')
add('International Relations','02 · Trade agreements & implementation',6,'India–UK FTA talks concluded: not yet entry into force','The governments announced conclusion of negotiations.',
'The announced package envisaged wide goods tariff liberalisation and services access.|A separate double-contribution arrangement concerns eligible temporary workers and social-security contributions.|May negotiation conclusion must be distinguished from subsequent signature and treaty commencement.',
'An FTA generally reduces barriers among partners; rules of origin determine which goods qualify and prevent simple transshipment abuse.',
'Assess tariff schedules, exclusions and firm-level compliance costs rather than treating headline coverage as immediate universal free trade.|AP exporters need product-specific rules and actual effective dates before pricing expected benefits.',
'Do not date later signature or ratification to May; the social-security arrangement is not a general income-tax exemption.',
'What determines whether an FTA translates negotiated market access into realised exports?',True)
add('International Relations','02 · Trade agreements & implementation',9,'India–Chile CEPA terms of reference','The two countries agreed a negotiating framework.',
'The terms of reference aim to build on the existing preferential trade agreement.|The proposed agenda extends to digital services, investment and critical minerals.|Terms of reference define the negotiation’s scope, not completed concessions.',
'A preferential agreement, a comprehensive agreement and an agreement to negotiate are different legal stages.',
'Diversification can create opportunities where infrastructure, standards and reliable supply accompany diplomacy.|Critical-mineral cooperation needs commercially viable extraction and processing, not only a mention in a negotiating agenda.',
'Do not call agreed negotiating terms a signed CEPA with immediately operative zero duties.',
'How can India’s trade strategy connect market access with resilient input supply?',priority='P2')
add('Economy','04 · Export taxes & competitiveness',27,'RoDTEP benefits restored for specified export categories','The government announced restoration from 1 June 2025.',
'The decision covered eligible exports from Advance Authorisation, SEZ and EOU categories.|RoDTEP remits specified embedded duties and taxes not refunded elsewhere.|Announcement in May and eligibility from June are separate dates.',
'Tax remission aims to avoid exporting embedded taxes; it differs conceptually from paying exporters simply for selling abroad.',
'Predictable remission supports costing and working-capital planning.|Evaluate claim rules, rates and timeliness rather than assuming a headline restoration reimburses every domestic tax.',
'Restoration is not retroactive coverage of every shipment in a previously excluded interval unless explicitly provided.',
'Why does predictable tax-remission administration matter for export competitiveness?',True,priority='P2')
add('Economy','05 · Startup finance & guarantees',9,'CGSS ceiling raised: guarantee is not a grant','DPIIT notified revised startup credit-guarantee provisions.',
'The maximum guarantee cover per borrower was raised from ₹10 crore to ₹20 crore.|The reported default coverage is 85% for loans up to ₹10 crore and 75% above that amount.|The annual fee for 27 specified champion sectors was reduced to 1%.',
'A credit guarantee shares eligible lender loss; it does not cancel borrower repayment obligations or replace credit appraisal.',
'Guarantees can address collateral constraints for viable firms but expose public resources if appraisal is weak.|AP startup support should link innovation assistance with cash-flow assessment and transparent eligibility.',
'₹20 crore is not a ₹20 crore cash grant for each recognised startup.',
'How can credit guarantees expand startup finance without encouraging poor underwriting?',True)
add('Agriculture','01 · MSP, procurement & price risk',28,'Kharif MSP 2025–26: announced prices versus procurement','The Cabinet approved MSPs for the coming marketing season.',
'Common paddy MSP was fixed at ₹2,369 per quintal, against ₹2,300 previously.|Ragi MSP was ₹4,886 and tur/arhar ₹8,000 per quintal.|The announcement refers to the 2025–26 kharif marketing season.',
'An MSP announcement, physical procurement and a universal legally enforceable buying obligation are distinct.',
'AP assessment should consider eligible quality, procurement access, payment timeliness and market prices.|Higher MSP alone cannot ensure diversification where water, extension, insurance and buyers are missing.',
'Do not infer that every farmer sells all output to government at the MSP.',
'How should price support be coordinated with sustainable cropping choices?',True)
add('Agriculture','02 · Credit & interest support',28,'MISS continued unchanged: separate Budget ambition from May terms','The Cabinet retained the interest-subvention component for FY2025–26.',
'The May release described eligible short-term KCC loans up to ₹3 lakh at 7%.|Eligible lenders receive 1.5% interest subvention; prompt repayment incentive can bring the borrower rate to 4%.|For loans exclusively for animal husbandry or fisheries, the interest benefit applies up to ₹2 lakh in this release.',
'Lender subvention and borrower prompt-repayment benefit are different components. A Budget proposal is not sufficient evidence that every operational limit has changed.',
'Credit support can reduce seasonal financing costs, but access depends on documentation, lending and repayment conditions.|Track the implementing circular and date before replacing operative thresholds with Budget announcements.',
'The February Budget’s ₹5 lakh enhancement announcement must not be silently substituted for the explicit unchanged ₹3 lakh terms in the 28 May decision.',
'Why must welfare-policy evaluation distinguish announcements from operational rules?',True,sources=['MY-MISS','MY-PRS'])
add('Polity & Governance','03 · Land records & registration',0,'Draft Registration Bill 2025: digital submission and expanded coverage','The government invited comments on a proposed replacement for the 1908 Act.',
'The draft expands specified documents requiring compulsory registration.|It provides for electronic submission and consent-based Aadhaar authentication.|It proposes additional registration supervisory offices that states may appoint.',
'Registration records documents; it is not automatically conclusive state-guaranteed title to every parcel.',
'Digitisation can reduce transaction friction if fraud prevention, accessible alternatives and grievance remedies are built in.|AP applications need reliable legacy records and verification, not simply moving a flawed process online.',
'This is a draft consultation, not proof that the Registration Act, 1908 was already repealed in May.',
'How can land-registration reform improve access without overstating title security?',True)
add('Environment','02 · Climate finance & classification',0,'Draft climate-finance taxonomy: supportive and transition activities','The Finance Ministry sought feedback on the proposed framework.',
'The draft classifies climate-supportive activities separately from transition activities.|It discusses emissions avoidance, intensity reduction and resilience.|Transition categories address sectors with limited feasible low-emission alternatives.',
'A taxonomy classifies activities; it is not itself a loan sanction, carbon-credit issuance or binding national emissions cap.',
'Credible thresholds and disclosure can improve allocation and reduce greenwashing.|Transition finance requires measurable progress and safeguards against locking in high-emission assets indefinitely.',
'Do not present a draft framework as a final mandatory list already certifying every investment.',
'How can transition finance remain credible while recognising development constraints?')
add('Economy','06 · Payment-system governance',20,'Payments Regulatory Board Regulations 2025','RBI issued a revised institutional framework.',
'The RBI Governor remains chairperson.|The board includes the deputy governor responsible for payment systems, an RBI officer and three central-government nominees.|The regulations replace the earlier 2008 board regulations.',
'Institutional governance, operational payment infrastructure and settlement finality are different aspects of the payments system.',
'Diverse technical expertise can improve oversight where mandates and accountability are clear.|Assess coordination and conflict-management safeguards alongside changes in composition.',
'The Payments Regulatory Board is not the Monetary Policy Committee and does not set the repo rate.',
'What governance capacities are needed as payment networks become critical public infrastructure?',priority='P2')
add('Economy','07 · Portfolio flows & debt markets',8,'FPI corporate-debt relaxation: identify the limits removed','RBI relaxed specified general-route constraints.',
'The relaxation removed the short-term corporate-debt investment limit described in the review.|It also removed specified investor concentration limits under the general route.|General route, voluntary retention route and fully accessible route remain distinct frameworks.',
'An investor-level sublimit is not the same as every aggregate regulatory ceiling, instrument condition or reporting rule.',
'Easier participation can deepen corporate-debt markets but also requires liquidity and macroprudential monitoring.|Firms’ financing benefits depend on actual demand, credit quality and currency-risk management.',
'Do not infer the abolition of every limit on all foreign investment in Indian debt.',
'How can debt-market opening balance depth with resilience to volatile flows?',priority='P2')
add('Economy','08 · Coal linkages & electricity',7,'Revised SHAKTI: coal allocation is not electricity-market deregulation','The Cabinet approved changes to coal allocation for the power sector.',
'Government-owned generation allocations at notified prices are retained.|For private generators, revised linkage auctions use a premium above the notified price.|Linkage duration can be up to 12 months or between one and 25 years.',
'A coal linkage supplies fuel; a power purchase agreement governs electricity sales. They are not interchangeable contracts.',
'Flexible sales and fuel availability can improve utilisation but must be assessed alongside transport, emissions and demand.|Fuel-security decisions should not crowd out transparent comparison with clean generation and storage.',
'A linkage is not an assurance that the plant runs profitably or that every electricity tariff is unregulated.',
'How should fuel-allocation reform fit a reliable and lower-emission power transition?')
add('Economy','09 · Mineral auctions & execution',1,'Draft mineral-auction timelines: speed with statutory safeguards','The Mines Ministry consulted on intermediary milestones.',
'The proposal sets steps between a Letter of Intent and execution/operationalisation.|The draft covers mining-plan approval, environmental clearance and lease execution stages.|Specified delays can lead to appropriation and replenishment of performance security.',
'An LoI is not an operating mine or a substitute for environmental and other statutory permissions.',
'Time-bound procedures can reduce avoidable uncertainty if agency capacity and accountability improve.|Clearance deadlines should not turn evidence-based appraisal into an automatic formality.',
'These were draft amendments; the proposed timeline is not proof that every clearance has a deemed-approval rule.',
'How can mining procedures become predictable without weakening safeguards?',priority='P2')
add('Environment','03 · Environmental clearance & legal chronology',16,'Vanashakti May ruling: preserve the historical snapshot','The Supreme Court rejected the retrospective-clearance mechanism in the May judgment.',
'The May decision invalidated the challenged retrospective-EC mechanism.|It linked prior appraisal to environmental-law and Article 21 protections.|Already granted clearances were protected by that decision’s relief.',
'Prior environmental appraisal seeks to evaluate alternatives and impacts before irreversible action; ex post approval changes that incentive.',
'Effective enforcement requires credible consequences and administratively workable compliance systems.|Later litigation matters: reporting reviewed for this edition records a November 2025 recall and subsequent 2026 proceedings.',
'Do not cite the May judgment as a timeless final statement of current law. Full latest judgment/order review remains pending.',
'Why does prior appraisal matter, and how should courts handle projects built without clearance?',sources=['MY-PRS','MY-EC-REVIEW'])
add('Society & Welfare','02 · Skills, ITIs & industry',7,'ITI upgradation: shared funding and industry involvement','The Cabinet approved the national scheme and five centres of excellence.',
'The approved scheme targets 1,000 government ITIs and five National Centres of Excellence.|The proposed ₹60,000 crore outlay comprises ₹30,000 crore central, ₹20,000 crore state and ₹10,000 crore industry shares.|Industry involvement extends to planning and management of upgradation.',
'An approved multi-year outlay, annual expenditure and a completed training outcome are different metrics.',
'Equipment matters when instructors, curricula and employer demand are aligned.|AP should measure completion, placement quality, wages and inclusion rather than training enrolment alone.',
'Do not count every targeted ITI as already upgraded or all outlay as money spent in May.',
'How can industry-linked skilling avoid becoming an infrastructure-only programme?',True)
add('Environment','04 · Renewable contracts & certificates',22,'Draft virtual PPAs: financial contracts, not a dedicated wire','CERC invited comments on VPPA guidelines.',
'The draft envisages long-term agreements between renewable generators and designated consumers.|Electricity is not physically exchanged between the contracting parties under the VPPA.|The proposed arrangement transfers relevant renewable energy certificates from earmarked generation.',
'Physical supply, financial settlement and environmental attributes are distinct transactions; claims must avoid double counting.',
'VPPAs may broaden access to renewable procurement where risks and certificate ownership are clear.|Counterparty risk, price basis and dispute mechanisms require attention alongside sustainability claims.',
'A draft VPPA is not an already operative national contract standard or permission to claim identical renewable attributes twice.',
'What governance safeguards make renewable-energy attribute claims credible?',priority='P2')
add('Science & Technology','03 · Satellite communications & spectrum',9,'TRAI satcom recommendations: policy advice versus allocation','TRAI proposed terms for administratively assigned satellite spectrum.',
'The reported recommendations include a 4% adjusted-gross-revenue charge subject to a minimum.|They propose an additional annual urban subscriber charge for NGSO services.|They recommend assignment for up to five years with possible extension.',
'GSO satellites appear fixed relative to the Earth; NGSO satellites do not. Administrative assignment is distinct from an auction.',
'Satellite connectivity can complement terrestrial networks in remote areas but affordability and capacity remain constraints.|AP disaster planning should consider resilient combinations rather than assume satellites replace all fibre and mobile networks.',
'TRAI recommendations are not proof that all suggested fees have already been adopted or that every operator is licensed.',
'How should satellite-spectrum policy balance inclusion, investment and fair competition?',True)
add('Society & Welfare','03 · Emergency care & road safety',5,'Cashless road-accident care: capped benefit and designated hospitals','The Ministry notified the treatment scheme.',
'The scheme provides up to ₹1.5 lakh per victim for a maximum of seven days from the accident.|Cashless treatment is provided through designated hospitals.|Funding uses the Motor Vehicle Accident Fund; states have implementation roles.',
'A treatment entitlement, a designated facility network and actual timely admission are separate requirements.',
'Reducing payment delays can support urgent care, but hospital availability, ambulance referral and claims administration determine access.|AP should track treatment refusals, time-to-care and rehabilitation gaps in addition to enrolment/awareness.',
'The cap is not unlimited lifetime treatment or reimbursement at any hospital under every circumstance.',
'How can emergency-care financing be coordinated with prevention and trauma-system capacity?',True)
add('Andhra Pradesh','01 · Capital infrastructure & delivery',2,'Amaravati relaunch: mixed project stages, not a completed capital','The PM launched a package including resumed capital-city works.',
'The official event value was over ₹58,000 crore across multiple development projects.|The package mixed inaugurations, dedications and foundation stones.|Capital institutions, roads, connectivity and flood-management infrastructure were part of the wider development agenda.',
'An aggregate event value is not the amount already spent or the value of projects all completed that day.',
'Implementation needs credible finance, procurement, land-pooling commitments and flood resilience.|Assess delivery milestones and livelihood safeguards alongside metropolitan economic ambition.',
'Do not describe every project as operational on 2 May or treat the whole package as capital-building construction alone.',
'What institutional safeguards can make capital-city development financially and socially sustainable?',True,sources=['MY-AP'])
add('Andhra Pradesh','02 · Quantum ecosystem & research',2,'Amaravati Quantum Valley: planned hardware, present cloud access','IBM described plans with AP and its collaboration with TCS.',
'The envisioned park anchor is IBM Quantum System Two with a 156-qubit Heron processor.|The IBM release makes physical deployment conditional on export licences and definitive agreements.|The announcement distinguishes cloud-resource access arrangements from a future on-site installation.',
'Physical qubits, logical error-corrected qubits and demonstrated useful quantum advantage are different measures.',
'Talent, algorithms, cryogenic/infrastructure capability and relevant users matter alongside acquiring hardware.|Public evaluation should test milestones and opportunity costs rather than promise that qubit count guarantees practical breakthroughs.',
'May plans do not prove the computer was installed or that the project achieved quantum advantage.',
'How can AP build an effective quantum ecosystem rather than a hardware-led prestige project?',True,sources=['MY-IBM'])
add('Andhra Pradesh','03 · Defence testing infrastructure',2,'Nagayalanka missile test range: foundation-stage investment','The event included laying the foundation for the DRDO range.',
'The reported range cost was around ₹1,460 crore.|Planned facilities include instrumentation, radars, telemetry and electro-optical systems.|The location is Nagayalanka in Andhra Pradesh.',
'A test range measures system performance under controlled conditions; it is not itself a missile-production factory.',
'Additional testing capacity can support reliable indigenous systems when safety, environmental compliance and technical validation are maintained.|Coastal infrastructure needs careful assessment of communities and ecosystems as well as strategic value.',
'Foundation laying is not evidence of commissioning, successful weapon tests or full operating capacity.',
'How should strategic testing infrastructure reconcile capability development with local safeguards?',True,sources=['MY-DRDO'])
add('Andhra Pradesh','04 · Public health participation',21,'YogAndhra campaign: May preparation versus June event','Local reporting recorded the Visakhapatnam curtain raiser.',
'The month-long initiative began on 21 May ahead of International Yoga Day.|The local launch was held at RK Beach, Visakhapatnam.|Training and demonstrations were planned ahead of the June programme.',
'Campaign participation is an output, not direct evidence of sustained behaviour change or clinical benefit.',
'Public-health activities can encourage accessible routines if participation is inclusive and voluntary.|Evaluate regular engagement and safe practice instead of assuming a record attendance figure establishes health outcomes.',
'The May launch and 21 June mass event are distinct. Do not backdate June turnout or records into May.',
'How can mass public-health campaigns produce measurable and sustained benefits?',True,priority='P2',sources=['MY-YOGA'])
add('Science & Technology','01 · Launch systems & mission reliability',18,'PSLV-C61/EOS-09: mission not accomplished','The launch from Sriharikota encountered a third-stage anomaly.',
'The first two stages were reported to perform normally.|ISRO’s initial statement identified an observation in the third stage and said the mission was not accomplished.|EOS-09 was intended as a radar Earth-observation mission.',
'A launch vehicle’s flight number, a spaceport launch count and a mission’s success are different descriptors.',
'Failure analysis and corrective qualification are essential to dependable operations.|Radar payload capabilities should be taught as intended mission design, not data already being delivered by a successfully deployed satellite.',
'Do not report EOS-09 as successfully operating in orbit or treat a preliminary suspected cause as a final investigation finding.',
'Why is transparent failure analysis central to high-reliability space programmes?',True,sources=['MY-PSLV'])
add('Agriculture','04 · Crop biotechnology & field evidence',4,'Genome-edited rice: Kamala and Pusa DST Rice 1','ICAR announced two rice varieties.',
'DRR Dhan 100 (Kamala) was developed by ICAR-IIRR, Hyderabad, from Samba Mahsuri.|Pusa DST Rice 1 was developed by ICAR-IARI from MTU 1010.|The announcement concerns targeted genome editing rather than assuming every variety involves foreign-gene insertion.',
'Genome editing includes multiple techniques and outcomes; it is not universally synonymous with transgenesis or absence of regulatory obligations.',
'Benefits need location-specific agronomy, seed availability and independent performance evidence.|AP’s rice systems make stress tolerance relevant, but trial averages cannot guarantee identical yields on every farm.',
'Do not present a launch as universal seed availability or make a blanket world-first claim without historical verification.',
'How should agricultural biotechnology combine innovation with transparent field evidence?',True,sources=['MY-RICE'])
add('International Relations','05 · Global health governance',20,'WHO Pandemic Agreement adopted: further legal steps remain','The World Health Assembly adopted the negotiated agreement.',
'Adoption followed the April conclusion of negotiations.|The agreement envisages cooperation on pandemic prevention, preparedness and response.|The PABS annex and subsequent signature/ratification sequence must be distinguished from adoption.',
'Adoption, opening for signature, national ratification and entry into force are separate treaty stages.',
'Equitable access requires practical financing, production and benefit-sharing arrangements.|Pathogen sharing and access to resulting countermeasures raise trust and distributive-justice questions.',
'Do not state that May adoption made the treaty automatically binding on every WHO member or transferred national health authority wholesale to WHO.',
'What makes equitable access a core condition of effective global pandemic cooperation?',sources=['MY-WHO'])
# Magazine-selected themes; concise originals, no wholesale source reproduction.
add('Polity & Governance','01 · Parliamentary agenda & representation',0,'Private Members’ Bills: legislative initiative beyond ministers','The magazine discussed declining space for non-government legislation.',
'A private member is an MP who is not a minister.|Private Members’ Bills create opportunities to propose legislation and debate neglected questions.|Introduction, debate and passage are separate stages.',
'Government/private-member classification depends on the sponsor, not whether a bill concerns private interests.',
'Low passage does not mean zero policy influence: debates can shape subsequent government proposals.|Adequate parliamentary time and research assistance can improve scrutiny without guaranteeing adoption.',
'There is no blanket exemption from party whips or the Tenth Schedule merely because a vote concerns a Private Member’s Bill.',
'How can Parliament make non-government legislative initiative more meaningful?',slug='private-member-bill')
add('Economy','02 · Employment statistics & definitions',0,'Revamped PLFS: first monthly bulletin and comparable denominators','The magazine examined the redesign effective from January 2025.',
'The first monthly bulletin was released on 15 May for April 2025.|It reported 5.1% CWS unemployment for persons aged 15 and above.|The redesigned survey extends short-interval indicators across rural and urban areas.',
'UR uses the labour force as denominator; WPR and LFPR use population. Current weekly status and usual status use different reference periods.',
'High-frequency estimates help detect shifts when seasonal patterns, sampling uncertainty and redesign breaks are understood.|Unemployment alone misses low earnings, irregular work and withdrawal from job search.',
'The April reference month is not the May publication month; do not directly mix CWS and usual-status estimates.',
'How can labour statistics reveal job quality as well as unemployment?',sources=['MY-PLFS'],slug='revamped-periodic-labor-force-survey-plfs')
add('Economy','10 · Ports & maritime logistics',0,'Vizhinjam: transshipment depends on networks, not depth alone','The issue covered inauguration of the Kerala port.',
'Vizhinjam is designed as a deepwater container transshipment hub.|The project uses a PPP within a landlord-port framework.|Transshipment transfers cargo between vessels en route to its final destination.',
'Container throughput, berth depth and ship size describe different aspects of port capability.',
'Competitive turnaround, customs, shipping-line connectivity and hinterland services influence actual cargo capture.|AP ports should be evaluated in relation to their cargo mix and connectivity, not assumed to replicate a different hub’s commercial model.',
'Do not treat inauguration or natural depth as evidence that all projected traffic and economic benefits have materialised.',
'What determines whether port infrastructure becomes a competitive logistics network?',True,slug='vizhinjam-international-seaport')
add('Economy','09 · Mining benefits & district governance',0,'DMFs: mining-affected communities before generic district spending','The issue reviewed parliamentary scrutiny of DMF implementation.',
'DMFs arise under the MMDR Act framework amended in 2015.|They are intended to benefit mining-affected persons and areas.|State rules and the relevant mineral/lease framework shape governance and contributions.',
'Mining royalty and the DMF contribution are not the same levy or a substitute for compliance and rehabilitation duties.',
'Participatory planning and public reporting can connect collections with health, water and livelihood needs.|AP mining districts need evidence on affected settlements and project outcomes, not only fund utilisation ratios.',
'Do not assume every district is mining-affected or that any general infrastructure project automatically meets beneficiary priorities.',
'How can DMF governance avoid replacing community benefit with spending targets?',True,slug='district-mineral-foundation-dmf')
add('Security','01 · Counterterrorism & escalation management',7,'Operation Sindoor: attribute official claims and date each phase','The issue analysed the response following the Pahalgam attack.',
'India’s 7 May statement reported strikes on nine terrorist-infrastructure sites.|The initial statement described the action as focused and non-escalatory and said it did not target Pakistani military facilities.|The initial phase must be distinguished from subsequent military exchanges and diplomatic developments.',
'Deterrence, operational objectives, escalation control and political signalling are separate levels of analysis.',
'Use reliable dated statements and distinguish official battle-damage claims from independently established evidence.|Civilian protection, information verification and disciplined communication remain important during security crises.',
'Do not extend the initial no-military-target statement to every later phase or infer a formal change to nuclear doctrine from rhetorical framing.',
'How can counterterrorism strategy combine credible deterrence with escalation control?',sources=['MY-SINDOOR'],slug='indias-new-security-doctrine')
add('Security','02 · Integrated air defence & evidence',0,'Air defence: sensors, networks and interceptors work together','The magazine examined technologies discussed during Operation Sindoor.',
'Air-defence systems connect detection, tracking, command decisions and response.|IACCS integrates information to support air operations.|Counter-drone measures can involve detection, electronic responses and kinetic interception.',
'An early-warning sensor, a command network and an interceptor are not interchangeable components.',
'Integrated systems need interoperability and resilient communications as well as individual platform performance.|Avoid unverified success-rate claims and attribution of every engagement to one publicly named weapon.',
'A platform’s presence in the national inventory is not proof of deployment or a particular kill in the operation.',
'Why does network integration matter as much as individual hardware in air defence?',slug='defense-technology-in-operation-sindoor')
add('Environment','05 · Chemicals & international conventions',0,'BRS COPs: three treaties, distinct legal functions','The issue reviewed the Geneva chemicals-and-waste meetings.',
'Basel addresses transboundary movements and management of hazardous wastes.|Rotterdam’s listed chemicals are subject to prior informed consent procedures.|Stockholm targets persistent organic pollutants through its annex-based controls.',
'Prior informed consent is not automatically a universal ban; treaty annex, exemption and implementation details matter.',
'Coordinated work can reduce chemical risks across production, trade, use and disposal.|Domestic effectiveness requires inventories, enforcement, alternatives and environmentally sound waste handling.',
'Do not confuse Stockholm chemical elimination restrictions with Rotterdam consent rules or the climate COP process.',
'Why do chemicals and waste require linked but distinct international legal instruments?',slug='2025-conferences-of-the-parties-to-the-basel-rotterdam-and-stockholm-convention')
add('Environment','06 · Biodiversity, knowledge & benefit sharing',0,'Access and benefit sharing: rights, institutions and traceability','The issue covered the 2025 ABS regulatory framework.',
'ABS links access to biological resources/associated knowledge with fair benefit sharing.|India’s institutions include NBA, State Biodiversity Boards and local Biodiversity Management Committees.|The domestic framework operates under the Biological Diversity Act and applicable regulations.',
'The CBD and Nagoya Protocol provide related international context; domestic permissions depend on specific user and use categories.',
'Fair implementation needs identifiable beneficiaries, documentation and enforceable benefit arrangements.|AP biodiversity governance should support local participation without assuming every biological transaction has identical permissions.',
'Do not confuse NBA regulations with a constitutional amendment or assume a named traditional-knowledge example proves uniform benefit delivery.',
'How can ABS reconcile research access with justice for resource and knowledge holders?',True,slug='biological-diversity-access-and-benefit-sharing-regulation-2025')
add('Society & Welfare','01 · Human development & measurement',0,'HDR 2025: publication year differs from HDI data year','The issue discussed UNDP’s report on people and possibilities in the AI age.',
'The 2025 report placed India at 130 of 193 with an HDI value of 0.685.|The HDI figures refer to 2023, not development outcomes measured in May 2025.|India remained in the medium human-development category in this release.',
'HDI combines health, education and income dimensions; inequality-adjusted HDI and MPI are distinct measures.',
'Aggregate improvement can coexist with uneven access and disparities across groups.|AP planning needs disaggregated health and education evidence rather than treating a national rank as a state performance score.',
'Do not compare ranks from different data vintages without checking revisions or confuse expected schooling with completed mean schooling.',
'Why should development policy go beyond growth and aggregate HDI rank?',True,sources=['MY-HDI'],slug='human-development-report-2025-widening-inequality')
add('Society & Welfare','04 · Demographic data & mortality',0,'SRS report: label reference years and denominators','The issue reviewed the release of demographic estimates.',
'SRS is administered through the Registrar General of India framework.|It estimates birth, death and other demographic indicators from sample-based continuous recording and survey checks.|The 2021 statistical report and the 2019–21 maternal-mortality estimate have different reference periods.',
'Crude birth/death rates use 1,000 population; IMR uses 1,000 live births and MMR uses 100,000 live births.',
'Trends help plan health services when methods, years and uncertainty are comparable.|The same national improvement can coexist with local care gaps needing AP district-level investigation.',
'The magazine’s crude-birth-rate formula showing ×100 is incorrect; use ×1,000. Publication in 2025 does not make the estimates 2025 observations.',
'Why are correct denominators essential to demographic policy analysis?',True,slug='sample-registration-system-srs-report-2021')
add('Society & Welfare','02 · Functional literacy & inclusion',0,'Mizoram’s literacy declaration: threshold is not 100%','The issue covered the declaration under the contemporary functional-literacy framework.',
'The declaration used the policy threshold associated with over 95% literacy.|ULLAS links adult learning with foundational and functional skills.|Historical Kerala and Ladakh declarations used different dates, administrative units and contexts.',
'A literacy threshold, a sampled literacy rate and universal demonstrated functional proficiency are different claims.',
'Post-declaration support matters for people still excluded and for retention of learning.|Digital and financial skills should be assessed with accessible tasks rather than inferred from a state-level headline.',
'Do not write that every resident is literate or erase Kerala’s earlier literacy movement by treating a contemporary designation as all-history first.',
'How should functional-literacy success be assessed beyond threshold declarations?',slug='mizoram-achieves-full-functional-literacy')
add('Science & Technology','04 · Personalised medicine & genome editing',0,'Personalised CPS1 therapy: somatic editing, not a universal cure','The issue discussed an infant treated with a customised gene-editing approach.',
'CPS1 deficiency impairs ammonia handling in the urea-cycle pathway.|The reported approach targeted the child’s specific genetic variant in liver cells.|Somatic editing differs from editing reproductive cells or embryos with heritable implications.',
'Targeted base editing and conventional double-strand-break editing are related but technically distinct approaches.',
'Precision therapy raises questions of off-target effects, delivery, follow-up, cost and fair access.|An encouraging individual case is important evidence but not proof of population-wide efficacy or long-term safety.',
'Do not describe a single treated patient as regulatory approval of a universal cure or as heritable germline editing.',
'How can personalised genome therapies balance innovation, safety and equitable access?',slug='gene-editing')
add('Science & Technology','05 · Synthetic media & digital harm',0,'Deepfakes: consent, evidence and proportionate remedies','The issue discussed harmful synthetic media and US legislation.',
'Deepfakes can manipulate or synthesise apparently authentic audio, images or video.|Non-consensual intimate imagery and deceptive impersonation are major harm categories.|India’s existing legal provisions may apply even without a single statute named a Deepfake Act.',
'Technical provenance and forensic detection support verification but do not determine lawful consent or harm on their own.',
'Timely remedies, victim support and evidence preservation should accompany enforcement.|Broad restrictions must distinguish harmful deception from labelled satire, accessibility tools and legitimate expression.',
'Do not repeat unverified universal prevalence percentages or assume every AI-generated image is criminal.',
'How can digital governance address synthetic-media harms without suppressing legitimate expression?',slug='deepfakes')
add('Society & Welfare','06 · End-of-life ethics & autonomy',0,'Dignity at the end of life: consent and safeguarding differ','The issue contrasted terminal illness, assisted dying and religious fasting debates.',
'Indian jurisprudence recognises dignity in end-of-life decisions within safeguards.|Withholding/withdrawing life-sustaining treatment is distinct from administering a lethal substance.|Adult informed choice and a young child’s capacity for consent require fundamentally different assessment.',
'Autonomy, beneficence, non-maleficence and protection of vulnerable people must be considered together.',
'Palliative care and support can reduce suffering without treating financial or familial pressure as free choice.|Advance directives and medical decision procedures require careful application of current binding safeguards.',
'Do not equate the right to dignity with an unrestricted right to active euthanasia, or a foreign bill’s passage with operative Indian law.',
'How should end-of-life policy protect autonomy without exposing vulnerable people to coercion?',slug='right-to-die-with-dignity')
add('International Relations','06 · UN mandates & peace operations',0,'UN peacekeeping: mandate, consent and impartiality','The issue covered India’s pledges at the 2025 ministerial.',
'The Security Council establishes mandates through resolutions.|The General Assembly has important financing/resource approval roles.|Core principles include consent, impartiality and limits on force subject to the mandate.',
'Impartiality does not mean doing nothing in the face of mandate violations; peacekeeping is distinct from unrestricted war fighting.',
'Credible missions require suitable mandates, equipment, protection and political processes.|Pledging a unit is not the same as deployment, and deployments do not substitute for a viable peace process.',
'Do not freeze a magazine’s mission count as a permanent fact or assume every mission has identical authority to use force.',
'What makes UN peacekeeping mandates operationally credible and politically sustainable?',slug='united-nations-peacekeeping')
add('Environment','07 · Urban floods & catchment planning',0,'Urban flooding: drainage depends on the whole catchment','The issue discussed Bengaluru’s pre-monsoon flooding.',
'Impervious surfaces can increase runoff and reduce infiltration.|Blocked drains, lost wetlands and construction in flow paths can amplify risk.|Extreme rainfall interacts with exposure and institutional preparedness.',
'Pluvial flooding, river flooding and coastal storm surge are distinct mechanisms that can overlap.',
'AP cities need drainage maintenance, floodplain protection and locally suitable blue-green infrastructure.|Design must address upstream/downstream effects and vulnerable settlements rather than merely shift water to another neighbourhood.',
'Do not use one fixed multiplier for all urban flood peaks or claim climate change explains every drainage failure.',
'How can urban flood management shift from reactive pumping to catchment-based risk reduction?',True,slug='urban-floods')
# Retain unrelated seeds, but remove the earlier thin May seeds now covered by this batch.
old=[n for n in N if n['date'].startswith('2025-05') and not n['id'].startswith('MY25-')]
# Keep seeds to avoid silently breaking links or overstating that all topics replace one another.
N=[n for n in N if not n['id'].startswith('MY25-')]+J
for name,obj in [('notes.json',N),('sources.json',S),('source-access.json',A)]: (R/'data'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2))
(R/'research/magazine-review/vision-inventory.json').write_text(json.dumps(D,ensure_ascii=False,indent=2))
print('Added',len(J),'May notes; retained',len(old),'existing May seeds; total',len(N))
# Upgrade and explicitly cross-link the inherited chronology seed, preserving its ID/bookmarks.
seed=next((n for n in N if n['id']=='CA-027'),None)
if seed:
 seed.update(why='The Indian Armed Forces announced Operation Sindoor on 7 May, following the 22 April Pahalgam attack.',static_link='Operational chronology, strategic doctrine and diplomatic outcomes are separate analytical layers. See MY25-030 for a companion treatment of evidence and escalation.',analysis=['Chronology should identify the dated phase rather than extend an initial statement to all later exchanges.','Assess deterrence and civilian protection without assuming unverified casualty or equipment-loss claims are established.'],evidence_access='Inherited retrospective reference supplemented by the initial official release excerpt inspected in this edition')
 seed['facts']=['The initial Ministry of Defence statement was issued on 7 May 2025.','It reported action against nine terrorist-infrastructure sites in Pakistan and Pakistan-occupied Jammu and Kashmir.','It described the initial action as focused and non-escalatory and said no Pakistani military facilities were targeted in that phase.']
 seed['sources']=list(dict.fromkeys(seed['sources']+['MY-SINDOOR']));seed['related_notes']=['MY25-030','MY25-031'];seed['status']='Historical initial-phase account; later phases require separately dated evidence'
 (R/'data/notes.json').write_text(json.dumps(N,ensure_ascii=False,indent=2))
