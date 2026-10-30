"""Native SwSh bag healing and capture flows in real wild battles."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_bag_categories.py').read_text().split('for mode in [0,1]:')[0],'helpers','exec'))
D=R/'docs/features/swsh-bag';D.mkdir(parents=True,exist_ok=True)
# Capture uses the Master Ball to make this an interface regression, not RNG testing.
import re
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'x.c').write_text('#include "global.h"\nconst unsigned v[]={ITEM_MASTER_BALL};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'x.c'),'-o',str(td/'x.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'x.o'),str(td/'x.bin')],check=True)
 master=struct.unpack('<I',(td/'x.bin').read_bytes())[0]
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('ClearBag')
 invoke('ScriptGiveMon',25,10,0);invoke('ScriptGiveMon',7,10,0)
 invoke('AddBagItem',c['ITEM_POTION'],3);invoke('AddBagItem',master,1)
 wr(0x03007400,1);invoke('SetMonData',symbols['gParties'],c['MON_DATA_HP'],0x03007400)
 invoke('CreateScriptedWildMon',261,3,0);invoke('BattleSetup_StartWildBattle')
 for i in range(1200):
  frames(1,1 if i%30==0 else 0)
  if rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:frames(40);break
 tap(16);tap(1);frames(240);wait('Task_BagMenu_HandleInput',900)
 check('battle_bag_open_'+str(mode),category()==0)
 for _ in range(c['BAG_MEDICINE']):tap(16);frames(50)
 tap(1);frames(30);tap(1);frames(240)
 check('medicine_party_open_'+str(mode),active('Task_HandleChooseMonInput') is not None)
 tap(1)
 for i in range(600):
  frames(1,1 if i%30==0 else 0)
  if invoke('GetMonData3',symbols['gParties'],c['MON_DATA_HP'],0)>1:break
 check('battle_heal_'+str(mode),invoke('GetMonData3',symbols['gParties'],c['MON_DATA_HP'],0)>1)
 check('battle_consumes_potion_'+str(mode),invoke('CountTotalItemQuantityInBag',c['ITEM_POTION'])==2)
 for i in range(900):
  frames(1,1 if i%30==0 else 0)
  if rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:frames(40);break
 # The battle action cursor stays on Bag after the item turn.
 tap(1);frames(240);wait('Task_BagMenu_HandleInput',900)
 for _ in range(c['BAG_MEDICINE']-c['BAG_BALLS']):tap(32);frames(50)
 check('ball_pocket_'+str(mode),category()==c['BAG_BALLS'])
 shutil.copy2(shot('bag-battle-'+str(mode)),D/('battle-'+str(mode)+'.png'))
 tap(1);frames(30);tap(1)
 for i in range(1800):
  frames(1,2 if i%30==0 else 0)
  if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
 check('ball_consumed_'+str(mode),invoke('CountTotalItemQuantityInBag',master)==0)
 check('catch_joins_party_'+str(mode),invoke('CountPartyMons')==3)
 check('capture_returns_field_'+str(mode),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 lib.shutdown()
(D/'battle-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'battle bag checks')
