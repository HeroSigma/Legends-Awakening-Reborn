"""Native icon menu lifecycle, options palette choice, and save compatibility."""
from pathlib import Path
import tempfile,struct
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/custom-start-menu';D.mkdir(exist_ok=True)
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/flags.h"\n#include "dexnav.h"\nconst unsigned v[]={FLAG_SYS_POKEDEX_GET,FLAG_SYS_POKEMON_GET,FLAG_SYS_POKENAV_GET,DN_FLAG_DEXNAV_GET};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True);flags=struct.unpack('<4I',(td/'c.bin').read_bytes())
def openmenu(page=0):
 wr(symbols['sStartMenuPage'],page,1);wr(symbols['sStartMenuCursorPos'],0,1);tap(8);frames(50)
 check('icon menu active',rd(symbols['sCustomMenu'])!=0)
for mode in [0,1]:
 start(mode);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',25,16,0)
 for f in flags:invoke('FlagSet',f)
 for theme in range(4):
  invoke('CustomStartMenu_SetTheme',theme)
  openmenu()
  check('theme getter '+str((mode,theme)),invoke('CustomStartMenu_GetTheme')==theme)
  shutil.copy2(shot('menu_theme_'+str(mode)+'_'+str(theme)),D/('theme-'+str(mode)+'-'+str(theme)+'.png'))
  tap(2);frames(20);check('theme menu closes',rd(symbols['sCustomMenu'])==0 and invoke('ArePlayerFieldControlsLocked')==0)
 invoke('CustomStartMenu_SetTheme',0);openmenu()
 for _ in range(6):tap(128)
 tap(1);frames(180)
 t=active('Task_OptionMenuProcessInput');check('options opened',t is not None)
 wr(symbols['gTasks']+t*40+8,7,2);tap(16);frames(4)
 check('theme changed through Options',rd(symbols['gTasks']+t*40+24,2)==1)
 shutil.copy2(shot('menu_options_'+str(mode)),D/('options-'+str(mode)+'.png'))
 tap(2);frames(240);check('Options returns to icon menu',rd(symbols['sCustomMenu'])!=0)
 check('Options choice persisted in variable',invoke('CustomStartMenu_GetTheme')==1)
 tap(2);frames(30)
 check('storage mode unaffected',invoke('StorageIsCollectionMode')==mode)
 check('save with chosen theme',invoke('TrySavingData',0)==1)
 invoke('CustomStartMenu_SetTheme',3);check('save reload',invoke('LoadGameSave',0)==1)
 check('theme survives save load',invoke('CustomStartMenu_GetTheme')==1)
 # Save confirmation must remove custom art, and cancellation rebuilds it.
 openmenu()
 for _ in range(5):tap(128)
 tap(1);frames(50);check('save dialog clears icons',rd(symbols['sCustomMenu'])==0)
 shutil.copy2(shot('custom_save'),D/'save.png')
 frames(120);tap(2);frames(100);check('cancel save rebuilds icons',rd(symbols['sCustomMenu'])!=0)
 tap(2);frames(30)
 # Opening the Journal uses the native field overlay and clears menu resources.
 openmenu(1);tap(128);tap(1);frames(40)
 check('Journal opens',active('Task_AdventureJournal') is not None and rd(symbols['sCustomMenu'])==0)
 tap(2);frames(30)
 check('Journal returns control',invoke('ArePlayerFieldControlsLocked')==0)
 for i in range(12):
  openmenu(i%2);tap(2);frames(5);check('repeat clean '+str((mode,i)),rd(symbols['sCustomMenu'])==0)
 invoke('CustomStartMenu_SetTheme',999);check('invalid theme clamped',invoke('CustomStartMenu_GetTheme')==0)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps({'passed':True,'checks':checks,'rom_sha256':hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()},indent=2)+'\n')
print('PASS',len(checks),'custom menu checks')
