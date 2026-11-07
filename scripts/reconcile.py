"""Refresh counts only. Preserve manually recorded evidence depth and open-audit status."""
import json,pathlib,csv,datetime,calendar,collections
R=pathlib.Path(__file__).resolve().parents[1]
N=json.loads((R/'data/notes.json').read_text());M=json.loads((R/'Package-Manifest.json').read_text());cutoff=datetime.date.fromisoformat(M['date'])
expanded=set()
for p in (R/'data').glob('*-mcqs.json'):
 stem=p.stem.replace('-mcqs','')
 if len(stem)==7 and stem[4]=='-':expanded.add(stem)
 else:
  try:expanded.add('2025-'+datetime.datetime.strptime(stem,'%B').strftime('%m'))
  except ValueError:pass
months=[];d=datetime.date(2025,1,1)
while d<=cutoff:
 months.append(d.strftime('%Y-%m'));d=datetime.date(d.year+int(d.month==12),d.month%12+1,1)
subjects=['Polity & Governance','Economy','Agriculture','Society & Welfare','Environment','Science & Technology','Security','International Relations','Andhra Pradesh','Culture & History','Awards & Sports']
def read(p):
 with (R/p).open(newline='')as f:r=csv.DictReader(f);return r.fieldnames,list(r)
def write(p,fields,rows):
 dest=R/p;tmp=dest.with_suffix('.csv.tmp')
 with tmp.open('w',newline='')as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
 tmp.replace(dest)
p='data/coverage-ledger.csv';fields,rows=read(p);by={(r['Month'],r['Subject']):r for r in rows};out=[]
for m in months:
 for s in subjects:
  row=by.get((m,s),dict.fromkeys(fields,'Pending'));c=sum(n['date'].startswith(m)and n['subject']==s for n in N)
  row.update(Month=m,Subject=s);row['Indexed notes']=c
  if row['Status']=='Pending'and c:row['Status']='Expanded / incomplete'if m in expanded else 'Partial'
  out.append(row)
write(p,fields,out)
p='data/daily-ledger.csv';fields,rows=read(p);by={r['Date']:r for r in rows};out=[];d=datetime.date(2025,1,1)
while d<=cutoff:
 key=str(d);row=by.get(key,dict.fromkeys(fields,'No'));c=sum(n['date']==key and n.get('date_precision','day')=='day'for n in N)
 row['Date']=key;row['Day-precision indexed notes']=c
 if row.get('Status')in ('No','Daily audit pending','Partial research / daily audit pending'):row['Status']='Partial research / daily audit pending'if c else 'Daily audit pending'
 out.append(row);d+=datetime.timedelta(days=1)
write(p,fields,out)
p='research/remaining-period-inventory.csv';fields,rows=read(p)
for row in rows:
 label=row['Period'].split(' (')[0]
 try:m=datetime.datetime.strptime(label,'%B %Y').strftime('%Y-%m')
 except ValueError:continue
 row['Notes already indexed']=sum(n['date'].startswith(m)for n in N)
write(p,fields,rows)
print(f'Updated counts for {len(months)} periods through {cutoff}; preserved source-reading and audit disclosures. No audit automatically closed.')
