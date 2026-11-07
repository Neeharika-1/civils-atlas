"""Check first question occurrence and final option share a page; not factual QA."""
import pathlib,json,pymupdf,datetime,re
R=pathlib.Path(__file__).resolve().parents[1];res=[]
for f in sorted((R/'data').glob('*-mcqs.json')):
 stem=f.stem.replace('-mcqs','');m=stem if re.fullmatch(r'\d{4}-\d{2}',stem) else '2025-'+str(datetime.datetime.strptime(stem,'%B').month).zfill(2)
 slug=datetime.datetime.strptime(m,'%Y-%m').strftime('%B-%Y');D=pymupdf.open(R/'volumes'/f'{slug}-Study-Volume.pdf');pages=[' '.join(p.get_text().split()) for p in D]
 start=next(i for i,p in enumerate(pages) if 'original questions, not previous-year questions. Answers follow all questions.' in p);end=next(i for i,p in enumerate(pages) if 'Explained answer key' in p);qp=pages[start:end];questions=json.loads(f.read_text())
 for q in questions:
  page=next(p for p in qp if str(q['id'])+'. ' in p)
  assert ' '.join(('D. '+q['options'][3]).split()) in page,(m,q['id'],'last option not on first question page')
 res.append({'month':m,'questions':len(questions),'status':'Question and final option verified on the same PDF page'})
(R/'research/edition-18-question-pagination.json').write_text(json.dumps(res,indent=2)+'\n');print('PASS',sum(x['questions'] for x in res),'questions in',len(res),'monthly volumes')
