"""Merge only the supplied researched delta; preserve existing user-edited note objects."""
import json,pathlib,re
R=pathlib.Path(__file__).resolve().parents[1]
def load(p,default):
 f=R/p
 return json.loads(f.read_text()) if f.exists() else default
def save(p,x):
 dest=R/p;tmp=dest.with_suffix(dest.suffix+'.tmp');tmp.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');tmp.replace(dest)
d=load('research/edition19/research-delta.json',None);assert d and d['batch']=='E19-2026-11-07'
notes=load('data/notes.json',[]);assert len(notes)>=1178,'Expected the previously imported study archive'
ids={n['id']for n in notes};new=[n for n in d['notes']if n['id']not in ids];notes.extend(new)
for file,key in [('data/sources.json','sources'),('data/source-access.json','source_access')]:
 data=load(file,{})
 for k,v in d[key].items():data.setdefault(k,v)
 save(file,data)
for file,key in [('data/research-updates.json','research_updates'),('data/research-practice.json','research_practice')]:
 data=load(file,[]);known={x['id']for x in data}
 data.extend(x for x in d[key]if x['id']not in known);save(file,data)
save('data/notes.json',notes)
manifest=load('Package-Manifest.json',{});monthly=sum(len(json.loads(p.read_text()))for p in (R/'data').glob('*-mcqs.json'));supp=len(load('data/research-practice.json',[]));frameworks=sum(len(re.findall(r'^## ',p.read_text(),re.M))for p in (R/'volumes').glob('*-Mains-Frameworks.md'))
manifest.update(edition='19',date='2026-11-07',notes=len(notes),source_references=len(load('data/sources.json',{})),original_mcqs=monthly+supp,monthly_mcqs=monthly,supplementary_mcqs=supp,original_mains_frameworks=frameworks,research_addendum_notes=14,research_addendum_sources=18,daily_website='Self-contained workflow prepared; actual run/deployment must be verified from hosted evidence',full_archive_complete=False)
manifest['november_2026_notes']=sum(n['date'].startswith('2026-11')for n in notes);manifest['november_2026_new_notes']=manifest['november_2026_notes']-1;manifest['november_2026_ap_notes']=sum(n['date'].startswith('2026-11')and n['ap']for n in notes)
manifest['november_2026_priority_counts']={p:sum(n['date'].startswith('2026-11')and n['priority']==p for n in notes)for p in ['P1','P2','P3']}
for obsolete in ['november_2026_pdf_pages','november_2026_pdf_words','packaged_file_count']:manifest.pop(obsolete,None)
save('Package-Manifest.json',manifest)
print(f'Merged {len(new)} new notes without overwriting existing note IDs; {len(notes)} total. Practice {monthly}+{supp}; Mains {frameworks}.')
