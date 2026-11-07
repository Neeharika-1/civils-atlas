import requests,bs4,json,pathlib,concurrent.futures,hashlib,time
R=pathlib.Path(__file__).resolve().parents[1];D=json.loads((R/'research/magazine-review/vision-inventory.json').read_text());C=pathlib.Path('/home/user/.cache/civils-magazine');C.mkdir(parents=True,exist_ok=True)
jobs=[]
for m,d in D.items():
 if not any(a['url']==d['entry_url'] for a in d['articles']):d['articles'].insert(0,dict(title=d['entry_url'].split('/')[-1].replace('-',' ').title(),url=d['entry_url'],review='Not yet reconciled'))
 for a in d['articles']:
  if '#' not in a['url']:jobs.append((m,a))
def get(x):
 m,a=x;u=a['url'];f=C/(m+'_'+hashlib.sha256(u.encode()).hexdigest()[:16]+'.txt')
 try:
  r=requests.get(u,timeout=35);r.raise_for_status();s=bs4.BeautifulSoup(r.text,'html.parser');body=s.select_one('#article-content')
  if not body:raise ValueError('Public article body missing')
  text=body.get_text('\n',strip=True);f.write_text(text);a['retrieval']='Public article body retrieved; not a full-review claim';a['headings']=[x.get_text(' ',strip=True) for x in body.find_all(['h2','h3','h4'])]
  a['primary_links']=[x['href'] for x in s.select('a[href]') if x['href'].startswith('https://') and 'visionias' not in x['href'] and not any(k in x['href'] for k in ['google','facebook','youtube','twitter','telegram','whatsapp','linkedin','instagram'])][-10:]
  a['words']=len(text.split())
 except Exception as e:a['retrieval']='Failed: '+str(e)
 return a
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:list(ex.map(get,jobs))
(R/'research/magazine-review/vision-inventory.json').write_text(json.dumps(D,ensure_ascii=False,indent=2))
print('Retrieved',sum(a.get('words',0)>0 for _,a in jobs),'public article bodies; failures',[(m,a['url'],a['retrieval']) for m,a in jobs if not a.get('words')]);print('Cache only: original bodies excluded from project/package.')
