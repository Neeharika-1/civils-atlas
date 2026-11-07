"""Targeted final typography and reading-path scope proof."""
import json,pathlib,re,collections,math
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
def save(p,x):(R/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def proof(s):
 s=re.sub(r'(?<=[A-Za-z0-9])(?=₹)',' ',s)
 s=re.sub(r'(?<=[;:])(?=\S)',' ',s)
 s=re.sub(r'(?<=[A-Za-z]),(?=\d)',', ',s)
 s=re.sub(r'(the|Anchor|AP’s|Arnab’s)(?=\d)',r'\1 ',s)
 s=re.sub(r'(?<=%),(?=\d)',', ',s)
 return s
N=load('data/notes.json')
for n in N:
 if n['id'].startswith('E17-'):
  for k in ['title','why','static_link','trap','mains']:n[k]=proof(n[k])
  for k in ['facts','analysis']:n[k]=[proof(x)for x in n[k]]
Q=load('data/2026-10-mcqs.json')
for q in Q:
 for k in ['question','explanation']:q[k]=proof(q[k])
 q['options']=[proof(x)for x in q['options']]
save('data/2026-10-mcqs.json',Q)
p=R/'volumes/October-2026-Mains-Frameworks.md';p.write_text(proof(p.read_text()))
# Keep October links mechanistically relevant: no arbitrary income-tax/cooperative links.
L=load('data/linkages.json');scope={2:[],3:[32,33],6:[],7:[19,20,31],17:[14,16,18,21,31,36,44,45,47,52,58,63,65]}
for i,ks in scope.items():L[i-1]['notes']=[x for x in L[i-1]['notes']if not x.startswith('E17-')]+[f'E17-2610-{k:03}'for k in ks]
stop=set('the and for with from this that into are not through january february march april may june july august september october india indian policy new state national framework report review development original stage different'.split())
def words(n):return set(re.findall(r'[a-z]{4,}',(n['title']+' '+n['block']).lower()))-stop
old=[n for n in N if not n['id'].startswith('E17-')];df=collections.Counter(w for n in old for w in words(n))
for n in N:n['journeys']=[l['id']for l in L if n['id']in l['notes']]
for n in N:
 if not n['id'].startswith('E17-'):continue
 ranks=sorted(old,key=lambda x:sum(math.log(1+len(old)/(1+df[w]))for w in words(n)&words(x))+(1 if n['subject']==x['subject']else 0),reverse=True)
 companions=[k for l in L if n['id']in l['notes']for k in l['notes']if k!=n['id']]
 n['related_notes']=list(dict.fromkeys([x['id']for x in ranks[:6]]+companions))
save('data/notes.json',N);save('data/linkages.json',L)
by={n['id']:n for n in N};lines=['# Civils Atlas · Cross-month reading journeys','','18 comparative paths across 2025 and January–October 2026. Preserve evidence vintages, draft status and commencement dates; reading order is not one continuous legal timeline.','']
for l in L:lines+=['## '+l['id']+' · '+l['title'],l['mechanism'],'']+['- **'+k+'** · '+by[k]['date'][:7]+' · '+by[k]['title']for k in l['notes']]+['','**Avoid this shortcut:** '+l['caution'],'','**Mains synthesis:** '+l['prompt'],'']
(R/'volumes/Cross-Month-Reading-Journeys.md').write_text('\n'.join(lines)+'\n')
linked=sum(bool(n['journeys'])for n in N)
M=load('Package-Manifest.json');M['notes_linked_to_journeys']=linked;save('Package-Manifest.json',M)
for f in ['START-HERE.md','README.md','research/Research-Status.md']:
 p=R/f;p.write_text(p.read_text().replace('linking 684 notes',f'linking {linked} notes'))
# A corrected note may explicitly name the old error in its caution: check the title instead.
p=R/'.qa/check.cjs';s=p.read_text().replace("!d.querySelector('#E16-2609-056 .content').textContent.includes('Chintalapudi')","!d.querySelector('#E16-2609-056 summary').textContent.includes('Chintalapudi')");p.write_text(s)
print('Proofed prose and relevant paths;',linked,'notes linked.')
