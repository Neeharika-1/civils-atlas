import requests,bs4,json,pathlib,concurrent.futures,hashlib,re
R=pathlib.Path(__file__).resolve().parents[1];p=R/'research/magazine-review/vision-inventory.json';D=json.loads(p.read_text());C=pathlib.Path('/home/user/.cache/civils-magazine');C.mkdir(parents=True,exist_ok=True)
slugs=['bharat-audyogik-vikas-yojna-bhavya', 'digital-public-infrastructure', 'regional-connectivity-scheme-rcs-modified-udan', 'fiscal-health-index', 'environment-impact-assessment', 'national-report-by-india-on-convention-on-biological-diversity', 'india-submits-1st-national-report-on-implementation-of-nagoya-protocol', 'indias-updated-nationally-determined-contribution-ndc', 'discovery-of-new-particle-by-large-hadron-collider', 'irnss-navic-1', 'mahad-satyagraha-4', 'energy-security-and-indias-foreign-policy']
def get(a):
 r=requests.get(a['url'],timeout=40);r.raise_for_status();s=bs4.BeautifulSoup(r.text,'html.parser');e=s.find('article') or s.find('main') or s
 for k in e.select('script,style,nav,header,footer'):k.decompose()
 text=e.get_text(' ',strip=True);(C/('2026-03_'+hashlib.sha256(a['url'].encode()).hexdigest()[:16]+'.txt')).write_text(text);a['retrieval']='Public body retrieved; selected lead/substantive passages inspected only';a['words']=len(text.split());return a,re.split(r'Posted \d+ \w+ \d{4}',text,maxsplit=1)[-1]
for a,t in concurrent.futures.ThreadPoolExecutor(max_workers=5).map(get,[a for a in D['2026-03']['articles'] if a['url'].split('/')[-1] in slugs]):print('\n'+a['url']+'\n'+t[:2200])
p.write_text(json.dumps(D,ensure_ascii=False,indent=2));(R/'research/magazine-review/edition10-selected.json').write_text(json.dumps({'2026-03':slugs},indent=2))
