"""Native selection, confirmation, cleanup and rescue callback tests."""
from pathlib import Path
import json,hashlib,shutil,struct,tempfile,subprocess
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/nine-starters';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
def capture(n):shutil.copy2(shot('starter_case_'+n),D/(n+'.png'))
def selection():return rd(rd(symbols['sStarterCase'])+12,1)
def confirming():return rd(rd(symbols['sStarterCase'])+25,1)
def open_case():
 wr(symbols['gMain']+8,symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_ChooseStarter']|1);wait('Task_StarterCase',1200);frames(80)
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\nconst unsigned values[]={MON_DATA_LEVEL,VAR_STARTER_MON};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 level_field,starter_var=struct.unpack('<2I',(td/'c.bin').read_bytes())
paths={0:[32],1:[],2:[16],3:[16,16],4:[128],5:[128,16],6:[128,32],7:[64],8:[16,64]}
groups=[0,1,2,0,2,1,0,1,2]
def choose(chosen):
 for key in paths[chosen]:tap(key)
 check(f"navigation_{chosen}",selection()==chosen)
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1)
 check(f'invalid_id_safe_{mode}',invoke('GetStarterPokemon',9)==invoke('GetStarterPokemon',0))
 for chosen in range(9):
  open_case();check(f'default_fire_{mode}_{chosen}',selection()==1)
  for _ in range(8):tap(16);frames(5)
  check(f'right_wrap_{mode}_{chosen}',selection()==1)
  for _ in range(8):tap(32);frames(5)
  check(f'left_wrap_{mode}_{chosen}',selection()==1)
  tap(2);check(f'cannot_skip_selection_{mode}_{chosen}',rd(symbols['sStarterCase'])!=0)
  tap(1);check(f'confirmation_{mode}_{chosen}',confirming())
  tap(2);check(f'decline_returns_{mode}_{chosen}',not confirming())
  choose(chosen)
  frames(20);capture(f'mode{mode}_choice{chosen}')
  tap(1);capture(f'mode{mode}_confirm{chosen}');tap(1)
  for i in range(1000):
   if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
   frames(1)
  else:raise AssertionError('return timeout')
  frames(60)
  check(f'correct_choice_{mode}_{chosen}',rd(symbols['gSpecialVar_Result'],2)==chosen)
  check(f'no_extra_gift_{mode}_{chosen}',rd(symbols['gPartiesCount'],1)==0)
  check(f'resources_released_{mode}_{chosen}',rd(symbols['sStarterCase'])==0)
  check(f'storage_preserved_{mode}_{chosen}',invoke('GetStorageBoxCount')==(60 if mode else 14))
 lib.shutdown()
# Exercise the real selection reward callback, not a custom give-mon path.
for chosen in range(9):
 start(0);invoke('CreateScriptedWildMon',261,100,0)
 invoke('ChooseStarter');wr(symbols['gMain']+4,symbols['CB2_ChooseStarter']|1)
 wait('Task_StarterCase',1200);frames(80)
 choose(chosen)
 tap(1);tap(1)
 for i in range(1400):
  if rd(symbols['gPartiesCount'],1)==1:break
  frames(1)
 else:raise AssertionError('starter was not awarded')
 check(f'native_callback_party_{chosen}',rd(symbols['gPartiesCount'],1)==1)
 check(f'native_callback_species_{chosen}',invoke('GetMonData3',symbols['gParties'],18,0)==invoke('GetStarterPokemon',chosen))
 check(f'native_callback_level_{chosen}',invoke('GetMonData3',symbols['gParties'],level_field,0)==5)
 check(f'native_callback_var_{chosen}',invoke('VarGet',starter_var)==groups[chosen])
 check(f'actual_starter_{chosen}',invoke('GetChosenStarterChoice')==chosen)
 check(f'unconventional_{chosen}',invoke('IsNonstandardStarter')==int(chosen>=3))
 check(f'starter_in_party_{chosen}',invoke('IsStarterInParty')==1)
 check(f'native_callback_cleanup_{chosen}',rd(symbols['sStarterCase'])==0)
 if chosen==1:
  for i in range(2400):
   if rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:break
   frames(1,1 if i%30==0 else 0)
  else:
   capture('battle_transition_failure')
   print('CALLBACK',hex(rd(symbols['gMain']+4)),'BATTLE',hex(rd(symbols['gBattleMainFunc'])),flush=True)
   for j in range(16):
    if rd(symbols['gTasks']+j*40+4,1):
     a=rd(symbols['gTasks']+j*40);print('TASK',j,[n for n,v in symbols.items() if v|1==a],flush=True)
   raise AssertionError('native first battle did not open')
  check('native_first_battle_ready',True)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'starter case checks',flush=True)
