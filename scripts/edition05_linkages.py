import json,pathlib,csv,collections
R=pathlib.Path(__file__).resolve().parents[1];N=json.loads((R/'data/notes.json').read_text());by={n['id']:n for n in N};S=json.loads((R/'data/sources.json').read_text())
rows=[
('Monetary decisions across the cycle','Rate, stance and transmission','FEB25-001 APR25-003 E5-2506-001 E5-2508-001 E5-2508-006','Distinguish a decision, its stance and a consultation about the framework. August rates remain a historical snapshot.','Why can easing and a neutral stance coexist?'),
('Income-tax legislative journey','Introduction → scrutiny → replacement/passage','FEB25-004 E5-2507-002 E5-2508-003','Do not backdate August passage to February; passage and the stated April 2026 commencement differ. Later legal changes need a fresh check.','How does scrutiny improve simplification without expanding intrusive powers unchecked?'),
('Census and representation','Cabinet decision → announced exercise','APR25-006 E5-2506-003 E5-2508-010','Caste enumeration, reference dates and Goa’s state-specific representation measure are distinct issues—not one completed nationwide delimitation.','What safeguards connect credible statistics with fair representation?'),
('Trade agreements and external shocks','Negotiation conclusion → signature → exposure','MY25-002 CA-033 E5-2508-021 E5-2508-031','EAEU negotiating terms are not the UK agreement; tariff headlines are product/date dependent. This is a comparative trade-policy path, not one treaty.','What converts diplomatic market access into resilient exports?'),
('Quantum capability and responsible claims','Deep tech → planned project → institutional approval','VM2504-004 MY25-020 E5-2507-026 E5-2507-020 E5-2507-032','The July nodes have different roles: institution, financing and cyber preparedness. None proves a fault-tolerant computer was commissioned.','How should AP evaluate quantum investment by validated capability?'),
('Cooperatives: principles, policy and credit','International theme → national policy → finance','VM2501-001 E5-2507-013 E5-2507-014','A policy does not amend every state law; a grant to NCDC is not a grant to every cooperative borrower.','How can modernisation reinforce member control?'),
('Critical-mineral value chains','Mission → notification → operating rights → amendment','CA-013 JAN25-037 E5-2506-010 E5-2507-041 E5-2508-015','The operating-rights and MMDR nodes concern different legal domains; discovery, extraction permission and refining capability are separate.','How can resource policy build supply resilience with ecological safeguards?'),
('Local government and operational devolution','Devolution evidence → finance → district follow-through','VM2502-002 E5-2507-030 E5-2508-044 E5-2508-045','DISHA monitoring is not a substitute for Panchayat power. Gram Urja Swaraj in this snapshot is a committee recommendation, not a universal launched entitlement.','What makes functions, funds and functionaries work together?'),
('AP transfers and women’s capabilities','Education → farm liquidity → mobility','E5-2506-018 E5-2508-029 E5-2508-030','These are separate schemes with different beneficiaries and fiscal arrangements. Gross/net transfers and Centre/state shares are not interchangeable.','How should AP assess inclusion, reliable delivery and capability outcomes?'),
('Maritime reform and coastal preparedness','Pollution event → commercial documents → shipping/ports law','E5-2506-028 E5-2507-022 E5-2508-016 E5-2508-017 E5-2508-018','Carriage documentation, vessel registration, coastal trading and port governance regulate different links. Passage does not prove implementation.','What complements legal reform in AP’s port-led development?'),
('Clean energy: different instruments','Taxonomy → contracts → storage → mobility','MY25-009 MY25-016 E5-2506-013 E5-2507-024 E5-2508-014 E5-2508-027','Classification, a draft financial contract, power-market rules and vehicle incentives are not one subsidy. Check segment-specific E-DRIVE dates.','How can credible rules reduce greenwashing and delivery risk?'),
('Learning, jobs and research ecosystems','Formal hiring → skills → technical education','E5-2507-009 E5-2507-010 E5-2508-028 E5-2507-020','Read the final RDI node as a thematic complement, not later chronology. A credential, payroll record and durable job are different outcomes.','How can education and innovation spending create additional productive work?'),
('Data power and responsible AI','Surveillance critique → dependency → financial safeguards','E5-2502-001 E5-2507-029 E5-2507-021 E5-2508-007 E5-2508-012','Conceptual critiques and committee reports are not statutory offences or automatically binding rules. Protect both security and remedies.','How can digital systems make consequential decisions contestable?'),
('Student safety and institutional ethics','Anti-ragging → wellbeing','E5-2502-002 E5-2507-034','Prevent harassment, protect reporting and seek qualified support; do not reduce individual distress to one cause or stigmatise help-seeking.','What does an accountable duty of care require beyond counselling?'),
('Space and evidence-led resilience','Launch → return; radar → weather and risk','E5-2506-025 E5-2507-028 E5-2507-027 E5-2506-026 E5-2508-033','This combines a two-date mission sequence with thematic applications. Radar, numerical forecasts and human spaceflight are different capabilities.','How can scientific milestone reporting avoid exaggerated readiness claims?'),
('Sport: policy, governance and fair adjudication','July introduction → August passage','E5-2507-019 E5-2507-017 E5-2508-023 E5-2507-018 E5-2508-025','Two separate Bill pathways sit beside one policy; appointment, commencement and operational independence still need checks.','How can sports institutions reconcile autonomy and athlete rights?'),
('Farm systems and sustainable livelihoods','District convergence → processing → Evergreen Revolution','E5-2507-015 E5-2507-016 E5-2508-032 E5-2508-041','A committee’s fishing-support proposal is not an implemented entitlement; convergence should include ecology and livelihood distribution.','How can agriculture policy improve resource productivity and farmer/fisher resilience?'),
('Three types of social protection','Retirement savings → life risk → accident risk','E5-2505-001 E5-2505-002 E5-2505-003 E5-2508-004','These are comparative products, not stages of one scheme. APY contributions, PMJJBY/PMSBY cover and UPS tax treatment have different eligibility.','How should social-protection literacy distinguish contributions, cover, claims and benefits?'),
]
J=[]
for i,(title,mechanism,ids,caution,prompt) in enumerate(rows,1):
 ids=ids.split();assert all(k in by for k in ids),(title,ids)
 J.append(dict(id=f'PATH-{i:02}',title=title,mechanism=mechanism,notes=ids,caution=caution,prompt=prompt))
for n in N:
 n['journeys']=[j['id'] for j in J if n['id'] in j['notes']]
 n['related_notes']=list(dict.fromkeys(k for j in J if n['id'] in j['notes'] for k in j['notes'] if k!=n['id']))
(R/'data/notes.json').write_text(json.dumps(N,ensure_ascii=False,indent=2));(R/'data/linkages.json').write_text(json.dumps(J,ensure_ascii=False,indent=2))
lines=['# Civils Atlas · Cross-month reading journeys','', '18 curated thematic paths. Arrows show an editorial reading order; some paths compare distinct policies rather than one legal timeline. Every node points to an actual study note. Current status must be separately verified.','']
for j in J:
 lines+=['## '+j['id']+' · '+j['title'],j['mechanism'],'']
 for k in j['notes']:n=by[k];lines+=['- **'+k+'** · '+n['date'][:7]+' · '+n['title']]
 lines+=['','**Avoid this shortcut:** '+j['caution'],'','**Mains synthesis:** '+j['prompt'],'']
(R/'volumes/Cross-Month-Reading-Journeys.md').write_text('\n'.join(lines))
D=json.loads((R/'research/magazine-review/vision-inventory.json').read_text());t=[]
for m,d in sorted(D.items()):
 for a in d['articles']:
  linked=[n['id'] for n in N if any(S[k][1]==a['url'] for k in n['sources'])]
  a['linked_notes']=linked;a['reconciliation']='Selected passages used; full-topic/primary audit open' if linked else 'Not incorporated; substantive reconciliation pending'
  if linked:a['review']='Selected passages incorporated into original notes; not complete article/issue review'
  t.append([m,d['web_posting_date'],a['title'],a['url'],a.get('retrieval','Not recorded'),a.get('words',''),a['reconciliation'],'; '.join(linked)])
(R/'research/magazine-review/vision-inventory.json').write_text(json.dumps(D,ensure_ascii=False,indent=2))
with (R/'research/magazine-review/vision-reconciliation.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Coverage month','Web posting date','Title','Official URL','Retrieval status','Retrieved words','Editorial reconciliation','Linked notes']);w.writerows(t)
print('Curated',len(J),'journeys;',sum(bool(n['journeys']) for n in N),'notes linked; magazine',sum(bool(x[-1]) for x in t),'/',len(t),'URLs linked')
