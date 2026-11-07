"""Permitted discovery, explicit access gaps, retained source obligations. Never authors verified notes."""
import argparse,concurrent.futures,datetime,functools,hashlib,json,os,pathlib,re,urllib.parse,urllib.robotparser
import requests
from bs4 import BeautifulSoup
R=pathlib.Path(__file__).resolve().parents[1]
UA='CivilsAtlasResearchBot/2.0 (personal exam research; source links retained)'
def read(name,default):
 p=R/'data'/name
 return json.loads(p.read_text()) if p.exists() else default
def save(name,value):
 p=R/'data'/name;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n');t.replace(p)
def canonical(url):
 p=urllib.parse.urlsplit(url)
 if p.scheme not in ('http','https') or not p.hostname or p.username or p.password:raise ValueError('Invalid source link')
 if p.hostname in ('localhost','127.0.0.1','::1'):raise ValueError('Local source link rejected')
 q=urllib.parse.parse_qsl(p.query);prid=next((v for k,v in q if k.lower()=='prid'),None)
 if prid and (p.hostname=='pib.gov.in' or p.hostname.endswith('.pib.gov.in')):
  if not prid.isdigit():raise ValueError('Invalid PIB ID')
  return 'https://www.pib.gov.in/PressReleasePage.aspx?PRID='+prid+'&reg=3&lang=1'
 return urllib.parse.urlunsplit((p.scheme,p.netloc,p.path,urllib.parse.urlencode([(k,v)for k,v in q if not k.lower().startswith('utm_')]),''))
@functools.lru_cache(maxsize=64)
def robot_policy(origin):
 rr=requests.get(origin+'/robots.txt',timeout=(8,15),headers={'User-Agent':UA})
 if rr.status_code in (404,410):return None
 if rr.status_code!=200:raise RuntimeError(f'robots unavailable ({rr.status_code}); manual review required')
 rp=urllib.robotparser.RobotFileParser();rp.parse(rr.text.splitlines());return rp

def collect(spec):
 now=datetime.datetime.now(datetime.timezone.utc).isoformat()
 log=dict(source=spec['name'],source_id=spec['id'],category=spec['category'],url=spec['url'],time=now,status='failed',discovered=0,attempts=[],source_read=False)
 routes=[{'url':spec['url'],'format':spec['format']}]+spec.get('fallbacks',[])
 for route in routes:
  url=route['url'];kind=route['format'];attempt=dict(url=url,format=kind)
  try:
   p=urllib.parse.urlsplit(canonical(url));origin=p.scheme+'://'+p.netloc
   policy=robot_policy(origin)
   if policy is not None and not policy.can_fetch(UA,url):raise RuntimeError('robots.txt disallows collection; manual review required')
   target=url
   for redirect in range(5):
    part=urllib.parse.urlsplit(canonical(target))
    targetpolicy=robot_policy(part.scheme+'://'+part.netloc)
    if targetpolicy is not None and not targetpolicy.can_fetch(UA,target):raise RuntimeError('Redirect target disallows collection')
    res=requests.get(target,timeout=(8,25),headers={'User-Agent':UA},allow_redirects=False)
    if res.status_code in (301,302,303,307,308):
     if not res.headers.get('Location'):raise RuntimeError('Redirect without Location')
     target=canonical(urllib.parse.urljoin(target,res.headers['Location']));continue
    res.raise_for_status();break
   else:raise RuntimeError('Too many redirects')
   if kind=='portal':
    attempt.update(status='review_required',http_status=res.status_code)
    log['attempts'].append(attempt);log.update(status='review_required',error='Interactive primary-document portal: open and review; an HTTP response is not document utilisation.')
    return [],log
   soup=BeautifulSoup(res.content,'xml' if kind=='rss' else 'html.parser');entries=[];seen=set()
   if kind=='rss':
    candidates=[]
    for item in soup.find_all('item'):
     if item.link and item.title:candidates.append((item.title.get_text(' ',strip=True),item.link.get_text(strip=True),item.pubDate.get_text(strip=True)if item.pubDate else None))
   else:
    candidates=[]
    for a in soup.find_all('a',href=True):
     link=urllib.parse.urljoin(res.url,a['href']);pattern=spec.get('link_pattern')
     if pattern and not re.search(pattern,link,re.I):continue
     # Prevent collecting ISRO navigation links to unrelated hosts.
     if spec['id']=='isro' and urllib.parse.urlsplit(link).hostname not in ('www.isro.gov.in','isro.gov.in'):continue
     title=a.get_text(' ',strip=True).replace('\u200b','')
     if len(title)<8:
      if title.lower()=='read':title='Magazine/source entry: '+urllib.parse.unquote(urllib.parse.urlsplit(link).path.rsplit('/',1)[-1]).replace('-',' ')
      else:continue
     candidates.append((title,link,None))
   for title,link,published in candidates:
    try:link=canonical(urllib.parse.urljoin(res.url,link))
    except ValueError:continue
    if link in seen or link==canonical(url):continue
    seen.add(link)
    # The publisher specifies personal RSS use. Do not publicly republish its article text or feed headlines.
    if spec.get('publishing')=='link-only':title=spec['name']+' · source link (open publisher)'
    entries.append(dict(title=title[:400],url=link,published_raw=published))
   attempt.update(status='ok'if entries else 'review_required',http_status=res.status_code,discovered=len(entries));log['attempts'].append(attempt)
   if entries:
    log.update(status='ok',discovered=len(entries),route_used=url,fallback_used=url!=spec['url']);return entries,log
   log.update(status='review_required',error='No matching items extracted. Manual check required; not evidence of no news.')
  except Exception as e:
   attempt.update(status='failed',error=str(e));log['attempts'].append(attempt);log['error']=str(e)
 return [],log

def run(limit=99):
 registry=read('source-registry.json',[])
 if not registry:raise RuntimeError('Required source registry is missing')
 year=datetime.datetime.now(datetime.timezone.utc).year
 if year>2026:
  for spec in registry:
   if spec['id']=='prs-current':spec.update(name=f'PRS {year} policy reviews',url=f'https://prsindia.org/policy/monthly-policy-review?month=All&year={year}',link_pattern=f'monthly-policy-review/[a-z]+-{year}')
 inbox=read('inbox.json',[]);known={x['url']:x for x in inbox};logs=[];fresh=0
 with concurrent.futures.ThreadPoolExecutor(max_workers=6)as pool:
  for items,log in pool.map(collect,registry[:limit]):
   logs.append(log)
   for item in items:
    if item['url']in known:
     row=known[item['url']];row['discovered_by']=sorted(set(row.get('discovered_by',[row.get('source','')])+[log['source']]))
     row['last_seen_at']=log['time'];continue
    item.update(id=hashlib.sha256(item['url'].encode()).hexdigest()[:16],source=log['source'],source_id=log['source_id'],discovered_by=[log['source']],discovered_at=log['time'],last_seen_at=log['time'],status='unreviewed',publication_date_verified=False,subject=None,block=None)
    inbox.append(item);known[item['url']]=item;fresh+=1
 logs.sort(key=lambda x:x['source']);now=datetime.datetime.now(datetime.timezone.utc).isoformat()
 ok=sum(x['status']=='ok'for x in logs);outcome='ok'if len(logs)==len(registry)and ok==len(logs)else'partial_failure'
 save('inbox.json',inbox);save('update-log.json',logs)
 event=os.getenv('GITHUB_EVENT_NAME','local-test');hosted=os.getenv('GITHUB_ACTIONS')=='true';repo=os.getenv('GITHUB_REPOSITORY')
 entry=dict(time=now,event=event,repository=repo,source_count=len(logs),sources_ok=ok,inbox_total=len(inbox),new_links=fresh,outcome=outcome,sources=logs)
 history=read('update-history.json',[]);history.append(entry);save('update-history.json',history[-365:])
 state=read('automation-status.json',{})
 state.update(schedule_utc='0 1 * * *',schedule_ist='06:30 Asia/Kolkata',last_run=now,last_run_environment='github-actions'if hosted else'local-test',last_event=event,repository=repo or state.get('repository'),latest_collection_outcome=outcome,sources_ok=ok,sources_tested=len(logs),sources_required=len(registry),new_links=fresh,mode='Source-link discovery only; reviewed notes require editorial work',not_freshness_guarantee=True)
 if event=='schedule'and hosted:state.update(scheduler_active=True,last_observed_scheduled_run=now,deployment_status='Scheduled GitHub run observed; source coverage remains a separate check')
 elif not state.get('last_observed_scheduled_run'):state.update(scheduler_active=False,deployment_status='Hosted '+event+' run observed; first scheduled run still pending'if hosted else'Local test; hosted activation must be checked separately')
 save('automation-status.json',state)
 sources=read('sources.json',{});notes=read('notes.json',[])
 def host(u):return (urllib.parse.urlsplit(u).hostname or '').removeprefix('www.')
 coverage=[];byid={x['source_id']:x for x in logs}
 for spec in registry:
  h=host(spec['url']);matching={k for k,v in sources.items()if host(v[1])==h}
  coverage.append(dict(source_id=spec['id'],name=spec['name'],category=spec['category'],required=True,status=byid.get(spec['id'],{}).get('status','not_checked'),archive_notes_referencing_domain=sum(bool(set(n['sources'])&matching)for n in notes),today_utilisation_verified=False))
 save('source-coverage.json',dict(updated_at=now,fully_utilised=False,scope='Endpoint access is not article reading. Archive domain references are historical, not proof of daily utilisation.',sources=coverage))
 print(json.dumps(dict(required=len(registry),tested=len(logs),working=ok,new_links=fresh,inbox_total=len(inbox),outcome=outcome,sources=logs),indent=2))
 return 0 if outcome=='ok'else 2
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--limit-sources',type=int,default=99);args=p.parse_args();raise SystemExit(run(args.limit_sources))
