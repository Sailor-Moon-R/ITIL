from pathlib import Path
from playwright.sync_api import sync_playwright
from threading import Thread
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import os
import base64
import urllib.request
APP=Path(__file__).resolve().parents[1]
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(APP),**kwargs)
 def log_message(self, format,*args):pass
srv=ThreadingHTTPServer(('127.0.0.1',0),Handler);Thread(target=srv.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{srv.server_port}/'
errors=[]
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(viewport={'width':1480,'height':900},accept_downloads=True)
 page.set_default_timeout(5000)
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.on('dialog',lambda d:d.accept())
 try:
  # Browser host blocks localhost. Verify all individual resources via actual HTTP requests,
  # then use the exact release contents with inline sources for interaction testing.
  for asset in ['index.html','assets/desktop.css','assets/estio-logo.png','data/scenarios.js','data/practical_missions.js','core/engine.js','core/desktop.js']:
   with urllib.request.urlopen(url+asset,timeout=8) as src:
    assert src.status==200 and src.read(),asset
  html=(APP/'index.html').read_text()
  html=html.replace('<link rel="stylesheet" href="assets/desktop.css">','<style>'+(APP/'assets/desktop.css').read_text()+'</style>')
  for name in ['data/scenarios.js','data/practical_missions.js','core/engine.js','core/desktop.js']:
   html=html.replace(f'<script defer src="{name}"></script>','')
  html=html.replace('</body>',''.join('<script>'+(APP/name).read_text()+'</script>' for name in ['data/scenarios.js','data/practical_missions.js','core/engine.js','core/desktop.js'])+'</body>')
  data='data:image/png;base64,'+base64.b64encode((APP/'assets/estio-logo.png').read_bytes()).decode()
  html=html.replace('src="assets/estio-logo.png"',f'src="{data}"')
  page.set_content(html,wait_until='load')
  assert page.locator('img.welcome-brand').count()==1
  assert page.locator('img.welcome-brand').evaluate('(el)=>el.complete&&el.naturalWidth>0'), 'Logo failed to load locally'
  page.locator('.accept').evaluate_all('(els)=>els.forEach(x=>{x.checked=true;x.dispatchEvent(new Event("change",{bubbles:true}))})')
  page.locator('#accept').click()
  assert page.locator('img.estio-brand').evaluate('(el)=>el.complete&&el.naturalWidth>0'), 'header logo failed'
  print('Estio logo local loads PASS')
  # close help and verify element actually gone; reopen, min and restore, max and close
  page.locator('#win-help [data-act="close"]').click()
  assert page.locator('#win-help').count()==0,'close did not remove visible element'
  assert page.locator('#task-items [data-app="help"]').count()==0,'taskbar item remains'
  page.locator('[data-act="open"][data-app="help"]').first.click()
  assert page.locator('#win-help').is_visible()
  page.locator('#win-help [data-act="minimize"]').click()
  assert not page.locator('#win-help').is_visible()
  page.locator('#task-items [data-app="help"]').click()
  assert page.locator('#win-help').is_visible()
  page.locator('#win-help [data-act="maximize"]').click()
  assert page.locator('#win-help').evaluate('(el)=>el.dataset.max')=='yes'
  page.locator('#win-help [data-act="close"]').click()
  assert page.locator('#win-help').count()==0
  page.locator('[data-act="open"][data-app="help"]').first.click()
  assert page.locator('#win-help').is_visible()
  page.locator('#win-help [data-act="close"]').click()
  print('Window close/reopen/minimize/maximize PASS')
  # 3 independent terminal windows
  for k in ('terminal','linux','cloudcli'):
   page.locator(f'[data-act="open"][data-app="{k}"]').first.click()
  assert page.locator('.window').count()>=4
  page.locator('#win-terminal [data-terminal-input="terminal"]').fill('hosts')
  page.locator('#win-terminal [data-terminal-input="terminal"]').press('Enter')
  assert 'ID-01' in page.locator('#console-terminal').inner_text()
  page.locator('#win-linux [data-terminal-input="linux"]').fill('asset HR-LT-05')
  page.locator('#win-linux [data-terminal-input="linux"]').press('Enter')
  page.locator('#win-linux [data-terminal-input="linux"]').fill('ps')
  page.locator('#win-linux [data-terminal-input="linux"]').press('Enter')
  assert 'msedge.exe' in page.locator('#console-linux').inner_text()
  page.locator('#win-cloudcli [data-terminal-input="cloudcli"]').fill('asset ID-01')
  page.locator('#win-cloudcli [data-terminal-input="cloudcli"]').press('Enter')
  page.locator('#win-cloudcli [data-terminal-input="cloudcli"]').fill('Get-WinEvent')
  page.locator('#win-cloudcli [data-terminal-input="cloudcli"]').press('Enter')
  assert 'ID-101' in page.locator('#console-cloudcli').inner_text()
  print('Three simultaneous independent terminal windows PASS')
  # practical lab completion of task 1
  page.locator('[data-act="open"][data-app="practice"]').first.click()
  assert 'assignment 1 of 7' in page.locator('#win-practice').inner_text().lower(),page.locator('#win-practice').inner_text()[:400]
  page.locator('#lab-command').fill('hosts');page.locator('#lab-command').press('Enter')
  page.locator('#lab-command').fill('asset ID-01');page.locator('#lab-command').press('Enter')
  page.locator('#win-practice [data-act="lab-check"]').click()
  assert 'Mission completed' in page.locator('#win-practice').inner_text()
  page.locator('#win-practice [data-act="lab-select"][data-id="s2"]').click()
  page.locator('#lab-command').fill('Get-WinEvent');page.locator('#lab-command').press('Enter')
  page.locator('[data-act="open"][data-app="siem"]').first.click()
  for item in ['ID-101','ID-103']:
   page.locator(f'#win-siem [data-act="inspect"][data-id="{item}"]').click()
  page.locator('#task-items [data-app="practice"]').click()
  page.locator('#win-practice [data-act="lab-check"]').click()
  assert 'Mission completed' in page.locator('#win-practice').inner_text()
  print('Hands-on lab milestones and 2 completions PASS')
  # exercise reset is independent of others; counts maintained
  page.locator('#win-practice [data-act="lab-task-reset"]').click()
  page.locator('#overlay-host [data-act="confirm"]').click()
  assert 'Mission completed' not in page.locator('#win-practice').inner_text()
  page.locator('#win-practice [data-act="lab-select"][data-id="s1"]').click()
  assert 'completed' in page.locator('#win-practice').inner_text().lower()
  page.locator('#win-practice [data-act="lab-select"][data-id="s2"]').click()
  page.locator('#win-practice [data-act="lab-check"]').click()
  assert 'Mission completed' not in page.locator('#win-practice').inner_text(), 'task reset did not require new terminal action'
  page.locator('#lab-command').fill('Get-WinEvent');page.locator('#lab-command').press('Enter')
  page.locator('#win-practice [data-act="lab-check"]').click()
  assert 'Mission completed' in page.locator('#win-practice').inner_text()
  print('Independent assignment reset and fresh command requirement PASS')
  # verify report includes practical and terminal history
  with page.expect_download() as d:page.locator('.taskbar [data-act="report"]').click()
  text=d.value.path().read_text()
  assert 'Practical Mission Work' in text and 'Map your environment' in text and 'Simulated terminal investigation history' in text
  print('Case-file export includes practical record PASS')
  page.locator('#win-practice').screenshot(path='/mnt/data/northbridge_v31_practice.png')
  page.screenshot(path='/mnt/data/northbridge_v31_desktop.png')
  page.set_viewport_size({'width':440,'height':850})
  page.locator('#task-items [data-app="practice"]').click()
  assert page.locator('#win-practice').is_visible()
  page.screenshot(path='/mnt/data/northbridge_v31_mobile.png')
  print('Mobile layout PASS')
 finally:
  print('PAGE ERRORS',errors)
  b.close();srv.shutdown()
assert not errors, errors
print('V3.1 QA PASS')
