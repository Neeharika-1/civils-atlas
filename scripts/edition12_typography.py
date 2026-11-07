import pathlib,json,re
R=pathlib.Path(__file__).resolve().parents[1]
W={'ClassXIIand':'Class XII and','MoUtotals':'MoU totals','PartIXAreference':'Part IXA reference','TyresPhaseIVexpansion':'Tyres Phase IV expansion','acreDRDOland':'acre DRDO land','ACoutput':'AC output','AMCAfighter':'AMCA fighter','AMCAinfrastructure':'AMCA infrastructure','APBILis':'APBIL is','APSSDCand':'APSSDC and','AYUSHdoctor':'AYUSH doctor','CBRand':'CBR and','CDRuse':'CDR use','CPIinflation':'CPI inflation','DCmodule':'DC module','DRIPfinancing':'DRIP financing','GDPfor':'GDP for','GDPgrowth':'GDP growth','GDPproduction':'GDP production','GOor':'GO or','GPcounts':'GP counts','IITMPune':'IITM Pune','LEAPmonitoring':'LEAP monitoring','MWhis':'MWh is','MWis':'MW is','NCMRWFare':'NCMRWF are','NIELITinnovation':'NIELIT innovation','PLFSself':'PLFS self','PMworking':'PM working','RMSAand':'RMSA and','TFRis':'TFR is','TNIEreports':'TNIE reports','UPpilot':'UP pilot','PhaseIIGPs':'Phase II GPs','PhaseIupgrades':'Phase I upgrades','APheadline':'AP headline','APfood':'AP food','APprices':'AP prices','APmunicipalities':'AP municipalities','APworkplace':'AP workplace','PMPOSHAN':'PM POSHAN','APTI':'APTI','ACand':'AC and','DCnameplate':'DC nameplate','MWhdivided':'MWh divided','CPI-IWadjustment':'CPI-IW adjustment','Q4working':'Q4 working','C2cost':'C2 cost','C2opportunity':'C2 opportunity','CET1is':'CET1 is','EFTAand':'EFTA and'}
W.update({'MWpDCsolar':'MWp DC solar','MWpDC':'MWp DC','MWAC':'MW AC','GPscope':'GP scope','MWaddition':'MW addition','MWhbattery':'MWh battery','MWor':'MW or','TFRbelow':'TFR below','acreDRDOallotment':'acre DRDO allotment','AMCAevent':'AMCA event','ENSOphase':'ENSO phase','GPcategories':'GP categories','MWhinto':'MWh into','MWhmeans':'MWh means','MWwithout':'MW without','DCratings':'DC ratings','GOand':'GO and','TFRfrom':'TFR from'})
def prose(s):
 for a in sorted(W,key=len,reverse=True):s=s.replace(a,W[a])
 s=re.sub(r'(\d+)(st|nd|rd|th)(?=[A-Z])',r'\1\2 ',s)
 s=re.sub(r'(?<=[A-Za-z%])(?=\d|₹)',' ',s);s=re.sub(r'(?<=\d)(?=[A-Za-z])(?!st\b|nd\b|rd\b|th\b)',' ',s);s=re.sub(r'(?<=[%+])(?=[A-Za-z])',' ',s);s=re.sub(r',(?=[A-Za-z₹])',', ',s);s=re.sub(r';(?=\S)','; ',s);s=re.sub(r'(?<=[A-Za-z]),(?=\d)',', ',s);s=re.sub(r':(?=[A-Za-z\d₹])',': ',s)
 for a,b in [('Q 4','Q4'),('CET 1','CET1'),('4 Ds','4Ds')]:s=s.replace(a,b)
 return s
p=R/'data/notes.json';N=json.loads(p.read_text())
for n in N:
 if n['id'].startswith('E12-'):
  if n['subject']=='Geography':n['subject']='Environment';n['block']='07 · ENSO and forecast uncertainty'
  for k in ['title','why','static_link','trap','mains','evidence_access']:n[k]=prose(n[k])
  for k in ['facts','analysis']:n[k]=[prose(x) for x in n[k]]
p.write_text(json.dumps(N,ensure_ascii=False,indent=2)+'\n')
p=R/'data/2026-05-mcqs.json';Q=json.loads(p.read_text())
for q in Q:
 for k in ['question','explanation']:q[k]=prose(q[k])
 q['options']=[prose(x) for x in q['options']]
p.write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
p=R/'volumes/May-2026-Mains-Frameworks.md';p.write_text('\n'.join(x if '**Study reference:**' in x else prose(x) for x in p.read_text().splitlines())+'\n')
for name in ['sources.json','source-access.json']:
 p=R/'data'/name;X=json.loads(p.read_text())
 for k,v in X.items():
  if k.startswith('E12-'):
   if isinstance(v,list):v[0]=prose(v[0])
   else:v['title']=prose(v['title']);v['access']=prose(v['access'])
 p.write_text(json.dumps(X,ensure_ascii=False,indent=2)+'\n')
print('Cleaned Edition12 prose; structural IDs/URLs preserved')
# Editorial priority and date precision are substantive metadata, not completion scores.
p=R/'data/notes.json';N=json.loads(p.read_text());p2={4,10,11,14,15,16,18,19,20,22,24,26,27,28,29,31,33,34,35,36,37,39,40,41,44,49,50,51,53,54,61}
for n in N:
 if n['id'].startswith('E12-'):
  i=int(n['id'].split('-')[-1]);n['priority']='P3' if i==52 else 'P2' if i in p2 else 'P1'
  if i in {55,59,60,61,63}:n['date_precision']='reporting-day'
p.write_text(json.dumps(N,ensure_ascii=False,indent=2)+'\n')
