"""Offline policy/parser tests; these do not prove hosted website access."""
import importlib.util,pathlib,types,unittest
from unittest.mock import patch
R=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('atlas_update',R/'scripts/update.py');u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
class Policy:
 def __init__(self,allowed=True):self.allowed=allowed
 def can_fetch(self,*args):return self.allowed
class Response:
 def __init__(self,url,status=200,body='',headers=None):self.url=url;self.status_code=status;self.content=body.encode();self.text=body;self.headers=headers or {}
 def raise_for_status(self):
  if self.status_code>=400:raise RuntimeError('HTTP '+str(self.status_code))
def stream(**kw):return dict(id='test',name='Test source',category='Test',url='https://example.org/list',format='html',link_pattern='article',**kw)
class Tests(unittest.TestCase):
 def test_canonical(self):
  self.assertEqual(u.canonical('https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=123&lang=1'),'https://www.pib.gov.in/PressReleasePage.aspx?PRID=123&reg=3&lang=1')
  self.assertIn('evil-pib.gov.in',u.canonical('https://evil-pib.gov.in/a?PRID=123'))
  for x in ['javascript:alert(1)','file:///tmp/x','http://localhost/x']:
   with self.assertRaises(ValueError):u.canonical(x)
 def test_robots_denial(self):
  with patch.object(u,'robot_policy',return_value=Policy(False)),patch.object(u.requests,'get')as get:
   items,log=u.collect(stream());self.assertFalse(items);self.assertEqual(log['status'],'failed');get.assert_not_called()
 def test_rss_official_fallback(self):
  xml='<rss><channel><item><title>Sample release</title><link>https://example.org/article/1</link></item></channel></rss>'
  def get(url,**kw):return Response(url,503)if url.endswith('/list')else Response(url,body=xml)
  with patch.object(u,'robot_policy',return_value=Policy()),patch.object(u.requests,'get',side_effect=get):
   items,log=u.collect(stream(fallbacks=[dict(url='https://example.org/feed',format='rss')]))
   self.assertEqual(len(items),1);self.assertTrue(log['fallback_used']);self.assertFalse(log['source_read']);self.assertEqual(len(log['attempts']),2)
 def test_redirect_policy_checked_before_fetch(self):
  calls=[]
  def policy(origin):return Policy(origin=='https://example.org')
  def get(url,**kw):calls.append(url);self.assertFalse(kw['allow_redirects']);return Response(url,302,headers={'Location':'https://blocked.example/article'})
  with patch.object(u,'robot_policy',side_effect=policy),patch.object(u.requests,'get',side_effect=get):
   items,log=u.collect(stream());self.assertEqual(calls,['https://example.org/list']);self.assertEqual(log['status'],'failed')
 def test_portal_is_not_utilised(self):
  spec=stream();spec['format']='portal'
  with patch.object(u,'robot_policy',return_value=Policy()),patch.object(u.requests,'get',return_value=Response(spec['url'])):
   items,log=u.collect(spec);self.assertFalse(items);self.assertEqual(log['status'],'review_required');self.assertFalse(log['source_read'])
 def test_express_link_only(self):
  s=stream();s.update(format='rss',publishing='link-only')
  xml='<rss><channel><item><title>Do not republish this headline</title><link>https://example.org/article/1</link></item></channel></rss>'
  with patch.object(u,'robot_policy',return_value=Policy()),patch.object(u.requests,'get',return_value=Response(s['url'],body=xml)):
   items,log=u.collect(s);self.assertEqual(log['status'],'ok');self.assertNotIn('Do not republish',items[0]['title'])
 def test_no_items_is_not_success(self):
  with patch.object(u,'robot_policy',return_value=Policy()),patch.object(u.requests,'get',return_value=Response('https://example.org/list',body='<html>Empty</html>')):
   items,log=u.collect(stream());self.assertEqual(log['status'],'review_required')
 def test_reachable_fallback_portal_remains_manual(self):
  def get(url,**kw):return Response(url,503)if url.endswith('/list')else Response(url)
  with patch.object(u,'robot_policy',return_value=Policy()),patch.object(u.requests,'get',side_effect=get):
   items,log=u.collect(stream(fallbacks=[dict(url='https://example.org/portal',format='portal')]))
   self.assertFalse(items);self.assertEqual(log['status'],'review_required');self.assertTrue(log['fallback_used']);self.assertTrue(log['portal_reachable']);self.assertFalse(log['source_read'])
 def test_manual_search_is_never_automatic_source_success(self):
  s=stream();s['manual_recovery']={'search_url':'https://www.google.com/search?q=site:example.org'}
  with patch.object(u,'robot_policy',return_value=Policy()),patch.object(u.requests,'get',return_value=Response(s['url'],503))as get:
   items,log=u.collect(s);self.assertFalse(items);self.assertEqual(log['status'],'failed');self.assertEqual(get.call_count,1);self.assertEqual(get.call_args.args[0],s['url'])
 def test_robots_403_unavailable_is_not_a_disallow_rule(self):
  u.robot_policy.cache_clear()
  with patch.object(u.requests,'get',return_value=Response('https://example.org/robots.txt',403)):
   self.assertIsNone(u.robot_policy('https://example.org'))
  u.robot_policy.cache_clear()
 def test_robots_server_failure_and_rate_limit_still_stop(self):
  for code in [401,429,503]:
   u.robot_policy.cache_clear()
   with patch.object(u.requests,'get',return_value=Response('https://example.org/robots.txt',code)):
    with self.assertRaises(RuntimeError):u.robot_policy('https://example.org')
  u.robot_policy.cache_clear()
 def test_actual_page_denial_is_not_bypassed(self):
  with patch.object(u,'robot_policy',return_value=Policy()),patch.object(u.requests,'get',return_value=Response('https://example.org/list',403))as get:
   items,log=u.collect(stream());self.assertFalse(items);self.assertEqual(log['status'],'failed');self.assertEqual(get.call_count,1)
if __name__=='__main__':unittest.main()
