"""Manual Edition17 prose proof; never edit IDs or URLs."""
import pathlib,json,re
R=pathlib.Path(__file__).resolve().parents[1];p=R/'data/notes.json';N=json.loads(p.read_text())
fix={'Q 2':'Q2','Q 1':'Q1','57 th':'57th','180 th':'180th','Segment 1':'Segment 1','inMWhorGWh':'in MWh or GWh','inMWorGWdiffers':'in MW or GW differs','ISTon':'IST on','Octoberand':'October and','Octoberassurance':'October assurance','Octoberbulletin':'October bulletin','OctoberCabinet':'October Cabinet','Octoberobservations':'October observations','Octoberreport':'October report','Octoberreports':'October reports','OctoberTOIreport':'October TOI report','Octoberusing':'October using','permonth':'per month','the3Rs':'the 3Rs','1.5°Cby':'1.5°C by','1.5°Cunder':'1.5°C under','from1.5':'from 1.5','as2.8':'as 2.8','a50%':'a 50%','the2026':'the 2026','a2026':'a 2026','Newtons':'Newtons','Acts1982':'Acts 1982'}
def clean(s):
 for a,b in fix.items():s=s.replace(a,b)
 # Word boundaries around dates and named authorities, not blanket acronym splitting.
 s=re.sub(r'(?<=[A-Za-z])(January|February|March|April|May|June|July|August|September|October|November|December)(?=\s|\d)',r' \1',s)
 s=re.sub(r'(January|February|March|April|May|June|July|August|September|October|November|December)(?=[A-Z])',r'\1 ',s)
 return s
for n in N:
 if not n['id'].startswith('E17-'):continue
 for k in ['title','why','static_link','trap','mains']:n[k]=clean(n[k])
 for k in ['facts','analysis']:n[k]=[clean(x)for x in n[k]]
p.write_text(json.dumps(N,ensure_ascii=False,indent=2)+'\n')
