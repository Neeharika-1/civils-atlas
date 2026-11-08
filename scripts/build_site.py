"""Fast daily app build only. Existing researched volumes are not silently regenerated."""
import datetime,json,pathlib,re
R=pathlib.Path(__file__).resolve().parents[1]
def load(name,default):
 p=R/'data'/name
 return json.loads(p.read_text()) if p.exists() else default
quiz=[];expanded=[]
for p in sorted((R/'data').glob('*-mcqs.json')):
 stem=p.stem.removesuffix('-mcqs')
 if re.fullmatch(r'\d{4}-\d{2}',stem):month=stem
 else:month='2025-'+datetime.datetime.strptime(stem,'%B').strftime('%m')
 expanded.append(month);quiz.extend(dict(q,month=month) for q in json.loads(p.read_text()))
D=dict(notes=load('notes.json',[]),sources=load('sources.json',{}),inbox=load('inbox.json',[]),logs=load('update-log.json',[]),quiz=quiz,expanded=sorted(expanded),source_access=load('source-access.json',{}),linkages=load('linkages.json',[]),automation=load('automation-status.json',{}),registry=load('source-registry.json',[]),source_coverage=load('source-coverage.json',{}),research_updates=load('research-updates.json',[]),research_practice=load('research-practice.json',[]),document_intake=load('document-intake.json',{}),compilation_registry=load('compilation-registry.json',[]),compilation_health=load('compilation-health.json',{}))
assert len({n['id'] for n in D['notes']})==len(D['notes'])
assert all(k in D['sources'] for n in D['notes'] for k in n['sources'])
assert D['notes'] and D['quiz'],'Refusing to publish an empty library'
s=(R/'template.html').read_text();assert s.count('__DATA__')==1
html=s.replace('__DATA__',json.dumps(D,ensure_ascii=False).replace('</','<\\/'))
p=R/'index.html';tmp=p.with_suffix('.html.tmp');tmp.write_text(html);tmp.replace(p)
print(f"Built daily home + {len(D['notes'])} researched notes, {len(D['quiz'])} MCQs, {len(D['registry'])} source obligations. Discovery is not editorial publication.")
