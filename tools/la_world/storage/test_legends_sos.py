"""Real scripted guardian introduction, reinforcements and cleanup in native mGBA."""
from pathlib import Path
import tempfile,struct,json,hashlib,subprocess,shutil
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/plate-guardian-sos';D.mkdir(parents=True,exist_ok=True)
names=['FLAG_BADGE08_GET','STATUS1_BURN','offsetof(struct BattlePokemon,status1)','VAR_LA_RIFT_TRACKER','SPECIES_LUGIA','MOVE_SPLASH','MON_DATA_HP','MON_DATA_MAX_HP','MON_DATA_SPECIES','sizeof(struct BattlePokemon)','offsetof(struct BattlePokemon,hp)','offsetof(struct BattlePokemon,statStages)','offsetof(struct BattlePokemon,species)','B_OUTCOME_WON','B_OUTCOME_RAN','B_OUTCOME_LOST','SPECIES_SHROOMISH','SPECIES_BRELOOM','STAT_DEF','STAT_SPDEF']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "battle.h"\n#include "pokemon.h"\n#include "constants/vars.h"\n#include "constants/moves.h"\n#include "constants/flags.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
checks=[]
def check(n,v):checks.append(dict(test=n,passed=bool(v)));assert v,n
def until(p,limit=15000,press=False):
 for i in range(limit):
  if p():return
  frames(1,1 if press and i%20==0 else 0)
 capture('failure')
 print('FAIL STATE',[(k,hex(rd(symbols[k],1 if k in ['gBattlerTarget','gBattlerFainted','gBattlerAttacker'] else 4))) for k in ['gBattlescriptCurrInstr','gBattlerTarget','gBattlerFainted','gBattlerAttacker']],flush=True)
 raise AssertionError(('timeout',hex(rd(symbols['gMain']+4)),hex(rd(symbols['gBattleMainFunc'])),rd(symbols['gBattleTurnCounter'],2)))
def special(name,index=3,level=40):
 wr(symbols['gSpecialVar_0x8004'],index,2);wr(symbols['gSpecialVar_0x8005'],level,2);invoke(name);return rd(symbols['gSpecialVar_Result'],2)
def mon(b):return symbols['gBattleMons']+b*c['sizeof(struct BattlePokemon)']
def alive(b):return rd(mon(b)+c['offsetof(struct BattlePokemon,hp)'],2)>0
def capture(n):shutil.copy2(shot('sos_'+n),D/(n+'.png'))
start(0)
invoke('FlagSet',c['FLAG_BADGE08_GET'])
check('unactivated_guardian_refused',special('LegendsSOS_StartGuardian')==0)
invoke('VarSet',c['VAR_LA_RIFT_TRACKER'],2);invoke('LegendsPlates_StartResearch')
check('activate_meadow',special('LegendsPlates_ActivateQuest')==1)
check('two_ready_Pokemon_required',special('LegendsSOS_StartGuardian')==2)
for i in range(2):
 invoke('ScriptGiveMon',c['SPECIES_LUGIA'],100,0)
 for slot in range(4):invoke('SetMonMoveSlot',symbols['gParties']+i*100,c['MOVE_SPLASH'],slot)
check('invalid_level_refused',special('LegendsSOS_StartGuardian',3,0)==0)
check('guardian_started',special('LegendsSOS_StartGuardian')==1)
until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True)
frames(30);capture('guardian_intro')
check('double_battle_starts_with_guardian_alone',rd(symbols['gBattlersCount'],1)==4 and alive(1) and not alive(3))
check('guardian_species',rd(mon(1)+c['offsetof(struct BattlePokemon,species)'],2)==c['SPECIES_BRELOOM'])
check('totem_defenses_boosted',all(rd(mon(1)+c['offsetof(struct BattlePokemon,statStages)']+c[x],1)==7 for x in ['STAT_DEF','STAT_SPDEF']))
check('guardian_capture_blocked',invoke('IsStoryBattleCaptureBlocked')==1)
# Repeated A advances text, Fight, first move and target selection naturally.
until(lambda:alive(3),press=True);frames(200);capture('ally_arrived')
check('ally_arrives_during_battle',rd(mon(3)+c['offsetof(struct BattlePokemon,species)'],2)==c['SPECIES_SHROOMISH'])
check('first_ally_uses_fresh_party_slot',rd(symbols['gBattlerPartyIndexes']+6,2)==1)
# Finish the arrival script and reach input before asserting no duplicate call.
until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True)
check('occupied_slot_prevents_call',invoke('LegendsSOS_TryCall')==0)

def burn_next_turn(b):
 wr(mon(b)+c['offsetof(struct BattlePokemon,hp)'],1,2)
 wr(mon(b)+c['offsetof(struct BattlePokemon,status1)'],c['STATUS1_BURN'])
burn_next_turn(3)
until(lambda:rd(symbols['gBattlerPartyIndexes']+6,2)==2 and alive(3),press=True)
until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True)
capture('second_ally')
check('replacement_call_uses_second_fresh_slot',rd(symbols['gBattlerPartyIndexes']+6,2)==2)
burn_next_turn(3)
until(lambda:not alive(3),press=True)
turn=rd(symbols['gBattleTurnCounter'],2)
until(lambda:rd(symbols['gBattleTurnCounter'],2)>=turn+3,press=True)
check('no_third_reinforcement',not alive(3) and rd(symbols['gBattlerPartyIndexes']+6,2)==2)
until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True)
burn_next_turn(1)
until(lambda:rd(symbols['sSOS'],1)==0,press=True)
frames(180);capture('guardian_victory')
check('actual_victory_records_pending_resonance',invoke('LegendsPlates_QuestState',50)==2)
check('victory_does_not_auto_deliver_Plate',invoke('LegendsPlates_CountCompleted')==0)
check('victory_clears_capture_restriction',invoke('IsStoryBattleCaptureBlocked')==0)
check('claim_after_battle_once',special('LegendsPlates_CollectResonance')==1 and special('LegendsPlates_CollectResonance')==0)
# A fresh ordinary scripted wild battle cannot inherit reinforcement state.
invoke('CreateRandomMon',symbols['gParties']+600,c['SPECIES_LUGIA'],5)
invoke('BattleSetup_StartScriptedWildBattle')
until(lambda:rd(symbols['gBattlersCount'],1)==2,press=True)
check('ordinary_wild_battle_keeps_single_format',rd(symbols['gBattlersCount'],1)==2)
check('ordinary_battle_does_not_call_for_help',invoke('LegendsSOS_TryCall')==0)
check('ordinary_battle_capture_allowed',invoke('IsStoryBattleCaptureBlocked')==0)
lib.shutdown()

for outcome in ['run','loss']:
 start(0);invoke('FlagSet',c['FLAG_BADGE08_GET'])
 invoke('VarSet',c['VAR_LA_RIFT_TRACKER'],2);invoke('LegendsPlates_StartResearch')
 special('LegendsPlates_ActivateQuest')
 for i in range(2):
  invoke('ScriptGiveMon',c['SPECIES_LUGIA'],100,0)
  for slot in range(4):invoke('SetMonMoveSlot',symbols['gParties']+i*100,c['MOVE_SPLASH'],slot)
 check(outcome+'_start',special('LegendsSOS_StartGuardian')==1)
 until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True)
 if outcome=='run':
  check('native_escape_resolves',invoke('TryRunFromBattle',0)==1)
 else:
  burn_next_turn(0);burn_next_turn(2)
 until(lambda:rd(symbols['sSOS'],1)==0,press=True)
 frames(180)
 check(outcome+'_quest_remains_active',invoke('LegendsPlates_QuestState',50)==1)
 check(outcome+'_no_reward',invoke('LegendsPlates_CountCompleted')==0)
 check(outcome+'_clears_SOS',rd(symbols['sSOS'],1)==0)
 lib.shutdown()
print('PASS',len(checks),'SOS battle checks',flush=True)
(D/'validation.json').write_text(json.dumps(dict(checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
