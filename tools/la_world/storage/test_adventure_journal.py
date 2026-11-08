"""Open the real Start-menu journal in isolated native mGBA."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0], 'pc_helpers', 'exec'))
D=R/'.la_work/qol_features/journal-test';D.mkdir(parents=True,exist_ok=True)
proof=R/'docs/features/adventure-journal';proof.mkdir(exist_ok=True)
start(0)
import tempfile,struct
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/flags.h"\n#include "dexnav.h"\nconst unsigned values[]={FLAG_SYS_POKEDEX_GET,FLAG_SYS_POKEMON_GET,FLAG_SYS_POKENAV_GET,DN_FLAG_DEXNAV_GET,FLAG_LA_MET_RED};\n')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 flags=struct.unpack('<5I',(td/'c.bin').read_bytes())
for f in flags:invoke('FlagSet',f)
invoke('IncrementGameStat',5)
for mode in [0,1]:
 invoke('StorageChangeMode',mode,1)
 before=[invoke('GetGameStat',i) for i in range(64)]
 wr(symbols['sStartMenuCursorPos'],0,1)
 tap(8);frames(60)
 count=rd(symbols['sNumStartMenuActions'],1)
 check('nine_menu_rows_'+str(mode),count==9)
 # JOURNAL replaces EXIT at the bottom; no overflow of the menu action buffer.
 for _ in range(count-1):tap(128)
 tap(1);frames(30)
 task=active('Task_AdventureJournal')
 check('journal_from_start_'+str(mode),task is not None)
 for page in range(3):
  check('page_'+str((mode,page)),rd(symbols['gTasks']+task*40+10,2)==page)
  if mode==0:shutil.copy2(shot('journal_page_'+str(page)),proof/('page_'+str(page)+'.png'))
  tap(16)
 check('wrap_forward_'+str(mode),rd(symbols['gTasks']+task*40+10,2)==0)
 tap(32);check('wrap_backward_'+str(mode),rd(symbols['gTasks']+task*40+10,2)==2)
 tap(2);frames(30)
 check('journal_closed_'+str(mode),active('Task_AdventureJournal') is None)
 check('overworld_return_'+str(mode),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 check('stats_read_only_'+str(mode),before==[invoke('GetGameStat',i) for i in range(64)])
 check('story_read_only_'+str(mode),invoke('FlagGet',flags[-1])==1)
# Reopen and close with START, exercising task/window reuse.
wr(symbols['sStartMenuCursorPos'],0,1)
tap(8);frames(50)
for _ in range(8):tap(128)
tap(1);frames(20);check('journal_reopens',active('Task_AdventureJournal') is not None)
tap(8);frames(30);check('start_closes_journal',active('Task_AdventureJournal') is None)
lib.shutdown()
(R/'docs/features/adventure-journal-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'adventure-journal checks')
