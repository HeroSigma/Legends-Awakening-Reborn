"""Native random-SOS eligibility, probability, helpers and ordinary capture rules."""
from pathlib import Path
R=Path.cwd()
source=(R/'tools/la_world/storage/test_legends_sos.py').read_text().split('checks=[]')[0]
source=source.replace("names=[","names=['ITEM_MASTER_BALL','SPECIES_MEWTWO','SPECIES_PIKACHU','BATTLE_TYPE_TRAINER','BATTLE_TYPE_DOUBLE','BATTLE_TYPE_SAFARI','MON_DATA_LEVEL',")
exec(compile(source,'sos_helpers','exec'))
D=R/'docs/features/random-wild-sos';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):checks.append(dict(test=n,passed=bool(v)));assert v,n
def until(p,limit=20000,press=False):
 for i in range(limit):
  if p():return
  frames(1,1 if press and i%20==0 else 0)
 shutil.copy2(shot('random_sos_failure'),D/'failure.png')
 raise AssertionError(('timeout',hex(rd(symbols['gMain']+4))))
def mon(b):return symbols['gBattleMons']+b*c['sizeof(struct BattlePokemon)']
def alive(b):return rd(mon(b)+c['offsetof(struct BattlePokemon,hp)'],2)>0
def capture(n):shutil.copy2(shot('random_sos_'+n),D/(n+'.png'))
enemy=symbols['gParties']+600
start(0)
invoke('CreateRandomMon',enemy,c['SPECIES_SHROOMISH'],20)
check('no_party_no_SOS',invoke('LegendsSOS_TryPrepareWild')==0)
invoke('ScriptGiveMon',c['SPECIES_LUGIA'],100,0)
check('one_ready_partner_keeps_normal_battle',invoke('LegendsSOS_TryPrepareWild')==0)
invoke('ScriptGiveMon',c['SPECIES_LUGIA'],100,0)
for flag in ['BATTLE_TYPE_TRAINER','BATTLE_TYPE_DOUBLE','BATTLE_TYPE_SAFARI']:
 wr(symbols['gBattleTypeFlags'],c[flag])
 check(flag+'_excluded',all(invoke('LegendsSOS_TryPrepareWild')==0 for i in range(20)))
wr(symbols['gBattleTypeFlags'],0)
for species in ['SPECIES_MEWTWO','SPECIES_LUGIA']:
 invoke('CreateRandomMon',enemy,c[species],30)
 check(species+'_never_calls',all(invoke('LegendsSOS_TryPrepareWild')==0 for i in range(20)))
invoke('CreateRandomMon',enemy,c['SPECIES_SHROOMISH'],20)
original=bytes(rd(enemy+i,1) for i in range(100))
accepted=0
for i in range(1000):
 if invoke('LegendsSOS_TryPrepareWild'):
  accepted+=1
  check('wild_not_guardian_'+str(i),invoke('LegendsSOS_IsGuardian')==0)
  invoke('LegendsSOS_Finish')
check('eligibility_is_occasional',70<=accepted<=180)
check('caller_data_preserved',bytes(rd(enemy+i,1) for i in range(100))==original)
check('random_SOS_never_grants_Plate_receipts',invoke('LegendsPlates_CountCompleted')==0)
# Start a real DexNav encounter through its dedicated production hook, retrying its
# natural eligibility roll rather than using a test-only forced encounter.
invoke('FlagSet',c['FLAG_BADGE08_GET'])
for i in range(2):
 for slot in range(4):invoke('SetMonMoveSlot',symbols['gParties']+i*100,c['MOVE_SPLASH'],slot)
for attempt in range(100):
 wr(symbols['gDexNavSpecies'],c['SPECIES_SHROOMISH'],2)
 invoke('CreateRandomMon',enemy,c['SPECIES_SHROOMISH'],20)
 invoke('BattleSetup_StartDexNavBattle')
 if rd(symbols['sSOS'],1):break
 # A normal encounter is still at its field transition task. Fresh boot avoids
 # advancing a pending transition while preparing the next native trial.
 start(0);invoke('FlagSet',c['FLAG_BADGE08_GET'])
 for i in range(2):
  invoke('ScriptGiveMon',c['SPECIES_LUGIA'],100,0)
  for slot in range(4):invoke('SetMonMoveSlot',symbols['gParties']+i*100,c['MOVE_SPLASH'],slot)
else:raise AssertionError('no random SOS encounter in 100 trials')
until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True)
check('production_hook_starts_double_with_caller_alone',rd(symbols['gBattlersCount'],1)==4 and alive(1) and not alive(3))
check('wild_capture_not_story_blocked',invoke('IsStoryBattleCaptureBlocked')==0)
check('full_HP_call_chance_25_percent',invoke('LegendsSOS_GetCallChance')==25)
hp=rd(mon(1)+c['offsetof(struct BattlePokemon,hp)'],2)
wr(mon(1)+c['offsetof(struct BattlePokemon,hp)'],max(1,hp//2),2)
check('half_HP_call_chance_50_percent',invoke('LegendsSOS_GetCallChance')==50)
wr(mon(1)+c['offsetof(struct BattlePokemon,hp)'],1,2)
check('quarter_HP_call_chance_75_percent',invoke('LegendsSOS_GetCallChance')==75)
# Restore caller HP and observe the real end-turn RNG/arrival.
wr(mon(1)+c['offsetof(struct BattlePokemon,hp)'],hp,2)
until(lambda:alive(3),press=True)
until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True)
capture('random_helper')
check('DexNav_search_species_unchanged_during_SOS',rd(symbols['gDexNavSpecies'],2)==c['SPECIES_SHROOMISH'])
check('helper_matches_caller_species',rd(mon(3)+c['offsetof(struct BattlePokemon,species)'],2)==c['SPECIES_SHROOMISH'])
check('helper_level_matches_local_caller',invoke('GetMonData3',enemy+100,c['MON_DATA_LEVEL'],0)==18)
check('wild_SOS_remains_catchable',invoke('IsStoryBattleCaptureBlocked')==0)
# End through native run resolution; no guardian receipt may be generated.
check('native_escape_works',invoke('TryRunFromBattle',0)==1)
until(lambda:rd(symbols['sSOS'],1)==0,press=True);frames(180)
check('wild_exit_clears_session',rd(symbols['sSOS'],1)==0)
check('wild_exit_no_Plate_credit',invoke('LegendsPlates_CountCompleted')==0)
# A story's ordinary scripted entry remains excluded even with a stale DexNav
# species. Only the dedicated DexNav script explicitly opts in.
invoke('CreateRandomMon',enemy,c['SPECIES_SHROOMISH'],20)
wr(symbols['gDexNavSpecies'],c['SPECIES_SHROOMISH'],2)
invoke('BattleSetup_StartScriptedWildBattle')
check('scripted_story_entry_never_enables_SOS',rd(symbols['sSOS'],1)==0)
check('scripted_story_entry_keeps_single_format',rd(symbols['gBattleTypeFlags'])==0)
lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(checks=checks,eligible_trials=1000,eligible=accepted,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'random SOS checks; eligibility',accepted,'/1000',flush=True)
