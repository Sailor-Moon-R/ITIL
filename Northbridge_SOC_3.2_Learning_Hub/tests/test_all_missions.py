from pathlib import Path
from playwright.sync_api import sync_playwright
A=Path(__file__).resolve().parents[1]
html=(A/'index.html').read_text().replace('<link rel="stylesheet" href="assets/desktop.css">','<style>'+(A/'assets/desktop.css').read_text()+'</style>')
for f in ['data/scenarios.js','data/practical_missions.js','core/engine.js','core/desktop.js']:
 html=html.replace(f'<script defer src="{f}"></script>','')
html=html.replace('</body>',''.join('<script>'+(A/f).read_text()+'</script>' for f in ['data/scenarios.js','data/practical_missions.js','core/engine.js','core/desktop.js'])+'</body>')
errors=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 for case in ['storm','invoice','lockdown','northbridge']:
  page=b.new_page(viewport={'width':1540,'height':940})
  page.set_default_timeout(5000)
  page.on('pageerror',lambda err:errors.append(str(err)))
  page.set_content(html,wait_until='load')
  page.locator('.accept').evaluate_all('(els)=>els.forEach(x=>{x.checked=true;x.dispatchEvent(new Event("change",{bubbles:true}))})')
  page.locator('#accept').click()
  page.evaluate('(id)=>window.NBEngine.setCase(id)',case)
  # open practice window
  page.locator('.shortcut[data-app="practice"]').click()
  tasks=page.evaluate('(id)=>window.NBSIM_LABS[id]',case)
  for t in tasks:
   page.locator(f'#win-practice [data-act="lab-select"][data-id="{t["id"]}"]').click(force=True)
   result=page.evaluate('''async (task)=>{
     const E=window.NBEngine,m=E.current(),st=m.labState;
     let problems=[];
     const candidates=['hosts','asset ID-01','asset HR-LT-05','asset FIN-LT-14','asset M365-01','asset FIN-WS-07','asset FS-01','asset NB-ID-01','asset NB-APP-02','asset NB-LT-042','Get-WinEvent','journalctl','Get-Process','tasklist','ps','netstat -ano','Get-NetTCPConnection','dir','cat 1','cat 2','cat 3','Get-FileHash 1','Get-FileHash 3','Get-Service','Get-Case'];
     for(const requirement of task.checks){
      const [type,label,a,b]=requirement;
      if(type==='terminal'){
        if(b)await E.runCommand('asset '+b,'practice');
        const cmd=candidates.find(x=>new RegExp(a,'i').test(x));
        if(!cmd){problems.push('No test command matches '+label);continue;}
        await E.runCommand(cmd,'practice');
      }else if(type==='inspect'){
        if(!E.getRecord(b))problems.push('Missing artefact '+b);
        E.inspect(a,b);
      }else if(type==='preserve'){
        if(!E.getRecord(a))problems.push('Missing preservable '+a);
        const r=await E.preserve(a,{purpose:'This artefact relates to the incident and supports evidence-based decisions.',handler:'Training Analyst',method:'Read-only simulation export into case file'});
        if(!r.ok)problems.push('Preserve failed '+a+' '+r.message);
      }else if(type==='action'){
        const r=E.response(a,b,'Incident Manager','Evidence supports proportionate and authorised action on the targeted fictional system.', '');
        if(!r.ok)problems.push('Response failed '+a+' '+b+' '+r.message);
      }else if(type==='ticket'){
        const r=E.ticket('incident','P2','Incident Manager','There is credible unusual activity to investigate, with clearly defined ownership and follow-up.');
        if(!r.ok)problems.push('Ticket failed '+r.message);
      }else if(type==='comms'){
        const r=E.communicate('Management','We are investigating a suspected security incident. Some effects are verified, while the precise scope remains uncertain. Next update will follow.', 'Communications Lead');
        if(!r.ok)problems.push('Communication failed '+r.message);
      }else if(type==='recovery'){
        const r=E.recovery('safe',[true,true,true],'Service Owner','Evidence and validation support staged restoration of a clean service.');
        if(!r.ok)problems.push('Recovery failed '+r.message);
      }else if(type==='late')E.clock(40);
      else if(type==='reflection')st.notes[task.id]='The evidence supports a cautious incident response. I would verify further log sources, communicate uncertainty, and follow the approved process.';
     }
     E.save();return problems;
   }''',t)
   page.locator('#win-practice [data-act="lab-check"]').click(force=True)
   success='Mission completed' in page.locator('#win-practice').inner_text()
   if not success or result:
    print('FAIL',case,t['id'],result,page.locator('#win-practice').inner_text()[-700:]);errors.append(case+'/'+t['id'])
   else:print('PASS',case,t['id'],t['title'])
  page.close()
 b.close()
print('FAILED:',errors)
assert not errors
print('ALL 28 HANDS-ON MISSIONS VALIDATED')
