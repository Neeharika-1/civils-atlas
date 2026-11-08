"""Collect public compilation metadata, never silently replace primary-source evidence."""
import concurrent.futures,datetime,hashlib,json,re
import update as u

def run():
 specs=u.read('compilation-registry.json',[])
 inbox=u.read('inbox.json',[]);known={x['url']:x for x in inbox};logs=[];added=0
 with concurrent.futures.ThreadPoolExecutor(max_workers=5)as pool:
  for spec,(items,log)in zip(specs,pool.map(u.collect,specs)):
   if spec['format']=='rss':items=[i for i in items if re.search(r'current-affairs|pib|editorial|magazine|compilation',i['url'],re.I)]
   log.update(secondary_source=True,coverage_note=spec.get('coverage_note',''),discovered=len(items))
   if not items and log['status']=='ok':log.update(status='review_required',error='No matching compilation entries; not proof of no coverage.')
   logs.append(log)
   for item in items:
    if item['url']in known:
     row=known[item['url']];row['discovered_by']=sorted(set(row.get('discovered_by',[row.get('source','')])+[spec['name']]));row['last_seen_at']=log['time'];continue
    item.update(id=hashlib.sha256(item['url'].encode()).hexdigest()[:16],source=spec['name'],source_id=spec['id'],discovered_by=[spec['name']],discovered_at=log['time'],last_seen_at=log['time'],status='unreviewed',secondary_source=True,publication_date_verified=False,subject=None,block=None)
    inbox.append(item);known[item['url']]=item;added+=1
 now=datetime.datetime.now(datetime.timezone.utc).isoformat();result=dict(updated_at=now,tested=len(specs),working=sum(l['status']=='ok'for l in logs),new_links=added,scope='Compilation metadata only; publisher text is not copied, and original source utilisation/facts are not verified.',results=logs)
 u.save('inbox.json',inbox);u.save('compilation-health.json',result)
 lines=['# Compilation reading desk',now,'Secondary sources. Collection dates are not article publication dates; links are not verified study notes.','']
 for spec in specs:
  lines+=['## '+spec['name'],spec.get('coverage_note',''),spec['url'],'']
  lines+=['- ['+i['title'].replace('[','').replace(']','')+']('+i['url']+')'for i in inbox if i.get('source_id')==spec['id']][-40:]
 (u.R/'research/Compilation-Reading-Desk.md').write_text('\n'.join(lines)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':run()
