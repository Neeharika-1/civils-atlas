"""Original study supplements based on selected public Vision IAS passages.
Coverage month != article posting/event date. Not wholesale republication or full-magazine certification.
"""
import json,pathlib,calendar
R=pathlib.Path(__file__).resolve().parents[1];N=json.loads((R/'data/notes.json').read_text());S=json.loads((R/'data/sources.json').read_text());A=json.loads((R/'data/source-access.json').read_text());D=json.loads((R/'research/magazine-review/vision-inventory.json').read_text());J=[];used={};counts={}
def article(m,slug):return next(a for a in D[m]['articles'] if a['url'].split('#')[0].endswith('/'+slug))
def cite(m,slug):
 a=article(m,slug);i=D[m]['articles'].index(a);k=f'V{m[2:4]}{m[5:]}-{i+1:02}'
 S[k]=['Vision IAS · '+m+' edition · '+a['title'].removeprefix('Next Article '),a['url']]
 A[k]=dict(title=S[k][0],url=a['url'],access='Official public web article: lead and selected substantive passages inspected; linked primary texts not necessarily reviewed',checked_on='2026-11-06',method='Assistant-led comparison; magazine assertions critically assessed, not independently certified')
 a['review']='Selected passages incorporated into original study note';used[(m,slug)]=k;return k

def add(m,slug,subject,block,title,why,facts,static,analysis,trap,mains,ap=False,priority='P1',extra=''):
 counts[m]=counts.get(m,0)+1;keys=[cite(m,x) for x in [slug]+([extra] if extra else [])]
 J.append(dict(id=f'VM{m[2:4]}{m[5:]}-{counts[m]:03}',date=m+'-'+str(calendar.monthrange(int(m[:4]),int(m[5:]))[1]),date_precision='month',subject=subject,block=block,title=title,why=why+' This is a '+m+' magazine-coverage supplement, not an assertion that every background development occurred that month.',facts=facts.split('|'),static_link=static,analysis=analysis.split('|'),trap=trap,mains=mains,ap=ap,priority=priority,sources=keys,status='Historical magazine-theme supplement; event chronology and current status separately checked where available',checked='2026-11-06',evidence_access='Selected official Vision IAS public article passages inspected; original synthesis/analysis, primary-source reconciliation still open',magazine_edition=m,magazine_posted=D[m]['web_posting_date'],content_type='magazine-supplement'))
# January: gaps not already adequately represented in the research volume.
m='2025-01'
add(m,'cooperatives','Economy','12 · Cooperatives & institutional governance','International Year of Cooperatives: governance before scale','The edition examined the 2025 international observance and cooperative institutions.',
'The 2025 theme is Cooperatives Build a Better World.|Cooperatives organise member ownership and mutual economic benefit rather than shareholder return alone.|Indian cooperative governance includes state and multi-state legal frameworks.',
'Article 19(1)(c), Article 43B and the constitutional litigation over Part IXB must be read together; do not assume every Part IXB provision applies unchanged to state societies.',
'Member participation, professional management and independent audits determine whether scale serves members.|AP dairy, credit and producer organisations need transparent elections and conflict controls, not simply more registrations.',
'The international-year designation does not mean the observance was first launched in January; the global launch predates 2025. Do not reproduce unverified cooperative-share statistics.',
'How can cooperative autonomy coexist with professional accountability?',True)
add(m,'10-years-of-niti-aayog','Polity & Governance','02 · Development institutions','NITI Aayog at ten: advisory federalism','NITI Aayog completed ten years from its 1 January 2015 establishment.',
'It was established by a Union Cabinet resolution, replacing the Planning Commission.|It is neither a constitutional body nor a statutory commission.|The Prime Minister chairs it; its role includes policy advice, monitoring and cooperative/competitive federalism.',
'An advisory institution differs from the Finance Commission, whose constitutional mandate concerns fiscal recommendations.',
'Comparative indicators can facilitate learning if methods and limitations are transparent.|AP should assess the diagnostic usefulness of rankings rather than treating advisory scoring as an automatic funding entitlement.',
'NITI Aayog does not have the same constitutional status or transfer-allocation role as the Finance Commission.',
'Discuss the value and limits of policy think tanks in cooperative federalism.',True)
add(m,'internet-shutdown','Polity & Governance','04 · Digital rights & proportionality','Internet shutdowns: legality is not necessity','The edition reviewed shutdown trends and the updated telecommunications framework.',
'The Temporary Suspension of Services Rules, 2024 operate under the Telecommunications Act, 2023.|Shutdowns affect communications, commerce, education and access to public services.|Different trackers can use different definitions of an incident and duration.',
'Constitutional review examines authority, legitimate purpose, necessity, proportionality and procedural safeguards; access restrictions and speech restrictions overlap.',
'Reasoned orders, periodic review and narrow geographic/time scope can reduce unnecessary harms.|Localised alternatives should be assessed before denying essential services to a whole population.',
'Do not treat a tracker’s count as a universally reconciled official total or assume statutory authority removes proportionality review.',
'What safeguards should constrain temporary communications restrictions?')
add(m,'rupee-depreciation','Economy','06 · Exchange rates & external payments','Rupee depreciation and internationalisation are different questions','The issue examined exchange-rate pressures alongside RBI measures supporting rupee settlement.',
'Depreciation means a currency loses value relative to another; a higher INR/USD quote means more rupees per dollar.|Rupee internationalisation concerns its use for cross-border pricing, settlement and financial claims.|Permitted rupee-account and settlement arrangements operate within FEMA rules and bank compliance.',
'A Vostro account is the foreign bank’s account from the domestic bank’s perspective; the corresponding Nostro is viewed from the account-owning bank’s perspective.',
'Currency weakness can raise imported-input costs even where some exporters gain on conversion.|Settlement in rupees can reduce some conversion exposure but requires willing counterparties, liquidity and usable balances.',
'International settlement facilities do not establish full capital-account convertibility or eliminate exchange-rate risk.',
'Can wider rupee settlement strengthen resilience without replacing macroeconomic stability?',True,extra='internationalisation-of-rupees')
add(m,'household-consumption-expenditure-survey-hces-2023-24','Economy','06 · Consumption data & inequality','HCES 2023–24: consumption is not income','The January issue interpreted results from the household consumption survey.',
'The survey reference period was August 2023–July 2024.|Reported MPCE excluding imputation was ₹4,122 rural and ₹6,996 urban.|Figures including imputed benefits differ and must not be mixed with the excluding-imputation series.',
'MPCE measures consumption expenditure per person per month. A consumption Gini is not automatically an income or wealth Gini.',
'Changing food/non-food shares inform welfare and price-index discussions, but nominal growth is not identical to improved real purchasing power.|National averages can obscure inter-state and social-group differences relevant to AP policy.',
'The publication/issue month is not the survey period. The magazine’s wording linking a consumption Gini directly to income inequality needs qualification.',
'How should household consumption data be used without overstating what it measures?',True)
add(m,'indias-digital-economy','Economy','10 · Digital economy measurement','Measuring the digital economy beyond the IT sector','The issue discussed MeitY’s commissioned measurement study.',
'The study was undertaken by ICRIER.|It draws on OECD/ADB measurement approaches.|The coverage includes digitally enabled portions of traditional industries, not just hardware and software firms.',
'A sector’s digitally enabled value added, platform turnover and the entire sector’s GDP contribution are different aggregates.',
'Comparable measurement can inform infrastructure, skills and inclusion policy.|Assess digital adoption alongside productivity, cybersecurity, access and distribution of gains rather than assuming all digitisation creates equal welfare.',
'Do not add overlapping ICT and digitally enabled sector estimates or confuse a forecast with measured current output.',
'Why does digital-economy measurement require careful boundaries?',True)
add(m,'annual-ground-water-quality-report-2024','Environment','02 · Groundwater & public health','Groundwater quality: quantity security is insufficient','The magazine examined CGWB’s 2024 assessment.',
'The Central Ground Water Board conducts groundwater assessment and monitoring.|Chemical contamination can involve nitrate, fluoride, arsenic or salinity with different local causes.|Extraction/recharge classification and chemical water quality answer different questions.',
'Aquifer storage, recharge, extraction stage and drinking-water safety must be assessed separately.',
'A state-level safe extraction category does not establish that every village has safe drinking water.|AP requires local sampling, contamination-source control and treatment matched to the pollutant, alongside aquifer management.',
'Do not equate sustainable extraction with potable water or assume a statewide average describes each assessment unit.',
'How can groundwater policy integrate quantity management with public-health protection?',True)
add(m,'iron-age-in-india','Culture & History','01 · Archaeology & scientific evidence','Tamil Nadu iron chronology: evaluate the dating context','The issue discussed Antiquity of Iron and new radiometric-date claims.',
'The report concerns archaeological sites in Tamil Nadu, including Sivagalai and Mayiladumparai.|Methods discussed include radiocarbon dating and optically stimulated luminescence.|Claims of very early iron technology depend on the association between dated samples, stratigraphy and metallurgical evidence.',
'Radiocarbon ordinarily dates associated organic material, not the age of an iron object directly; sediment dating addresses another evidentiary question.',
'New dates can revise chronologies when context and independent analyses are robust.|Distinguish a reported claim from a universally established world-first conclusion and make uncertainty intelligible to readers.',
'Do not present every proposed date as direct dating of iron or collapse publication, sample context and technological onset into one date.',
'Why must archaeological chronologies be assessed through context as well as laboratory dates?',priority='P2')
add(m,'oxfam-report-on-widening-global-economic-inequalities','Society & Welfare','06 · Wealth, power & inequality','Oxfam’s Takers Not Makers: interpreting inequality claims','The issue examined the advocacy organisation’s wealth-inequality report.',
'The report is titled Takers Not Makers: The Unjust Poverty and Unearned Wealth of Colonial Inheritance.|It discusses wealth concentration, inheritance, monopoly power and colonial legacies.|It is an Oxfam analysis, not an Indian official household income survey.',
'Wealth is a stock, income is a flow and consumption is another distributional measure. PPP poverty lines require a stated base and reference year.',
'Analyse methods and assumptions before using striking global wealth claims as universal facts.|Public finance, competition policy and broad access to capabilities address different mechanisms of inequality.',
'Do not treat advocacy estimates as court findings about every billionaire or use an undated PPP poverty threshold as permanently current.',
'How should policymakers distinguish different mechanisms underlying economic inequality?',priority='P2')
add(m,'shift-in-india-afghanistan-relations','International Relations','01 · Neighbourhood diplomacy','India–Afghanistan engagement: contact is not recognition','The issue reviewed the Dubai meeting involving India’s Foreign Secretary and Afghanistan’s acting foreign minister.',
'The meeting represented high-level engagement with Afghanistan’s de facto authorities.|Humanitarian assistance, regional security and connectivity are distinct policy dimensions.|Diplomatic contact does not by itself constitute formal recognition of a government.',
'Recognition, consular presence, technical engagement and humanitarian cooperation have different legal and political meanings.',
'Engagement can protect interests while preserving concern for security, inclusive governance and human rights.|Assess proposed connectivity against implementation capacity and regional constraints, not only strategic narratives.',
'Do not infer formal recognition or treaty obligations from a meeting alone.',
'How can pragmatic engagement with de facto authorities preserve humanitarian and security priorities?')
# February.
m='2025-02'
add(m,'freebies','Polity & Governance','03 · Welfare, elections & fiscal accountability','Welfare versus freebies: evaluate design, not labels','The issue revisited judicial observations on electoral promises and welfare.',
'Articles 38, 39 and 41 express welfare-oriented constitutional principles.|Budget support can finance public services, insurance, transfers or consumption subsidies with different effects.|An observation in a hearing is not necessarily a final binding finding about all welfare programmes.',
'Public goods, merit goods, social protection and poorly targeted subsidies should not be reduced to a single undefined category.',
'Assess incidence, fiscal sustainability, administrative cost and demonstrable capability gains.|AP welfare debates need expenditure and outcome evidence rather than assuming all transfers either eliminate poverty or discourage work.',
'Do not convert a judge’s observation into a universal causal finding that recipients stop working.',
'What criteria distinguish sustainable social protection from fiscally irresponsible electoral promises?',True)
add(m,'satus-of-devolution-to-panchayats-in-states','Polity & Governance','05 · Local self-government','Devolution Index: institutions need functions, finance and staff','The issue examined the Panchayati Raj Ministry/IIPA assessment.',
'The report evaluates state/UT devolution through six dimensions.|Karnataka, Kerala and Tamil Nadu are the reported leading states.|A constitutional institution may exist without equivalent operational control over funds and functionaries.',
'Article 243G and the Eleventh Schedule relate to panchayat responsibilities; actual devolution requires state legal and administrative action.',
'Compare practical planning powers and predictable finance rather than elections alone.|AP local bodies need capacity, staffing, transparency and accountable discretion, not merely centrally or state-designed projects delivered through them.',
'An index ranking is method- and period-dependent, not proof that every panchayat in a leading state is effective.',
'Why does democratic decentralisation require more than regular local elections?',True)
add(m,'major-and-minor-minerals','Economy','11 · Mineral regulation & critical resources','Barytes, felspar, mica and quartz reclassified','The issue reported a move from minor to major-mineral treatment.',
'The minerals named were barytes, felspar, mica and quartz.|The rationale includes their association with critical minerals and industrial uses.|Regulatory classification is different from geological abundance or market value.',
'Mineral status under the MMDR framework affects regulatory treatment; minor does not simply mean unimportant or low-priced.',
'AP’s barytes resources make reporting, associated-mineral recovery and compliance particularly relevant.|Policy should connect extraction with processing, environmental management and credible resource information.',
'Do not assume all existing leases instantly vanished or that every associated mineral has a commercially recoverable reserve.',
'How should mineral regulation support critical-resource recovery without weakening environmental oversight?',True)
add(m,'geo-economic-fragmentation','International Relations','04 · Trade, technology & strategic risk','Geo-economic fragmentation: diversification versus decoupling','The issue used the Economic Survey to examine strategically driven economic barriers.',
'Fragmentation can affect trade, investment, payments and technology diffusion.|Friendshoring favours politically aligned partners; nearshoring prioritises geographic proximity.|Selective supply-chain relocation is not proof that all global integration has ended.',
'Concentration risk, resilience, efficiency and comparative advantage are related but distinct policy considerations.',
'Diversification can reduce a single-point dependency while raising costs or creating new common exposures.|AP export sectors need market and input-risk mapping rather than assuming every relocation opportunity will become a local investment.',
'Do not equate a policy-driven trend with the complete replacement of globalisation.',
'How can economic resilience be improved without indiscriminate self-isolation?',True)
add(m,'triangular-partnership','International Relations','05 · Development cooperation','Triangular cooperation: roles matter more than the number three','The issue reviewed OECD/Islamic Development Bank discussion of development partnerships.',
'Triangular cooperation combines complementary resources and expertise among development partners.|A facilitating partner can support cooperation between a pivotal partner and a beneficiary partner.|Its purpose is development co-creation, not necessarily military or diplomatic alignment.',
'Triangular cooperation is distinct from any generic three-country agreement or a strategic triangle.',
'Partner-led priorities, shared learning and local institutional capacity can improve delivery.|Evaluate accountability and transaction costs so additional partners do not simply multiply coordination burdens.',
'Do not call every three-party MoU triangular development cooperation or treat historical project proposals as completed projects.',
'When can triangular development cooperation outperform a conventional donor-recipient model?',priority='P2')
add(m,'three-language-formula','Society & Welfare','02 · Education, language & federalism','Three-language formula: policy flexibility and implementation','The issue addressed state objections and NEP 2020’s approach.',
'NEP 2020 provides flexibility in language choice within a three-language approach.|At least two of the three languages are to be native to India.|Mother-tongue/home-language teaching recommendations and the three-language formula are related but separate policy elements.',
'Education is in the Concurrent List; language learning, teaching medium and official-language status are not interchangeable.',
'Multilingual opportunity requires trained teachers, suitable materials and realistic progression.|AP implementation should respect learner mobility, local languages and access without assuming a single imposed language follows from the policy.',
'An education policy is not a standalone law mandating Hindi in every state or fixing one medium for every institution.',
'How can multilingual education balance federal choice with equitable learning opportunities?',True)
add(m,'swachh-bharat-mission-grameen-sbm-g','Society & Welfare','03 · Sanitation & public services','SBM-Grameen: sustaining ODF and managing waste','The issue discussed parliamentary scrutiny of rural sanitation.',
'SBM-G is a centrally sponsored rural-sanitation programme.|ODF sustainability extends beyond constructing individual household toilets.|ODF Plus involves solid/liquid waste management and improved cleanliness alongside sustaining open-defecation-free status.',
'An infrastructure count, regular use, safe waste handling and health outcomes are different indicators.',
'Water availability, repairs, inclusion and local maintenance determine whether gains endure.|Village-level systems need predictable resources and behaviour-sensitive evaluation, not only declaration or award metrics.',
'Do not assume a declared ODF village has solved every sanitation or waste-management problem.',
'Why must rural-sanitation policy move from asset creation to sustained service delivery?',True)
add(m,'deep-ocean-mission','Science & Technology','05 · Ocean technology & safety','Matsya 6000: testing is not a completed deep dive','The issue reported wet testing of the indigenous submersible programme.',
'Matsya 6000 is being developed under Samudrayaan within the Deep Ocean Mission.|The design objective is a three-person vehicle capable of reaching 6,000 metres.|NIOT, Chennai, under the Ministry of Earth Sciences is the development institution.',
'Pressure qualification, wet tests, crew safety and a demonstrated operational deep dive are distinct validation stages.',
'Ocean technology can support biodiversity research and resource assessment while requiring rigorous environmental safeguards.|Qualification must test life support, communications, recovery and emergency contingencies, not only nominal depth design.',
'A wet test does not prove that people already reached 6,000 metres in the vehicle.',
'How should deep-sea exploration combine technological ambition with human and ecological safety?',True)
add(m,'non-communicable-diseases-ncd','Society & Welfare','04 · Preventive health & continuity of care','Intensified NCD screening: diagnosis must lead to care','The issue covered the Health Ministry’s special screening drive.',
'The drive targeted people aged 30 years and above.|It included prevalent NCDs and oral, breast and cervical cancer screening.|Ayushman Arogya Mandirs and other facilities form part of delivery under NP-NCD.',
'Screening identifies risk or possible disease; confirmatory diagnosis, referral, treatment and follow-up remain necessary.',
'Coverage can improve early detection only when diagnostics and affordable continuing care are available.|AP should track referral completion, medicine availability and control of disease, not simply people screened.',
'A screening target is not achieved universal coverage, and a positive screen is not automatically a confirmed diagnosis.',
'What makes a mass screening programme translate into better health outcomes?',True)
add(m,'soil-health-card-scheme','Agriculture','05 · Soil testing & nutrient management','Soil Health Cards at ten: test quality and farmer use','The issue reviewed a programme launched in 2015.',
'The scheme supports soil testing and nutrient-management recommendations.|It has been integrated into the Soil Health and Fertility component of the RKVY framework.|A card must link a representative sample to useful, crop-appropriate advice.',
'Soil fertility includes chemical, biological and physical properties; a nutrient recommendation is not a guarantee of higher yield.',
'Laboratory quality, correct sampling and extension determine whether advice changes practice.|AP nutrient policy should connect testing with balanced input prices, soil organic matter and local crop conditions.',
'Do not treat a card issued as proof that recommendations were followed or that every soil constraint was measured.',
'Why does soil-testing policy need extension and input-market reform alongside laboratories?',True,priority='P2')
add(m,'pradhan-mantri-annadata-aay-sanrakshan-abhiyan-pm-aasha-1','Agriculture','05 · Price assurance & procurement','PM-AASHA: price support is not universal automatic procurement','The issue examined continuation and the integrated price-assurance framework.',
'PM-AASHA covers mechanisms supporting prices for notified pulses, oilseeds and copra.|Price Support Scheme procurement involves eligible registered farmers and prescribed quality conditions.|Procurement operations depend on applicable conditions and state/nodal-agency arrangements.',
'MSP announcement, physical procurement and price-deficiency support are different mechanisms.',
'Price assurance works better with predictable purchase access, payment and storage.|AP diversification needs attention to tenants, small lots, quality testing and market access rather than assuming an MSP declaration ensures sale at that price.',
'Do not apply one crop/year’s procurement ceiling or waiver indiscriminately to every commodity and season.',
'How can price-assurance programmes support diversification without creating exclusion or unsustainable stocks?',True)
add(m,'hybrid-warfare','Security','03 · Information, cyber & critical infrastructure','Hybrid threats: resilience across institutional boundaries','The issue highlighted convergence between conventional and non-kinetic threats.',
'Hybrid strategies can combine military, cyber, economic and information instruments.|Critical infrastructure can be targeted without a formally declared war.|Domestic and cross-border responsibilities can overlap during such incidents.',
'Hybrid warfare and asymmetric warfare overlap but are not exact synonyms; every protest, cyber incident or critical opinion is not warfare.',
'Preparedness needs continuity planning, trusted communication, cyber hygiene and clear civil-military roles.|Protecting security must preserve evidentiary standards and civil liberties rather than attributing all social disagreement to foreign actors.',
'A broad security label does not establish attribution or justify unrestricted surveillance.',
'How can societies build resilience to hybrid threats without securitising legitimate democratic activity?')
m='2025-03'
add(m,'judicial-accountability','Polity & Governance','01 · Judicial ethics & accountability','Judicial accountability: inquiry is not a finding of guilt','The issue examined institutional responses to allegations concerning a High Court judge.',
'Constitutional removal and an in-house inquiry are separate mechanisms.|The Judges Inquiry Act, 1968 supplies part of the parliamentary removal framework.|Asset disclosure, conflict management and reasoned complaint procedures serve different accountability purposes.',
'Judicial independence protects adjudication; it does not imply immunity from every form of accountability. Allegations require due process.',
'Transparent institutional responses can protect both public trust and fair treatment of the individual.|Reform should provide credible scrutiny without giving litigants or governments coercive control over decisions.',
'Do not equate discovery allegations with adjudicated corruption. The magazine’s suggestion that a 1999 mechanism was based on 2002 principles is chronologically unsound.',
'How can judicial accountability be strengthened without compromising independent adjudication?')
add(m,'regulating-big-tech','Economy','08 · Competition & digital markets','Digital competition: ex ante duties versus ex post cases','The issue discussed proposals for a digital competition framework.',
'Ex ante regulation imposes specified obligations before or irrespective of proving a particular violation.|Ex post competition enforcement examines conduct and liability through cases.|Network effects, data advantages and switching barriers can affect market contestability.',
'Dominance is not automatically unlawful; abuse of dominance and restrictions on competition require a legal test.',
'Targeted obligations may address fast-moving market tipping, but broad duties can impose compliance costs on useful innovation.|Clear designation criteria, proportionality and appeal rights should accompany enforcement.',
'A draft Digital Competition Bill or consultation is not an enacted universal ban on large technology firms.',
'When is ex ante regulation justified in digital markets?',priority='P2')
add(m,'bilateral-investment-treaty-bit','International Relations','04 · Investment protection & regulatory space','Revisiting the Model BIT: protection with policy space','The issue discussed the Budget’s intention to make the model investment text more investor-friendly.',
'India’s 2015 Model BIT replaced the earlier 1993 model.|BITs define covered investment and investor protections within negotiated terms.|Investor-state and state-state dispute mechanisms are distinct.',
'A model negotiating text is not a single treaty automatically binding all investment partners; each concluded agreement matters.',
'Predictable protections can reduce arbitrary treatment while preserving legitimate public-interest regulation.|Assess dispute safeguards, legal costs and regulatory autonomy alongside capital-attraction claims.',
'Do not treat an announced model revision as a signed new treaty or assume every regulatory loss is compensable expropriation.',
'How can investment treaties balance credible protection with sovereign regulatory responsibility?')
add(m,'indian-ocean-rim-association-iora-1','International Relations','02 · Indian Ocean institutions','IORA: regional cooperation beyond naval security','The issue discussed India’s forthcoming 2025–27 chairmanship.',
'IORA is an intergovernmental association established in 1997.|Its secretariat is in Mauritius.|Its agenda links sustainable development and cooperation across the Indian Ocean region.',
'IORA, BIMSTEC and the Indian Ocean Naval Symposium are distinct institutions with different membership and mandates.',
'Cooperation in disaster management, fisheries and maritime capacity can supply useful regional public goods.|AP’s ports and coastal institutions can connect to wider capacity building, but chairmanship is not proof that proposed projects are delivered.',
'The March discussion of a forthcoming chairmanship is not evidence that India took over the chair in March.',
'How can Indian Ocean regional institutions demonstrate practical value beyond summit declarations?',True,priority='P2')
add(m,'liquidity-deficit','Economy','07 · Monetary operations & banking liquidity','Liquidity infusion: OMO purchases and forex swaps','The issue reviewed RBI operations during tight banking-system liquidity.',
'An RBI purchase of government securities through OMO normally adds rupee liquidity.|In an RBI USD/INR buy-sell swap, banks initially sell dollars for rupees and reverse the exchange later.|Tax payments into government balances can drain banking-system liquidity until expenditure returns funds.',
'Liquidity conditions, the policy rate, bank solvency and credit demand are different dimensions of monetary transmission.',
'Operations can alleviate temporary funding friction without resolving weak borrower demand or credit quality.|Assess tenor and the causes of the shortage before interpreting each injection as a permanent change in policy stance.',
'Do not confuse buying foreign currency initially with selling dollars to absorb rupees, or call every liquidity operation a repo-rate cut.',
'Why must monetary analysis distinguish price signals from liquidity operations?')
add(m,'50-years-of-microfinance','Society & Welfare','05 · Credit inclusion & household risk','Microfinance: access, affordability and over-indebtedness','The issue revisited the history of microfinance and SEWA Bank.',
'SEWA Bank was established in Gujarat in 1974.|Microfinance targets financial access for low-income households and small enterprises.|A provider’s legal form determines whether it may accept deposits; not every MFI is a deposit-taking bank.',
'Microcredit, SHG-bank linkage, insurance and savings are related but different financial services.',
'Access can help households manage livelihood needs when product design matches repayment capacity.|Multiple borrowing, coercive recovery and poorly timed instalments can transform formal access into financial stress.',
'Fifty years from 1974 falls in 2024; this March issue’s retrospective theme must not be presented as a new March 2025 foundation event.',
'How can microfinance inclusion be measured beyond loan disbursement totals?',True)
add(m,'remittances-to-india','Economy','06 · Migration & external transfers','RBI remittance survey: changing origins and state shares','The issue discussed findings for FY2023–24.',
'The reported inward-remittance total was USD 118.7 billion.|The US accounted for 27.7% in the survey; the UAE remained an important source.|The report identified Maharashtra as the leading recipient state, followed by Kerala and Tamil Nadu.',
'Remittances are transfers, not merchandise exports or FDI. Survey reference periods and country/state shares must be labelled.',
'Diversified migration can alter remittance resilience to particular labour-market or oil-price shocks.|AP analysis needs actual state data and migrant profiles rather than assuming all overseas income comes from the Gulf.',
'Do not infer that every advanced economy exceeds every Gulf country, or apply 2023–24 survey shares as current 2026 shares.',
'What does a change in remittance origins imply for migration and financial-inclusion policy?',True)
add(m,'unified-pension-scheme-1','Economy','09 · Pensions & social security','UPS operational regulations: an option within NPS','The issue discussed regulations for operationalising the Unified Pension Scheme.',
'UPS is an option for specified central-government employees covered by NPS.|Its implementation framework involves PFRDA regulations.|The operational date discussed was 1 April 2025, subject to applicable eligibility and option procedures.',
'Assured payout, qualifying service, contributions and withdrawal conditions must be examined together; a scheme label is not enough.',
'Employees need clear comparable information on risks, conditions and long-term benefits.|Fiscal evaluation should account for contribution design and contingent obligations rather than treating assured benefits as costless.',
'UPS means Unified, not Universal Pension Scheme. It does not automatically cover every state employee or all citizens.',
'How should pension reform balance retirement security with transparent fiscal risk?')
add(m,'farmer-producer-organizations','Agriculture','07 · Producer institutions & market access','10,000 FPO milestone: formation versus viability','The issue reviewed the formation programme and its institutional support.',
'The central-sector formation scheme was launched in 2020.|Cluster-Based Business Organisations provide aggregation and professional handholding.|Small, marginal and women farmers are among the priority groups.',
'Registration, paid-up membership, active trade and sustainable producer income are different stages of institutional development.',
'Aggregation works when input services, finance, governance and buyers address genuine member needs.|AP FPOs should be assessed through member participation, margins and timely payments, not the number of registrations alone.',
'The magazine issue month need not equal the date of the 10,000th formation milestone. A registered FPO is not automatically commercially viable.',
'What institutional conditions make producer aggregation economically useful?',True)
add(m,'national-board-for-wildlife-nbwl','Environment','04 · Wildlife institutions & decision-making','NBWL: full-board and standing-committee roles','The issue discussed the full-board meeting chaired by the Prime Minister at Gir.',
'NBWL is a statutory body under the Wildlife Protection Act framework.|The Prime Minister chairs the board.|A full-board meeting and decisions of its Standing Committee are not identical institutional events.',
'Wildlife governance must distinguish policy advice, project-specific appraisal, legal approval and implementation monitoring.',
'Landscape impacts and cumulative pressures require evidence beyond individual project boundaries.|Transparent conditions and follow-up matter as much as a meeting’s announcements.',
'A long gap between full-board meetings does not prove that every wildlife statutory process stopped during that interval.',
'How can wildlife institutions ensure decisions remain ecologically informed and accountable?',priority='P2')
add(m,'river-dolphins','Environment','04 · River biodiversity & survey evidence','River-dolphin estimation: survey baseline and uncertainty','The issue covered India’s first comprehensive river-dolphin estimation.',
'The reported estimate was 6,327 river dolphins.|It comprised 6,324 Gangetic and three Indus river dolphins in the survey.|The report is Population Status of River Dolphins in India–2024, associated with WII/Project Dolphin.',
'An abundance estimate depends on survey coverage and detection methods; comparing unlike historical estimates does not establish a precise trend.',
'Flow, habitat connectivity, pollution and accidental capture are central conservation concerns.|Dolphin protection can reinforce whole-river management, but cannot be reduced to a single population headline.',
'These are river dolphins, not all marine cetaceans in India. Do not infer a precise population decline by mixing non-comparable past estimates.',
'Why must biodiversity counts be interpreted together with survey methods and habitat condition?')
add(m,'marine-heatwaves','Environment','01 · Ocean climate & fisheries','Marine heatwaves: use the percentile definition','The issue highlighted studies of unusually warm ocean conditions.',
'Marine heatwaves are persistent anomalously warm ocean conditions relative to a local seasonal baseline.|The widely used definition exceeds the seasonally varying 90th percentile for at least five consecutive days.|They can affect corals, fisheries and aquaculture through heat stress and ecosystem changes.',
'A relative climatological threshold differs from one fixed global sea temperature or a universal anomaly of 3–4°C.',
'Coastal livelihoods require monitoring, early warning and locally suitable response planning.|AP aquaculture and marine fisheries face different exposure pathways; a global anomaly cannot substitute for local risk evidence.',
'The magazine’s simple 3–4°C wording is not the general scientific threshold; an independent research-group definition is used here.',
'How should ocean-warming risk inform coastal livelihood planning?',True)
add(m,'light-supersolid','Science & Technology','03 · Quantum materials & experimental claims','Light-related supersolidity in polariton systems','The issue discussed an experimental claim involving light–matter quasiparticles.',
'Supersolidity combines spatial ordering with superfluid-like coherence/properties.|The experiment concerns polariton systems, not ordinary room light turning into a rigid object.|Polaritons arise from coupled light and matter excitations.',
'A quasiparticle describes collective behaviour in a material/system; it is not automatically a free elementary particle.',
'Precise identification of the engineered system prevents a striking headline from becoming an incorrect general law.|Experimental evidence and reproducibility should be separated from speculative future applications.',
'Do not write that photons generally become an everyday frictionless solid or that a laboratory result proves commercial readiness.',
'Why is accurate terminology essential when communicating quantum-material discoveries?',priority='P2')
m='2025-04'
add(m,'states-demand-for-autonomy','Polity & Governance','01 · Federalism & reform proposals','Tamil Nadu’s autonomy committee: proposal versus constitutional change','The issue discussed the committee headed by former judge Kurian Joseph.',
'The committee’s remit concerns Centre–state constitutional, legal and policy relations.|It was asked to review earlier federalism recommendations and state administrative concerns.|A state-appointed committee cannot itself amend the Constitution or redistribute legislative lists.',
'The Union, State and Concurrent Lists allocate legislative competence subject to constitutional provisions and judicial interpretation.',
'Informed review can identify genuine administrative and fiscal coordination problems.|Evaluate proposed remedies against accountability, national coordination and the experience of other states, including AP.',
'A committee’s terms of reference are not adopted reforms or a binding judicial ruling.',
'How should federal reform proposals balance state autonomy with shared national responsibilities?',True)
add(m,'chinas-rare-earth-elements-export-control','International Relations','04 · Critical supply chains & export controls','China’s rare-earth controls: licensing is not a blanket ban','The issue examined restrictions affecting seven rare-earth elements and related products.',
'The reported April measures require export licences for covered products.|Rare earths comprise 17 elements, not all critical minerals.|Economic vulnerability can arise from processing and magnet-manufacturing concentration as well as mining.',
'Resource occurrence, proven reserves, separation technology and usable industrial inputs are different steps in a supply chain.',
'Diversified processing, recycling and material-efficient design may reduce exposure over time.|Strategic stockpiling helps only where specifications, shelf life and downstream capability are understood.',
'Do not call a licensing requirement a total prohibition on every rare-earth shipment or assume domestic ore instantly solves processing dependence.',
'How can supply-chain policy address vulnerabilities beyond owning mineral reserves?')
add(m,'india-saudi-arabia-relations','International Relations','03 · Gulf diplomacy & energy','India–Saudi relations: energy, investment and cooperation','The issue reviewed the Prime Minister’s visit and partnership discussions.',
'The Strategic Partnership Council dates to 2019.|The visit outcomes included broader cooperation in defence, tourism/culture and other sectors.|Investment ambitions and proposed refinery cooperation require subsequent implementation evidence.',
'Energy trade, strategic partnership mechanisms and realised direct investment are different measures of bilateral relations.',
'Diversification can link traditional hydrocarbon trade with technology, skills and future energy systems.|Diaspora welfare and credible commercial delivery should accompany strategic declarations.',
'Do not report a targeted investment amount or proposed refinery as completed investment or operating capacity.',
'How should India deepen Gulf partnerships beyond oil trade and remittances?')
add(m,'innovation-ecosystem-for-deep-tech','Science & Technology','06 · Innovation & research commercialisation','Deep-tech innovation: patient capital and scientific capability','The issue discussed calls for stronger science-based startup development.',
'Deep-tech ventures rely on substantive scientific or engineering advances.|They often face longer development, testing and certification cycles than routine digital services.|University laboratories, skilled teams and early customers are important ecosystem components.',
'Technology readiness, product-market fit and investment valuation answer different questions.',
'Patient finance and access to test facilities can address risks conventional short-horizon funding struggles to bear.|AP innovation hubs should reward validated capability and useful adoption, not simply registrations or unicorn targets.',
'Do not assume every AI-labelled company is deep tech or that a prototype is a certified market-ready product.',
'What institutional support helps scientific discovery become a viable public or commercial solution?',True)
add(m,'indias-defence-exports-1','Security','04 · Defence industrial capability','Defence exports FY2024–25: value and capability differ','The issue covered the reported annual export record.',
'The reported FY2024–25 export value was ₹23,622 crore.|Private firms contributed ₹15,233 crore and DPSUs ₹8,389 crore in that account.|The stated 2029 goal is ₹50,000 crore, not the achieved current value.',
'Export value, export authorisations, signed contracts and delivered systems must be distinguished.',
'Long-term competitiveness requires quality, certification, maintenance support and dependable supply.|Assess indigenous value addition and critical import dependencies alongside rising sales.',
'A listed platform in a national portfolio is not proof that each type has already been exported commercially.',
'How can defence exports build durable industrial capability rather than only headline revenue?')
add(m,'biological-weapons-convention-bwc','Security','03 · Biological security & dual use','BWC at fifty: norms, verification and cooperation','The April issue revisited the convention’s 1975 entry into force.',
'The convention opened for signature in 1972 and entered into force in 1975.|It prohibits biological and toxin weapons within its obligations.|India is a party; peaceful biological research remains distinct from prohibited weapon development.',
'Dual-use research can support medicine or create security risks; intent, capability, oversight and safeguards require careful evaluation.',
'Biological security requires laboratory practice, reporting, health preparedness and international trust.|Weak verification and rapidly changing biotechnology make cooperation and credible domestic oversight important.',
'The 50-year anniversary falls in March 2025, not a new April entry-into-force event. Do not confuse BWC with the chemical-weapons treaty.',
'What makes biological-arms control particularly challenging in an era of accessible biotechnology?')
add(m,'bio-input-resource-centres-brcs','Agriculture','05 · Natural farming & input quality','Bio-Input Resource Centres: access requires quality assurance','The issue examined guidelines under the National Mission on Natural Farming.',
'BRCs are envisaged as local enterprises supplying biological farming inputs.|Guidelines discussed ₹1 lakh assistance for setting up a centre with specified cost exclusions.|Potential operators include eligible farmers, FPOs, SHGs and other institutions.',
'Biological inputs vary in composition, viability, storage and agronomic suitability; natural is not a guarantee of efficacy or safety.',
'Local access can lower some logistical barriers where quality and farmer demand are established.|AP implementation should support testing, clear instructions, demonstration and monitoring rather than assume a uniform replacement for all conventional inputs.',
'Setup assistance is not proof of a running enterprise or a universal yield guarantee.',
'How should bio-input programmes combine local enterprise with scientific quality control?',True)
add(m,'functional-de-extinction','Science & Technology','04 · Biotechnology, ecology & ethics','Dire-wolf claims: engineered traits are not species resurrection','The issue discussed a company’s claims about gene-edited grey-wolf pups.',
'The company described animals with selected traits intended to resemble the extinct dire wolf.|Editing traits in a living species does not recreate the full extinct genome or historical population.|Functional resemblance and restoration of an ecological role are separate, testable claims.',
'Species identity, genotype, phenotype and ecosystem function should not be used interchangeably.',
'Assess evidence, animal welfare, habitat suitability and opportunity costs compared with conserving threatened living species.|Corporate publicity requires independent scientific scrutiny before entering study notes as an established breakthrough.',
'Do not state unqualifiedly that an extinct species has been brought back or released into its former ecological niche.',
'What ethical and ecological tests should govern claims of de-extinction?',priority='P2')
add(m,'workplace-automation','Society & Welfare','05 · Work, skills & algorithmic management','Workplace automation: tasks are not whole occupations','The issue reviewed AI adoption and worker implications.',
'Automation can substitute for particular tasks while complementing others.|Algorithmic management can affect allocation, performance monitoring and work intensity.|Job effects depend on adoption, demand, institutions and worker adaptation, not technological capability alone.',
'Labour productivity, employment, wages and job quality may move differently after automation.',
'Training must connect to actual transitions and accessible new opportunities.|Data rights, contestable assessments and safety protections should accompany efficiency gains; automated systems can also reproduce bias.',
'Do not treat an exposure estimate as a count of jobs already lost or claim automation inherently eliminates discrimination.',
'How can automation policy distribute productivity gains while protecting worker agency?',True)
add(m,'green-hydrogen-certification-scheme-of-india','Environment','01 · Hydrogen, standards & carbon accounting','Green Hydrogen Certification Scheme: measure the production boundary','The issue covered the April certification initiative under the National Green Hydrogen Mission.',
'The framework concerns measuring, reporting, verifying and certifying hydrogen-production emissions.|The benchmark is no more than 2 kg CO₂-equivalent per kg of hydrogen within the specified accounting boundary.|Eligible pathways and evidence of energy/input use matter, not merely the label of the plant.',
'Well-to-gate emissions, downstream transport/use and a product certificate are different accounting concepts.',
'Credible certification can support buyers’ trust if independent verification and traceability work.|AP hydrogen investment evaluation should include power sourcing, water, utilisation and offtake rather than assume every hydrogen project is low-carbon.',
'A green-hydrogen certificate is not automatically a tradeable carbon credit or evidence of zero lifecycle emissions.',
'Why do clear boundaries and verification matter more than colour labels in hydrogen policy?',True)
add(m,'vaikom-satyagraha-2','Culture & History','02 · Social reform & anti-caste movements','Vaikom centenary: public-road access and anti-caste reform','The issue revisited the movement and its 1925 withdrawal centenary.',
'The movement challenged caste-based restrictions on public roads around the Vaikom temple in Travancore.|It used nonviolent protest and repeated attempts to access restricted roads.|The withdrawal in November 1925 and later temple-entry reforms are distinct milestones.',
'Road-access rights, access to a temple’s interior and broader abolition of untouchability have different legal/social histories.',
'Historical study should recognise the participation of marginalised groups alongside prominent leaders.|A successful concession can be important without being misdescribed as the complete end of caste discrimination.',
'The April issue’s centenary theme is not evidence that the November withdrawal occurred in April, or that all temple-entry restrictions ended immediately.',
'How did anti-caste movements connect everyday access with wider claims to citizenship and dignity?',priority='P2')
# Independent checks for specific magazine simplifications.
S['V-MHW-DEF']=['Marine Heatwaves International Working Group · Scientific definition','https://www.marineheatwaves.org/mhw-overview.html']
A['V-MHW-DEF']=dict(title=S['V-MHW-DEF'][0],url=S['V-MHW-DEF'][1],access='Independent research-group definition inspected through search excerpt',checked_on='2026-11-06')
S['V-MIN-PIB']=['PIB · Mineral reclassification, 21 February; 20 February notification','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2105215&reg=48&lang=2']
A['V-MIN-PIB']=dict(title=S['V-MIN-PIB'][0],url=S['V-MIN-PIB'][1],access='Primary release excerpt inspected; full-document review pending',checked_on='2026-11-06')
for n in J:
 if n['title'].startswith('Marine heatwaves'):n['sources'].append('V-MHW-DEF')
 if n['title'].startswith('Barytes'):n['sources'].append('V-MIN-PIB')
# Re-runnable construction batch; preserve all other notes.
N=[n for n in N if not n['id'].startswith('VM25')]+J
for name,obj in [('notes.json',N),('sources.json',S),('source-access.json',A)]: (R/'data'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2))
(R/'research/magazine-review/vision-inventory.json').write_text(json.dumps(D,ensure_ascii=False,indent=2))
print('Magazine gap supplements:',counts,'total',len(J),'archive',len(N))
