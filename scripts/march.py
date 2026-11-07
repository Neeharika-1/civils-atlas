"""March 2025 research batch. Historical snapshots; no daily completeness claim."""
import pathlib,json
R=pathlib.Path(__file__).resolve().parents[1];N=json.loads((R/'data/notes.json').read_text());S=json.loads((R/'data/sources.json').read_text());A=json.loads((R/'data/source-access.json').read_text());J=[]
def source(k,t,u,full=False):
 S[k]=[t,u];A[k]=dict(title=t,url=u,access='Substantive article/web synthesis read; linked documents not necessarily independently reviewed' if full else 'Search-result source extract inspected; full document review pending',checked_on='2026-11-06',method='Assistant-led web research; no independent human editorial certification')
source('M-PRS','PRS · March 2025 monthly review; all six chunks read','https://prsindia.org/policy/monthly-policy-review/march-2025',True)
source('M-UPI','PIB · Cabinet UPI incentive decision, 19 March; substantive release read','https://pib.gov.in/PressReleasePage.aspx?PRID=2112771',True)
source('M-STARTUP','The New Indian Express · AP startup policy, 26 March; full article body read','https://www.newindianexpress.com/states/andhra-pradesh/2025/Mar/26/andhra-pradesh-government-unveils-startup-policy-2024-29',True)
source('M-TOUR','The New Indian Express · AP tourism land orders, 11 March/report 12 March; article body read','https://www.newindianexpress.com/states/andhra-pradesh/2025/Mar/12/andhra-pradesh-tourism-land-policy-announced',True)
source('M-APCAB','The New Indian Express · AP Cabinet meeting of 7 March, reported 8 March','https://www.newindianexpress.com/states/andhra-pradesh/2025/Mar/08/cabinet-nod-to-tourism-land-policy-digital-health-centre-in-andhra-pradeshs-kuppam')
source('M-P4','PTI / The Week · P4 launch, 30 March; use article dateline, not erroneous search-page age','https://www.theweek.in/wire-updates/national/2025/03/30/mds16-ap-poverty-cm.html')
source('M-P4PRE','The New Indian Express · P4 design before launch, 25 March','https://www.newindianexpress.com/states/andhra-pradesh/2025/Mar/25/andhra-government-to-launch-zero-poverty-p4-programme-on-ugadi')
source('M-SIPB','The New Indian Express · SIPB decisions of 13 March, reported 14 March','https://www.newindianexpress.com/states/andhra-pradesh/2025/Mar/14/sipb-clears-rs-121-lakh-crore-investment-proposals-in-andhra-pradesh')
source('M-SPADEX','ISRO · SpaDeX undocking, 13 March','https://www.isro.gov.in/spadex_undocking_successful.html')
source('M-BLUE','NASA · Blue Ghost landing on 2 March; article 4 March','https://www.nasa.gov/image-article/blue-ghost-lands-on-moon/')
source('M-SPHEREX','NASA/JPL · SPHEREx and PUNCH launch, 11 March US local time','https://www.jpl.nasa.gov/news/nasa-launches-missions-to-study-sun-universes-beginning/')
source('M-CREW','NASA · Crew-9 return, 18 March; retrospective article 19 March','https://www.nasa.gov/image-article/welcome-home-crew-9/')
source('M-WMO','WMO · State of Global Climate 2024, released 19 March 2025','https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2024')
source('M-AIR','PTI / The Week · IQAir 2024 report released 11 March 2025','https://www.theweek.in/wire-updates/national/2025/03/11/del1-air-pollution-report.html')
source('M-WATER','UNESCO · 2025 World Water Development Report overview','https://www.unesco.org/reports/wwdr/en/2025')
source('M-WATERDATE','UNESCO · Report launch, 21 March 2025','https://www.unesco.org/en/articles/launch-2025-united-nations-world-water-development-report')
source('M-MADHAV','PW OnlyIAS · Madhav tiger-reserve declaration, 9 March; report 10 March','https://pwonlyias.com/current-affairs/madhav-national-park/')
source('M-MUDUMAL','UNESCO WHC · Mudumal tentative-list entry; submission 11 February, March news context','https://whc.unesco.org/en/tentativelists/6802/')
source('M-MUDUMALNEWS','The Indian Express · March report on tentative-list additions','https://indianexpress.com/article/india/telangana-mudumal-megalithic-menhirs-tentative-unesco-heritage-list-india-9887184/')
source('M-HAPPY','The Federal · World Happiness Report 2025, 20 March','https://thefederal.com/category/news/finland-still-happiest-country-in-world-check-indias-rank-in-2025-report-177444')
source('M-TB','WHO · World TB Day statement, 24 March 2025','https://www.who.int/southeastasia/news/detail/24-03-2025-world-tb-day-yes!-we-can-end-tb-commit-invest-deliver')
source('M-MAHA','MEA · MAHASAGAR announcement, 12 March','https://mea.gov.in/newsdetail1?13355=')
source('M-MAHANEWS','The Hindu · India–Mauritius visit and MAHASAGAR, 12 March','https://www.thehindu.com/news/national/mauritius-visit-pm-modi-announces-indias-mahasagar-vision-for-global-south/article69321315.ece')
source('M-NZ','PM India · India–New Zealand joint statement, 17 March','https://www.pmindia.gov.in/en/news_updates/india-new-zealand-joint-statement/?comment=disable')
source('M-BRAHMA','PIB · Operation Brahma naval response, 30 March','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2116801&reg=48&lang=2')
source('M-BRAHMA2','PIB · Army medical response to Myanmar earthquake, 29 March','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2116635&reg=48&lang=2')
source('M-VARUNA','PIB · Varuna culmination account, 24 March','https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2114535')
source('M-CHAMPS','ICC · India wins Champions Trophy final, 9 March','https://www.icc-cricket.com/tournaments/champions-trophy-2025/news/live-india-and-new-zealand-on-crossroads-in-the-champions-trophy-final')
source('M-ABEL','Abel Prize · 2025 laureate; full substantive page read','https://abelprize.no/abel-prize-laureates/2025',True)
source('M-ABELDATE','ICMAT · Abel announcement, 26 March','https://www.icmat.es/news/26-03-25-en/')
source('M-OSCARS','Associated Press · 97th Academy Awards live results, 2 March US time','https://apnews.com/live/oscars-2025-updates')
def add(subject,block,day,title,why,facts,static,analysis,trap,mains,src='M-PRS',priority='P1',ap=False,precision='day'):
 keys=src.split(',');J.append(dict(id=f'MAR25-{len(J)+1:03}',subject=subject,block=block,date=f'2025-03-{day:02}',date_precision=precision,title=title,why=why,facts=facts.split('|'),static_link=static,analysis=analysis.split('|'),trap=trap,mains=mains,sources=keys,priority=priority,ap=ap,status='March historical snapshot; later law and implementation require separate review',checked='2026-11-06',evidence_access='Full substantive synthesis/article read; independent primary-document checks may remain open' if any(k in ['M-PRS','M-UPI','M-STARTUP','M-TOUR'] for k in keys) else 'Source extract(s) inspected; full-document review pending'))
add('Economy','06 · External sector & balance of payments',28,'Q3 current account deficit: 1.1% of GDP','RBI released October–December 2024 balance-of-payments data in March.',
'The current account deficit was USD 11.5 billion, or 1.1% of GDP, in Q3 FY2024–25.|The preceding quarter recorded a USD 16.7 billion deficit, or 1.8% of GDP.|Net services receipts of USD 51.2 billion partly offset a USD 79.2 billion merchandise trade deficit.|The release reported net capital-account outflow of USD 26.8 billion, unlike the USD 17.3 billion inflow a year earlier.',
'The current account records goods, services and income/transfers; it is not the government fiscal account. Financing composition matters alongside the deficit.',
'Services and remittances can cushion the goods deficit, but do not remove sensitivity to energy prices and global demand.|Volatile portfolio flows can pressure reserves even when the current-account gap appears manageable.',
'This is Q3 FY2024–25 data released in March, not March-only trade or the final full-year CAD.',
'Why must current-account sustainability be assessed together with the composition of capital flows?')
add('Economy','07 · Digital payments & financial inclusion',19,'Low-value UPI incentive: payment ecosystem, not universal cashback','Cabinet approved a ₹1,500 crore incentive scheme for FY2024–25.',
'Only small-merchant UPI person-to-merchant transactions up to ₹2,000 qualify for the 0.15% incentive.|Government pays acquiring banks; the incentive is then shared among payment-system stakeholders.|Of admitted claims, 80% is disbursed without the performance conditions; the remaining 20% depends on technical-decline and uptime criteria.|Zero MDR does not mean that building and operating payment infrastructure has no cost.',
'MDR is the merchant-facing acceptance charge; a government incentive is a distinct financing mechanism. P2P transfers differ from P2M transactions.',
'Public subsidy can extend acceptance among price-sensitive merchants while preserving zero-MDR policy.|Linking part of reimbursement to reliability shifts attention from transaction counts to service quality and consumer trust.',
'Do not describe this as 0.15% cashback to every merchant or every UPI user. The approved scheme period is FY2024–25.',
'Evaluate the use of performance-linked subsidies to support a reliable low-cost digital payments ecosystem.','M-UPI',ap=True)
add('Economy','08 · Financial markets & regulation',24,'SEBI board decisions: FPI disclosures and conflicts of interest','The March board meeting approved changes to market regulation and internal-governance review.',
'The board approved raising the aggregate equity-AUM disclosure threshold for specified FPIs from ₹25,000 crore to ₹50,000 crore.|The separate trigger based on over 50% of Indian equity assets in one corporate group should not be confused with this aggregate threshold.|Investment advisers and research analysts were allowed to charge agreed advance fees for up to one year.|A high-level committee was constituted to review conflicts of interest, property disclosures and investments concerning SEBI members and officials.',
'Beneficial-ownership disclosure helps identify concentration and control behind investment vehicles; regulator integrity is an institutional-governance question.',
'Threshold recalibration should reduce disproportionate compliance without making concentrated ownership opaque.|Conflict rules require declarations, recusal, oversight and transparent handling, not only a committee announcement.',
'A board approval is not proof that every consequential circular took effect on the meeting date.',
'How can securities regulators balance proportional compliance with transparent beneficial ownership?')
add('Economy','08 · Banking & directed credit',24,'Revised priority-sector lending directions','RBI revised the targets and classification framework, superseding the September 2020 directions.',
'The urban co-operative bank priority-sector target was fixed at 60% of adjusted net bank credit rather than the previously planned 75% endpoint.|The eligible renewable-energy loan ceiling rose from ₹30 crore to ₹35 crore.|Individual credit limits for artisans, village and cottage industries under weaker sections rose to ₹2 lakh.|Transgenders and joint liability groups were added to the weaker-sections definition.',
'PSL directs a share of bank credit to specified development priorities; classification as PSL is not a grant, loan waiver or guarantee of sanction.',
'Target design must reflect institutional capacity, repayment risk and the possibility of misclassification.|For AP, assess whether farmers, women, artisans and renewable enterprises actually receive affordable credit, not merely whether banks meet reporting targets.',
'Do not apply the 60% urban co-operative bank target to every commercial bank or claim that eligible borrowers automatically obtain a loan.',
'Discuss how priority-sector lending can become more inclusive without weakening credit discipline.',ap=True)
add('Economy','08 · Banking law & depositor protection',1,'Banking Laws amendment passes Parliament','The March monthly review records parliamentary passage of the 2024 Bill.',
'The Bill amends five banking statutes, including the RBI Act and Banking Regulation Act.|It permits up to four nominees for deposits, safe custody and lockers, with different modes for deposits and other assets.|Deposits may have simultaneous or successive nominations; safe-custody articles and lockers use successive nominations.|It changes the cash-reserve fortnight definition to days 1–15 and day 16 to month-end, and extends eligible co-operative-bank director tenure from eight to ten years.',
'Nomination facilitates bank settlement after death; questions of ultimate inheritance and beneficial ownership must be considered separately.',
'Clear nomination can reduce unclaimed balances and family disputes where customers are informed and records updated.|Longer director tenure may improve continuity but increases the importance of board accountability in co-operative banks.',
'This note indexes March parliamentary passage at month precision; re-check assent and provision-wise commencement before citing operative law.',
'Assess the depositor-protection and governance implications of the Banking Laws amendment.',precision='month')
add('Polity & Governance','04 · Citizenship, migration & civil liberties',11,'Immigration and Foreigners Bill: consolidation and obligations','The Bill was introduced in Lok Sabha on 11 March; the review also records Lok Sabha passage during the month.',
'The proposed framework consolidates four laws dealing with entry, registration, foreigners and carriers’ liability.|It provides for a Bureau of Immigration and requires relevant travel documents and visas for foreigners.|Registration obligations and information duties extend to specified educational and medical institutions.|The carrier definition includes passenger and cargo transport by land, water or air.',
'Citizenship, permission to enter, refugee protection and immigration registration are related but legally distinct issues.',
'Unified administration can remove fragmented procedures and improve border management.|Data collection and reporting should be necessary, proportionate and accompanied by clear safeguards, especially in hospitals and universities.',
'Introduction and passage by one House are not equivalent to assent, commencement or the resolution of every refugee-law question.',
'How should immigration regulation balance administrative coordination, security and procedural fairness?')
add('Polity & Governance','05 · Disaster governance',1,'Disaster Management amendment: urban and state capacity','Parliament passed the amendment Bill during March.',
'NDMA and SDMA are assigned preparation of disaster-management plans at their respective levels.|New functions include reviewing emerging risks, technical assistance, minimum-relief guidance and disaster databases.|NDMA is to assess state preparedness and conduct post-disaster preparedness/response audits.|States may establish Urban Disaster Management Authorities and State Disaster Response Forces.',
'The disaster cycle spans prevention, mitigation, preparedness, response and recovery. Legal authority alone is not operational capacity.',
'Urban authorities can address heat, floods and infrastructure risks if coordinated with municipalities and land-use institutions.|AP requires coastal warning systems, shelter access, drills and resilient infrastructure, alongside state-level response capacity.',
'A statutory power to establish a body does not prove that every state has constituted, staffed and funded it.',
'Explain how urban disaster authorities can improve resilience without multiplying administrative silos.',ap=True,precision='month')
add('Economy','09 · Maritime trade & transport law',1,'Bills of Lading Bill: Lok Sabha passage','The Lok Sabha passed the Bill replacing the 1856 framework.',
'A bill of lading is a key document in the carriage of goods by sea.|The Bill retains rights of suit and liabilities for the consignee or an endorsee to whom property in the goods passes.|It retains the rule on conclusive evidence of shipment in the stated statutory context.|It adds a central-government direction-making power for implementing the law.',
'In commercial shipping, distinguish a bill of lading from a charterparty, marine insurance and a customs declaration.',
'Legal modernisation supports predictable cargo claims and documentary trade.|New drafting should be assessed for practical clarity and dispute resolution, not assumed to create new physical port capacity.',
'Lok Sabha passage is not passage by both Houses. This is a month-level March snapshot, not a commencement claim.',
'Why does predictable documentation law matter for export competitiveness?',priority='P2',ap=True,precision='month')
add('Economy','09 · Ports & coastal federalism',28,'Indian Ports Bill introduced','The Bill proposed replacing the Indian Ports Act, 1908.',
'It provides for a Maritime State Development Council to guide data, transparency and intergovernmental coordination.|It gives statutory recognition to listed State Maritime Boards.|States must constitute dispute-resolution committees for specified disputes involving non-major ports; appeals lie to the High Court within 60 days.|Ports are required to prepare waste-reception/handling plans and report pollution threats.',
'Ports combine Union and state responsibilities; maritime development must incorporate navigation safety, competition and coastal environmental protection.',
'AP’s port-led development requires hinterland links and credible concession/dispute institutions as well as construction.|Shared data and pollution duties can improve coordination, but central and state roles need clear boundaries.',
'The March event is introduction, not completion of parliamentary passage or automatic implementation at every port.',
'Discuss the federal and environmental dimensions of modernising Indian port governance.',ap=True)
add('Economy','10 · Industrial regulation & safety',1,'Boilers Bill passes Parliament','The March review records passage of legislation replacing the Boilers Act, 1923.',
'The framework regulates manufacture, installation, use and repair of boilers and components.|The main objective is safe operation of boilers.|PRS describes the Bill as retaining the existing Act’s provisions while seeking greater clarity in their presentation.',
'A boiler heats fluid under pressure; inspection, certification and operator competence protect workers and surrounding communities.',
'Recasting old legislation can improve accessibility, but safety still depends on inspection capacity and maintenance.|Compliance simplification should reduce ambiguity rather than dilute accountability for hazardous equipment.',
'Replacement of a colonial-era Act is not proof of deregulation or the removal of safety inspections.',
'How can industrial regulation be simplified while preserving worker safety?',priority='P2',precision='month')
add('Economy','11 · Energy exploration & regulation',1,'Oilfields amendment: separating petroleum regulation','Parliament passed amendments to the Oilfields (Regulation and Development) Act, 1948.',
'The framework concerns exploration and extraction of petroleum and natural gas.|The expanded mineral-oils definition includes naturally occurring hydrocarbons, coal-bed methane and shale gas/oil.|The definition excludes coal, lignite and helium.',
'An unconventional hydrocarbon resource remains distinct from the host mineral; extraction also involves water, land and environmental governance.',
'Clarity about covered resources can reduce investor uncertainty and improve regulatory design.|Exploration policy must account for climate strategy, methane control and local ecological costs as well as import substitution.',
'Coal-bed methane is included, but that does not bring coal itself into the revised mineral-oils definition.',
'Explain why legal certainty in hydrocarbon exploration must be combined with environmental safeguards.',precision='month')
add('Economy','10 · Manufacturing & value chains',28,'Electronics Component Manufacturing Scheme','Cabinet approved a ₹22,919 crore component-manufacturing scheme.',
'The scheme is intended to attract both domestic and global investment.|It aims to increase domestic value addition in electronics manufacturing.|It provides differentiated incentives for component categories and seeks integration with global value chains.',
'Assembly output, domestic component production and indigenous design capabilities are different stages of manufacturing depth.',
'Component capability can reduce imported-input dependence but needs testing facilities, skilled workers and reliable logistics.|Evaluate incentive cost against incremental local value addition, learning and durable supplier capability rather than gross sales alone.',
'Approved funding and investment ambitions are not investment realised, disbursements or jobs already created.',
'Why should India’s electronics strategy move beyond final assembly?',ap=True)
add('Economy','09 · Railway institutions',1,'Railways amendment consolidates Railway Board law','Parliament passed the Railways (Amendment) Bill, 2024 during March.',
'The amendment seeks to repeal the Indian Railway Board Act, 1905.|Railway Board provisions are incorporated into the Railways Act, 1989.|The stated purpose includes eliminating the need to refer to two separate laws.',
'Indian Railways is a departmental undertaking; statutory consolidation and organisational privatisation are not synonyms.',
'Consolidation can improve legal usability and decision clarity.|Service quality still depends on safety investment, maintenance, staffing and accountable administration, not drafting changes alone.',
'Do not describe this legal consolidation as privatisation of Indian Railways.',
'Distinguish statutory consolidation from substantive reform of railway performance.',priority='P2',precision='month')
add('Economy','10 · MSME classification',21,'Revised MSME thresholds notified for 1 April','The March notification implemented classification changes announced in the Budget.',
'Micro enterprises: investment up to ₹2.5 crore and turnover up to ₹10 crore.|Small enterprises: investment up to ₹25 crore and turnover up to ₹100 crore.|Medium enterprises: investment up to ₹125 crore and turnover up to ₹500 crore.|The revised classification takes effect from 1 April 2025.',
'The classification uses composite investment-and-turnover criteria; these limits are not the amount of subsidy or bank credit.',
'Higher ceilings may let firms expand without abruptly losing category-linked benefits.|Formalisation policy should also address delayed payments, market access and technology adoption; reclassification alone cannot solve these constraints.',
'Both criteria matter. The tourism-project categories in AP’s tourism land policy use a different sectoral classification.',
'Evaluate the benefits and limitations of raising MSME classification thresholds.',ap=True)
add('Agriculture','08 · Biofuels & cooperative industry',6,'Modified ethanol interest-subvention scheme','A notified scheme supports cooperative sugar mills switching to multi-feedstock ethanol plants.',
'Eligible conversion allows inputs such as maize and damaged foodgrains in addition to sugarcane.|Interest support is 6% per annum or 50% of the interest, whichever is lower, for five years.|At least 75% of ethanol from converted plants must be supplied to oil marketing companies for petrol blending.|The notified scheme requires applications within six months.',
'Ethanol blending substitutes part of petrol demand; feedstock choice determines water, food-market and seasonal implications.',
'Multi-feedstock capacity can improve plant utilisation when cane supply fluctuates.|Subsidies should be assessed against food/feed competition, water stress and financially viable cooperative governance.',
'This is not a 6% grant on project cost or an unrestricted subsidy for every private distillery.',
'Assess the resource-security trade-offs in promoting multi-feedstock ethanol.',ap=True)
add('Agriculture','05 · Fertilisers & input policy',28,'Kharif 2025 nutrient-based subsidy','Cabinet approved the seasonal P&K fertiliser subsidy rates.',
'The approved Kharif period is 1 April–30 September 2025.|The decision concerns phosphatic and potassic fertilisers under nutrient-based subsidy.|The estimated subsidy expenditure for the season is ₹37,216 crore.',
'NBS relates support to specified nutrients; it should not be conflated with the separate urea subsidy and price-control arrangements.',
'Predictable subsidy can support seasonal supply and affordability.|Balanced nutrient use also requires soil testing, extension, quality assurance and attention to relative prices rather than subsidy volume alone.',
'The estimated seasonal outlay is not money already spent, and the NBS decision does not cover every fertiliser identically.',
'How can fertiliser support encourage balanced nutrient use instead of merely higher consumption?',ap=True)
add('Agriculture','09 · Livestock productivity',19,'Revised Rashtriya Gokul Mission','Cabinet expanded the indigenous-bovine and productivity programme.',
'An additional ₹1,000 crore raises the 2021–22 to 2025–26 allocation to ₹3,400 crore.|The programme supports conservation of indigenous bovine breeds and genetic improvement.|New components include one-time assistance of 35% of capital cost for rearing centres and 3% interest subvention on farmer loans to purchase high-yielding breeds.',
'Productivity depends on breeding, feed, veterinary support and management. Genetic improvement should preserve adaptation and diversity.',
'Higher-yielding animals need appropriate feed, water and disease management; breeding assistance alone is insufficient.|For AP, small dairy holders require accessible animal-health services and fair milk procurement alongside breed improvement.',
'The ₹3,400 crore total is for the programme period, not an additional March-only allocation.',
'How can livestock productivity rise without neglecting indigenous genetic resources?',ap=True)
add('Agriculture','09 · Dairy value chains',19,'Revised National Programme for Dairy Development','Cabinet approved additional support for dairy infrastructure.',
'An additional ₹1,000 crore was approved for the 2021–22 to 2025–26 implementation period.|The programme seeks better milk procurement and processing capacity.|Quality-control and modernisation of dairy infrastructure are part of its objectives.',
'Dairy value chains link dispersed daily producers to testing, chilling, transport, processing and markets; a cold-chain failure can erase farm-level gains.',
'Infrastructure works best when producer organisations can maintain equipment and receive timely payments.|Quality testing and transparent fat/SNF-based pricing are important complements to expanding processing capacity.',
'The additional ₹1,000 crore is not the entire scheme allocation or proof that new infrastructure is already operational.',
'Explain how dairy infrastructure can raise smallholder income while strengthening food safety.',priority='P2',ap=True)
add('Agriculture','09 · Animal health & One Health',5,'Livestock Health and Disease Control: Pashu Aushadhi','Cabinet revised the animal-health programme and added a medicine-access component.',
'The programme addresses livestock disease prevention and control.|Vaccination, surveillance and upgraded veterinary facilities form part of its approach.|Pashu Aushadhi was added as a new component of the revised scheme.',
'One Health links animal, human and environmental health; access to veterinary medicines must be paired with rational use and antimicrobial stewardship.',
'Disease control protects livestock livelihoods and can reduce zoonotic risks.|Affordable medicines require quality assurance, diagnostic support, cold chains where needed and safeguards against indiscriminate antibiotic use.',
'A medicine-access component is not evidence that all veterinary medicines are free or that diseases have been eradicated.',
'How can better veterinary access be reconciled with antimicrobial stewardship?',ap=True)
add('Polity & Governance','02 · Parliament & public finance',10,'Budget Session resumes: finance and legislative business','The second half of the Budget Session resumed after the February recess.',
'The session had recessed from 14 February to 9 March and reconvened on 10 March.|The March review records passage of the Finance Bill and three Appropriation Bills.|Parliament also passed the Manipur budget while President’s Rule was in force.',
'An Appropriation Bill authorises withdrawal from the Consolidated Fund; the Finance Bill gives effect to taxation proposals. These functions are distinct.',
'Budget scrutiny should connect legal authorisation with allocation priorities and subsequent expenditure outcomes.|President’s Rule changes the legislative route for state finance, making transparent parliamentary scrutiny particularly important.',
'Parliamentary authorisation of expenditure is not actual expenditure or evidence of programme delivery.',
'Distinguish the roles of the Finance Bill and Appropriation Bills in legislative control of public money.',priority='P2')
add('Andhra Pradesh','01 · Welfare, poverty & participation',30,'P4–Margadarsi Bangaru Kutumbam launched','AP launched its Public Private People Partnership initiative at Ugadi.',
'The model seeks voluntary support and mentorship from the affluent for economically weaker families.|Participants providing support are called Margadarsi; beneficiary families are Bangaru Kutumbam.|The launch reporting describes a top-10%/bottom-20% mobilisation model.|Pre-launch clarification said participation was voluntary and distinct from regular welfare schemes.',
'Philanthropy, CSR, government welfare entitlements and public-private infrastructure contracts are different institutional arrangements.',
'Mentorship can address education, skills and livelihood bottlenecks beyond one-time transfers.|Beneficiary selection, privacy, grievance redress and continuity need safeguards so access does not depend on political patronage or donor preference.',
'Launch is not measured poverty elimination. Do not present voluntary donor support as a guaranteed statutory payment to every family.',
'Critically assess the P4 model as a complement—not a substitute—to accountable public welfare.','M-P4,M-P4PRE',ap=True)
add('Andhra Pradesh','02 · Innovation, enterprise & employment',24,'AP Innovation and Startup Policy 4.0, 2024–29','A March government order formalised the policy; the substantive press account was published on 26 March.',
'The policy sets targets of 20,000 startups and one lakh jobs over five years; these are goals, not achieved totals.|Ratan Tata Innovation Hub in Amaravati is envisaged as the central hub, with five regional centres.|The report lists regional centres at Rajahmundry, Vijayawada, Visakhapatnam, Tirupati and Anantapur.|The design includes departmental innovation challenges and proof-of-concept support, with performance-linked institutional funding.',
'An incubator supports early ventures; a unicorn is a valuation category, not necessarily a profitable or job-intensive firm.',
'Problem-led government procurement and university-industry collaboration can improve market access for startups.|Measure survival, follow-on investment, revenue, inclusion and durable employment rather than registrations or valuation targets alone.',
'Hub provision in a policy is not evidence that every regional hub was already operational in March. Re-check the original GO before relying on exact incentive eligibility.',
'Propose an outcome-based monitoring framework for Andhra Pradesh’s startup policy.','M-STARTUP',ap=True)
add('Andhra Pradesh','03 · Tourism & land governance',11,'Tourism Land Allotment Policy: implementation terms','March orders detailed land terms under the 2024–29 tourism framework.',
'The report describes 33-year leases, extendable by another 33 years, for MSME tourism projects.|For large, mega and ultra-mega projects it describes 66-year leases, extendable by 33 years, or project-dependent freehold terms.|Reported construction timelines are 18 months for MSME, two years for large, three for mega and four for ultra-mega projects.|Sectoral project investment bands and land norms differ by tourism-project category.',
'A lease gives time-bound rights under stated conditions; it is not identical to an outright transfer. Public land carries an opportunity cost.',
'Long tenures can support capital-intensive tourism if selection is competitive and milestones are enforceable.|Coastal regulation, local access, carrying capacity and community livelihoods must constrain development, rather than being treated as afterthoughts.',
'These are tourism-policy project categories, not the national MSME enterprise thresholds. The March snapshot does not certify that later policy amendments are identical.',
'How should AP balance tourism investment incentives with accountable public-land management?','M-TOUR',ap=True)
add('Andhra Pradesh','04 · Public health & digital services',7,'Cabinet clears Kuppam Digital Health Centre','The 7 March Cabinet decision was reported the following day.',
'Cabinet approved establishment of a Digital Health Centre at Kuppam.|The reported estimated cost was ₹5.34 crore.|The decision establishes policy approval, not a verified opening date or completed service network.',
'Telehealth can connect peripheral patients with specialists, but clinical assessment, referrals and emergency care still require physical capacity.',
'Digital services can reduce travel costs when diagnostics, trained staff, connectivity and referral transport are available.|Assess patient outcomes, accessibility, consent and data security instead of counting video consultations alone.',
'Do not treat Cabinet approval as inauguration or claim that remote consultation replaces all in-person care.',
'What design safeguards would make a digital health centre genuinely useful to underserved patients?','M-APCAB',priority='P2',ap=True)
add('Andhra Pradesh','05 · State finance & public enterprises',7,'APMDC debenture proposal: scrutinising off-budget exposure','Cabinet approved a proposal for APMDC to raise funds through debentures.',
'The reported proposed borrowing amount was ₹9,000 crore.|The described instruments were secured, rated, listed and redeemable debentures.|Cabinet approval is not confirmation that the entire amount was issued, subscribed or spent.',
'A public enterprise’s liabilities differ legally from direct state debt, but guarantees, asset pledges and fiscal support can transmit risk to the budget.',
'Scrutiny should examine use of proceeds, repayment cash flows, security, guarantees and contingent liabilities.|Ratings and listing improve information but do not eliminate credit risk or the opportunity cost of encumbering public assets.',
'Do not automatically add the proposed amount to realised state debt, or assume every enterprise liability is explicitly state-guaranteed.',
'How should states make public-enterprise borrowing and contingent liabilities more transparent?','M-APCAB',ap=True)
add('Andhra Pradesh','02 · Industrial investment & employment',13,'SIPB investment approvals: pipeline versus realised investment','The State Investment Promotion Board approved proposals; reporting followed on 14 March.',
'The reported approved investment proposals totalled ₹1,21,659 crore from ten companies.|The proposals covered industry, energy and tourism.|The reported employment potential was 80,104 jobs; it was a projection, not verified employment.|The Chief Minister called for monitoring approved projects and their movement to ground operations.',
'Investment stages include proposal, approval, land/clearances, financial closure, construction and commercial operation. Each requires separate evidence.',
'Public dashboards should show stage conversion, delays, fiscal concessions and independently verifiable jobs.|AP’s development case should weigh water, power, land and local-skill requirements alongside headline investment size.',
'SIPB approval is not expenditure, operational capacity or employment already generated. Newspaper totals need reconciliation with official project records.',
'Design a transparent investment-tracking dashboard that avoids confusing approvals with outcomes.','M-SIPB',ap=True)
add('Science & Technology','02 · Lunar exploration & commercial space',2,'Blue Ghost lands at Mare Crisium','Firefly Aerospace’s first lunar lander reached the Moon under NASA’s commercial delivery programme.',
'Blue Ghost Mission 1 landed on 2 March near Mons Latreille in Mare Crisium on the lunar near side.|It delivered ten NASA science and technology instruments.|The delivery was part of Commercial Lunar Payload Services and the Artemis campaign.|The planned surface science period was approximately one lunar day, or about 14 Earth days.',
'A commercial payload-delivery contract is distinct from a government agency owning and operating every spacecraft. The lunar near side differs from the far side and polar regions.',
'Commercial procurement may diversify delivery options and reduce some costs, but reliability must be demonstrated mission by mission.|Surface measurements and technology tests support future exploration without themselves constituting a crewed landing.',
'Blue Ghost did not land at the lunar south pole and was not an Indian mission. NASA’s article date was 4 March, not the landing date.',
'Assess the opportunities and risks of commercial procurement models for lunar exploration.','M-BLUE',priority='P2')
add('Science & Technology','03 · Cosmology & astronomical observation',11,'SPHEREx launches: infrared all-sky spectroscopy','NASA launched the observatory from California with PUNCH as a rideshare mission.',
'SPHEREx stands for Spectro-Photometer for the History of the Universe, Epoch of Reionization and Ices Explorer.|It was launched on a Falcon 9 from Vandenberg on 11 March US local time.|It will survey the sky in 102 wavelength bands.|Scientific aims concern the early universe, galaxy history and water/organic ices in the Milky Way.',
'Spectroscopy separates light by wavelength to infer composition and physical properties; an all-sky survey differs from deep observation of selected targets.',
'Large surveys can reveal statistical patterns that targeted observations cannot establish alone.|Comparing instruments requires attention to wavelength, survey strategy and scientific question, not simply mirror size or launch cost.',
'The US-local launch date is 11 March; it was 12 March in India. SPHEREx is not a solar-wind mission—that role belongs to the accompanying PUNCH.',
'Explain how all-sky spectroscopy complements targeted astronomical observations.','M-SPHEREX',priority='P2')
add('Science & Technology','04 · Heliophysics & space weather',11,'PUNCH: linking the solar corona to the solar wind','The four-satellite mission launched alongside SPHEREx.',
'PUNCH means Polarimeter to Unify the Corona and Heliosphere.|The mission comprises four small satellites.|It studies how the Sun’s outer atmosphere transitions into the solar wind.|It shares a launch with SPHEREx but has a distinct heliophysics objective.',
'The corona is the Sun’s outer atmosphere; the heliosphere is the region influenced by the solar wind. Polarimetry uses light’s polarisation to investigate structures.',
'Understanding solar-wind evolution improves scientific interpretation of space-weather disturbances.|Space-weather awareness matters for satellites, navigation, communications and electrical infrastructure, but research success does not imply perfect storm prediction.',
'Do not interchange SPHEREx’s cosmological objective with PUNCH’s solar objective or infer guaranteed prediction of every geomagnetic storm.',
'Why is heliophysics a practical concern for increasingly space-dependent societies?','M-SPHEREX',priority='P2')
add('Science & Technology','01 · Human spaceflight & mission safety',18,'Crew-9 return brings Williams and Wilmore home','The Dragon spacecraft splashed down off Florida following a long-duration ISS expedition.',
'The returning crew comprised NASA’s Nick Hague, Suni Williams and Butch Wilmore and Roscosmos’ Aleksandr Gorbunov.|The return was aboard SpaceX Dragon on 18 March US local time.|Williams and Wilmore returned with Crew-9 rather than on the Starliner spacecraft on which they had flown to the ISS.|NASA’s post-return account describes extensive scientific and technology-demonstration work during the expedition.',
'ISS crew rotation, test-flight certification and emergency rescue are distinct operational categories; redundancy is a key safety principle.',
'Alternative certified transport and international cooperation can provide resilience when mission plans change.|Long-duration stays also require attention to physiology, rehabilitation, crew workloads and adequate station logistics.',
'A return after an extended mission should not be reduced to an unsupported claim of an uncontrolled emergency rescue. This date follows the US-local mission record.',
'What does flexible crew transport reveal about risk management in human spaceflight?','M-CREW',priority='P2')
add('Environment','01 · Climate evidence & adaptation',19,'WMO State of the Global Climate 2024 report','The March release assembled updated temperature, ocean, cryosphere and impact evidence.',
'The report identifies 2024 as the warmest year in the observational record.|Estimated global annual temperature was 1.55 ± 0.13°C above the 1850–1900 baseline.|Ocean heat and sea-level rise are highlighted as long-lived consequences.|The report emphasises early warnings and climate services for reducing social and economic losses.',
'An annual global temperature anomaly is not the same as the Paris Agreement’s long-term warming level. WMO annual monitoring complements IPCC assessments.',
'For coastal AP, sea-level rise, storm surge and compound flooding make adaptation planning essential even when near-term emissions improve.|Risk-based infrastructure, ecosystem buffers and accessible warnings should be evaluated through avoided losses and vulnerable populations reached.',
'One year above 1.5°C does not by itself establish that the long-term Paris temperature threshold has been permanently breached.',
'Explain why climate adaptation requires long-lived risk planning as well as annual temperature monitoring.','M-WMO',ap=True)
add('Environment','03 · Air pollution & environmental health',11,'IQAir World Air Quality Report 2024','A March release presented annual PM2.5 comparisons based on monitoring data.',
'The report ranked India fifth among covered countries for 2024 annual PM2.5 pollution.|Byrnihat topped the report’s city list and Delhi was identified as the most polluted capital.|The reporting said 13 of the 20 most polluted cities were in India.|The WHO annual PM2.5 guideline cited in the coverage is 5 micrograms per cubic metre.',
'PM2.5 is fine particulate matter; an annual concentration ranking differs from a daily AQI reading. Monitoring coverage affects comparability.',
'Airshed management must coordinate transport, industry, construction, fuel use and regional sources.|AP cities need reliable local monitoring and emissions inventories rather than assuming a national ranking describes every neighbourhood’s exposure.',
'IQAIR is not an official Indian statutory regulator. A 2024 annual ranking released in 2025 is not real-time pollution or a universal disease-risk ranking.',
'Why should air-quality policy use both monitoring and source-specific emissions inventories?','M-AIR',ap=True)
add('Environment','02 · Cryosphere & water security',21,'UN World Water Development Report: mountains and glaciers','UNESCO’s 2025 report focused on the world’s water towers and downstream dependence.',
'The report’s title is Mountains and glaciers: Water towers.|It examines mountain water and the rapidly changing cryosphere, not only glacier ice.|The launch was set for 21 March, the first World Day for Glaciers, alongside World Water Day observances.|UNESCO’s overview highlights water supply, sanitation, ecosystems and water-dependent economic activities.',
'The cryosphere includes glaciers, snow, ice caps and permanently frozen ground. River flow also depends on rainfall, storage and watershed conditions.',
'Retreat can initially alter runoff and hazard patterns and later weaken dry-season buffering; effects vary by basin.|AP’s rivers should not be labelled glacier-fed merely because a global report stresses Himalayan water security. Translate lessons into catchment, storage and demand governance appropriate to the basin.',
'World Water Day is 22 March; World Day for Glaciers is 21 March. Do not call all Indian rivers glacier-fed.',
'How should water-security planning account for upstream ecological change and downstream dependence?','M-WATER,M-WATERDATE',ap=True)
add('Environment','04 · Protected areas & landscape conservation',9,'Madhav becomes India’s 58th tiger reserve: March snapshot','The Union Environment Minister announced tiger-reserve recognition for Madhav.',
'Madhav is in Shivpuri district, Madhya Pradesh.|It was described at the time as India’s 58th tiger reserve and Madhya Pradesh’s ninth.|The reserve is associated with dry deciduous and thorn-forest landscapes and lakes.',
'National park designation and tiger-reserve notification are different legal/conservation concepts. Effective tiger conservation requires prey, habitat and landscape connectivity.',
'An additional designation can focus planning and resources, but outcomes depend on protection and neighbouring land use.|Human-wildlife conflict mitigation and local-community participation must accompany species recovery.',
'The ordinal is a dated March count, not the current November 2026 national total. Primary notification review remains pending.',
'Why is landscape-level management essential even after an area receives tiger-reserve status?','M-MADHAV',priority='P2')
add('Culture & History','03 · Megaliths & heritage governance',15,'Mudumal menhirs: tentative-list news, not World Heritage inscription','March reporting highlighted the Telangana site’s inclusion in India’s UNESCO Tentative List.',
'UNESCO’s entry places Mudumal in Narayanapet district, Telangana, near the Krishna River.|The site contains standing stones or menhirs in a megalithic landscape.|The UNESCO record gives 11 February 2025 as the submission date; this note uses the March reporting date.|The nomination description discusses proposed archaeo-astronomical associations; these should be attributed rather than overstated as universally settled findings.',
'A menhir is an upright standing stone; dolmens, cists and stone circles are different megalithic forms. A tentative list precedes possible nomination and evaluation.',
'Heritage protection must preserve the landscape and archaeological context, not just individual stones.|Interpretation can support community tourism while distinguishing established evidence from proposed astronomical explanations.',
'Mudumal is in Telangana, not Andhra Pradesh or Karnataka. Tentative listing is not UNESCO World Heritage inscription.',
'How should archaeological heritage be interpreted responsibly without turning tentative scientific claims into certainties?','M-MUDUMAL,M-MUDUMALNEWS',priority='P2',precision='reporting-day')
add('Society & Welfare','06 · Wellbeing & development measurement',20,'World Happiness Report 2025','The annual report foregrounded caring, sharing and social connections.',
'Finland ranked first for the eighth consecutive year.|India ranked 118 among 147 countries, compared with 126 among 143 in the previous edition.|The report was produced by Oxford’s Wellbeing Research Centre with Gallup, the UN Sustainable Development Solutions Network and an independent editorial board.|The ranking is based on surveyed life evaluations; explanatory variables are not simply added up to create the ranking.',
'Subjective wellbeing complements income, health and education indicators; survey methods and uncertainty matter when comparing countries.',
'Social support and trust can shape lived wellbeing beyond per-capita income.|A rank improvement should be checked against score changes, sample uncertainty and the changing country set before inferring major policy success.',
'The six explanatory factors are not six mechanical weights that directly generate the country ranking. Rank and score changes are different.',
'Can subjective wellbeing indicators improve public policy without replacing objective deprivation measures?','M-HAPPY',priority='P2')
add('Society & Welfare','04 · Public health & tuberculosis',24,'World TB Day: Commit, Invest, Deliver','WHO warned that funding pressures and missed cases threaten TB-control progress.',
'The 2025 theme was Yes! We Can End TB: Commit, Invest, Deliver.|The observance recalls Robert Koch’s 1882 announcement of the TB bacterium.|WHO highlighted sustained investment, diagnostics, treatment access and social support.|The statement linked resource constraints with the rollout of newer diagnostics and drug-resistant-TB regimens.',
'TB is caused by Mycobacterium tuberculosis; detecting infection, diagnosing active disease and identifying drug resistance require different clinical decisions.',
'Effective programmes connect timely diagnosis with adherence support, nutrition and reduction of catastrophic household costs.|Treatment success should be monitored alongside missed cases and resistance; a target year or campaign slogan is not an elimination certificate.',
'India’s 2025 elimination ambition must not be rewritten as a verified achievement. A symptom screen alone does not confirm TB.',
'Why does ending tuberculosis require social protection as well as better drugs?','M-TB',ap=True)
add('International Relations','02 · Indian Ocean & Global South',12,'MAHASAGAR vision announced in Mauritius','The Prime Minister articulated an expanded cooperation vision during the Mauritius visit.',
'MAHASAGAR stands for Mutual and Holistic Advancement for Security and Growth Across Regions.|The announcement was made in Mauritius on 12 March.|The visit foregrounded maritime security, development cooperation and India’s engagement with the Global South.|India reiterated support for Mauritius’s sovereignty regarding Chagos in the visit reporting.',
'Mauritius is in the south-western Indian Ocean. Maritime diplomacy links EEZ security, capacity building, connectivity and development, but national sovereignty remains central.',
'Trust depends on locally useful capacity and respect for partner priorities rather than only strategic rhetoric.|AP’s maritime institutions and eastern seaboard illustrate domestic capabilities supporting wider Indian Ocean engagement, not a direct MAHASAGAR entitlement.',
'A strategic vision is not a mutual-defence treaty or proof that every proposed project has been funded and delivered.',
'How can India combine maritime security cooperation with a development-oriented Global South agenda?','M-MAHA,M-MAHANEWS',ap=True)
add('International Relations','04 · Trade diplomacy & Indo-Pacific',17,'India–New Zealand: FTA negotiations and Raisina Dialogue','Christopher Luxon’s official visit linked trade talks with broader strategic engagement.',
'The leaders agreed to launch negotiations for a mutually beneficial free trade agreement.|Luxon was chief guest for the tenth Raisina Dialogue in New Delhi.|The joint statement welcomed New Zealand into the Indo-Pacific Oceans Initiative partnership.|Capacity building, maritime cooperation and technology were among the engagement areas.',
'An FTA negotiation, signed agreement, ratification and entry into force are separate stages. Tariff preferences depend on negotiated schedules and origin rules.',
'Complementarity in services and technology must be balanced against politically sensitive agricultural sectors.|Trade gains require standards compliance, logistics and firm-level access as well as tariff negotiation.',
'The March announcement does not mean an FTA entered into force or that India joined an unrelated regional trade bloc.',
'What domestic-policy considerations should shape India’s FTA negotiations with an advanced agricultural economy?','M-NZ')
add('International Relations','03 · Neighbourhood & humanitarian assistance',29,'Operation Brahma: Myanmar earthquake response','India mobilised humanitarian assistance following the 28 March earthquake.',
'Operation Brahma provided disaster assistance to Myanmar.|The Army’s initial medical deployment announcement described a 118-member specialist task force.|INS Satpura and INS Savitri of the Eastern Naval Command sailed for Yangon on 29 March.|The response involved coordination across MEA, the armed forces and NDRF; subsequent deployments require their own dated updates.',
'HADR is humanitarian assistance and disaster relief. Rapid access, coordination, health logistics and host-country consent determine operational effectiveness.',
'Pre-positioned assets and trained joint teams can save time during regional disasters.|The Eastern Naval Command connects AP’s maritime geography to India’s regional relief capacity; assistance should prioritise need and respect civilian coordination.',
'This note records the initial March response, not final casualties or cumulative assistance. Operation Brahma is not a combat operation.',
'Explain how preparedness at home strengthens India’s ability to deliver regional humanitarian assistance.','M-BRAHMA,M-BRAHMA2',ap=True)
add('Security','05 · Maritime exercises & interoperability',19,'VARUNA 2025: India–France naval exercise','The bilateral exercise ran from 19 to 22 March; PIB reported its culmination on 24 March.',
'VARUNA is an India–France naval exercise.|Activities included air defence, anti-submarine warfare, surface operations and replenishment at sea.|French Rafale-M and Indian MiG-29K aircraft participated in the air-defence component.|The drills focused on interoperability and the exchange of operational practices.',
'Replenishment at sea extends endurance; anti-submarine warfare requires sensing, classification and coordinated response. Exercises differ from military alliances.',
'Complex drills build procedural familiarity and logistics coordination beyond diplomatic declarations.|Partnerships strengthen capacity, but operational interoperability does not erase each country’s independent strategic choices.',
'Do not confuse VARUNA with other partners’ exercises or describe its conduct as a binding collective-defence commitment.',
'How do recurring naval exercises translate diplomatic partnerships into operational capability?','M-VARUNA',priority='P2')
add('Awards & Sports','01 · International sport',9,'India wins the 2025 ICC Champions Trophy','India defeated New Zealand in the final in Dubai.',
'India won the final by four wickets.|The final was played in Dubai, United Arab Emirates, on 9 March.|The competition began in February and concluded in March; its title result belongs in March.',
'The Champions Trophy is an ODI tournament, distinct from the ODI World Cup and the T20 World Cup.',
'For factual recall, pair winner, runner-up, format, venue and date rather than memorising every match score.|A sports result can support broader discussion of institutions and participation, but one victory does not establish population-wide sporting development.',
'Do not put the winner in the February snapshot merely because the tournament started that month.',
'Why should sports-development policy track participation and infrastructure as well as elite victories?','M-CHAMPS',priority='P3')
add('Awards & Sports','02 · Scientific & mathematical honours',26,'Masaki Kashiwara: 2025 Abel Prize','The Japanese mathematician was announced as the 2025 laureate.',
'The laureate is associated with Kyoto University, Japan.|The official citation recognises fundamental contributions to algebraic analysis and representation theory.|It specifically cites the theory of D-modules and discovery of crystal graphs.',
'The Abel Prize is a major mathematics award; it is not a Nobel Prize category. Announcement and award ceremony dates differ.',
'Foundational mathematics can transform methods across disciplines long before immediate commercial applications are apparent.|Research evaluation should preserve space for sustained abstract work alongside mission-oriented science.',
'The official laureate year is 2025; one inspected newspaper headline incorrectly labelled it 2024. Prefer the prize authority.',
'Why should science policy support foundational research whose applications are not immediately predictable?','M-ABEL,M-ABELDATE',priority='P3')
add('Awards & Sports','03 · Cinema & cultural recognition',2,'Anora wins Best Picture at the 97th Academy Awards','The ceremony was held on 2 March US local time, corresponding to 3 March in India.',
'Anora won Best Picture.|Sean Baker won Best Director for Anora.|The film received five awards overall; the total for the film differs from an individual winner’s award tally.',
'The Oscars are conferred by the Academy of Motion Picture Arts and Sciences. Ceremony year and the release year of eligible films need not be identical.',
'Independent film recognition can prompt discussion of creative industries, distribution and cultural expression.|Award success is a selective indicator of recognition, not a complete measure of a national film industry’s output or inclusion.',
'Do not confuse the five awards for Anora with the number personally won by Sean Baker, or treat the US date as India’s local date.',
'What enables independent cinema to find audiences beyond major commercial distribution networks?','M-OSCARS',priority='P3')
# Enrich the existing March seed rather than duplicate it.
for n in N:
 if n['id']=='CA-015':
  n.update(date='2025-03-13',date_precision='day',why='ISRO separated the SpaDeX satellites after the January docking demonstration.',facts=['ISRO accomplished SpaDeX undocking on 13 March at about 09:20 IST.','The operation took place in an approximately 460 km circular orbit with 45-degree inclination.','The satellites subsequently orbited independently; ISRO reported normal health.','This followed the first docking on 16 January; later re-docking and power-transfer experiments belong to later chronology.'],static_link='Rendezvous brings spacecraft together, docking connects them and undocking separates them under controlled conditions; each is a distinct mission capability.',analysis=['Safe separation complements docking and is necessary for reusable, multi-module or servicing mission architectures.','A small-satellite technology demonstration supports future missions but does not certify that a crewed station or lunar sample-return programme is operational.'],trap='March 13 was undocking, not the first docking. Do not move the April re-docking and power-transfer experiments into March.',mains='Why are both docking and controlled undocking necessary for complex future space missions?',sources=['M-SPADEX'],evidence_access='ISRO source extract inspected; full-document review pending',status='March historical snapshot; later mission milestones separately dated',checked='2026-11-06')
N=[n for n in N if not n['id'].startswith('MAR25-')]+J
for f,v in [('notes.json',N),('sources.json',S),('source-access.json',A)]: (R/'data'/f).write_text(json.dumps(v,ensure_ascii=False,indent=2))
print('March new',len(J),'March total',sum(n['date'].startswith('2025-03') for n in N),'archive',len(N),'sources',len(S))
