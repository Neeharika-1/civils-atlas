"""Export integrity, not independent factual validation. Requires optional pymupdf."""
import json,pathlib,datetime,zipfile,re,collections
import pymupdf as fitz
from docx import Document
R=pathlib.Path(__file__).resolve().parents[1];N=json.loads((R/'data/notes.json').read_text());out=[]
months=sorted(datetime.datetime.strptime(p.name,'%B-%Y-Study-Volume.pdf').strftime('%Y-%m') for p in (R/'volumes').glob('*-Study-Volume.pdf'))
for m in months:
 slug=datetime.datetime.strptime(m,'%Y-%m').strftime('%B-%Y');base=R/'volumes'/f'{slug}-Study-Volume';ns=[n for n in N if n['date'].startswith(m)];d=fitz.open(str(base)+'.pdf');text='\n'.join(p.get_text() for p in d);flat=' '.join(text.split());doc=Document(str(base)+'.docx');word='\n'.join(p.text for p in doc.paragraphs);md=pathlib.Path(str(base)+'.md').read_text()
 for n in ns:
  assert n['id'] in text,(m,n['id'],'PDF');assert n['id'] in word,(m,n['id'],'DOCX');assert n['id'] in md,(m,n['id'],'MD')
 assert '30 original questions' in flat,(m,'MCQ intro');assert 'Explained answer key' in text
 framework=(R/'volumes'/f'{slug}-Mains-Frameworks.md').read_text();assert len(re.findall(r'^## ',framework,re.M))==8
 assert len(re.findall(r'^## ',framework,re.M))==8
 with zipfile.ZipFile(str(base)+'.docx') as z:assert z.testzip() is None
 blanks=[i+1 for i,p in enumerate(d) if len(p.get_text().strip())<100];assert not blanks,(m,blanks)
 assert '\ufffd' not in text,(m,'replacement glyph')
 out.append(dict(month=m,notes=len(ns),pages=len(d),pdf_bytes=pathlib.Path(str(base)+'.pdf').stat().st_size,docx_paragraphs=len(doc.paragraphs),pdf_links=sum(len(p.get_links()) for p in d),status='IDs / questions / framework count / OOXML / nonblank pages / replacement glyph checks PASS'))
 # Render one representative new study page for a human visual check.
 for marker,name in [('Talliki Vandanam:','June-Talliki'),('NISAR launched:','July-NISAR'),('Stree Shakti launch:','August-Stree')]:
  for i,p in enumerate(d):
   if marker in p.get_text():
    dst=R/'.qa'/f'{name}.png';p.get_pixmap(matrix=fitz.Matrix(1.25,1.25)).save(dst);break
archive='\n'.join(p.text for p in Document(R/'Study-Notes.docx').paragraphs)
assert all(n['id'] in archive for n in N)
j=fitz.open(R/'volumes/Cross-Month-Reading-Journeys.pdf');jt='\n'.join(p.get_text() for p in j);assert all(f'PATH-{x:02}' in jt for x in range(1,19))
for p in (R/'volumes').glob('*.docx'):
 with zipfile.ZipFile(p) as z:assert z.testzip() is None
result=dict(status='PASS',date='2026-11-07',monthly_volumes=out,archive_notes=len(N),reading_atlas_paths=18,reading_atlas_pages=len(j),scope='Text/package integrity only; no independent factual/completeness certification')
(R/'research/edition-18-document-checks.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
