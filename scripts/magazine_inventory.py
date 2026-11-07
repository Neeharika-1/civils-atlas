"""Inventory publicly accessible official magazine web editions; no login/download bypass."""
import requests,bs4,pathlib,json,concurrent.futures
R=pathlib.Path(__file__).resolve().parents[1]
editions={'2025-01':('2025-02-22','polity-and-governance/cooperatives'),'2025-02':('2025-03-24','polity-and-governance/freebies'),'2025-03':('2025-04-16','polity-and-governance/judicial-accountability'),'2025-04':('2025-05-17','polity-and-governance/separation-of-powers'),'2025-05':('2025-06-17','polity-and-governance/private-member-bill')}
def get(item):
 month,(date,slug)=item;u=f'https://visionias.in/current-affairs/monthly-magazine/{date}/{slug}';res=requests.get(u,timeout=40);res.raise_for_status();soup=bs4.BeautifulSoup(res.text,'html.parser');links={}
 for a in soup.select('a[href]'):
  href=a['href']
  if f'/monthly-magazine/{date}/' in href:
   url='https://visionias.in'+href if href.startswith('/') else href
   if url.split('#')[0]!=u or '#' in url:links[url]=a.get_text(' ',strip=True)
 # Do not persist full publisher articles in the distributed project.
 return month,{'coverage_month':month,'web_posting_date':date,'entry_url':u,'articles':[{'title':t,'url':v,'review':'Not yet reconciled'} for v,t in links.items()]}
D=dict(concurrent.futures.ThreadPoolExecutor(max_workers=5).map(get,editions.items()));(R/'research/magazine-review/vision-inventory.json').write_text(json.dumps(D,ensure_ascii=False,indent=2))
for m,d in sorted(D.items()):
 print('\n',m,len(d['articles']))
 for a in d['articles']:print(a['title'][:100],a['url'].replace('https://visionias.in/current-affairs/monthly-magazine/',''))
