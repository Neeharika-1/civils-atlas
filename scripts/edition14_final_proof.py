import pathlib,json,random
R=pathlib.Path(__file__).resolve().parents[1]
fix={'daycertificate':'day certificate','croreapplicant':'crore applicant','lakhcroreexactly':'lakh crore exactly','lakhcrore':'lakh crore','toFY':'to FY','MWpower':'MW power','MWofannualelectricity':'MW of annual electricity','MWperhour':'MW per hour','MWbaseline':'MW baseline','croreparts':'crore parts','croreexpansion':'crore expansion','PVonly':'PV only','CPIand':'CPI and','OMquashed':'OM quashed','MWwith':'MW with','ASU/homoeopathic':'ASU/homoeopathic','floor₹':'floor ₹','10%threshold':'10% threshold','to2030':'to 2030','all23':'all 23','chunks0':'chunks 0','yearone':'year one'}
def proof(s):
 for a,b in fix.items():s=s.replace(a,b)
 return s
def obj(x):
 if isinstance(x,str):return proof(x)
 if isinstance(x,list):return [obj(v) for v in x]
 if isinstance(x,dict):return {k:obj(v) for k,v in x.items()}
 return x
p=R/'data/notes.json';N=json.loads(p.read_text());N=[obj(n) if n['id'].startswith('E14') else n for n in N];p.write_text(json.dumps(N,ensure_ascii=False,indent=2)+'\n')
p=R/'data/2026-07-mcqs.json';Q=obj(json.loads(p.read_text()));Q[7]['question']='What legislative stage does the reviewed July birth-registration Bill account report?'
slots=[0]*8+[1]*8+[2]*7+[3]*7;random.Random(1414).shuffle(slots)
for q,pos in zip(Q,slots):
 correct=q['options'].pop(q['answer']);q['options'].insert(pos,correct);q['answer']=pos
p.write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
for fn in ['START-HERE.md','README.md','volumes/July-2026-Mains-Frameworks.md']:
 p=R/fn;p.write_text(proof(p.read_text()))
p=R/'research/Research-Status.md';s=p.read_text();sep='## Historical status through Edition 13';a,b=s.split(sep,1);p.write_text(proof(a)+sep+b)
print('Explicit prose correction and balanced30-answer distribution complete')
