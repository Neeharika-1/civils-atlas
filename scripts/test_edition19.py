"""Structural/evidence-contract checks, not independent factual or legal certification."""
import json,pathlib,unittest,collections,datetime
R=pathlib.Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
class ResearchTests(unittest.TestCase):
 def setUp(self):
  self.notes=load('data/notes.json');self.byid={n['id']:n for n in self.notes};self.new=[n for n in self.notes if n['id'].startswith('E19-')]
 def test_new_note_contract(self):
  self.assertEqual(len(self.new),14)
  for n in self.new:
   self.assertGreaterEqual(len(n['facts']),5);self.assertGreaterEqual(len(n['analysis']),3)
   for key in ['why','static_link','trap','mains','evidence_access']:self.assertTrue(n[key])
   datetime.date.fromisoformat(n['date'])
   for k in n['sources']:self.assertIn(k,load('data/sources.json'));self.assertIn(k,load('data/source-access.json'))
 def test_backfills_and_cutoff(self):
  expected={'E19-001':'2026-04-09','E19-002':'2026-05-05','E19-003':'2026-03-11','E19-004':'2026-03-28'}
  for k,d in expected.items():self.assertEqual(self.byid[k]['date'],d);self.assertEqual(self.byid[k]['date_precision'],'day')
  self.assertEqual(sum(n['date'].startswith('2026-11')for n in self.new),10)
  self.assertTrue(all(n['date']<='2026-11-07'for n in self.new))
 def test_practice(self):
  q=load('data/research-practice.json');self.assertEqual(len(q),14);self.assertEqual(len({x['id']for x in q}),14)
  for x in q:
   self.assertIn(x['ref'],self.byid);self.assertEqual(len(set(x['options'])),4);self.assertIn(x['answer'],range(4));self.assertTrue(x['explanation'])
  self.assertEqual(dict(collections.Counter(x['answer']for x in q)),{0:4,1:4,2:3,3:3})
 def test_stage_cautions_retained(self):
  for id,words in [('E19-006',['in force','15 July','17 July']),('E19-007',['draft','Gazette']),('E19-010',['seven','15']),('E19-012',['turnover','income']),('E19-011',['toll-free','GNSS'])]:
   text=json.dumps(self.byid[id],ensure_ascii=False).lower()
   for word in words:self.assertIn(word.lower(),text)
 def test_required_sources_retained(self):
  r=load('data/source-registry.json');self.assertEqual(len(r),18);self.assertTrue(all(x['required']for x in r))
  self.assertTrue({'pib-daily','express-india','express-explained','vision-daily','vision-monthly','ap-finance','ap-orders'}<={x['id']for x in r})
 def test_automatic_intake_is_not_verification(self):
  p=R/'data/document-intake.json'
  if not p.exists():self.skipTest('No intake result yet')
  for doc in load('data/document-intake.json')['documents']:
   self.assertFalse(doc['human_verified']);self.assertFalse(doc.get('publication_date_verified',False))
if __name__=='__main__':unittest.main()
