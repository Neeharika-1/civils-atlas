"""Targeted proof of Edition16 human prose; no identifier/URL substitutions."""
import pathlib,json,re
R=pathlib.Path(__file__).resolve().parents[1];p=R/'data/notes.json';N=json.loads(p.read_text())
fix={'isUS$':'is US$','areUS$':'are US$','₹ ':'₹','US$ ':'US$','Q 1':'Q1','GW h':'GWh','MW h':'MWh','up totwo':'up to two','forone':'for one','threemonths':'three months','sevendays':'seven days','fiveyears':'five years','five-year':'five-year','inSangam':'in Sangam','Andhra Pradesh':'Andhra Pradesh','S. Typhi':'S. Typhi','S.Paratyphi':'S. Paratyphi','stem-cell':'stem-cell','approved₹':'approved ₹','and/or':'and/or'}
extra={'BoPbasis':'BoP basis','AggregateWMA':'Aggregate WMA','ChapterIII':'Chapter III','LandStackdeployment':'LandStack deployment','RPwDframework':'RPwD framework','UPIQR':'UPI QR','CBRNrecce':'CBRN recce','DEFSAC':'DEFSAC','BOOM':'BOOM','andNCCF':'and NCCF','typhoidalSalmonella':'typhoidal Salmonella','everySalmonellainfection':'every Salmonella infection','aGLOF':'a GLOF','anNCRdraft':'an NCR draft','NCRdraft':'NCR draft','accuratePrelimsquestions':'accurate Prelims questions','previousthreemonths':'previous three months','IPrights':'IP rights','first-stateBill':'first-state Bill','Schemebenefits':'Scheme benefits','inAssam':'in Assam','andSumatran':'and Sumatran'}
protect=['BoP','AoN','MoU','LandStack','RPwD','CosmoCube','OneHealth','Bhu-Aadhaar']
def clean(s):
 for a,b in extra.items():s=s.replace(a,b)
 for i,x in enumerate(protect):s=s.replace(x,'§'+chr(65+i)+'§')
 s=re.sub(r'(?<=[a-z])(?=[A-Z])',' ',s)
 for i,x in enumerate(protect):s=s.replace('§'+chr(65+i)+'§',x)
 for a,b in fix.items():s=s.replace(a,b)
 s=re.sub(r'(?<=[,:;])(?=[A-Za-z₹])',' ',s)
 s=re.sub(r'(?<=\d),(?=\d+%)',', ',s)
 s=re.sub(r'(?<=[a-z])(?=₹)',' ',s)
 s=s.replace('OneHealth','One Health').replace('CPDhours','CPD hours').replace('GW h','GWh').replace('MW h','MWh')
 return re.sub(' +',' ',s)
for n in N:
 if not n['id'].startswith('E16-'):continue
 for k in ['title','why','static_link','trap','mains','status','evidence_access']:n[k]=clean(n[k])
 for k in ['facts','analysis']:n[k]=[clean(x)for x in n[k]]
p.write_text(json.dumps(N,ensure_ascii=False,indent=2)+'\n')
