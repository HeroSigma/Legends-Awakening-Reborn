"""Real Wattson script and battle state in singles and doubles, isolated saves."""
from pathlib import Path
R=Path.cwd()
source=(R/'tools/la_world/storage/test_gimmick_shop_milestones.py').read_text().split('checks=[]')[0]
source=source.replace("names=[", "names=['MON_DATA_HELD_ITEM','VAR_LA_PARADIGM_ARC','VAR_LA_MAUVILLE_RIFT','sizeof(struct BattlePokemon)','offsetof(struct BattleStruct,gimmick.usableGimmick)','GIMMICK_MEGA',")
source=source.replace('#include "item.h"\\n','#include "item.h"\\n#include "battle.h"\\n#include "battle_gimmick.h"\\n#include "constants/vars.h"\\n')
exec(compile(source,'gimmick_helpers','exec'))
checks=[]
def check(n,v):checks.append(dict(test=n,passed=bool(v)));assert v,n
def until(predicate,limit=12000,press=False):
 for i in range(limit):
  if predicate():return
  frames(1,1 if press and i%20==0 else 0)
 raise AssertionError(('timeout',hex(rd(symbols['gMain']+4))))
mg=json.loads((R/'data/maps/map_groups.json').read_text())
for group,gname in enumerate(mg['group_order']):
 if 'MauvilleCity_Gym' in mg[gname]:mid=mg[gname].index('MauvilleCity_Gym');break
for double in [False,True]:
 start(0)
 for name in ['FLAG_LA_RED_DEX_GIFTS','FLAG_BADGE01_GET','FLAG_BADGE02_GET']:invoke('FlagSet',c[name])
 invoke('VarSet',c['VAR_LA_PARADIGM_ARC'],1);invoke('VarSet',c['VAR_LA_MAUVILLE_RIFT'],3)
 for species in [1,4,7,25,133,155]:invoke('ScriptGiveMon',species,26,0)
 warp(group,mid,5,3)
 wr(symbols['gSpecialVar_LastTalked'],1,2)
 wr(symbols['gSelectedObjectEvent'],invoke('GetObjectEventIdByLocalIdAndMap',1,mid,group),1)
 invoke('ScriptContext_SetupScript',symbols['MauvilleCity_Gym_EventScript_Wattson'])
 until(lambda:active('Task_HandleMultichoiceInput') is not None,press=True);frames(20)
 if double:tap(128)
 tap(1);until(lambda:active('Task_HandleYesNoInput') is not None);frames(20);tap(1)
 until(lambda:rd(symbols['gBattlersCount'],1)==(4 if double else 2),press=True)
 until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True);frames(30)
 check(f'{double}_actual_battle_Mega_configuration',invoke('LegendsTrainer_Gimmick',c['TRAINER_WATTSON_1'])==4)
 opponent=symbols['gParties']+600;ace=opponent+500
 check(f'{double}_ace_has_Manectite',invoke('GetMonData3',ace,c['MON_DATA_HELD_ITEM'],0)==c['ITEM_MANECTITE'])
 # Inspect the ace on the enemy battler, using the same conversion as a switch-in.
 wr(symbols['gBattlerPartyIndexes']+2,5,2)
 invoke('PokemonToBattleMon',ace,symbols['gBattleMons']+c['sizeof(struct BattlePokemon)'])
 check(f'{double}_native_Mega_eligible',invoke('CanMegaEvolve',1)==1)
 invoke('AssignUsableGimmicks')
 b=rd(symbols['gBattleStruct'])+c['offsetof(struct BattleStruct,gimmick.usableGimmick)']
 check(f'{double}_engine_assigns_Mega',rd(b+1,1)==c['GIMMICK_MEGA'])
 lib.shutdown()
(D/'battle-validation.json').write_text(json.dumps(dict(checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'live Wattson Mega battle checks',flush=True)
