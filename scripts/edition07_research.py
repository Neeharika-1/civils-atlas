import pathlib,requests,bs4,json,hashlib,concurrent.futures
R=pathlib.Path(__file__).resolve().parents[1];P=R/'research/magazine-review/vision-inventory.json';D=json.loads(P.read_text());C=pathlib.Path('/home/user/.cache/civils-magazine');C.mkdir(parents=True,exist_ok=True)
sel={'2025-11':['legal-aid-in-india','g20','unfccc-cop-30','national-one-health-mission-nohm','national-action-plan-on-antimicrobial-resistance-20','bhagwan-birsa-munda','ethics-of-neuro-tech-revolution','protection-of-plant-varieties-and-farmers-rights-act-2001'],'2025-12':['digital-constitutionalism','panchayats-extension-to-scheduled-areas-act-1996','prevention-of-sexual-harassment-posh-act-2013','dynamic-groundwater-resources-assessment','localization-of-disaster-risk-reduction-drr','social-media-ban-for-children','unesco-intangible-cultural-heritage-list','right-to-disconnect']}
def get(v):
 m,a=v;r=requests.get(a['url'],timeout=35);r.raise_for_status();s=bs4.BeautifulSoup(r.text,'html.parser');e=s.find('article') or s.find('main') or s
 for k in e.select('script,style,nav,header,footer'):k.decompose()
 text=e.get_text(' ',strip=True);(C/(m+'_'+hashlib.sha256(a['url'].encode()).hexdigest()[:16]+'.txt')).write_text(text);return m,a,text
jobs=[(m,a) for m in sel for a in D[m]['articles'] if a['url'].split('/')[-1] in sel[m]]
for m,a,t in concurrent.futures.ThreadPoolExecutor(max_workers=6).map(get,jobs):
 a['retrieval']='Public body retrieved; selected lead passages inspected only';a['words']=len(t.split());print('\n'+m+' '+a['url']+'\n'+t[:4400])
P.write_text(json.dumps(D,ensure_ascii=False,indent=2));(R/'research/magazine-review/edition07-selected.json').write_text(json.dumps(sel,indent=2))
