"""Merge additional public editions; do not overwrite existing review metadata."""
import requests,bs4,json,pathlib,concurrent.futures,hashlib
R=pathlib.Path(__file__).resolve().parents[1];p=R/'research/magazine-review/vision-inventory.json';D=json.loads(p.read_text());C=pathlib.Path('/home/user/.cache/civils-magazine');C.mkdir(parents=True,exist_ok=True)
E={'2025-06':('2025-07-22','polity-and-governance/50-years-of-emergency'),'2025-07':('2025-08-19','polity-and-governance/digital-colonialism'),'2025-08':('2025-09-04','polity-and-governance/the-constitution-one-hundred-and-thirtieth-amendment-bill-2025')}
for m,(date,slug) in E.items():
 if m in D:continue
 u=f'https://visionias.in/current-affairs/monthly-magazine/{date}/{slug}';r=requests.get(u,timeout=35);r.raise_for_status();s=bs4.BeautifulSoup(r.text,'html.parser');links={u:slug.replace('-',' ').title()}
 for a in s.select('a[href]'):
  v=a['href'];v='https://visionias.in'+v if v.startswith('/') else v
  if f'/monthly-magazine/{date}/' in v and '#' not in v:links[v]=a.get_text(' ',strip=True).removeprefix('Next Article ')
 D[m]=dict(coverage_month=m,web_posting_date=date,entry_url=u,articles=[dict(title=t,url=v,review='Not yet reconciled') for v,t in links.items()])
 def get(a):
  try:
   rr=requests.get(a['url'],timeout=35);rr.raise_for_status();b=bs4.BeautifulSoup(rr.text,'html.parser').select_one('#article-content');txt=b.get_text('\n',strip=True) if b else '';(C/(m+'_'+hashlib.sha256(a['url'].encode()).hexdigest()[:16]+'.txt')).write_text(txt);a.update(words=len(txt.split()),retrieval='Public body retrieved; substantive review pending',headings=[x.get_text(' ',strip=True) for x in b.find_all(['h2','h3','h4'])] if b else [])
  except Exception as e:a['retrieval']='Retrieval failed: '+str(e)
 with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:list(ex.map(get,D[m]['articles']))
 p.write_text(json.dumps(D,ensure_ascii=False,indent=2))
for m in E:
 print('\n',m)
 for a in D[m]['articles']:print(a['url'].split('/')[-1],a.get('words',0))
