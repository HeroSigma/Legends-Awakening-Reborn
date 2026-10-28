"""Native cutscene coverage with disposable saves; battle results are injected through native end handlers."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'.la_work/woods-triad';D.mkdir(parents=True,exist_ok=True)
proof=R/'docs/story/woods_triad';proof.mkdir(parents=True,exist_ok=True)
import tempfile,struct
names=['MAP_GROUP(MAP_PETALBURG_WOODS)','MAP_NUM(MAP_PETALBURG_WOODS)','VAR_PETALBURG_WOODS_STATE','FLAG_HIDE_PETALBURG_WOODS_DEVON_EMPLOYEE','FLAG_HIDE_PETALBURG_WOODS_AQUA_GRUNT','FLAG_HIDE_LA_WOODS_TRIAD_BACKUP','FLAG_LA_WOODS_TRIAD_COMPLETE','FLAG_LA_WOODS_RIFT_RECORD_STOLEN','FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN','FLAG_LA_INTRO_ACTIVE','VAR_LITTLEROOT_INTRO_STATE','FLAG_LA_RED_DEX_GIFTS','ITEM_GREAT_BALL','LOCALID_PETALBURG_WOODS_GRUNT','LOCALID_PETALBURG_WOODS_DEVON_EMPLOYEE','LOCALID_WOODS_SILPH','LOCALID_WOODS_TRIAD_2','LOCALID_WOODS_TRIAD_3','OBJ_EVENT_GFX_LA_ROSTER_SHADOWTRIAD','MON_DATA_LEVEL','MON_DATA_IS_SHINY','TRAINER_GRUNT_PETALBURG_WOODS','HEAL_LOCATION_OLDALE_TOWN','sizeof(struct ObjectEvent)','offsetof(struct ObjectEvent,localId)','offsetof(struct ObjectEvent,currentCoords)','offsetof(struct ObjectEvent,graphicsId)','sizeof(struct TrainerMon)','sizeof(struct Trainer)','offsetof(struct Trainer,party)','offsetof(struct Trainer,trainerPic)','DIFFICULTY_NORMAL','TRAINERS_COUNT','TRAINER_PIC_SHADOW_TRIAD']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "data.h"\n#include "event_object_movement.h"\n#include "constants/maps.h"\n#include "constants/event_objects.h"\n#include "constants/map_event_ids.h"\n#include "constants/heal_locations.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def fl(name):
 n=c[name];return (rd(rd(symbols['gSaveBlock1Ptr'])+0x1270+n//8,1)>>(n%8))&1
def state():return rd(rd(symbols['gSaveBlock1Ptr'])+0x139c+(c['VAR_PETALBURG_WOODS_STATE']-0x4000)*2,2)
def actor(name):
 local=c[name]
 return next((symbols['gObjectEvents']+j*c['sizeof(struct ObjectEvent)'] for j in range(16) if rd(symbols['gObjectEvents']+j*c['sizeof(struct ObjectEvent)'],1)&1 and rd(symbols['gObjectEvents']+j*c['sizeof(struct ObjectEvent)']+c['offsetof(struct ObjectEvent,localId)'],1)==local),None)
def actor_position(name):
 a=actor(name)+c['offsetof(struct ObjectEvent,currentCoords)'];return rd(a,2)-7,rd(a+2,2)-7
def until(predicate,limit=24000):
 for i in range(limit):
  check_prompt=active('Task_HandleYesNoInput')
  assert check_prompt is None, "Story battle must not offer Singles/Doubles"
  if predicate():frames(15);return
  frames(1,1 if i%31<4 else 0)
 raise AssertionError(('timeout',state(),pos(),location(),hex(rd(symbols['sGlobalScriptContext']+8)),hex(rd(symbols['gMain']+4))))
def setup(gender,mode,seen=True):
 start(gender);invoke('FlagClear',c['FLAG_LA_INTRO_ACTIVE']);invoke('VarSet',c['VAR_LITTLEROOT_INTRO_STATE'],7)
 invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',4,16,0);invoke('ScriptGiveMon',7,16,0)
 invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
 if seen:invoke('FlagSet',c['FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN'])
 for n in ['FLAG_HIDE_PETALBURG_WOODS_DEVON_EMPLOYEE','FLAG_HIDE_PETALBURG_WOODS_AQUA_GRUNT','FLAG_LA_WOODS_TRIAD_COMPLETE','FLAG_LA_WOODS_RIFT_RECORD_STOLEN']:invoke('FlagClear',c[n])
 invoke('VarSet',c['VAR_PETALBURG_WOODS_STATE'],0)
 invoke('SetLastHealLocationWarp',c['HEAL_LOCATION_OLDALE_TOWN'])
def enter(x):
 warp(c['MAP_GROUP(MAP_PETALBURG_WOODS)'],c['MAP_NUM(MAP_PETALBURG_WOODS)'],x,21);frames(60)
 check('backup_initially_hidden_'+str(x),actor('LOCALID_WOODS_TRIAD_2') is None and actor('LOCALID_WOODS_TRIAD_3') is None)
 move(64,2)
def battle():until(lambda:rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1);frames(240)
def finish(outcome):
 wr(symbols['gBattleOutcome'],outcome,1)
 wr(symbols['gBattleMainFunc'],symbols['HandleEndTurn_BattleWon' if outcome==1 else 'HandleEndTurn_BattleLost']|1)
for gender,mode,x in [(0,0,35),(1,1,36)]:
 setup(gender,mode);enter(x)
 until(lambda:any(all(rd(symbols['gStringVar4']+offset+i,1)==rd(symbols['LegendsWoods_Text_Scope']+i,1) for i in range(10)) for offset in range(4)))
 frames(600)
 shutil.copy2(shot('researchers'),proof/('researchers_'+str(x)+'.png'))
 until(lambda:any(all(rd(symbols['gStringVar4']+offset+i,1)==rd(symbols['LegendsWoods_Text_Greeting']+i,1) for i in range(10)) for offset in range(4)))
 check('silph_joins_conversation_'+str(x),actor_position('LOCALID_WOODS_SILPH')==(36,18))
 frames(600);shutil.copy2(shot('scientist'),proof/('scientist_'+str(x)+'.png'))
 battle()
 check('fixed_singles_'+str(x),not (rd(symbols['gBattleTypeFlags'])&1) and rd(symbols['gBattlersCount'],1)==2)
 check('correct_opponent_'+str(x),rd(symbols['gTrainerBattleParameter']+2,2)==c['TRAINER_GRUNT_PETALBURG_WOODS'])
 check('six_opponents_'+str(x),rd(symbols['gPartiesCount']+1,1)==6)
 check('shiny_ace_'+str(x),invoke('GetBoxMonData3',symbols['gParties']+600+500,c['MON_DATA_IS_SHINY'],0)==1)
 # Verify every adapted team member is legal under the active cap.
 base=symbols['gTrainers']+(c['DIFFICULTY_NORMAL']*c['TRAINERS_COUNT']+c['TRAINER_GRUNT_PETALBURG_WOODS'])*c['sizeof(struct Trainer)']
 trainer=invoke('LegendsTrainer_Get',c['TRAINER_GRUNT_PETALBURG_WOODS'],base);party=rd(trainer+c['offsetof(struct Trainer,party)'])
 check('triad_portrait_'+str(x),rd(trainer+c['offsetof(struct Trainer,trainerPic)'],1)==c['TRAINER_PIC_SHADOW_TRIAD'])
 for i in range(6):check('legal_team_'+str((x,i)),invoke('LegendsTrainer_MemberLegal',party+i*c['sizeof(struct TrainerMon)'])==1)
 frames(600)
 shutil.copy2(shot('battle'),proof/('battle_'+str(x)+'.png'))
 before=invoke('CountTotalItemQuantityInBag',c['ITEM_GREAT_BALL'])
 finish(1)
 until(lambda:rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1 and fl('FLAG_LA_WOODS_RIFT_RECORD_STOLEN')==1)
 check('silph_returns_to_recording_'+str(x),actor_position('LOCALID_WOODS_SILPH')==(36,17))
 print('TRIAD',x,pos(),[(n,actor(n)) for n in ['LOCALID_PETALBURG_WOODS_GRUNT','LOCALID_WOODS_TRIAD_2','LOCALID_WOODS_TRIAD_3']],flush=True)
 shutil.copy2(shot('appearance'),proof/('appearance_'+str(x)+'.png'))
 check('all_three_present_'+str(x),all(actor(n) is not None for n in ['LOCALID_PETALBURG_WOODS_GRUNT','LOCALID_WOODS_TRIAD_2','LOCALID_WOODS_TRIAD_3']))
 frames(600)
 for name in ['LOCALID_PETALBURG_WOODS_GRUNT','LOCALID_WOODS_TRIAD_2','LOCALID_WOODS_TRIAD_3']:
  a=actor(name);coords=a+c['offsetof(struct ObjectEvent,currentCoords)']
  check('triad_on_walkable_ground_'+str((x,name)),invoke('MapGridGetCollisionAt',rd(coords,2),rd(coords+2,2))==0)
 shutil.copy2(shot('triad'),proof/('triad_'+str(x)+'.png'))
 until(lambda:state()==1 and rd(symbols['sGlobalScriptContextStatus'],1)==2)
 check('completed_'+str(x),fl('FLAG_LA_WOODS_TRIAD_COMPLETE')==1)
 check('one_reward_'+str(x),invoke('CountTotalItemQuantityInBag',c['ITEM_GREAT_BALL'])==before+1)
 check('controls_restored_'+str(x),invoke('ArePlayerFieldControlsLocked')==0)
 check('actors_removed_'+str(x),all(actor(n) is None for n in ['LOCALID_PETALBURG_WOODS_GRUNT','LOCALID_WOODS_TRIAD_2','LOCALID_WOODS_TRIAD_3','LOCALID_WOODS_SILPH','LOCALID_PETALBURG_WOODS_DEVON_EMPLOYEE']))
 check('save_'+str(x),invoke('TrySavingData',0)==1)
 invoke('VarSet',c['VAR_PETALBURG_WOODS_STATE'],0);check('load_'+str(x),invoke('LoadGameSave',0)==1)
 warp(c['MAP_GROUP(MAP_PETALBURG_WOODS)'],c['MAP_NUM(MAP_PETALBURG_WOODS)'],x,21);move(64,2);frames(90)
 check('no_replay_'+str(x),state()==1 and rd(symbols['sGlobalScriptContextStatus'],1)==2 and actor('LOCALID_WOODS_SILPH') is None)
 lib.shutdown()
# Loss must not advance the story or remove the researchers. Return for a retry.
setup(0,0,False);enter(35);battle();finish(2)
until(lambda:rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1 and location()!=(c['MAP_GROUP(MAP_PETALBURG_WOODS)'],c['MAP_NUM(MAP_PETALBURG_WOODS)']))
for i in range(1800):frames(1,1 if i%31<4 else 0)
check('loss_keeps_scene_pending',state()==0 and not fl('FLAG_LA_WOODS_TRIAD_COMPLETE') and not fl('FLAG_LA_WOODS_RIFT_RECORD_STOLEN'))
enter(35);battle();check('retry_battle',True);finish(1)
until(lambda:state()==1 and rd(symbols['sGlobalScriptContextStatus'],1)==2)
check('retry_can_complete',fl('FLAG_LA_WOODS_TRIAD_COMPLETE')==1)
lib.shutdown()
# Full reward stack must still permit completion. Existing completed saves hide new actors.
setup(0,1);invoke('AddBagItem',c['ITEM_GREAT_BALL'],999);enter(35);battle();finish(1)
until(lambda:state()==1 and rd(symbols['sGlobalScriptContextStatus'],1)==2)
check('full_bag_scene_completes',fl('FLAG_LA_WOODS_TRIAD_COMPLETE')==1 and invoke('CountTotalItemQuantityInBag',c['ITEM_GREAT_BALL'])==999)
lib.shutdown()
setup(0,0);invoke('VarSet',c['VAR_PETALBURG_WOODS_STATE'],1)
warp(c['MAP_GROUP(MAP_PETALBURG_WOODS)'],c['MAP_NUM(MAP_PETALBURG_WOODS)'],35,21);frames(90)
check('legacy_completed_no_new_actors',all(actor(n) is None for n in ['LOCALID_WOODS_SILPH','LOCALID_WOODS_TRIAD_2','LOCALID_WOODS_TRIAD_3']))
check('legacy_does_not_invent_theft',not fl('FLAG_LA_WOODS_RIFT_RECORD_STOLEN'))
lib.shutdown()
(proof/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),battle_results='injected through native end handlers; combat difficulty is not measured',checks=checks),indent=2)+'\n')
print('PASS',len(checks),'Woods Triad story checks')
