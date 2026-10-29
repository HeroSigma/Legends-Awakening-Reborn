"""Real Start-menu return/close regression using an isolated new-game battery."""
from pathlib import Path
R=Path('/home/allan/projects/Legends-Awakening-Reborn')
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0], 'helpers', 'exec'))
D=R/'.la_work/start-menu-test';D.mkdir(exist_ok=True)
start(0)
invoke('ScriptGiveMon',265,10,0)
import tempfile,struct
if True:
 with tempfile.TemporaryDirectory() as td:
  td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/flags.h"\n#include "dexnav.h"\nconst unsigned v[]={FLAG_SYS_POKEDEX_GET,FLAG_SYS_POKEMON_GET,FLAG_SYS_POKENAV_GET,DN_FLAG_DEXNAV_GET};\n')
  subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
  subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
  flags=struct.unpack('<4I',(td/'c.bin').read_bytes())
for f in flags:invoke('FlagSet',f)

for mode in [0,1]:
 invoke('StorageChangeMode',mode,1)
 for mask in range(16):
  for i,f in enumerate(flags):invoke('FlagSet' if mask&(1<<i) else 'FlagClear',f)
  for key in [2,8]:
   wr(symbols['sStartMenuPage'],0,1)
   tap(8);frames(40)
   check('direct_open_'+str((mode,mask,key)),active('Task_ShowStartMenu') is not None)
   check('bounded_rows_'+str((mode,mask,key)),rd(symbols['sNumStartMenuActions'],1)<=8)
   tap(16);frames(30)
   check('services_page_'+str((mode,mask,key)),rd(symbols['sStartMenuPage'],1)==1 and rd(symbols['sNumStartMenuActions'],1)==(4 if mask&8 else 3))
   tap(32);frames(30)
   check('adventure_page_'+str((mode,mask,key)),rd(symbols['sStartMenuPage'],1)==0)
   tap(key);frames(20)
   check('direct_close_'+str((mode,mask,key)),active('Task_ShowStartMenu') is None and rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 for f in flags:invoke('FlagSet',f)
 # Pokedex, Pokemon, Bag, trainer card, Options. Exercise immediate repeated
 # B input as well as waiting for each returned Start menu to finish fading.
 for page,option in [(0,0),(0,1),(0,2),(0,4),(0,6)]:
  for rapid in [False,True]:
   wr(symbols['sStartMenuPage'],page,1)
   wr(symbols['sStartMenuCursorPos'],0,1)
   tap(8);frames(50)
   for _ in range(option):tap(128)
   tap(1);frames(180)
   check('entered_submenu_'+str((mode,option,rapid)),rd(symbols['gMain']+4)!=symbols['CB2_Overworld']|1)
   expected_location=location()
   tap(2)
   if rapid:
    for _ in range(60):tap(2)
   else:
    frames(240)
    check('submenu_return_'+str((mode,option)),active('Task_ShowStartMenu') is not None)
    tap(2);frames(180)
   check('submenu_closed_'+str((mode,option,rapid)),active('Task_ShowStartMenu') is None)
   check('no_reset_'+str((mode,option,rapid)),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1 and location()==expected_location)
   check('controls_released_'+str((mode,option,rapid)),invoke('ArePlayerFieldControlsLocked')==0)
 # Journal closes directly to the field.
 wr(symbols['sStartMenuPage'],1,1)
 wr(symbols['sStartMenuCursorPos'],0,1)
 tap(8);frames(50)
 tap(128)
 tap(1);frames(30);check('journal_open_'+str(mode),active('Task_AdventureJournal') is not None)
 tap(2);frames(30)
 check('journal_exit_'+str(mode),active('Task_AdventureJournal') is None and rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
# Capture both fully unlocked pages and verify repeated shoulder-button switching.
for page in [0,1]:
 wr(symbols['sStartMenuPage'],page,1);wr(symbols['sStartMenuCursorPos'],0,1)
 tap(8);frames(50)
 shutil.copy2(shot('page_'+str(page)),R/'docs/features'/('start-menu-page-'+str(page)+'.png'))
 for key in [256,512]:
  for press in range(6):
   before=rd(symbols['sStartMenuPage'],1);tap(key);frames(25)
   check('shoulder_cycles_'+str((page,key,press)),rd(symbols['sStartMenuPage'],1)==(before^1))
  check('shoulder_wrap_'+str((page,key)),rd(symbols['sStartMenuPage'],1)==page)
 # EXIT remains a real selectable classic entry on both lists.
 for _ in range(rd(symbols['sNumStartMenuActions'],1)-1):tap(128)
 tap(1);frames(30)
 check('exit_action_'+str(page),active('Task_ShowStartMenu') is None and invoke('ArePlayerFieldControlsLocked')==0)
lib.shutdown()
result=dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks)
(D/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',len(checks),'Start menu checks')
