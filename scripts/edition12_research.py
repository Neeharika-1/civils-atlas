import pathlib,json,requests,bs4,concurrent.futures,hashlib,re
R=pathlib.Path(__file__).resolve().parents[1];p=R/'research/magazine-review/vision-inventory.json';D=json.loads(p.read_text());links=json.load(open('/home/user/may-vision-links.json'));C=pathlib.Path('/home/user/.cache/civils-magazine');C.mkdir(exist_ok=True,parents=True)
D['2026-05']={'web_posting_date':'2026-06-30','archive_confirmation':'Official archive explicitly labels May2026 and links the30June posting; read7November2026.','articles':[dict(title=t.replace('Next Article ',''),url=u,retrieval='Not retrieved',linked_notes=[],reconciliation='Not incorporated; substantive reconciliation pending') for u,t in links.items()]}
def get(a):
 r=requests.get(a['url'],timeout=40);r.raise_for_status();s=bs4.BeautifulSoup(r.text,'html.parser');e=s.find('article') or s.find('main') or s
 for k in e.select('script,style,nav,header,footer'):k.decompose()
 text=e.get_text(' ',strip=True);(C/('2026-05_'+hashlib.sha256(a['url'].encode()).hexdigest()[:16]+'.txt')).write_text(text);a.update(retrieval='Public body retrieved; passage selection pending',words=len(text.split()));return a
selected=[a for a in D['2026-05']['articles'] if '/news-in-shorts' not in a['url']]
for a in concurrent.futures.ThreadPoolExecutor(max_workers=7).map(get,selected):print(a['url'].split('/')[-1],a['words'])
p.write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n');(R/'research/magazine-review/edition12-selected.json').write_text(json.dumps({'2026-05':[a['url'].split('/')[-1] for a in selected],'scope':'Public bodies retrieved; actual incorporated/reviewed subsets recorded after passage inspection, not full-issue audit'},indent=2)+'\n')
