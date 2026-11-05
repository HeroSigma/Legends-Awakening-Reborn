"""Native May -> Silver scene, legal teams and independent retry checkpoint.
Disposable saves only. Battle outcomes are injected after native turn readiness.
"""
from pathlib import Path
import tempfile,struct,json,hashlib,re
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/story/rustboro_silver';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
names=['offsetof(struct SaveBlock1,flags)','FLAG_LA_RED_DEX_GIFTS','FLAG_LA_MET_BRENDAN_AND_MAY','FLAG_BADGE01_GET','FLAG_HIDE_RUSTBORO_CITY_RIVAL','FLAG_MET_RIVAL_RUSTBORO','FLAG_DEFEATED_RIVAL_RUSTBORO','FLAG_ENABLE_RIVAL_MATCH_CALL','FLAG_LA_MET_SILVER','FLAG_LA_DEFEATED_SILVER_RUSTBORO','FLAG_LA_HIDE_RUSTBORO_SILVER','VAR_RUSTBORO_CITY_STATE','VAR_ROUTE104_STATE','TRAINER_SILVER_RUSTBORO','TRAINER_MAY_RUSTBORO_TREECKO','TRAINER_MAY_RUSTBORO_TORCHIC','TRAINER_MAY_RUSTBORO_MUDKIP','LOCALID_LA_RUSTBORO_SILVER','LOCALID_PLAYER','LOCALID_RUSTBORO_RIVAL','OBJ_EVENT_GFX_LA_ROSTER_MAY','OBJ_EVENT_GFX_LA_ROSTER_SILVER','TRAINER_PIC_SILVER_HNS','MC_HEADER_BRENDAN','MC_HEADER_MAY','sizeof(struct Trainer)','offsetof(struct Trainer,party)','offsetof(struct Trainer,items)','offsetof(struct Trainer,trainerPic)','sizeof(struct TrainerMon)','offsetof(struct TrainerMon,lvl)','MON_DATA_SPECIES','MON_DATA_IS_SHINY','MON_DATA_HP','MON_DATA_MAX_HP','MON_DATA_STATUS','MON_DATA_HP_IV','MON_DATA_ATK_IV','MON_DATA_DEF_IV','MON_DATA_SPEED_IV','MON_DATA_SPATK_IV','MON_DATA_SPDEF_IV','SPECIES_ZUBAT','SPECIES_GASTLY','SPECIES_MAGNEMITE','SPECIES_ABRA','SPECIES_SNEASEL','SPECIES_TOTODILE','HEAL_LOCATION_OLDALE_TOWN','FONT_NORMAL','CHAR_W','MAX_TRAINERS_COUNT','TRAINERS_COUNT','DIFFICULTY_NORMAL']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "data.h"\n#include "text.h"\n#include "pokenav.h"\n#include "constants/map_event_ids.h"\n#include "constants/event_objects.h"\n#include "constants/heal_locations.h"\n#include "constants/characters.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def flag(n):return (rd(rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,flags)']+c[n]//8,1)>>(c[n]%8))&1
def actor(local):
 return next((symbols['gObjectEvents']+j*36 for j in range(16) if rd(symbols['gObjectEvents']+j*36,1)&1 and rd(symbols['gObjectEvents']+j*36+8,1)==c[local]),None)
def xy(local):
 a=actor(local);return (rd(a+16,2)-7,rd(a+18,2)-7) if a else None
def capture(n):shutil.copy2(shot('silver_'+n),D/(n+'.png'))
expected={};observed=set()
def prefixes():
 expected.clear();observed.clear()
 for n in symbols:
  if n.startswith('LegendsRustboroRivals_Text_'):
   invoke('StringExpandPlaceholders',symbols['gStringVar4'],symbols[n]);expected[n]=bytes(rd(symbols['gStringVar4']+j,1) for j in range(12))
 wr(symbols['gStringVar4'],255,1)
def scene_advance(target,tag,limit=22000):
 global observed
 for i in range(limit):
  msg=[bytes(rd(symbols['gStringVar4']+o+j,1) for j in range(12)) for o in [0,3]]
  for n,v in expected.items():
   if n not in observed and v in msg:
    observed.add(n)
    if n.endswith('_Offscreen'):
     check('north_entry_'+tag,xy('LOCALID_LA_RUSTBORO_SILVER')==(18,48));capture(tag+'_north')
    if n.endswith('_Name'):
     check('arrival_positions_'+tag,xy('LOCALID_LA_RUSTBORO_SILVER')==(18,54) and xy('LOCALID_PLAYER')==(18,55) and xy('LOCALID_RUSTBORO_RIVAL')==(17,54));capture(tag+'_introduction')
  if target():return
  if active('Task_HandleYesNoInput') is not None:
   check('only_may_acceptance_prompt_'+tag,not flag('FLAG_LA_MET_SILVER'))
  frames(1,1 if i%31<4 else 0)
 capture(tag+'_timeout');raise AssertionError(('timeout',tag,location(),pos(),hex(rd(symbols['gMain']+4))))
def battle_ready(tid):return rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1 and rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1 and rd(symbols['gTrainerBattleParameter']+2,2)==tid
def finish(outcome):
 wr(symbols['gBattleOutcome'],outcome,1);wr(symbols['gBattleMainFunc'],symbols['HandleEndTurn_BattleWon' if outcome==1 else 'HandleEndTurn_BattleLost']|1)
def setup(gender,mode,x,choice,badge,won=False):
 start(gender);invoke('StorageChangeMode',mode,1);invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS']);invoke('FlagSet',c['FLAG_LA_MET_BRENDAN_AND_MAY'])
 if badge:invoke('FlagSet',c['FLAG_BADGE01_GET'])
 invoke('ScriptGiveMon',4,16,0);invoke('ScriptGiveMon',7,16,0);invoke('RecordStarterChoice',choice)
 invoke('FlagClear',c['FLAG_HIDE_RUSTBORO_CITY_RIVAL']);invoke('VarSet',c['VAR_RUSTBORO_CITY_STATE'],7);invoke('VarSet',c['VAR_ROUTE104_STATE'],2)

 if won:invoke('FlagSet',c['FLAG_DEFEATED_RIVAL_RUSTBORO'])
 invoke('SetLastHealLocationWarp',c['HEAL_LOCATION_OLDALE_TOWN']);prefixes();warp(0,3,x,56);move(64,1)
for gender,mode,x,choice,badge in [(0,0,12,3,0),(1,1,19,8,1),(0,1,19,5,1),(1,0,12,4,0)]:
 tag=f'{gender}_{mode}_{x}_{choice}';print('CASE',tag,flush=True);setup(gender,mode,x,choice,badge)
 group=[0,1,2,0,2,1,0,1,2][choice];may=c[['TRAINER_MAY_RUSTBORO_TREECKO','TRAINER_MAY_RUSTBORO_TORCHIC','TRAINER_MAY_RUSTBORO_MUDKIP'][group]]
 scene_advance(lambda:battle_ready(may),tag+'_may')
 check('may_for_both_genders_'+tag,rd(actor('LOCALID_RUSTBORO_RIVAL')+4,2)==c['OBJ_EVENT_GFX_LA_ROSTER_MAY'])
 check('both_contacts_'+tag,invoke('MatchCall_GetEnabled',c['MC_HEADER_BRENDAN']) and invoke('MatchCall_GetEnabled',c['MC_HEADER_MAY']))
 # May's fight leaves the team tired; Silver must receive a full heal first.
 wr(0x03007400,1);invoke('SetMonData',symbols['gParties'],c['MON_DATA_HP'],0x03007400)
 finish(1);scene_advance(lambda:battle_ready(c['TRAINER_SILVER_RUSTBORO']),tag+'_silver');frames(35);capture(tag+'_battle')
 check('may_win_preserved_'+tag,flag('FLAG_DEFEATED_RIVAL_RUSTBORO'))
 check('silver_not_completed_before_win_'+tag,flag('FLAG_LA_MET_SILVER') and not flag('FLAG_LA_DEFEATED_SILVER_RUSTBORO'))
 check('fixed_single_battle_'+tag,rd(symbols['gBattlersCount'],1)==2 and not(rd(symbols['gBattleTypeFlags'])&1))
 check('full_heal_'+tag,invoke('GetMonData3',symbols['gParties'],c['MON_DATA_HP'],0)==invoke('GetMonData3',symbols['gParties'],c['MON_DATA_MAX_HP'],0))
 check('six_opponents_'+tag,rd(symbols['gPartiesCount']+1,1)==6)
 for slot,name in enumerate(['SPECIES_ZUBAT','SPECIES_GASTLY','SPECIES_MAGNEMITE','SPECIES_ABRA','SPECIES_SNEASEL','SPECIES_TOTODILE']):
  mon=symbols['gParties']+600+slot*100
  check('canonical_family_'+tag+'_'+str(slot),invoke('GetMonData3',mon,c['MON_DATA_SPECIES'],0)==c[name])
  check('shiny_ace_'+tag+'_'+str(slot),invoke('GetMonData3',mon,c['MON_DATA_IS_SHINY'],0)==int(slot==5))
  check('perfect_ivs_'+tag+'_'+str(slot),all(invoke('GetMonData3',mon,c[f],0)==31 for f in ['MON_DATA_HP_IV','MON_DATA_ATK_IV','MON_DATA_DEF_IV','MON_DATA_SPEED_IV','MON_DATA_SPATK_IV','MON_DATA_SPDEF_IV']))
 base=symbols['gTrainers']+(c['DIFFICULTY_NORMAL']*c['TRAINERS_COUNT']+c['TRAINER_SILVER_RUSTBORO'])*c['sizeof(struct Trainer)'];t=invoke('LegendsTrainer_Get',c['TRAINER_SILVER_RUSTBORO'],base);team=rd(t+c['offsetof(struct Trainer,party)'])
 check('silver_hns_portrait_'+tag,rd(t+c['offsetof(struct Trainer,trainerPic)'],1)==c['TRAINER_PIC_SILVER_HNS'])
 check('two_heals_'+tag,rd(t+c['offsetof(struct Trainer,items)'],2)!=0 and rd(t+c['offsetof(struct Trainer,items)']+2,2)!=0)
 for slot in range(6):check('legal_and_capped_'+tag+'_'+str(slot),invoke('LegendsTrainer_MemberLegal',team+slot*c['sizeof(struct TrainerMon)'])==1)
 finish(1);scene_advance(lambda:flag('FLAG_LA_DEFEATED_SILVER_RUSTBORO') and rd(symbols['sGlobalScriptContextStatus'],1)==2,tag+'_outro')
 check('silver_hidden_after_win_'+tag,actor('LOCALID_LA_RUSTBORO_SILVER') is None and flag('FLAG_LA_HIDE_RUSTBORO_SILVER'))
 check('controls_returned_'+tag,invoke('ArePlayerFieldControlsLocked')==0)
 check('all_dialogue_'+tag,all('LegendsRustboroRivals_Text_'+n in observed for n in ['Offscreen','Name','Johto','Partner','Accept','Admission','Offer','Farewell']))
 check('save_'+tag,invoke('TrySavingData',0)==1);invoke('FlagClear',c['FLAG_LA_DEFEATED_SILVER_RUSTBORO']);check('load_'+tag,invoke('LoadGameSave',0)==1)
 warp(0,3,18,55);frames(90);check('no_replay_'+tag,flag('FLAG_LA_DEFEATED_SILVER_RUSTBORO') and actor('LOCALID_LA_RUSTBORO_SILVER') is None and rd(symbols['sGlobalScriptContextStatus'],1)==2)
 lib.shutdown()
# A loss preserves May's victory and resumes directly at Silver after whiteout.
setup(0,1,12,3,1)
scene_advance(lambda:battle_ready(c['TRAINER_MAY_RUSTBORO_TREECKO']),'retry_may')
finish(1);scene_advance(lambda:battle_ready(c['TRAINER_SILVER_RUSTBORO']),'retry_first')
finish(2)
scene_advance(lambda:rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1 and location()!=(0,3),'whiteout')
for i in range(1800):frames(1,1 if i%31<4 else 0)
check('loss_keeps_may_win_and_silver_pending',flag('FLAG_DEFEATED_RIVAL_RUSTBORO') and flag('FLAG_LA_MET_SILVER') and not flag('FLAG_LA_DEFEATED_SILVER_RUSTBORO'))
check('pending_save',invoke('TrySavingData',0)==1)
check('pending_load',invoke('LoadGameSave',0)==1)
wr(symbols['gFieldCallback2'],0);wr(symbols['gFieldCallback'],0)
warp(0,3,18,55);frames(90)
check('silver_waits_after_reload',xy('LOCALID_LA_RUSTBORO_SILVER')==(18,54))
move(64,0);tap(64);tap(1)
scene_advance(lambda:battle_ready(c['TRAINER_SILVER_RUSTBORO']),'retry_only_silver')
check('retry_heals',invoke('GetMonData3',symbols['gParties'],c['MON_DATA_HP'],0)==invoke('GetMonData3',symbols['gParties'],c['MON_DATA_MAX_HP'],0))
finish(1);scene_advance(lambda:flag('FLAG_LA_DEFEATED_SILVER_RUSTBORO') and rd(symbols['sGlobalScriptContextStatus'],1)==2,'retry_finish')
check('retry_can_complete',flag('FLAG_LA_DEFEATED_SILVER_RUSTBORO'))
lib.shutdown()
# Existing saves that already beat May introduce Silver without another May battle.
setup(1,1,19,8,1,True)
scene_advance(lambda:battle_ready(c['TRAINER_SILVER_RUSTBORO']),'existing_may_win')
check('existing_save_skips_may_fight',flag('FLAG_DEFEATED_RIVAL_RUSTBORO') and flag('FLAG_LA_MET_SILVER'))
finish(1);scene_advance(lambda:flag('FLAG_LA_DEFEATED_SILVER_RUSTBORO') and rd(symbols['sGlobalScriptContextStatus'],1)==2,'existing_finish')
lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False,battle_outcomes='Injected after native turn readiness; difficulty is not inferred.'),indent=2)+'\n')
print('PASS',len(checks),'Rustboro Silver scene checks',flush=True)
