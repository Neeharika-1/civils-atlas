"""Daily discovery ONLY. Never promotes source text into reviewed study notes."""
import os,argparse,concurrent.futures,datetime,hashlib,json,pathlib,re,time,urllib.parse,urllib.robotparser
import requests
from bs4 import BeautifulSoup
R=pathlib.Path(__file__).resolve().parents[1]
START='2025-01-01'
SITES=[('PIB daily','https://www.pib.gov.in/allrelease.aspx?reg=3&lang=1','html'),('PIB 2025 ministry reviews','https://www.pib.gov.in/EventDetail.aspx?ID=1229&reg=3&lang=1','html'),('PRS 2025 policy reviews','https://prsindia.org/policy/monthly-policy-review?month=All&year=2025','html'),('PRS 2026 policy reviews','https://prsindia.org/policy/monthly-policy-review?month=All&year=2026','html'),('The Hindu national','https://www.thehindu.com/news/national/feeder/default.rss','rss'),('The Hindu Andhra Pradesh','https://www.thehindu.com/news/national/andhra-pradesh/feeder/default.rss','rss'),('Indian Express India','https://indianexpress.com/section/india/feed/','rss'),('ISRO news','https://www.isro.gov.in/Updates.html','html')]
CURRENT_YEAR=datetime.datetime.now(datetime.timezone.utc).year
if CURRENT_YEAR>2026:
 SITES.append((f'PRS {CURRENT_YEAR} policy reviews',f'https://prsindia.org/policy/monthly-policy-review?month=All&year={CURRENT_YEAR}','html'))
def canonical(url):
 p=urllib.parse.urlsplit(url)
 if p.scheme not in ('http','https') or not p.hostname: raise ValueError('Non-web source URL rejected')
 q=urllib.parse.parse_qsl(p.query)
 # PIB language/render variants of the same release share one identity.
 prid=next((v for k,v in q if k.lower()=='prid'),None)
 if prid and p.hostname and (p.hostname=='pib.gov.in' or p.hostname.endswith('.pib.gov.in')): return 'https://www.pib.gov.in/PressReleasePage.aspx?PRID='+prid+'&reg=3&lang=1'
 return urllib.parse.urlunsplit((p.scheme,p.netloc,p.path,urllib.parse.urlencode([(k,v) for k,v in q if not k.startswith('utm_')]),''))
def collect(spec):
 name,url,kind=spec; entries=[]; log={'source':name,'url':url,'time':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  base=urllib.parse.urlsplit(url); robots=urllib.robotparser.RobotFileParser()
  rr=requests.get(f'{base.scheme}://{base.netloc}/robots.txt',timeout=15)
  if rr.status_code==200:
   robots.parse(rr.text.splitlines())
   if not robots.can_fetch('CivilsAtlasResearchBot',url): raise RuntimeError('robots.txt disallows collection; manual review required')
  elif rr.status_code not in (404,410): raise RuntimeError(f'robots unavailable ({rr.status_code}); conservative manual fallback')
  res=requests.get(url,timeout=25,headers={'User-Agent':'CivilsAtlasResearchBot/1.0 (personal exam study; source links retained)'})
  res.raise_for_status(); soup=BeautifulSoup(res.content,'xml' if kind=='rss' else 'html.parser')
  if kind=='rss':
   for item in soup.find_all('item'):
    if item.link and item.title: entries.append({'title':item.title.get_text(' ',strip=True),'url':canonical(item.link.get_text(strip=True)),'published_raw':item.pubDate.get_text(strip=True) if item.pubDate else None})
  else:
   for a in soup.find_all('a',href=True):
    link=urllib.parse.urljoin(url,a['href']); title=a.get_text(' ',strip=True).replace('\u200b','')
    if len(title)<(3 if name.startswith('PRS') else 25): continue
    if name.startswith('PRS') and not re.fullmatch(r'[A-Za-z]+ 20\d{2}',title): continue
    if name.startswith('PIB') and not re.search(r'PRID=\d+',link,re.I): continue
    if name.startswith('PRS') and not re.search(r'monthly-policy-review/[a-z]+-20\d{2}',link): continue
    if name.startswith('ISRO') and ('isro.gov.in' not in link or not link.endswith('.html')): continue
    entries.append({'title':title,'url':canonical(link),'published_raw':None})
  log.update(status='ok' if entries else 'empty_requires_check',discovered=len(entries))
 except Exception as e: log.update(status='failed',error=str(e))
 return entries,log
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--limit-sources',type=int,default=99);args=parser.parse_args()
 path=R/'data/inbox.json'; inbox=json.loads(path.read_text()) if path.exists() else []; known={x['url'] for x in inbox};logs=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  jobs={pool.submit(collect,s):s for s in SITES[:args.limit_sources]}
  for job in concurrent.futures.as_completed(jobs):
   spec=jobs[job];items,log=job.result();logs.append(log)
   for x in items:
    if x['url'] in known: continue
    known.add(x['url']);x.update(id=hashlib.sha256(x['url'].encode()).hexdigest()[:16],source=spec[0],discovered_at=log['time'],status='unreviewed',publication_date_verified=False,subject=None,block=None)
    inbox.append(x)
 logs.sort(key=lambda x:x['source'])
 def save(name,value):
  dest=R/'data'/name; tmp=dest.with_suffix(dest.suffix+'.tmp');tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n');tmp.replace(dest)
 save('inbox.json',inbox);save('update-log.json',logs)
 now=datetime.datetime.now(datetime.timezone.utc).isoformat()
 hp=R/'data/update-history.json';history=json.loads(hp.read_text()) if hp.exists() else []
 event=os.getenv('GITHUB_EVENT_NAME','local-test');repo=os.getenv('GITHUB_REPOSITORY')
 entry=dict(time=now,event=event,repository=repo,source_count=len(logs),sources_ok=sum(x['status']=='ok'for x in logs),inbox_total=len(inbox),outcome='ok'if all(x['status']=='ok'for x in logs)else 'partial_failure',sources=logs)
 history.append(entry);save('update-history.json',history[-365:])
 sp=R/'data/automation-status.json';state=json.loads(sp.read_text()) if sp.exists() else {}
 scheduled=event=='schedule' and os.getenv('GITHUB_ACTIONS')=='true'
 state.update(schedule_utc='0 1 * * *',schedule_ist='06:30 Asia/Kolkata',last_run=now,last_run_environment='github-actions'if os.getenv('GITHUB_ACTIONS')=='true'else 'local-test',last_event=event,repository=repo or state.get('repository'),latest_collection_outcome=entry['outcome'],sources_ok=entry['sources_ok'],sources_tested=len(logs),mode='Source-link discovery only; reviewed notes require editorial work',not_freshness_guarantee=True)
 if scheduled:state.update(scheduler_active=True,last_observed_scheduled_run=now,deployment_status='Scheduled GitHub run observed; inspect source failures separately')
 elif not state.get('last_observed_scheduled_run'):state.update(scheduler_active=False,deployment_status='Manual GitHub run observed; awaiting first scheduled run'if repo else 'Configured and locally tested; repository deployment pending')
 save('automation-status.json',state)
 print(json.dumps({'inbox_total':len(inbox),'sources':logs},indent=2))
 # A partial failure is surfaced in the UI and workflow rather than silently ignored.
 if any(x['status']!='ok' for x in logs): raise SystemExit(2)
