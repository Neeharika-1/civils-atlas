"""Structural checks, not factual or completeness certification."""
import datetime,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1];N=json.loads((R/'data/notes.json').read_text());S=json.loads((R/'data/sources.json').read_text());A=json.loads((R/'data/source-access.json').read_text());ids=set()
for n in N:
 assert n['id'] not in ids;ids.add(n['id'])
 assert '2025-01-01'<=n['date']<='2026-11-07';datetime.date.fromisoformat(n['date'])
 assert n['facts'] and n['trap'] and n['mains'] and n['priority'] in ['P1','P2','P3']
 assert n.get('date_precision','day') in ['day','month','reporting-day']
 if n.get('magazine_edition'):assert n['date'][:7]==n['magazine_edition'] and n['date_precision']=='month' and n.get('magazine_posted')
 for k in n['sources']:assert k in S and S[k][1].startswith('https://') and k in A,(n['id'],k)
 if n['date']<'2025-09' or n['id'].startswith(('E6-','E7-','E8-','E9-','E10-','E11-','E12-','E13-','E14-','E15-','E16-','E17-','E18-')):assert all(n.get(k) for k in ['why','static_link','analysis','evidence_access']) and len(n['facts'])>=3,n['id']
total=0
for p in sorted((R/'data').glob('*-mcqs.json')):
 Q=json.loads(p.read_text());assert len(Q)==30;assert len(set(q['id'] for q in Q))==30
 for q in Q:assert len(set(q['options']))==4 and 0<=q['answer']<4 and q['ref'] in ids and q['explanation']
 total+=len(Q)
print(f'PASS: {len(N)} notes, {len(S)} references, {total} MCQ schemas. Expanded note fields, dates, IDs and references valid; not factual certification.')

L=json.loads((R/'data/linkages.json').read_text());assert len(L)==18
for j in L:
 assert len(j['notes'])>=2 and all(k in ids for k in j['notes'])
for n in N:
 assert all(k in ids and k!=n['id'] for k in n.get('related_notes',[]))
