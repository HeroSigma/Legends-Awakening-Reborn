"""Catch the remaining SOS helper through the real Ball script and return callback."""
from pathlib import Path
R=Path.cwd()
source=(R/'tools/la_world/storage/test_legends_sos.py').read_text().split('checks=[]')[0]
source=source.replace("names=[","names=['FLAG_SYS_GAME_CLEAR','SPECIES_MAGIKARP','ITEM_MASTER_BALL','BALL_THROW_UNABLE_TWO_MONS','BALL_THROW_ABLE','B_OUTCOME_CAUGHT',")
source=source.replace('#include "global.h"','#include "global.h"'+chr(92)+'n#include "item_use.h"')
exec(compile(source,'capture_helpers','exec'))
D=R/'docs/features/random-wild-sos';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):checks.append(dict(test=n,passed=bool(v)));assert v,n
def until(p,limit=20000,press=False):
 for i in range(limit):
  if p():return
  frames(1,1 if press and i%20==0 else 0)
 shutil.copy2(shot('sos_capture_failure'),D/'capture_failure.png')
 print('FAIL',[(k,hex(rd(symbols[k]))) for k in ['gBattleOutcome','gBattleMainFunc','gBattlescriptCurrInstr','gLastUsedItem','gLastThrownBall']],flush=True)
 raise AssertionError('capture test timeout')
def mon(b):return symbols['gBattleMons']+b*c['sizeof(struct BattlePokemon)']
def alive(b):return rd(mon(b)+c['offsetof(struct BattlePokemon,hp)'],2)>0
start(0);invoke('FlagSet',c['FLAG_BADGE08_GET'])
for i in range(2):
 invoke('ScriptGiveMon',c['SPECIES_LUGIA'],100,0)
 for slot in range(4):invoke('SetMonMoveSlot',symbols['gParties']+i*100,c['MOVE_SPLASH'],slot)
enemy=symbols['gParties']+600
invoke('CreateRandomMon',enemy,c['SPECIES_MAGIKARP'],20)
wr(symbols['gBattleTypeFlags'],0)
until(lambda:invoke('LegendsSOS_TryPrepareWild')==1,press=False)
invoke('BattleSetup_StartDoubleWildBattle')
until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True)
until(lambda:alive(3),press=True)
until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True)
check('two_opponents_block_Ball_aim',invoke('GetBallThrowableState')==c['BALL_THROW_UNABLE_TWO_MONS'])
wr(mon(1)+c['offsetof(struct BattlePokemon,hp)'],1,2)
wr(mon(1)+c['offsetof(struct BattlePokemon,status1)'],c['STATUS1_BURN'])
until(lambda:not alive(1),press=True)
until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True)
check('one_remaining_helper_allows_Ball',invoke('GetBallThrowableState')==c['BALL_THROW_ABLE'])
check('catch_target_is_remaining_helper',invoke('GetCatchingBattler')==3)
invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])
invoke('AddBagItem',c['ITEM_MASTER_BALL'],1)
wr(symbols['gLastUsedItem'],c['ITEM_MASTER_BALL'],2);wr(symbols['gBattlerAttacker'],0,1);wr(symbols['gBattlerTarget'],3,1)
cb1=rd(symbols['gMain']);wr(symbols['gMain'],0)
invoke('BattleScriptExecute',symbols['BattleScript_BallThrow']);wr(symbols['gMain'],cb1)
until(lambda:rd(symbols['gBattleOutcome'],1)==c['B_OUTCOME_CAUGHT'],press=True)
until(lambda:rd(symbols['sSOS'],1)==0,press=True);frames(180)
check('caught_helper_added_to_party',invoke('GetMonData3',symbols['gParties']+200,c['MON_DATA_SPECIES'],0)==c['SPECIES_MAGIKARP'])
check('capture_clears_SOS',rd(symbols['sSOS'],1)==0)
check('capture_no_Plate_progress',invoke('LegendsPlates_CountCompleted')==0)
shutil.copy2(shot('sos_helper_caught'),D/'helper_caught.png')
lib.shutdown()
(D/'capture-validation.json').write_text(json.dumps(dict(checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'random SOS capture checks',flush=True)
