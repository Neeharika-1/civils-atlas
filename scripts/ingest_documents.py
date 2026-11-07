"""Daily permitted primary-PDF intake. Text extraction is NOT human verification or note authoring."""
import concurrent.futures,datetime,hashlib,io,json,pathlib,re,urllib.parse
import requests,shutil,subprocess,tempfile
from pypdf import PdfReader
from update import robot_policy,canonical,UA,save,read
R=pathlib.Path(__file__).resolve().parents[1]
# Conservative original-publisher allowlist; no newspaper PDFs, proxies, paywalls or user login.
HOSTS={'apfinance.gov.in','www.apfinance.gov.in'}
def intake(item):
 url=item['url'];row=dict(url=url,source=item.get('source','AP Finance'),checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='failed',human_verified=False)
 try:
  target=url
  for _ in range(5):
   p=urllib.parse.urlsplit(canonical(target))
   if p.hostname not in HOSTS:raise RuntimeError('Redirect/source outside primary-document allowlist')
   policy=robot_policy(p.scheme+'://'+p.netloc)
   if policy is not None and not policy.can_fetch(UA,target):raise RuntimeError('robots disallows document retrieval')
   res=requests.get(target,timeout=(8,30),headers={'User-Agent':UA},allow_redirects=False,stream=True)
   if res.status_code in (301,302,303,307,308):
    location=res.headers.get('Location');res.close()
    if not location:raise RuntimeError('Redirect without Location')
    target=canonical(urllib.parse.urljoin(target,location));continue
   res.raise_for_status();chunks=[];size=0
   with res:
    for chunk in res.iter_content(65536):
     size+=len(chunk)
     if size>10*1024*1024:raise RuntimeError('Document exceeds conservative 10 MiB limit')
     chunks.append(chunk)
   data=b''.join(chunks);break
  else:raise RuntimeError('Too many redirects')
  if not data.lstrip().startswith(b'%PDF'):raise RuntimeError('Source did not return a PDF')
  pdf=PdfReader(io.BytesIO(data),strict=False)
  if pdf.is_encrypted:raise RuntimeError('Encrypted document requires authorised manual review')
  if len(pdf.pages)>50:raise RuntimeError('Over 50 pages: manual full-document review required')
  pages=[page.extract_text()or''for page in pdf.pages];scanned=[i for i,t in enumerate(pages)if len(t.strip())<40];ocr=[]
  if scanned and len(scanned)<=8 and shutil.which('pdftoppm') and shutil.which('tesseract'):
   with tempfile.TemporaryDirectory(prefix='atlas-primary-ocr-')as tmp:
    folder=pathlib.Path(tmp);source=folder/'source.pdf';source.write_bytes(data)
    for i in scanned:
     prefix=folder/f'page-{i+1}'
     subprocess.run(['pdftoppm','-f',str(i+1),'-l',str(i+1),'-r','180','-singlefile','-png','-q',str(source),str(prefix)],check=True,timeout=40,capture_output=True)
     result=subprocess.run(['tesseract',str(prefix)+'.png','stdout','-l','eng','--psm','3'],check=True,timeout=40,capture_output=True,text=True)
     pages[i]=result.stdout;ocr.append(i+1)
  text='\n'.join(pages);complete=all(len(t.strip())>=40 for t in pages)
  row.update(status='machine_text_extracted'if complete else'partial_or_scan_requires_review',pages=len(pages),pages_with_text=sum(len(t.strip())>=40 for t in pages),ocr_pages=ocr,text_characters=len(text),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),publication_date_verified=False)
  date=re.search(r'Dated\s*[:.\-]?\s*(\d{1,2})[.\-/](\d{1,2})[.\-/](20\d{2})',text[:8000],re.I)
  if date:
   try:row['document_date_candidate']=datetime.date(int(date[3]),int(date[2]),int(date[1])).isoformat()
   except ValueError:pass
  row['reading_limit']='Machine extraction/OCR attempted across '+str(len(pages))+' pages; no legal-status certification or human fact verification. OCR may contain errors; scanned-page OCR is limited to eight pages per document. Full text is not republished.'
 except Exception as e:row['error']=str(e)
 return row
if __name__=='__main__':
 # Only current indexed AP Finance PDF links; no automatic expansion to all referenced sites.
 items=[x for x in read('inbox.json',[])if urllib.parse.urlsplit(x['url']).hostname in HOSTS and urllib.parse.urlsplit(x['url']).path.lower().endswith('.pdf')]
 items=sorted({x['url']:x for x in items}.values(),key=lambda x:x['url'])
 # Explicit work budget, carried forward as pending rather than claimed complete.
 previous={x['url']:x for x in read('document-intake.json',{}).get('documents',[])}
 items=sorted(items,key=lambda x:previous.get(x['url'],{}).get('checked_at',''))
 selected=items[:12];pending=items[12:]
 with concurrent.futures.ThreadPoolExecutor(max_workers=3)as pool:rows=list(pool.map(intake,selected))
 cited=read('source-access.json',{})
 for row in rows:
  keys=[k for k,v in cited.items()if v.get('url')==row['url'] and v.get('retrieval_sha256')]
  row['cited_source_ids']=keys
  row['cited_version_changed']=any(cited[k]['retrieval_sha256']!=row.get('sha256')for k in keys) if row.get('sha256')else None
  prior=previous.get(row['url'],{})
  if row.get('sha256') and prior.get('sha256'):
   row['content_changed_since_previous']=row['sha256']!=prior['sha256']
   row['previous_sha256']=prior['sha256']
 done={x['url']:x for x in rows}
 for item in pending:
  done[item['url']]=dict(previous.get(item['url'],{}),url=item['url'],source=item.get('source','AP Finance'),status='pending_budget',human_verified=False,reading_limit='Not examined in this run: 12-document daily intake budget. A prior extraction is not a current check.')
 result=dict(updated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='AP Finance primary PDFs only; extraction is not verification. Other publishers remain separate access obligations.',attempted=len(selected),pending=len(pending),extracted=sum(x['status']=='machine_text_extracted'for x in rows),documents=sorted(done.values(),key=lambda x:x['url']))
 save('document-intake.json',result);print(json.dumps(result,indent=2))
