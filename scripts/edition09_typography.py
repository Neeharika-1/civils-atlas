import json,pathlib,re
R=pathlib.Path(__file__).resolve().parents[1]
def prose(s):
 s=re.sub(r'(?<=[A-Za-z%])(?=\d|₹)',' ',s)
 s=re.sub(r'(?<=\d)(?=[A-Za-z])(?!st\b|nd\b|rd\b|th\b)',' ',s)
 s=re.sub(r'(?<=\S)([:;])(?=\S)',r'\1 ',s)
 s=re.sub(r',(?=[A-Za-z₹])',', ',s)
 return s
p=R/'data/notes.json';N=json.loads(p.read_text());ids=set(json.loads((R/'research/edition-09-id-map.json').read_text()).values())
for n in N:
 if n['id'] in ids:
  for k in ['title','why','static_link','trap','mains']:n[k]=prose(n[k])
  for k in ['facts','analysis']:n[k]=[prose(v) for v in n[k]]
p.write_text(json.dumps(N,ensure_ascii=False,indent=2)+'\n')
p=R/'data/2026-02-mcqs.json';Q=json.loads(p.read_text())
for q in Q:
 for k in ['question','explanation']:q[k]=prose(q[k])
 q['options']=[prose(v) for v in q['options']]
p.write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
p=R/'volumes/February-2026-Mains-Frameworks.md';p.write_text('\n'.join(line if '**Study reference:**' in line else prose(line) for line in p.read_text().splitlines())+'\n')
# Narrative guides: preserve inline code/paths and explicit IDs.
for name in ['START-HERE.md','README.md','research/Research-Status.md','research/magazine-review/Integration-Report.md']:
 p=R/name;s=p.read_text();s=re.sub(r'(?<=[A-Za-z])(?=202[56])',' ',s);s=re.sub(r'(?<=\d)(?=February|January|March|April|November|December)',' ',s);s=re.sub(r'(?<=\d)(?=crore|lakh|days|day|working|year|IST)',' ',s);p.write_text(s)
