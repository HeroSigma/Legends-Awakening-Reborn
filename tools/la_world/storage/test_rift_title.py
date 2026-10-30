"""Native title preview and transitions, disposable emulator batteries only."""
from pathlib import Path
import json,hashlib,shutil
R=Path('/home/allan/projects/Legends-Awakening-Reborn')
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/art/title_screen/rift_preview';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600)
wr(symbols['gMain']+4,symbols['CB2_InitTitleScreen']|1);frames(90)
check('title_active',active('Task_LegendsTitle') is not None)
check('bitmap_mode4',rd(0x04000000,2)==0x404)
shutil.copy2(shot('rift_title_native'),D/'title-native.png')
tap(8);wait('Task_HandleMainMenuInput',1200)
check('start_opens_no_save_menu',active('Task_HandleMainMenuInput') is not None)
tap(2);wait('Task_LegendsTitle',1200);frames(90)
check('no_save_b_returns_title',active('Task_LegendsTitle') is not None)
tap(1);wait('Task_HandleMainMenuInput',1200)
check('a_opens_menu',active('Task_HandleMainMenuInput') is not None)
lib.shutdown()
for mode in [0,1]:
 start(0);invoke('ScriptGiveMon',255,16,0)
 if mode:invoke('StorageChangeMode',1,1)
 expected=(location(),pos());check(f'save_{mode}',invoke('TrySavingData',0)==1)
 frames(20,15);frames(600)
 # Skip the boot animation using a real title/menu transition.
 for i in range(2400):
  if active('Task_LegendsTitle') is not None:break
  frames(1,8 if i%120==0 else 0)
 else:raise AssertionError('title boot timeout')
 frames(90);tap(8);wait('Task_MainMenuMain',1200);frames(30)
 check(f'continue_available_{mode}',active('Task_MainMenuMain') is not None)
 tap(2);wait('Task_LegendsTitle',1200);frames(90)
 check(f'saved_b_returns_title_{mode}',active('Task_LegendsTitle') is not None)
 tap(8);wait('Task_MainMenuMain',1200);frames(30);tap(1)
 for i in range(1800):
  if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
  frames(1)
 else:raise AssertionError('continue timeout')
 frames(90)
 check(f'continue_location_{mode}',(location(),pos())==expected)
 check(f'continue_storage_{mode}',invoke('GetStorageBoxCount')==(60 if mode else 14))
 check(f'continue_party_{mode}',rd(symbols['gPartiesCount'],1)==1)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'title checks',flush=True)
