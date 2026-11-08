"""Native player Band unlock and generated trainer ace eligibility."""
from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct,json,hashlib
names=['FLAG_LA_RED_DEX_GIFTS','TRAINER_CALVIN_1','ITEM_DYNAMAX_BAND','ITEM_TERA_ORB','offsetof(struct BattleStruct,gimmick.usableGimmick)','ITEM_CHARIZARDITE_X','ITEM_NORMALIUM_Z','sizeof(struct BattlePokemon)','offsetof(struct BattlePokemon,item)','sizeof(struct Pokemon)']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "battle.h"\n#include "constants/flags.h"\n#include "constants/items.h"\n#include "constants/opponents.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
start(0);invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
seen=set()
for seed in range(32):
 for j in range(4):wr(rd(symbols['gSaveBlock2Ptr'])+10+j,(seed>>(8*j))&255,1)
 seen.add(invoke('LegendsTrainer_Gimmick',c['TRAINER_CALVIN_1']))
check('ordinary_trainers_support_three_gimmicks',seen=={1,2,3})
for seed in range(32):
 for j in range(4):wr(rd(symbols['gSaveBlock2Ptr'])+10+j,(seed>>(8*j))&255,1)
 if invoke('LegendsTrainer_Gimmick',c['TRAINER_CALVIN_1'])==3:break
for sp in [1,4,7,25,133,155]:invoke('ScriptGiveMon',sp,16,0)
warp(0,17,37,16)
wr(symbols['gSpecialVar_LastTalked'],2,2)
wr(symbols['gSelectedObjectEvent'],invoke('GetObjectEventIdByLocalIdAndMap',2,17,0),1)
invoke('ScriptContext_SetupScript',symbols['Route102_EventScript_Calvin'])
for i in range(16000):
 frames(1,1 if i%24<3 else 0)
 if rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1 and rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:break
else:raise AssertionError('Battle did not reach action selection')
check('player_without_band_cannot_dynamax',invoke('CanDynamax',0)==0)
invoke('AddBagItem',c['ITEM_DYNAMAX_BAND'],1)
check('band_unlocks_player_without_arena_flag',invoke('CanDynamax',0)==1)
item=symbols['gBattleMons']+c['offsetof(struct BattlePokemon,item)']
for n in ['ITEM_CHARIZARDITE_X','ITEM_NORMALIUM_Z']:
 wr(item,c[n],2)
 check('held_gimmick_blocks_dynamax_'+n,invoke('CanDynamax',0)==0)
wr(item,0,2)
check('removing_gimmick_item_restores_dynamax',invoke('CanDynamax',0)==1)
check('ordinary_first_mon_not_dynamax_ace',invoke('CanDynamax',1)==0)
wr(symbols['gBattlerPartyIndexes']+2,5,2)
invoke('PokemonToBattleMon',symbols['gParties']+11*c['sizeof(struct Pokemon)'],symbols['gBattleMons']+c['sizeof(struct BattlePokemon)'])
check('actual_generated_trainer_ace_can_dynamax',invoke('CanDynamax',1)==1)
invoke('AddBagItem',c['ITEM_TERA_ORB'],1)
invoke('AssignUsableGimmicks')
tap(1);frames(60)
gimmick=rd(symbols['gBattleStruct'])+c['offsetof(struct BattleStruct,gimmick.usableGimmick)']
check('move_menu_starts_with_dynamax',rd(gimmick,1)==4)
tap(4);frames(15)
check('select_cycles_to_tera',rd(gimmick,1)==5)
tap(4);frames(15)
check('select_cycles_back_to_dynamax',rd(gimmick,1)==4)
tap(8);frames(15)
check('start_selects_dynamax',invoke('IsGimmickSelected',0,4)==1)
print(shot('dynamax_band_unlocked'),flush=True)
report=dict(passed=True,checks=checks,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),user_save_loaded=False)
(R/'docs/features/dynamax-band-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS',len(checks),'Dynamax checks',flush=True)
