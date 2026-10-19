from pathlib import Path
from threading import Thread
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import base64,urllib.request,os,re
from playwright.sync_api import sync_playwright
APP=Path(__file__).resolve().parents[1]
class H(SimpleHTTPRequestHandler):
 def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(APP),**kwargs)
 def log_message(self,*args):pass
s=ThreadingHTTPServer(('127.0.0.1',0),H);Thread(target=s.serve_forever,daemon=True).start();url=f'http://127.0.0.1:{s.server_port}/'
for path in ['index.html','knowledge/index.html','knowledge/content.js','knowledge/knowledge.js','knowledge/knowledge.css','assets/estio-logo.png','data/practical_missions.js','core/desktop.js']:
 with urllib.request.urlopen(url+path,timeout=6) as a: assert a.status==200 and a.read(),path
print('HTTP resources PASS')
def inline_guide():
 html=(APP/'knowledge/index.html').read_text().replace('<link rel="stylesheet" href="knowledge.css">','<style>'+(APP/'knowledge/knowledge.css').read_text()+'</style>')
 for path in ['../data/practical_missions.js','content.js','knowledge.js']:
  html=html.replace(f'<script defer src="{path}"></script>','')
 scripts=''.join('<script>'+(APP/('data/practical_missions.js' if v=='practical' else 'knowledge/'+v+'.js')).read_text()+'</script>' for v in ['practical','content','knowledge'])
 html=html.replace('</body>',scripts+'</body>')
 pic=base64.b64encode((APP/'assets/estio-logo.png').read_bytes()).decode();html=html.replace('src="../assets/estio-logo.png"',f'src="data:image/png;base64,{pic}"')
 return html

def inline_desk():
 html=(APP/'index.html').read_text().replace('<link rel="stylesheet" href="assets/desktop.css">','<style>'+(APP/'assets/desktop.css').read_text()+'</style>')
 for f in ['data/scenarios.js','data/practical_missions.js','core/engine.js','core/desktop.js']:html=html.replace(f'<script defer src="{f}"></script>','')
 scripts=''.join('<script>'+(APP/p).read_text()+'</script>' for p in ['data/scenarios.js','data/practical_missions.js','core/engine.js','core/desktop.js'])
 html=html.replace('</body>',scripts+'</body>')
 pic=base64.b64encode((APP/'assets/estio-logo.png').read_bytes()).decode();return html.replace('src="assets/estio-logo.png"',f'src="data:image/png;base64,{pic}"')
errors=[]
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 try:
  page=b.new_page(viewport={'width':1440,'height':900});page.on('pageerror',lambda err:errors.append('guide:'+str(err)))
  page.set_content(inline_guide(),wait_until='load');assert page.locator('h1').inner_text()=='What is incident management?'
  assert page.locator('.navbtn').count()==15
  assert 'Northbridge' in page.locator('body').inner_text()
  print('Intro and all 15 concepts PASS')
  page.screenshot(path='/mnt/data/Northbridge_SOC_3.2_Learning_Hub/knowledge/assets/qa_intro.png',full_page=True)
  page.locator('[data-topic="preserve"]').click();assert 'Evidence collection and preservation' in page.locator('h1').inner_text()
  assert page.locator('a[href*="case=lockdown"][href*="task=l4"]').count()>=1
  print('Evidence preservation maps to actual application PASS')
  page.locator('[data-topic="severity"]').click();assert page.locator('select[data-variable="impact"]').count()==1
  page.locator('select[data-variable="impact"]').select_option('high');page.locator('select[data-variable="urgency"]').select_option('high')
  assert 'Immediate crisis-level coordination' in page.locator('.experimentout').inner_text()
  print('Interactive severity explainer PASS')
  page.locator('[data-topic="timeline"]').click();page.locator('[data-demo="volume"]').click();assert '512 MB outbound TLS' in page.locator('.stageinfo').inner_text()
  page.locator('#topic-search').fill('custody');assert page.locator('.navbtn').count()==1
  page.locator('#topic-search').fill('');assert page.locator('.navbtn').count()==15
  page.locator('[data-topic="contain"]').click();page.locator('[data-stage="2"]').click();assert 'Authorised' in page.locator('.stageinfo').inner_text()
  print('Evidence demo, topic search, response map PASS')
  page.locator('[data-mode="light"]').click();page.locator('[data-mode="read"]').click();page.locator('[data-mode="zoom"]').click();assert page.locator('body').evaluate('(e)=>e.classList.contains("lightmode")&&e.classList.contains("readmode")')
  print('Accessible settings controls PASS')
  page.set_viewport_size({'width':430,'height':900});page.screenshot(path='/mnt/data/Northbridge_SOC_3.2_Learning_Hub/knowledge/assets/qa_mobile.png',full_page=True)
  assert page.locator('h1').is_visible();print('Mobile rendering PASS')
  # Browser policy blocks localhost/file URLs. Verify the exact release code in inline mode,
  # with location.search substituted only for the test document so the case selector can be exercised.
  desk=b.new_page(viewport={'width':1440,'height':900})
  desk.on('pageerror',lambda err:errors.append('desk:'+str(err)))
  app_html=inline_desk().replace('new URLSearchParams(location.search)','new URLSearchParams("?case=lockdown&task=l4&tool=practice")')
  desk.set_content(app_html,wait_until='load')
  desk.locator('.accept').evaluate_all('(els)=>els.forEach(x=>{x.checked=true;x.dispatchEvent(new Event("change",{bubbles:true}))})')
  desk.locator('#accept').click()
  assert desk.locator('#win-practice').is_visible()
  assert 'Preserve ransomware evidence' in desk.locator('#win-practice').inner_text()
  assert desk.locator('.top a[href="knowledge/index.html"]').count()==1
  print('First-run agreement, task deep-link selection and guide back-link PASS')
  assert desk.locator('#win-practice [data-act="lab-task-reset"]').count()==1
  # Verify that another linked task in a separate case also launches by ID.
  desk2=b.new_page(viewport={'width':1280,'height':860})
  desk2.on('pageerror',lambda err:errors.append('desk2:'+str(err)))
  app2=inline_desk().replace('new URLSearchParams(location.search)','new URLSearchParams("?case=northbridge&task=n5&tool=practice")')
  desk2.set_content(app2,wait_until='load')
  desk2.locator('.accept').evaluate_all('(els)=>els.forEach(x=>{x.checked=true;x.dispatchEvent(new Event("change",{bubbles:true}))})')
  desk2.locator('#accept').click()
  assert 'Preserve cloud evidence' in desk2.locator('#win-practice').inner_text()
  print('Northbridge deep-link assignment PASS')
  desk2.close()
  desk.close();page.close()
 finally:b.close();s.shutdown()
assert not errors,errors
print('KNOWLEDGE HUB QA PASS')
