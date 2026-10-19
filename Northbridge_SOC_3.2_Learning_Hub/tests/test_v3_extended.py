"""Extended UI regression. Uses inlined release assets because the hosted/file URLs are restricted by this test environment."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import hashlib,json
A=Path(__file__).resolve().parents[1]
h=(A/'index.html').read_text().replace('<link rel="stylesheet" href="assets/desktop.css">','<style>'+(A/'assets/desktop.css').read_text()+'</style>')
for src in ('data/scenarios.js','data/practical_missions.js','core/engine.js','core/desktop.js'):h=h.replace(f'<script defer src="{src}"></script>','')
h=h.replace('</body>',''.join('<script>'+(A/f).read_text()+'</script>' for f in ('data/scenarios.js','data/practical_missions.js','core/engine.js','core/desktop.js'))+'</body>')
errors=[]
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 pg=b.new_page(viewport={'width':1460,'height':900},accept_downloads=True)
 pg.set_default_timeout(8000)
 pg.on('pageerror',lambda x:errors.append(str(x)))
 pg.on('dialog',lambda x:x.accept())
 pg.set_content(h)
 pg.locator('.accept').evaluate_all('(a)=>a.forEach(x=>{x.checked=true;x.dispatchEvent(new Event("change",{bubbles:true}))})')
 pg.locator('#accept').click()
 pg.locator('#win-help [data-act="close"]').click()
 # canonical SHA-256 must work without secure context and detect altered lab copy
 assert pg.evaluate("async()=>await NBEngine.hash('abc')") == hashlib.sha256(b'abc').hexdigest()
 assert pg.evaluate("async()=>await NBEngine.hash('étude 🦄')") == hashlib.sha256('étude 🦄'.encode()).hexdigest()
 # Open Event Viewer and inspect alert, resulting practice record is shared with SIEM inspection
 pg.locator('.shortcut[data-app="eventviewer"]').click()
 pg.locator('#win-eventviewer [data-filter="evchannel"]').select_option('Security')
 pg.locator('#win-eventviewer [data-act="inspect"]').first.click()
 assert pg.evaluate("NBEngine.current().inspected.siem.length")>=1
 pg.locator('.shortcut[data-app="packet"]').click()
 pg.locator('#win-packet [data-act="packet-select"]').first.click()
 assert pg.evaluate("NBEngine.current().inspected.network.length")>=1
 # Service desk triage and comms exercises
 pg.locator('.shortcut[data-app="tickets"]').click()
 pg.locator('#ticket-priority').select_option('P3 Medium')
 pg.locator('#ticket-reason').fill('Sign-ins are unsuccessful and conditional access blocked the suspicious source. Investigate any unexpected successful sessions.')
 pg.locator('#win-tickets [data-act="save-ticket"]').click()
 assert 'Incident desk ticket updated' in pg.locator('#win-tickets').inner_text()
 pg.locator('.shortcut[data-app="comms"]').click()
 pg.locator('#comms-body').fill('We have investigated unusual login attempts and presently have no confirmed hostile session. We will monitor identity logs and update leadership at 09:00.')
 pg.locator('#win-comms [data-act="send-comms"]').click()
 assert 'simulated outbox' in pg.locator('#win-comms').inner_text()
 # Timeline builder using inspected source
 pg.locator('.shortcut[data-app="timeline"]').click()
 pg.locator('#timeline-reference').select_option('ID-101')
 pg.locator('#timeline-note').fill('First unsuccessful external login attempt; not itself evidence that an attacker succeeded.')
 pg.locator('#win-timeline [data-act="add-timeline"]').click()
 assert 'ID-101' in pg.evaluate('NBEngine.current().timelineEntries.map(x=>x.reference).join(",")')
 # Evidence workflow and tamper detection
 pg.locator('[data-act="restore"][data-app="eventviewer"]').click()
 pg.locator('#win-eventviewer [data-act="flag"]').click()
 pg.locator('.shortcut[data-app="locker"]').click()
 pg.locator('#win-locker [data-act="choose-evidence"]').first.click()
 pg.locator('#ev-purpose').fill('Correlate suspicious attempts and block outcomes for a defensible login chronology.')
 pg.locator('#win-locker [data-act="preserve"]').click()
 ref=pg.evaluate('NBEngine.current().preserved[0].id')
 assert pg.evaluate('async()=> (await NBEngine.verify(NBEngine.current().preserved[0].id)).same')
 pg.evaluate('NBEngine.mutate(NBEngine.current().preserved[0].id)')
 assert pg.evaluate('async()=> !(await NBEngine.verify(NBEngine.current().preserved[0].id)).same')
 # Verify standalone tool reset and local backup don't alter service-desk record
 pg.locator('[data-act="restore"][data-app="timeline"]').click()
 pg.locator('#win-timeline [data-act="reset-tool"]').click()
 pg.locator('#overlay-host [data-act="confirm"]').click()
 assert pg.evaluate('NBEngine.current().timelineEntries.length')==0
 assert pg.evaluate('NBEngine.current().tickets.length')==1
 # user-generated report sanitisation and included sections
 report=pg.evaluate('NBEngine.report()')
 assert 'Service desk triage' in report and 'Stakeholder communications' in report
 assert '<script' not in report
 progress=json.loads(pg.evaluate('NBEngine.exportJSON()'))
 assert progress['missions']['storm']['tickets'][0]['priority']=='P3 Medium'
 pg.locator('[data-act="case-picker"]').click();pg.locator('[data-act="choose-case"][data-id="invoice"]').click()
 assert pg.evaluate('NBEngine.current().tickets.length')==0
 pg.locator('#win-brief [data-act="reset-case"]').click()
 pg.locator('#overlay-host [data-act="confirm"]').click()
 assert pg.evaluate('NBEngine.state.missions.storm.tickets.length')==1
 # Responsive rendering
 pg.set_viewport_size({'width':390,'height':780})
 pg.locator('.taskbar [data-act="open"][data-app="brief"]').click()
 pg.screenshot(path='/mnt/data/northbridge_v3_mobile_qa.png',full_page=True)
 assert pg.locator('#win-brief').is_visible()
 print('EXTENDED V3 QA PASS; inspected, tickets, communications, timeline, hashes, reset, report, state, mobile')
 print('PAGE ERRORS',errors)
 assert not errors
 b.close()
