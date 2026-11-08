"""Native title menu tests with isolated batteries, never the release save."""
from pathlib import Path
import json, hashlib, shutil
R=Path('/home/allan/projects/Legends-Awakening-Reborn')
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0], 'helpers', 'exec'))
D=R/'docs/features/main_menu_mugshot';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)))
 assert v,n
def capture(n):shutil.copy2(shot('main_menu_'+n),D/(n+'.png'))
def menu():
 wr(symbols['gMain']+4,symbols['CB2_InitMainMenu']|1)
 wait('Task_MainMenuMain',1200);frames(30)
def selected():return rd(symbols['sSelectedOption'],1)
for gender,mode,count in [(0,0,0),(0,1,6),(1,0,1),(1,1,6)]:
 tag=f'g{gender}_mode{mode}_party{count}'
 start(gender)
 if mode:check(tag+'_enable',invoke('StorageChangeMode',mode,1)==1)
 for species in [255,656,810,559,903,679][:count]:invoke('ScriptGiveMon',species,16,0)
 expected=(location(),pos())
 check(tag+'_save',invoke('TrySavingData',0)==1)
 check(tag+'_load',invoke('LoadGameSave',0)==1)
 menu();capture(tag)
 check(tag+'_continue_default',selected()==0)
 check(tag+'_location_preserved',location()==expected[0])
 for repeat in range(3):
  if repeat==0:tap(128);tap(16)
  check(tag+f'_options_selected_{repeat}',selected()==2)
  tap(1);wait('Task_OptionMenuProcessInput',1000);frames(30)
  tap(2);wait('Task_MainMenuMain',1200);frames(30)
  check(tag+f'_options_return_{repeat}',selected()==2)
  check(tag+f'_storage_after_options_{repeat}',invoke('GetStorageBoxCount')==(60 if mode else 14))
 capture(tag+'_options_return')
 tap(64);check(tag+'_continue_selected',selected()==0)
 tap(1)
 for i in range(1500):
  if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
  frames(1)
 else:raise AssertionError(tag+'_continue_timeout')
 frames(90)
 check(tag+'_party_preserved',rd(symbols['gPartiesCount'],1)==count)
 check(tag+'_continue_same_map',(location(),pos())==expected)
 check(tag+'_storage_preserved',invoke('GetStorageBoxCount')==(60 if mode else 14))
 menu();tap(2);frames(180)
 check(tag+'_back_frees_menu',rd(symbols['sMainMenuDataPtr'])==0)
 menu();tap(128);tap(1)
 wait('Task_LegendsCreator_Update',1800)
 check(tag+'_new_game_uses_legends_creator',rd(symbols['sMainMenuDataPtr'])==0)
 capture(tag+'_creator')
 lib.shutdown()
# No-save setup keeps New Game and Options available without auto-starting.
assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600)
wr(symbols['gMain']+4,symbols['CB2_InitMainMenu']|1)
wait('Task_HandleMainMenuInput',1200);frames(30)
capture('no_save')
check('no_save_uses_native_choices',rd(symbols['sMainMenuDataPtr'])==0)
tap(128);tap(1);wait('Task_OptionMenuProcessInput',1000);frames(30)
tap(2);wait('Task_HandleMainMenuInput',1200)
check('no_save_options_return',rd(symbols['sMainMenuDataPtr'])==0)
lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'native main menu checks',flush=True)
