"""Offline collector unit checks. Does not claim hosted Actions execution."""
import unittest,importlib.util,pathlib,types
from unittest.mock import patch
R=pathlib.Path(__file__).resolve().parents[1];spec=importlib.util.spec_from_file_location('collector',R/'scripts/update.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def response(status,text):return types.SimpleNamespace(status_code=status,text=text,content=text.encode(),raise_for_status=lambda:None)
class DailyTests(unittest.TestCase):
 def test_pib_dedup(self):
  self.assertEqual(m.canonical('https://pib.gov.in/PressReleseDetail.aspx?PRID=123&lang=2'),m.canonical('https://www.pib.gov.in/PressReleasePage.aspx?PRID=123&lang=1'))
 def test_reject_script(self):
  with self.assertRaises(ValueError):m.canonical('javascript:alert(1)')
 def test_robots_block(self):
  with patch.object(m.requests,'get',return_value=response(200,'User-agent: *\nDisallow: /'))as get:
   rows,log=m.collect(('Fixture','https://example.com/feed','rss'));self.assertFalse(rows);self.assertEqual(log['status'],'failed');self.assertEqual(get.call_count,1)
 def test_robots_unavailable(self):
  with patch.object(m.requests,'get',return_value=response(403,''))as get:
   rows,log=m.collect(('Fixture','https://example.com/feed','rss'));self.assertFalse(rows);self.assertEqual(get.call_count,1)
 def test_rss_date_and_title_metadata(self):
  xml='<rss><channel><item><title>Fixture item</title><link>https://example.com/story?utm_source=test</link><pubDate>Fri, 06 Nov 2026 12:00:00 GMT</pubDate></item></channel></rss>'
  with patch.object(m.requests,'get',side_effect=[response(404,''),response(200,xml)]):
   rows,log=m.collect(('Fixture','https://example.com/feed','rss'));self.assertEqual(log['status'],'ok');self.assertEqual(rows[0]['url'],'https://example.com/story');self.assertIn('06 Nov',rows[0]['published_raw'])
if __name__=='__main__':unittest.main()
