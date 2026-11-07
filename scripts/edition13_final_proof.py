import json,pathlib,re
R=pathlib.Path(__file__).resolve().parents[1]
W={'AGPUcount':'A GPU count','APCabinet':'AP Cabinet','APProtection':'AP Protection','ATLASbriefing':'ATLAS briefing','BISsubject':'BIS subject','CBSEcircular':'CBSE circular','DNAfrom':'DNA from','DRCand':'DRC and','FIIsand':'FIIs and','FiberNetfinancing':'FiberNet financing','GISplanning':'GIS planning','GPStracking':'GPS tracking','GRAMGimplementation':'GRAMG implementation','HUDCOspecial':'HUDCO special','IVof':'IV of','MROinvestment':'MRO investment','MROis':'MRO is','MWcapacity':'MW capacity','MWhgeneration':'MWh generation','MoUalone':'MoU alone','MoUalready':'MoU already','MoUfrom':'MoU from','MoUscover':'MoUs cover','MoUsinclude':'MoUs include','MoUsor':'MoUs or','OCIstatus':'OCI status','OMCsunder':'OMCs under','PPPsallocate':'PPPs allocate','PRSrecords':'PRS records','PTIfigure':'PTI figure','PTIreports':'PTI reports','QGPfuel':'QGP fuel','Mo SPIrelease':'MoSPI release','Mo SPI':'MoSPI','Ordinanceis':'Ordinance is','Junefinancial':'June financial','Eyeunder':'Eye under','AUS$':'A US$','article’s':'article’s','RBIprimary':'RBI primary','dijets':'dijets','EU states':'EU states','UPIagreement':'UPI agreement','ThreeLanguage':'Three Language','min(85% netloss':'min(85% net loss'}
def clean(s):
 for a in sorted(W,key=len,reverse=True):s=s.replace(a,W[a])
 s=re.sub(r'\b(Article\s+\d+)\s+([A-Z])\b',r'\1\2',s)
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
p=R/'volumes/June-2026-Mains-Frameworks.md';p.write_text('\n'.join(s if '**Study reference:**' in s else clean(s) for s in p.read_text().splitlines())+'\n')
