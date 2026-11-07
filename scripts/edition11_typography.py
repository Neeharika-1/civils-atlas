import pathlib,json,re
R=pathlib.Path(__file__).resolve().parents[1]
WORDS={'LokSabha':'Lok Sabha','RajyaSabha':'Rajya Sabha','Article368':'Article 368','Article21':'Article 21','BankRate':'Bank Rate','ExportPromotionMission':'Export Promotion Mission','NewZealand':'New Zealand','CoalControllerOrganisation':'Coal Controller Organisation','FinanceCommission':'Finance Commission','SocialSecurityCode':'Social Security Code','MarchAssembly':'March Assembly','APCRDAAct':'APCRDA Act','CensusAct':'Census Act','CensusRules':'Census Rules','SupremeCourt':'Supreme Court','PaymentsVision':'Payments Vision','ArtemisII':'Artemis II','OneHealth':'One Health','JyotibaPhule':'Jyotiba Phule','SavitribaiPhule':'Savitribai Phule','SatyashodhakSamaj':'Satyashodhak Samaj','JanVishwas':'Jan Vishwas','GramSabha':'Gram Sabha','IndiraAwasYojana':'Indira Awas Yojana','ReidWiseman':'Reid Wiseman','VictorGlover':'Victor Glover','ChristinaKoch':'Christina Koch','JeremyHansen':'Jeremy Hansen','SanDiego':'San Diego','SriSathyaSaidistrict':'Sri Sathya Sai district','Handri-NeevaSujalaSravanthi':'Handri-Neeva Sujala Sravanthi','thePunganurbranchcanal':'the Punganur branch canal','forBudagatlapalem':'for Budagatlapalem','andKothapatnam':'and Kothapatnam','atPuttaparthi':'at Puttaparthi','underDRDO':'under DRDO','TheHindu':'The Hindu','APcensus':'AP census','APheatwave':'AP heatwave','DRDOallotment':'DRDO allotment','APdistrict':'AP district','APuse':'AP use','APcombine':'AP combine','APturn':'AP turn','APmeasure':'AP measure','GWmeasures':'GW measures','TWhor':'TWh or','GWh/TWhor':'GWh/TWh or','CPIinflation':'CPI inflation','APfood':'AP food','PLFSage':'PLFS age','SEIDfor':'SEID for','OTShousing':'OTS housing','OTSarrangement':'OTS arrangement','MPCvoted':'MPC voted','inApril':'in April','inMay':'in May','The15':'The 15','The30':'The 30','coldchain':'cold chain','PRStrack':'PRS track','DTAproducers':'DTA producers','NewZealand100':'New Zealand 100','APCRDA-notified-area':'APCRDA-notified-area','theGazette':'the Gazette','sitevalue':'site value','house-construction':'house-construction','Housingquality':'Housing quality','givingrise':'giving rise','Overloadedvehicles':'Overloaded vehicles','youngworkers':'young workers'}
WORDS.update({'AprilCabinet':'April Cabinet','CentralActs':'Central Acts','aMarch':'a March','areMarchprovisionaldata':'are March provisional data','forMay':'for May','inFY':'in FY','inSri':'in Sri','inThe':'in The','itsApril':'its April','provisionalMarch':'provisional March','thFinance':'th Finance','theMarch':'the March','thesePhase':'these Phase','throughFY':'through FY','toMarch':'to March','APalready':'AP already','APvisits':'AP visits','CPIis':'CPI is','CPIrelease':'CPI release','CSRbudget':'CSR budget','HNSSPhase':'HNSS Phase','IIHandri':'II Handri','IIlanded':'II landed','IIwas':'II was','IIworks':'II works','MMTfoodgrain':'MMT foodgrain','MMTimports':'MMT imports','PLFSheadline':'PLFS headline','STinformation':'ST information','andAPCRDA':'and APCRDA','DTAproducers':'DTA producers','ForAP':'For AP','AprilLok':'April Lok','AprilRajya':'April Rajya','Aprilreported':'April reported','birthanniversary':'birth anniversary','The3':'The 3','The2':'The 2'})
def prose(s):
 for a,b in WORDS.items():s=s.replace(a,b)
 s=re.sub(r'(?<=[A-Za-z%])(?=\d|₹)',' ',s);s=re.sub(r'(?<=\d)(?=[A-Za-z])(?!st\b|nd\b|rd\b|th\b)',' ',s);s=re.sub(r'(?<=[%+])(?=[A-Za-z])',' ',s);s=re.sub(r'(?<=\S)([:;])(?=\S)',r'\1 ',s);s=re.sub(r',(?=[A-Za-z₹])',', ',s);s=re.sub(r'(\d+)\s+(st|nd|rd|th)\b',r'\1\2',s);s=s.replace('thanniversary','th anniversary');s=re.sub(r'(\d+)th e\b',r'\1 the',s);s=re.sub(r'(\d+)st art\b',r'\1 start',s);return s
p=R/'data/notes.json';N=json.loads(p.read_text())
for n in N:
 if n['id'].startswith('E11-') or n['id']=='E10-2603-007':
  for k in ['title','why','static_link','trap','mains','evidence_access']:n[k]=prose(n[k])
  for k in ['facts','analysis']:n[k]=[prose(x) for x in n[k]]
p.write_text(json.dumps(N,ensure_ascii=False,indent=2)+'\n')
p=R/'data/2026-04-mcqs.json';Q=json.loads(p.read_text())
for q in Q:
 for k in ['question','explanation']:q[k]=prose(q[k])
 q['options']=[prose(x) for x in q['options']]
p.write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
p=R/'volumes/April-2026-Mains-Frameworks.md';p.write_text('\n'.join(x if '**Study reference:**' in x else prose(x) for x in p.read_text().splitlines())+'\n')
for name in ['sources.json','source-access.json']:
 p=R/'data'/name;X=json.loads(p.read_text())
 for k,v in X.items():
  if k.startswith('E11-'):
   if isinstance(v,list):v[0]=prose(v[0])
   else:v['title']=prose(v['title']);v['access']=prose(v['access'])
 p.write_text(json.dumps(X,ensure_ascii=False,indent=2)+'\n')
print('Cleaned Edition11 prose; IDs, URLs and structural metadata preserved')

# Restore Markdown strong-delimiter spacing after prose cleanup.
p=R/'volumes/April-2026-Mains-Frameworks.md';p.write_text(re.sub(r'\*\*([^*\n]+?): \*\*',r'**\1:**',p.read_text()))
