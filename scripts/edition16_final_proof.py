"""Manual word-boundary proof, Edition16 prose only; identifiers never touched."""
import json,pathlib
R=pathlib.Path(__file__).resolve().parents[1];p=R/'data/notes.json';N=json.loads(p.read_text())
fix={'asautism':'as autism','canOne Health':'can One Health','claimedpartyfreeze':'claimed party freeze','cmrest':'cm rest','dalintervention':'dal intervention','dalrequest':'dal request','DRincreases':'DR increases','ETVBharat':'ETV Bharat','fortransmission':'for transmission','fromthree':'from three','lakhcrore':'lakh crore','lakhtonnes':'lakh tonnes','localfactory':'local factory','netprimaryincome':'net primary income','netsecondaryincome':'net secondary income','Netservices':'Net services','Openweights':'Open weights','overfive':'over five','Personaltransfer':'Personal transfer','potentialjobs':'potential jobs','proposedCosmoCube':'proposed CosmoCube','reserveasset':'reserve asset','Septemberevent':'September event','Septemberlaunch':'September launch','Septemberpension':'September pension','Septemberreport':'September report','Septembersubcommittee':'September subcommittee','sorder':'s order','toseven':'to seven','completedLandStack':'completed LandStack','Currentaccount':'Current account','Secondaryincome':'Secondary income','income+':'income +','income−':'income −','CapitalMission':'Cabinet Mission'}
# Currency-format and punctuation edits are explicit, not substitutions inside numeric groups.
fix.update({'US$4.2 billion,0.5%':'US$4.2 billion, 0.5%','April–June;8.1':'April–June; 8.1','ChapterIII':'Chapter III','GWh BESS':'GWh BESS'})
def clean(s):
 for a,b in fix.items():s=s.replace(a,b)
 return s
for n in N:
 if not n['id'].startswith('E16-'):continue
 for k in ['title','why','static_link','trap','mains']:n[k]=clean(n[k])
 for k in ['facts','analysis']:n[k]=[clean(x)for x in n[k]]
p.write_text(json.dumps(N,ensure_ascii=False,indent=2)+'\n')
# Update the new titles in the reading-journey index after proof.
by={n['id']:n for n in N};f=R/'volumes/Cross-Month-Reading-Journeys.md';s=f.read_text()
import re
for n in N:
 if n['id'].startswith('E16-'):s=re.sub(r'(?m)^- \*\*'+re.escape(n['id'])+r'\*\*.*$',f"- **{n['id']}** · {n['date'][:7]} · {n['title']}",s)
f.write_text(s)
