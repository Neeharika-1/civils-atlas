import requests,bs4,json,pathlib,concurrent.futures,hashlib
R=pathlib.Path(__file__).resolve().parents[1];p=R/'research/magazine-review/vision-inventory.json';D=json.loads(p.read_text());C=pathlib.Path('/home/user/.cache/civils-magazine');C.mkdir(parents=True,exist_ok=True)
for m,date,slug in [('2025-09','2025-10-04','criminalisation-of-politics'),('2025-10','2025-11-12','prison-reforms')]:
 if m not in D:
  u=f'https://visionias.in/current-affairs/monthly-magazine/{date}/polity-and-governance/{slug}';s=bs4.BeautifulSoup(requests.get(u,timeout=30).text,'html.parser');links={u:slug.replace('-',' ').title()}
  for a in s.select('a[href]'):
   v=requests.compat.urljoin(u,a['href'])
   if f'/monthly-magazine/{date}/' in v and '#' not in v:links[v]=a.get_text(' ',strip=True).removeprefix('Next Article ')
  D[m]=dict(coverage_month=m,web_posting_date=date,entry_url=u,articles=[dict(title=t,url=v,review='Not yet reconciled') for v,t in links.items()])
 print('\n',m)
 for a in D[m]['articles']:print(a['url'].split('/')[-1])
p.write_text(json.dumps(D,ensure_ascii=False,indent=2))
for name in ['september','october']:
 u=f'https://prsindia.org/policy/monthly-policy-review/{name}-2025';s=bs4.BeautifulSoup(requests.get(u,timeout=30).text,'html.parser')
 print(name,'primary references',[(a.get_text(' ',strip=True),a['href']) for a in s.select('a[href]') if any(k in a['href'] for k in ['pib.gov.in','rbi.org','egazette'])][:10])
