import json,pathlib,csv,datetime,calendar,collections
R=pathlib.Path(__file__).resolve().parents[1];N=json.loads((R/'data/notes.json').read_text());S=json.loads((R/'data/sources.json').read_text())
# Evidence provenance is explicit. Most search-result extracts were not whole-page reviews.
full={'J-PRS','J-LEADS','J-AWARDS'};meta={}
for k,(t,u) in S.items():
 access='Full substantive text read' if k in full else ('Search-result source extract inspected; full page/document review pending' if k.startswith('J-') else 'Source check recorded in first edition; full-text access provenance not retained')
 meta[k]={'title':t,'url':u,'access':access,'checked_on':'2026-11-06','method':'Human-directed web research; no automated factual certification'}
for n in N:
 if n['id'].startswith('JAN25-'):
  n['evidence_access']='Full PRS monthly synthesis read; linked primary references may remain unopened' if 'J-PRS' in n['sources'] else ('Full substantive PIB text read' if any(k in full for k in n['sources']) else 'Source extract(s) inspected; full-document review pending')
for n in N:
 if n['id']=='CA-013':n.update(why='Cabinet approved a seven-year critical-mineral mission on 29 January.',static_link='Resource security concerns the entire chain from exploration to processing and recycling, not merely owning a mineral deposit.',analysis=['Processing technology and concentrated supply chains can remain bottlenecks even when domestic reserves exist.','Diversified imports, domestic processing, recycling and environmental safeguards should reinforce one another.'])
 if n['id']=='CA-014':n.update(why='ISRO demonstrated satellite docking on 16 January after a December 2024 launch.',static_link='Rendezvous approaches two spacecraft; docking creates a controlled mechanical connection. This enables multi-launch architectures.',analysis=['Docking is an enabling technology for orbital infrastructure and future multi-module missions.','A demonstration is an important step, not proof that every human-spaceflight or lunar mission has already been accomplished.'])
 if n['id']=='CA-023':n.update(why='Indore and Udaipur received India’s first Wetland City Accreditations in January.',static_link='Accreditation recognises urban wetland stewardship; it differs from listing an individual wetland as internationally important.',analysis=['Urban wetlands can reduce flooding and support water quality when catchments and inflows are protected.','Recognition must translate into land-use enforcement, sewage control and local stewardship.'])
 if n['id']=='CA-025':n.update(why='The IBCA framework entered into force on 23 January.',static_link='Big-cat cooperation links species knowledge with habitat, prey and landscape protection.',analysis=['Cross-country research and finance can strengthen conservation, but local land-use and human-wildlife conflict still determine outcomes.','Membership interest, ratification and operational programmes should be tracked separately.'])
 if n['id']=='CA-029':n.update(why='The 18 January distribution event highlighted rural residential-property records.',static_link='A cadastral record can support certainty and transactions but does not by itself resolve every competing legal claim.',analysis=['Property mapping may help formal credit and local planning where institutions recognise and maintain the record.','Participatory objections, protection of vulnerable residents and affordable correction are essential.'])
 n.setdefault('evidence_access','First-edition source check; independent full-text provenance not retained')
(R/'data/notes.json').write_text(json.dumps(N,ensure_ascii=False,indent=2));(R/'data/source-access.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
months=[]
for y in [2025,2026]:
 for m in range(1,13):
  k=f'{y}-{m:02}'
  if k<='2026-11':months.append(k)
subjects=list(dict.fromkeys(n['subject'] for n in N))
with (R/'data/coverage-ledger.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Month','Subject','Indexed notes','Status','PRS monthly synthesis','PIB daily reconciliation','Newspaper 1 daily reconciliation','Newspaper 2 daily reconciliation','AP/specialist reconciliation','Exclusions reconciled','Comments'])
 for m in months:
  for s in subjects:
   c=sum(n['subject']==s and n['date'].startswith(m) for n in N)
   w.writerow([m,s,c,'Expanded / incomplete' if m=='2025-01' and c else ('Partial' if c else 'Pending'),'Read in full' if m=='2025-01' else 'Pending','Pending','Pending','Pending','Partial' if m=='2025-01' else 'Pending','Pending','Counts are not coverage percentages; source extracts and full text distinguished.'])
with (R/'data/daily-ledger.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Date','Day-precision indexed notes','PIB reconciled','Newspaper streams reconciled','AP sources reconciled','Status'])
 d=datetime.date(2025,1,1)
 while d<=datetime.date(2026,11,6):
  c=sum(n['date']==str(d) and n.get('date_precision','day')=='day' for n in N)
  w.writerow([str(d),c,'No','No','No','Partial research / daily audit pending' if c else 'Daily audit pending']);d+=datetime.timedelta(days=1)
with (R/'research/remaining-period-inventory.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Period','Notes already indexed','Editorial status','PRS task','PIB task','Newspaper task','Andhra Pradesh task','Specialist task','Close-out condition'])
 for m in months[1:]:
  date=datetime.date.fromisoformat(m+'-01');monthname=date.strftime('%B %Y');end='6 November 2026' if m=='2026-11' else str(calendar.monthrange(date.year,date.month)[1])
  w.writerow([monthname+(' (1–6 only)' if m=='2026-11' else ''),sum(n['date'].startswith(m) for n in N),'Backfill not completed','Locate/read '+monthname+' review; follow primary citations','Reconcile dated ministry releases; separate routine duplicates','Reconcile national + independent + AP reporting, day by day','Read dated GOs, cabinet decisions, fiscal/irrigation/capital records','RBI/MoSPI/MEA/courts/Gazette/ISRO/UN/reports/culture/sport','No completion until daily sources, exclusions and failures are resolved'])
print('Source access',len(meta),'coverage cells',len(months)*len(subjects),'remaining monthly work packages',len(months)-1)
