import json,pathlib,collections,datetime
R=pathlib.Path(__file__).resolve().parents[1];N=json.loads((R/'data/notes.json').read_text());D=json.loads((R/'research/magazine-review/vision-inventory.json').read_text());S=json.loads((R/'data/sources.json').read_text());L=json.loads((R/'data/update-log.json').read_text())
counts=collections.Counter(n['date'][:7] for n in N)
table='| Expanded month | Notes | Original MCQs | Mains frameworks |\n|---|---:|---:|---:|\n'+'\n'.join('| '+datetime.date.fromisoformat(m+'-01').strftime('%B %Y')+f' | {counts[m]} | 30 | 8 |' for m in sorted(D))
start=f'''# Civils Atlas · Edition 05
UPSC + Andhra Pradesh APPSC · English · Edition updated: **7 November 2026**

## Open the library
Open **index.html**. It now starts at June 2025, the beginning of the new expansion. Quick buttons open June, July and August. The month filter reaches all notes; **Monthly practice** has a separate month selector and document links.

{table}

Each of the eight expanded volumes has PDF, editable DOCX and Markdown versions in **volumes/**, including 30 questions, explanations and 8 original Mains frameworks. **Study-Notes.docx** holds all **462 notes**: 444 in January–August and 18 later seeds. **317 source-reference entries**, not 317 fully reviewed primary texts. Total: **240 original MCQs / 64 frameworks**.

## What changed in this continuation
- **130 new notes**: 12 earlier gap repairs, 31 June, 42 July and 45 August. Two inherited July notes were enriched, not counted as new; the duplicate CETA event was merged into its original ID.
- **18 cross-month reading journeys** connect 74 notes. Open **Linked reading paths** in the app, or **Cross-Month-Reading-Journeys.pdf / .docx / .md** in volumes. Connections are editorial guidance, not proof that different schemes are one programme.
- New breadth includes legislation, digital governance, cooperative finance, research/jobs/skills, climate/energy, maritime reform, student wellbeing, culture and sports. AP notes include education transfers, quantum institutions, irrigation appraisal, mobility and farm support.
- The all-six-page mirrored Talliki Vandanam GO reading qualifies the simple gross-minus-deduction headline: category-specific adjustments exist. Its unofficial host is explicitly recorded.
- Official public Vision IAS articles guide gap discovery and thematic links alongside PRS, primary and newspaper/regional research. No full magazines are redistributed. Coverage month, posting date and event chronology remain distinct.

## Still unfinished—do not mistake this for full coverage
No month has passed daily PIB/two-paper/AP reconciliation. **September 2025–7 November 2026 spans 15 periods still requiring substantial chronological backfill.** January–August also retain shorts/maps, primary verification, P3 and district-level gaps. The 18 later seeds do not substitute for those months. See **research/Research-Status.md** and the coverage ledgers.

## Daily updating
The collector was retested on 7 November. PRS discovery was repaired using year/month filters; the two Hindu feeds and ISRO also responded. PIB automated endpoints still returned 403; the Indian Express robots check returned 403, so collection was not attempted there. Failures are visible in the app and logs.

**The 06:30 IST workflow is supplied, not activated on a durable host.** An enabled hosting repository or always-on machine is still needed; none was supplied or configured here. It discovers unreviewed candidates, not verified daily notes. A browser/preview cannot keep researching after this snapshot.

## Rebuild safely
`pip install -r requirements.txt` then `python scripts/validate.py && python scripts/reconcile.py && python scripts/build.py`.

The delivered JSON is the source of truth. Historical authoring scripts are not automatic updaters; do not rerun them over edits. Edition 05 construction order, only if deliberately reconstructing: edition05.py → edition05_practice.py → edition05_linkages.py → edition05_corrections.py → edition05_practice_review.py. Do not confuse a successful build with factual or completeness certification.
'''
(R/'START-HERE.md').write_text(start)
report=f'''# Research status · Edition 05

**Edition updated / requested archive cut-off: 7 November 2026, India time. Requested scope: 1 January 2025 to this date. Full scope is NOT yet delivered.**

## Substantive progress
{table}

**462 notes / 317 source-reference entries / 240 original MCQs / 64 Mains frameworks.** January–August contain 444 notes; 18 later seeds remain. The continuation adds 130 original notes and enriches two July seeds. An enriched CETA seed replaces—not duplicates—the new draft of that event. Practice questions and frameworks are not previous-year papers, predictions or official exam-validated material.

The 18 curated reading journeys connect 74 notes across months and subject mechanisms. They explicitly distinguish comparative reading order from a legal/event timeline. Both app and documents retain related note IDs.

## Evidence actually inspected
- Prior edition: full PRS January–May monthly reviews, substantive Union/AP Budget analyses and selected PIB, AP, scientific and other primary/article bodies. Existing access provenance is retained, not upgraded by the new batch.
- June PRS chunks 0–4 and reference chunk 5; reference tail 6 not fully reviewed. July chunks 0–7 and August chunks 0–10 reach the start of references; their reference tails are not fully reviewed. These substantive syntheses do NOT establish independent reading of every linked primary document.
- Public Vision IAS selected leads/substantive passages in January–August, referenced in the reconciliation CSV. Automated retrieval of other articles is not substantive review. 101 of 382 inventory URLs link to 100 study notes; 281 URLs remain unincorporated. These are URLs, not an audited denominator of unique topics.
- Full substantive NASA Earthdata NISAR article; substantive portions of PIB Dhan Dhaanya and Ujjwala explainers; full TeamLease secondary August MPC account.
- **All six pages** of an APUTF-hosted copy of AP G.O.Ms.27, 12 June 2025. This is a mirrored government-order text, not an official-host/signature authentication. Full substantive PTI Stree Shakti launch/scope news bodies were read.
- Many remaining references were inspected only as search excerpts. Every new source entry distinguishes access scope; no access to a login-gated magazine PDF was bypassed.

## Unfinished acceptance criteria
1. **All 23 monthly audit packages remain open.** No complete PIB/two-paper/AP daily reconciliation; all 676 dates retain audit work.
2. **15 periods, September 2025–7 November 2026, need substantial chronological authoring.** Later seeds remain sparse. January–August are expanded selected batches, not exhaustive months.
3. Magazine shorts, maps, unincorporated long articles, exclusions and independent primary checks remain incomplete. Source retrieval counts are not reading/coverage percentages.
4. AP official-host GO authentication, budget annexures, district records, socio-economic surveys, irrigation permissions and state implementation checks need systematic work. National notes tagged AP-linked are not AP-specific evidence.
5. Books/authors, obituaries, appointments and additional awards/sports remain uneven. Culture/GS4 breadth was improved, not closed out.
6. Current-law monitoring is NOT implemented. Bills, passage, assent, commencement, rules, appointments and later court decisions are distinct. Historical dates and tariff/rate/report snapshots are not certified current at November 2026.
7. Exact APPSC notification/paper mapping remains uncertified. Priorities and static/Mains links are editorial learning guidance.
8. **Durable daily scheduling remains unactivated.** No user repository or always-on host was supplied. Workflow configuration and local tests do not mean a scheduled service is live.

## Collector test and repaired omission
On 7 November the collector was run, repaired and rerun. The bare PRS index defaulted to June 2012, and the minimum title-length filter discarded month labels. Explicit year/month filtering plus appropriate month-title matching now yields 12 references for 2025 and 10 for 2026. These are discovery candidates, not new authored notes.

Latest results: five successful source streams (two PRS yearly indexes, Hindu national/AP and ISRO), two PIB endpoints failed with HTTP 403, and Indian Express robots access returned 403 (conservative stop). The inbox holds 205 unreviewed candidates, not 205 additional notes. Exit status 2 correctly exposes partial failure. See data/update-log.json; no bypass was attempted.

## New corrections and restraint
| Risk | Editorial treatment |
|---|---|
| Talliki ₹15,000 treated as net for everyone | ₹2,000 general deduction; ₹13,000 before category-specific RTE/scholarship adjustments; expected/uncorrected records are not all-paid totals |
| Annadata fully attributed to one government | Annual ₹14,000 state + ₹6,000 Centre; first described combined instalment ₹5,000 + ₹2,000 |
| Stree Shakti called universal free travel | Domicile/identity, girls/women/transgender beneficiaries and five service categories; premium/interstate exclusions; reimbursements matter |
| 130th Bill called an enacted constitutional amendment | Introduced/referred in August snapshot; custody, conviction and membership disqualification differ |
| PRS August MSF shown as 5.25% | Corroborating resolution account supports 5.75%; do not copy SDF as the lending-corridor ceiling |
| Dhan Dhaanya ₹24,000 crore called six-year total | Official explainer specifies annual outlay over six years; targets are not achievements |
| RDI corpus treated as universal July grants | Corpus/commitment/disbursement and concessional loans/equity differentiated |
| E-DRIVE extension applied to every category | Segment-specific windows/exceptions retained |
| June Axiom issue implied July return occurred in June | Separate 25 June launch and 15 July return; do not retain incorrect planned-duration figure as actual stay |
| BharatFS June magazine confused adoption date | May adoption separated from June coverage and July answer |
| NISAR wavelength details conflict across NASA pages | No disputed numerical S-band wavelength retained; radar bands/repeat cycle and readiness distinctions retained |
| AI171 sequence treated as final causal attribution | Preliminary report not final cause/blame; systemic safety committee report is a separate source |
| Maratha forts counted as twelve UNESCO additions | One serial property; eleven Maharashtra components plus Gingee, Tamil Nadu |
| Sankaran Nair dramatisation confused O’Dwyer and Dyer | Distinguish civil libel defendant from massacre command; dubious superlatives excluded |
| Kakori martyr list treated as action participant list | Roshan Singh execution does not establish physical participation in the train action |
| Unverified WEF score / timeless changing totals | Score omitted; dated rank retained; historical totals/US tariffs not certified current |
| Short-news cache files shared a final URL slug | URL-hash filenames now distinguish subject pages; cached retrieval still not review |

Earlier edition corrections remain in historical reports. Do not rerun old destructive magazine inventory/enrichment scripts. The current delivered data is authoritative.

## Verification boundaries
Structural validators test identifiers, fields, dates, source links, question shapes, references and reading-path integrity. App tests check filters, navigation, bookmarks, practice and document paths. Export checks inspect text presence and OOXML packages. **These are not independent factual or completeness certification.**
'''
(R/'research/Research-Status.md').write_text(report)
rows=[]
for m,d in sorted(D.items()):rows.append('| '+m+' | '+d['web_posting_date']+' | '+str(len(d['articles']))+' | '+str(sum(bool(a.get('linked_notes')) for a in d['articles']))+' |')
mag='''# Official Vision IAS integration · Edition 05

Updated 7 November 2026. Original English summaries and analytical study guidance; not magazine reproductions. Public official web editions were used. Login-gated PDF actions were not bypassed, and article bodies are not distributed in the package.

The archive has 462 notes, 317 source-reference entries, 240 original MCQs and 64 Mains frameworks. This continuation adds 130 notes and enriches two existing July notes. 38 newly incorporated magazine article URLs supplement the earlier 63; independent research is retained.

| Coverage month | Official posting date | Inventory URLs | URLs linked to notes |
|---|---|---:|---:|
'''+ '\n'.join(rows)+'''

**101 URLs link to 100 notes; 281 URLs remain unincorporated.** Multiple URLs can inform one note, short pages aggregate topics, and anchored/parent URLs can overlap. This is not a coverage percentage or full-magazine review. Selected leads/substantive passages were read; retrieval of other bodies is not editorial review. Maps/image-only material remains unreconciled.

Coverage month is not event date or web-posting date. Magazine-supplement notes are explicitly indexed by coverage month with posting metadata. June's BharatFS and Axiom-4 examples illustrate why chronology needs correction against other sources.

## Breadth and linkage
The new selected pass adds GS4/privacy/surveillance and student safety, early architecture and documentary heritage, social-insurance comparisons, digital dependency, local finances, BRICS, quantum cyber-readiness, biofuels, heritage/sport, sustainable agriculture, disaster evidence, tribal governance and civic ethics. 18 independently authored reading paths connect actual note IDs and distinguish comparisons from legal timelines.

## Access and corrections
Read ../Research-Status.md for the access contract and correction ledger. The source registry records partial PRS reference reading, NASA/PIB article scopes, AP mirrored-order provenance, newspaper extracts and full news-body readings individually. A magazine assertion is not automatically accepted: unsupported scores, superlatives, ancient chronology and speculative final-cause claims are omitted or qualified.

## Unfinished
Unincorporated articles/shorts/maps, topic omissions, district/state GOs, primary documents and daily two-paper/PIB reconciliation remain open. No issue or month is certified complete. Source cache filenames now use URL hashes to avoid collisions; original article bodies remain outside the distributed project.
'''
(R/'research/magazine-review/Integration-Report.md').write_text(mag)
p=R/'README.md';old=p.read_text();keep=old[old.index('## Daily automation'):];keep=keep.replace('150 MCQs','240 MCQs').replace('675 dates','676 dates')
startauto=keep.index('### First collection test') if '### First collection test' in keep else keep.index('### Latest collection test');endauto=keep.index('## Editorial review')
keep=keep[:startauto]+'''### Latest collection test · 7 November 2026
The inbox holds 205 unreviewed links. The bare PRS index defaulted to June 2012; explicit 2025/2026 filters and a corrected title-length check now discover 22 monthly-review references. Hindu national/AP and ISRO endpoints responded. Both PIB endpoints returned 403; the Indian Express robots endpoint returned 403, so no collection was attempted there. Exit 2 correctly exposes partial failure. Discovery does not establish publication dates or complete review, and RSS feeds do not provide a complete historical archive. No access-control bypass is implemented.

'''+keep[endauto:]
intro='''# Civils Atlas — UPSC × Andhra Pradesh APPSC

**Research edition 05 · 7 November 2026 · Eight expanded selected monthly volumes. Full requested archive remains incomplete.**

Read [START-HERE.md](START-HERE.md). Open index.html for the offline library, now starting at June. Quick month buttons, separate monthly practice, bookmarks, filters and cross-month reading paths work without external scripts/fonts.

'''+table+'''

462 notes, 317 source-reference entries, 240 original MCQs and 64 original Mains frameworks. There are 444 notes in January–August plus 18 later seeds. Each monthly volume has PDF/DOCX/Markdown; Study-Notes.docx contains the full working archive. Cross-Month-Reading-Journeys has 18 curated paths connecting 74 notes in app, PDF, Word and Markdown. Practice is original, not official past papers or predictions.

## New substance and source access
130 new notes plus two enriched July seeds; the duplicate CETA event was merged into CA-033. June/July/August have 31/44/45 notes; 12 earlier additions address ethical, cultural, safety and social-protection gaps. AP education, mobility, farm support, quantum institutions and water-appraisal distinctions are included.

Official public Vision IAS passages guide breadth alongside independent PRS, primary and newspaper/regional research. 101 selected inventory URLs inform 100 magazine-assisted notes; 281 remain unincorporated. Coverage month differs from posting/event dates. No magazine bodies or login-gated PDFs are redistributed. Read research/magazine-review/Integration-Report.md and vision-reconciliation.csv.

Source counts are not fully read primary-document counts. Access labels distinguish full bodies, selected chunks, excerpts and a six-page AP GO mirror not independently authenticated on an official host. Historical legal/statistical notes do not certify the latest position.

## Still unfinished
All 23 monthly audits and 676 daily-source audits remain open. September 2025–7 November 2026 spans 15 periods requiring substantial backfill; January–August also remain selective. AP district/GOs, magazine shorts/maps, primary verification, P3 miscellany and exact APPSC paper mapping remain uneven. See research/Research-Status.md and the CSV ledgers. No hidden background researcher will finish them after this snapshot.

- data/notes.json: authored study notes, not overwritten by discovery.
- data/linkages.json: curated reading paths; related note IDs are embedded in notes.
- data/source-access.json: actual recorded access scope.
- data/inbox.json and update-log.json: unreviewed candidates and visible collector failures.
- data/coverage-ledger.csv: 253 subject-month cells; counts are not coverage percentages.
- data/daily-ledger.csv: 676 dated audit rows, all not fully reconciled.
- research/remaining-period-inventory.csv: required work across 23 open monthly audits.

'''
p.write_text(intro+keep)
print('Updated start guide, README, evidence status and magazine integration report')
