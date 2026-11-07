import pathlib,json,re,collections
R=pathlib.Path(__file__).resolve().parents[1]
# Apply only prose; never IDs, file paths, dates, source keys or URLs.
W={'DISHA2.0':'DISHA 2.0','BankRate':'Bank Rate','UnionList':'Union List','StateList':'State List','RightBank':'Right Bank','WorldEnvironmentDay':'World Environment Day','InternationalDayofYoga':'International Day of Yoga','InternationalDayofYogain':'International Day of Yoga in','UNGeneralAssembly':'UN General Assembly','EkPedMaaKeNaam':'Ek Ped Maa Ke Naam','MegaScienceVision':'Mega Science Vision','MadhyaPradesh':'Madhya Pradesh','UttarPradesh':'Uttar Pradesh','IndiaHouse':'India House','FrenchPondicherry':'French Pondicherry','V.V.S.Aiyar':'V. V. S. Aiyar','V.O.ChidambaramPillai':'V. O. Chidambaram Pillai','ChidambaramPillaiorother':'Chidambaram Pillai or other','APPowerFinanceCorporation':'AP Power Finance Corporation','APStateFiberNetLimited':'AP State FiberNet Limited','CentralGovernmentGeneralPoolOfficeAccommodation':'Central Government General Pool Office Accommodation','GeneralPoolResidentialAccommodation':'General Pool Residential Accommodation','TransplantationofHumanOrgansAct':'Transplantation of Human Organs Act','ProtectionofDepositorsofFinancialEstablishments':'Protection of Depositors of Financial Establishments','APReorganisationAct':'AP Reorganisation Act','CoalControllerOrganisation':'Coal Controller Organisation','WorldEnvironment':'World Environment','MadridProtocol':'Madrid Protocol','AntarcticTreaty':'Antarctic Treaty','SummerSolstice':'Summer Solstice','Rayalaseema':'Rayalaseema','NationalDay':'National Day','AgriGoldcases':'Agri Gold cases','AgriGold':'Agri Gold','NationalFood':'National Food','PPI-based':'PPI-based','governments':'governments','Billion':'Billion'}
# Joined everyday words from compact authoring are explicitly corrected rather than guessed.
W.update({'concessionaire':'concessionaire','croreishousing':'crore is housing','croreoffices':'crore offices','crorehousing':'crore housing','croreofnewfibreis':'crore of new fibre is','croreofwages':'crore of wages','crorediffers':'crore differs','crorecash':'crore cash','crorefare':'crore fare','crorethe':'crore the','croreis':'crore is','crorestate':'crore state','crorecentral':'crore central','croreguarantee':'crore guarantee','lakhpermanent':'lakh permanent','lakhpersons':'lakh persons','lakhcompleted':'lakh completed','lakhconstructionman-days':'lakh construction man-days','lakhman-days':'lakh man-days','man-daysper':'man-days per','sevenlakh':'seven lakh','below':'below','kgper':'kg per','kghousehold':'kg household','persondoes':'person does','JanPHEIC':'Jan PHEIC','deathanniversary':'death anniversary','daysfor':'days for','daydistribution':'day distribution','daysunchanged':'days unchanged','yearsand':'years and','monthsof':'months of','acresis':'acres is','acresof':'acres of','countriesthen':'countries then','first-ever':'first-ever','underDBFOT':'under DBFOT','sectoral':'sectoral','publicuse':'public use','newly-signed':'newly signed','special-courtposts':'special-court posts','Beach-shackpilot':'Beach-shack pilot','tourismpermission':'tourism permission','Juneapproval':'June approval','officeapproval':'office approval','officeproject':'office project','statehood':'statehood','on approval':'on approval','termlimits':'term limits','PhH':'PHH','coalmarket':'coal market','the2019':'the 2019','the35':'the 35'})
AC=['DISHA','FCRA','GDP','GVA','CPI','WPI','IIP','PPI','MPC','SDF','MSF','RBI','FII','FIIs','BIS','FEMA','NRI','NRIs','OCI','OCIs','FPI','FDI','DSA','DSAs','NBFC','NBFCs','OTP','OMC','OMCs','ATF','AP','APPSC','APCRDA','NREDCAP','HUDCO','CGGPOA','GPRA','DPR','GO','GOs','THOTA','PM-KUSUM','DBFOT','AIS','NAS','EMT','EMTs','UNEP','WHO','DRC','PHEIC','ATLAS','QGP','IMI','ALS','RF','IT','OT','IoT','NCRB','BNSS','NEP','CBSE','CSR','MoU','MoUs','IP','AI','GPU','GPUcount','MW','MWh','AAY','PHH','UNCCD','UN','RELOS','EU','Seychelles','Slovakia','Slovenia','Telangana','Tungabhadra','Visakhapatnam','Chambal','Chittoor','Amaravati','Polavaram','June','July','May','April','January','November','December','FY','Q4','US','Sanjeevani']
def prose(s):
 for a in sorted(W,key=len,reverse=True):s=s.replace(a,W[a])
 s=re.sub(r'(?<=[A-Za-z%])(?=\d|₹)',' ',s)
 s=re.sub(r'(?<=\d)(?=[A-Za-z])(?!st\b|nd\b|rd\b|th\b)',' ',s)
 s=re.sub(r'(\d)(st|nd|rd|th)(?=[A-Za-z])',r'\1\2 ',s)
 for a in sorted(AC,key=len,reverse=True):
  s=re.sub(r'(?<=[a-z])(?='+re.escape(a)+r'\b)',' ',s)
  s=re.sub(r'\b'+re.escape(a)+r'(?=[a-z])',a+' ',s)
 # Word-end-to-title-case joins; protect established brands.
 for a,b in [('FiberNet','Fiber§Net'),('Nyaya Setu','Nyaya Setu')]:s=s.replace(a,b)
 s=re.sub(r'(?<=[a-z])(?=[A-Z])',' ',s).replace('Fiber§Net','FiberNet')
 s=re.sub(r',(?=\S)',', ',s);s=re.sub(r';(?=\S)','; ',s);s=re.sub(r':(?=\S)',': ',s)
 s=re.sub(r'(?<=[%+])(?=[A-Za-z])',' ',s)
 for a,b in [('Q 4','Q4'),('Q 1','Q1'),('Q 2','Q2'),('Q 3','Q3'),('3 rd','3rd'),('12 th','12th'),('65 years','65 years')]:s=s.replace(a,b)
 s=re.sub(r'\b(crore|lakh|kg|days|years|months|acres|billion)(?=[a-z])',r'\1 ',s)
 return s
N=json.loads((R/'data/notes.json').read_text())
for n in N:
 if n['id'].startswith('E13-'):
  for k in ['title','why','static_link','trap','mains','evidence_access']:n[k]=prose(n[k])
  for k in ['facts','analysis']:n[k]=[prose(s) for s in n[k]]
  if int(n['id'][-3:]) in range(46,59):n['date_precision']='reporting-day'
(R/'data/notes.json').write_text(json.dumps(N,ensure_ascii=False,indent=2)+'\n')
Q=json.loads((R/'data/2026-06-mcqs.json').read_text())
for q in Q:
 for k in ['question','explanation']:q[k]=prose(q[k])
 q['options']=[prose(s) for s in q['options']]
(R/'data/2026-06-mcqs.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
p=R/'volumes/June-2026-Mains-Frameworks.md';p.write_text('\n'.join(s if '**Study reference:**' in s else prose(s) for s in p.read_text().splitlines())+'\n')
for name in ['sources.json','source-access.json']:
 p=R/'data'/name;d=json.loads(p.read_text())
 for k,v in d.items():
  if k.startswith('E13-'):
   if isinstance(v,list):v[0]=prose(v[0])
   else:v['title']=prose(v['title']);v['access']=prose(v['access'])
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Edition13prose spacing cleaned; structural data preserved')
