"""Preserve depth in early legacy seeds without adding duplicate notes."""
import json,pathlib
R=pathlib.Path(__file__).resolve().parents[1];p=R/'data/notes.json';N=json.loads(p.read_text())
extra={
'CA-001':['Revenue deficit was estimated at 1.5% of GDP; all these FY2025–26 figures are Budget Estimates, not audited outcomes.'],
'CA-003':['The rebate-based relief and the standard deduction are separate mechanisms; special-rate income requires separate treatment.'],
'CA-004':['The proposed design uses convergence of existing programmes and partnership with states, not merely a new unconditional transfer.'],
'CA-005':['The four-year procurement commitment is distinct from the six-year mission duration; the announcement is not evidence that all procurement had begun.'],
'CA-006':['The Budget described KCC as facilitating short-term loans to 7.7 crore farmers, fishers and dairy farmers.','The ₹5 lakh figure concerns the proposed limit under interest subvention; it is not a ₹5 lakh cash grant to every cardholder.'],
'CA-007':['The stated geographic emphasis included the Andaman and Nicobar and Lakshadweep islands, not only mainland coastal states.','The announcement concerned a regulatory/enabling framework; it did not itself establish a new universal fisher cash entitlement.'],
'CA-008':['The investment and turnover criteria are separate components of the composite enterprise classification.','The February announcement preceded the March notification and 1 April effective date, which are tracked in a separate March note.'],
'CA-010':['The Budget described the measures as likely to assist nearly one crore gig workers.','Registration, identity documentation and healthcare linkage are different implementation steps; the announcement does not verify universal enrolment.'],
'CA-012':['The Urban Challenge Fund was to support part of bankable urban project costs, not replace all project financing.'],
'CA-014':['The demonstration followed the PSLV-C60 launch of the two satellites on 30 December 2024.'],
'CA-017':['The figure is a current-price state aggregate; price changes are included, unlike in a constant-price real-growth estimate.'],
'CA-018':['The announced benefit was framed per school-going child; eligibility and actual payment require subsequent implementation records.'],
'CA-019':['The proposal doubles the stated relief amount; it is not a change to the biological conservation rationale for a seasonal ban.','The February Budget commitment precedes the April launch reporting; the two milestones must not be treated as simultaneous.'],
'CA-020':['The design envisaged a hub-and-zonal-centre network; a Budget proposal is not confirmation that every centre was operating.'],
'CA-023':['Indore is in Madhya Pradesh and Udaipur is in Rajasthan; accreditation of a city differs from Ramsar listing of a specific wetland.']}
for n in N:
 for v in extra.get(n['id'],[]):
  if v not in n['facts']:n['facts'].append(v)
p.write_text(json.dumps(N,ensure_ascii=False,indent=2));print('Enriched',len(extra),'legacy seeds; no added note count')
