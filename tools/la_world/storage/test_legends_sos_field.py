"""Play the Meadow guardian's field dialogue and reward scripts in native mGBA."""
from pathlib import Path
R=Path.cwd()
source=(R/'tools/la_world/storage/test_legends_sos.py').read_text().split('checks=[]')[0]
source=source.replace("names=[","names=['FLAG_TEMP_13','ITEM_MEADOW_PLATE',")
exec(compile(source,'sos_helpers','exec'))
checks=[]
def check(n,v):checks.append(dict(test=n,passed=bool(v)));assert v,n
def until(p,limit=15000,press=False):
 for i in range(limit):
  if p():return
  frames(1,1 if press and i%20==0 else 0)
 shutil.copy2(shot('sos_field_failure'),D/'field_failure.png')
 raise AssertionError(('timeout',hex(rd(symbols['gMain']+4))))
def capture(n):shutil.copy2(shot('sos_field_'+n),D/(n+'.png'))
mg=json.loads((R/'data/maps/map_groups.json').read_text())
for g,gn in enumerate(mg['group_order']):
 if 'PetalburgWoods' in mg[gn]:n=mg[gn].index('PetalburgWoods');break
def guardian_id():return invoke('GetObjectEventIdByLocalIdAndMap',17,n,g)
def talk():
 wr(symbols['gSpecialVar_LastTalked'],17,2)
 wr(symbols['gSelectedObjectEvent'],guardian_id(),1)
 invoke('ScriptContext_SetupScript',symbols['LegendsPlates_MeadowGuardian'])
start(0)
warp(g,n,17,20)
check('guardian_hidden_without_research',guardian_id()>=16 and invoke('FlagGet',c['FLAG_TEMP_13'])==1)
invoke('VarSet',c['VAR_LA_RIFT_TRACKER'],2);invoke('LegendsPlates_StartResearch')
warp(g,n,17,20)
check('Blank_Plate_alone_does_not_spawn_guardian',guardian_id()>=16)
wr(symbols['gSpecialVar_0x8004'],3,2);invoke('LegendsPlates_ActivateQuest')
warp(g,n,17,20);frames(60)
check('activated_quest_spawns_Breloom',guardian_id()<16 and invoke('FlagGet',c['FLAG_TEMP_13'])==0)
check('guardian_and_approach_are_walkable',invoke('MapGridGetCollisionAt',24,26)==0 and invoke('MapGridGetCollisionAt',24,27)==0)
capture('meadow_guardian')
talk();until(lambda:active('Task_HandleYesNoInput') is not None,press=True);frames(20);tap(128);tap(1);frames(180)
check('decline_does_not_start_battle',rd(symbols['sSOS'],1)==0 and invoke('LegendsPlates_QuestState',50)==1)
talk();until(lambda:active('Task_HandleYesNoInput') is not None,press=True);frames(20);tap(1)
until(lambda:rd(symbols['sGlobalScriptContextStatus'],1)==2,press=True)
check('missing_party_leaves_guardian_available',rd(symbols['sSOS'],1)==0 and guardian_id()<16)
invoke('FlagSet',c['FLAG_BADGE08_GET'])
for i in range(2):
 invoke('ScriptGiveMon',c['SPECIES_LUGIA'],100,0)
 for slot in range(4):invoke('SetMonMoveSlot',symbols['gParties']+i*100,c['MOVE_SPLASH'],slot)
talk();until(lambda:active('Task_HandleYesNoInput') is not None,press=True);frames(20);tap(1)
until(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,press=True)
check('field_script_starts_real_guardian_battle',rd(symbols['sSOS'],1)==1)
bm=symbols['gBattleMons']+c['sizeof(struct BattlePokemon)']
wr(bm+c['offsetof(struct BattlePokemon,hp)'],1,2)
wr(bm+c['offsetof(struct BattlePokemon,status1)'],c['STATUS1_BURN'])
until(lambda:rd(symbols['sSOS'],1)==0,press=True)
frames(180)
until(lambda:rd(symbols['sGlobalScriptContextStatus'],1)==2,press=True)
until(lambda:rd(symbols['sGlobalScriptContextStatus'],1)==2,press=True);frames(90)
capture('meadow_collected')
check('field_reward_delivered',invoke('CountTotalItemQuantityInBag',c['ITEM_MEADOW_PLATE'])==1)
check('field_quest_claimed',invoke('LegendsPlates_QuestState',50)==3)
check('guardian_removed_after_success',guardian_id()>=16)
warp(g,n,17,20)
check('guardian_stays_hidden_on_return',guardian_id()>=16)
lib.shutdown()
(D/'field-validation.json').write_text(json.dumps(dict(checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'guardian field checks',flush=True)
