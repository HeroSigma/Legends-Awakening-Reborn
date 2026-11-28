"""Actual Birch offer/awakening scripts, consent, speaker text and no repeats."""
from pathlib import Path
R=Path.cwd()
source=(R/'tools/la_world/storage/test_legends_plates.py').read_text().split('checks=[]')[0]
source=source.replace("names=[", "names=['FLAG_BADGE03_GET','FLAG_HIDE_LITTLEROOT_TOWN_BIRCHS_LAB_BIRCH','VAR_LA_OAK_STARTER',")
exec(compile(source,'plate_helpers','exec'))
checks=[]
def check(n,v):checks.append(dict(test=n,passed=bool(v)));assert v,n
def plate_call(name,index):
 wr(symbols['gSpecialVar_0x8004'],index,2);invoke(name);return rd(symbols['gSpecialVar_Result'],2)
def qty(name):return invoke('CountTotalItemQuantityInBag',c[name])
def run_script(label,answer=None):
 invoke('ScriptContext_SetupScript',symbols[label]);offered=False
 for i in range(16000):
  if active('Task_HandleYesNoInput') is not None:
   frames(30);shutil.copy2(shot('blank_plate_offer'),D/'birch_offer.png');offered=True;tap(1 if answer else 2);frames(30)
  if i>60 and rd(symbols['sGlobalScriptContextStatus'],1)==2:
   frames(60);return offered
  frames(1,1 if i%18==0 else 0)
 raise AssertionError('Plate scene did not return control')
mg=json.loads((R/'data/maps/map_groups.json').read_text())
for group,gname in enumerate(mg['group_order']):
 if 'LittlerootTown_ProfessorBirchsLab' in mg[gname]:mid=mg[gname].index('LittlerootTown_ProfessorBirchsLab');break
start(0);invoke('VarSet',c['VAR_LA_RIFT_TRACKER'],2);invoke('VarSet',c['VAR_LA_OAK_STARTER'],10)
invoke('FlagSet',c['FLAG_BADGE03_GET']);invoke('FlagClear',c['FLAG_HIDE_LITTLEROOT_TOWN_BIRCHS_LAB_BIRCH']);warp(group,mid,6,5)
wr(symbols['gSpecialVar_LastTalked'],1,2)
wr(symbols['gSelectedObjectEvent'],invoke('GetObjectEventIdByLocalIdAndMap',1,mid,group),1)
check('actual_Birch_offer_can_decline',run_script('LittlerootTown_ProfessorBirchsLab_EventScript_Birch',False))
check('decline_grants_nothing',qty('ITEM_BLANK_PLATE')==0 and invoke('FlagGet',c['FLAG_LA_BLANK_PLATE_RECEIVED'])==0)
check('actual_Birch_retry_can_accept',run_script('LittlerootTown_ProfessorBirchsLab_EventScript_Birch',True))
check('accept_grants_one_blank',qty('ITEM_BLANK_PLATE')==1 and invoke('FlagGet',c['FLAG_LA_BLANK_PLATE_RECEIVED'])==1)
check('Birch_activates_Meadow_lead',invoke('LegendsPlates_QuestState',50)==1)
invoke('LegendsPlates_PrepareBirch');check('research_not_offered_again',rd(symbols['gSpecialVar_Result'],2)==0)
for i in range(17):
 plate_call('LegendsPlates_ActivateQuest',i);wr(symbols['gBattleOutcome'],c['B_OUTCOME_WON'],1);plate_call('LegendsPlates_RecordGuardianResult',i);plate_call('LegendsPlates_CollectResonance',i)
check('actual_Birch_awakening_has_no_second_offer',not run_script('LittlerootTown_ProfessorBirchsLab_EventScript_Birch'))
check('scene_upgrades_in_place',qty('ITEM_BLANK_PLATE')==0 and qty('ITEM_LEGEND_PLATE')==1)
check('scene_marks_awakened',invoke('FlagGet',c['FLAG_LA_LEGEND_PLATE_AWAKENED'])==1)
invoke('LegendsPlates_PrepareBirch');check('awakening_not_replayed',rd(symbols['gSpecialVar_Result'],2)==0)
check('control_restored',invoke('ArePlayerFieldControlsLocked')==0)
# Existing Blank Plate saves receive the new lead without a second grant.
start(0);invoke('VarSet',c['VAR_LA_RIFT_TRACKER'],2);invoke('VarSet',c['VAR_LA_OAK_STARTER'],10)
invoke('FlagSet',c['FLAG_BADGE03_GET']);invoke('FlagClear',c['FLAG_HIDE_LITTLEROOT_TOWN_BIRCHS_LAB_BIRCH']);warp(group,mid,6,5)
invoke('LegendsPlates_StartResearch')
check('older_research_has_no_Meadow_lead',invoke('LegendsPlates_QuestState',50)==0)
wr(symbols['gSpecialVar_LastTalked'],1,2)
wr(symbols['gSelectedObjectEvent'],invoke('GetObjectEventIdByLocalIdAndMap',1,mid,group),1)
check('older_save_lead_needs_no_second_item_offer',not run_script('LittlerootTown_ProfessorBirchsLab_EventScript_Birch'))
check('older_save_Birch_activates_Meadow',invoke('LegendsPlates_QuestState',50)==1)
check('older_save_keeps_one_Blank_Plate',qty('ITEM_BLANK_PLATE')==1)
invoke('LegendsPlates_PrepareBirch');check('older_save_lead_does_not_repeat',rd(symbols['gSpecialVar_Result'],2)==0)
lib.shutdown()
(D/'scene-validation.json').write_text(json.dumps(dict(checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'Plate scene checks',flush=True)
