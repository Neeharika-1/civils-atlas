import pathlib,json,re
R=pathlib.Path(__file__).resolve().parents[1]
fix={'Sloveniafor':'Slovenia for','Visakhapatnambasing':'Visakhapatnam basing','RELOSoperationalisation':'RELOS operationalisation','IMIresistance':'IMI resistance','Amaravatiand':'Amaravati and','Buddhistheritage':'Buddhist heritage','UNESCOlisting':'UNESCO listing','APPSCcomparison':'APPSC comparison','NCRBPrison':'NCRB Prison','Scheduleis':'Schedule is','Corporationfor':'Corporation for','FiberNetwiththe':'FiberNet with the','Chittoordistrict':'Chittoor district','NREDCAPfor':'NREDCAP for','APCRDAland':'APCRDA land','Operateand':'Operate and','Cabinetdecision':'Cabinet decision','Cabinetapprovalaloneauthorises':'Cabinet approval alone authorises','Cabinetapproval':'Cabinet approval','Establishmentsframework':'Establishments framework','Unionoffice':'Union office','Uniondecision':'Union decision','CCEAdecision':'CCEA decision','Accommodationis':'Accommodation is','CGGPOAoffice':'CGGPOA office','Chiralaand':'Chirala and','Vishwaschanges':'Vishwas changes','federalismdiscussion':'federalism discussion','Telanganaformation':'Telangana formation','Organisationis':'Organisation is','toinclude':'to include','Gazettewas':'Gazette was','PM-KUSUMproposal':'PM-KUSUM proposal','APordinance':'AP ordinance','APapproved':'AP approved','APshould':'AP should','APneeds':'AP needs','APpublic':'AP public','AP’sAmaravati':'AP’s Amaravati','IndianOcean':'Indian Ocean','Indiaweed':'India weed','Rabi':'Rabi','MayPHEIC':'May PHEIC','Juneoutbreak':'June outbreak','Junepolicy':'June policy','Junedigital':'June digital','JunePTI':'June PTI','Mayoverlap':'May overlap','stopwords':'stopwords','quantumlink':'quantum link','Telugudisclosure':'Telugu disclosure','bothAP':'both AP','EMTskills':'EMT skills','hillaccess':'hill access','currentaccount':'current account','grosswithout':'gross without','termlimits':'term limits','UPIacceptance':'UPI acceptance','DSA s':'DSAs','FII s':'FIIs','NRI s':'NRIs','OCI s':'OCIs','OMC s':'OMCs','NBFC s':'NBFCs','EMT s':'EMTs','Mo U s':'MoUs','Mo U':'MoU','Mo Us':'MoUs','GPU count':'GPU count','GPU s':'GPUs','legitimate':'legitimate','fiveMo':'five Mo','newVisakhapatnam':'new Visakhapatnam','PHEICdetermination':'PHEIC determination','ASLpathway':'ALS pathway','ALSpathway':'ALS pathway','Indiafor':'India for','NCRBreport':'NCRB report','PM-KUSUMis':'PM-KUSUM is','Cabinetreporting':'Cabinet reporting','CoalController':'Coal Controller','DBFOTestablishes':'DBFOT establishes','ATFsmoothing':'ATF smoothing','Act1994':'Act 1994','MayPHEIC':'May PHEIC','quarterlysurplus':'quarterly surplus','ancientIndia':'ancient India','newIIP':'new IIP','IIPseries':'IIP series','netloss':'net loss','grossloss':'gross loss','lifetimeclaim':'lifetime claim','losswindow':'loss window','CRBreport':'CRB report','reportingclock':'reporting clock','min(85%':'min(85%','statetotal':'state total','EUmember':'EU member'}
ac=['APPSC','APCRDA','NREDCAP','CGGPOA','WHO','FCRA','THOTA','FEMA','RBI','MPC','GDP','GVA','IIP','PPI','ATF','DBFOT','CSR','AAY','PHH','DPR','GO','IP','AIS','NAS','EMT','ALS','IMI','AP','NCRB','RELOS','PHEIC','DFPD']
def clean(s):
 for k in sorted(fix,key=len,reverse=True):s=s.replace(k,fix[k])
 for a in sorted(ac,key=len,reverse=True):s=re.sub(r'\b'+a+r'(?=[a-z]{2})',a+' ',s)
 s=re.sub(r'(?<=\d),\s+(?=\d)',',',s)
 s=re.sub(r'\b(\d+)\s*(st|nd|rd|th)(?=[a-zA-Z])',r'\1\2 ',s)
 s=re.sub(r'(?<=[a-z])(?=[A-Z])',' ',s)
 s=s.replace('Fiber Net','FiberNet').replace('Mo Us','MoUs').replace('Mo U s','MoUs').replace('Mo U','MoU')
 return s
for name in ['notes.json','2026-06-mcqs.json','sources.json','source-access.json']:
 p=R/'data'/name;d=json.loads(p.read_text())
 if name=='notes.json':
  for n in d:
   if n['id'].startswith('E13-'):
    for k in ['title','why','static_link','trap','mains','evidence_access']:n[k]=clean(n[k])
    for k in ['facts','analysis']:n[k]=list(map(clean,n[k]))
 elif name.endswith('mcqs.json'):
  for q in d:
   for k in ['question','explanation']:q[k]=clean(q[k])
   q['options']=list(map(clean,q['options']))
 else:
  for k,v in d.items():
   if k.startswith('E13-'):
    if isinstance(v,list):v[0]=clean(v[0])
    else:v['title']=clean(v['title']);v['access']=clean(v['access'])
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=R/'volumes/June-2026-Mains-Frameworks.md';p.write_text('\n'.join(x if '**Study reference:**' in x else clean(x) for x in p.read_text().splitlines())+'\n')
