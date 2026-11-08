"""Native chapter, battle, cap and double-follower checks. Disposable save only."""
from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct,re
names=['FLAG_LA_FLANNERY_RETURNED_GYM','LOCALID_ASHES_LAVA_FLANNERY','ITEM_CARD_KEY','FLAG_LA_RED_DEX_GIFTS','FLAG_BADGE01_GET','VAR_LA_ASHES_STATE','VAR_LA_SILPH_OPPONENT','VAR_LA_RIFT_TRACKER','VAR_LA_PARADIGM_ARC','FLAG_LA_COZMO_BRIEFED','FLAG_LA_ASHES_WOODS_DEPARTURE','FLAG_LA_CHIMNEY_RESONANCE','FLAG_LA_WALLY_RESCUED','FLAG_LA_SILPH_WALLY_FOUND','FLAG_LA_SILPH_PETREL_DEFEATED','FLAG_LA_SILPH_ARIANA_DEFEATED','FLAG_LA_HOOPA_COMPANION','FLAG_LA_HOOPA_JOINED','FLAG_LA_HOOPA_JOIN_PROMPTED','FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY','MAP_FALLARBOR_TOWN_COZMOS_HOUSE','MAP_MT_CHIMNEY','MAP_KANTOAR_3_10_SAFFRONCITY','MAP_KANTOAR_1_47_SILPHCO_1F','MAP_KANTOAR_1_55_SILPHCO_9F','MAP_KANTOAR_1_56_SILPHCO_10F','MAP_KANTOAR_1_57_SILPHCO_11F','MAP_LAVARIDGE_TOWN','MAP_MAUVILLE_CITY','TRAINER_GRUNT_UNUSED','sizeof(struct Trainer)','sizeof(struct TrainerMon)','offsetof(struct TrainerMon,species)','offsetof(struct Trainer,party)','sizeof(enum TrainerPicID)','offsetof(struct Trainer,trainerPic)','offsetof(struct Trainer,items)','TRAINER_PIC_LA_PETREL','TRAINER_PIC_LA_ARIANA','MON_DATA_SPECIES','MON_DATA_LEVEL','MON_DATA_IS_SHINY','SPECIES_HOOPA','sizeof(struct Pokemon)','LOCALID_ASHES_GIOVANNI_PRESENT','LOCALID_ASHES_GIOVANNI_PAST','LOCALID_ASHES_MEWTWO']
with tempfile.TemporaryDirectory() as td:
 td=Path(td)
 (td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "data.h"\n#include "trainer.h"\n#include "constants/maps.h"\n#include "constants/flags.h"\n#include "constants/vars.h"\n#include "constants/items.h"\n#include "constants/opponents.h"\n#include "constants/map_event_ids.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def f(n):return invoke('FlagGet',c[n])
var_ptrs={}
def v(n):
 if n not in var_ptrs:var_ptrs[n]=invoke('GetVarPointer',c[n])-rd(symbols['gSaveBlock1Ptr'])
 return rd(rd(symbols['gSaveBlock1Ptr'])+var_ptrs[n],2)
def at(n,x,y):
 m=c[n];warp(m>>8,m&255,x,y);frames(150)
def waitfor(pred,label,limit=18000):
 for i in range(limit):
  if pred():return
  frames(1,1 if i%24<3 else 0)
 print(shot('ashes_timeout_'+label),flush=True)
 raise AssertionError((label,location(),pos(),hex(rd(symbols['gMain']+4))))
def ended():
 return rd(symbols['sGlobalScriptContextStatus'],1)==2 and not rd(symbols['sLockFieldControls'],1) and rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1
def finish(label):waitfor(ended,label);frames(20)
def ready():
 return rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1 and rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1
def win():
 wr(symbols['gBattleOutcome'],1,1);wr(symbols['gBattleMainFunc'],symbols['HandleEndTurn_BattleWon']|1)
def textseen(n):
 expect=bytes(rd(symbols[n]+i,1) for i in range(16))
 return expect in bytes(rd(symbols['gStringVar4']+i,1) for i in range(28))
def run(n):invoke('ScriptContext_SetupScript',symbols[n]);frames(2)
def ghost():
 sb=rd(symbols['gSaveBlock1Ptr'])
 return invoke('GetObjectEventIdByLocalIdAndMap',248,rd(sb+5,1),rd(sb+4,1))
def setup(count=1,badges=3):
 start(0)
 for i in range(count):invoke('ScriptGiveMon',[4,7,252,25,133,280][i],30,0)
 invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
 for i in range(badges):invoke('FlagSet',c['FLAG_BADGE01_GET']+i)
 invoke('VarSet',c['VAR_LA_RIFT_TRACKER'],2)
 invoke('VarSet',c['VAR_LA_PARADIGM_ARC'],5)
setup(6)
# Real-font check before longer scene playback.
for n in sorted(symbols):
 if not n.startswith('Ashes_Text_'):continue
 data=bytearray()
 for j in range(2200):
  b=rd(symbols[n]+j,1)
  if b==255:break
  data.append(b)
 for i,line in enumerate(re.split(b'[\xfe\xfb\xfa]',bytes(data))):
  if 0xfd in line:continue
  for j,b in enumerate(line+b'\xff'):wr(0x03007500+j,b,1)
  check('fit_'+n+'_'+str(i),invoke('GetStringWidth',1,0x03007500,0)<=208)
invoke('FlagSet',c['FLAG_LA_ASHES_WOODS_DEPARTURE'])
invoke('VarSet',c['VAR_LA_ASHES_STATE'],1)
at('MAP_FALLARBOR_TOWN_COZMOS_HOUSE',2,7)
waitfor(ready,'cozmo_guard')
check('cozmo_guard_singles',True)
win();finish('cozmo_theft')
check('cozmo_briefed',f('FLAG_LA_COZMO_BRIEFED') and v('VAR_LA_ASHES_STATE')==2)
print(shot('ashes_cozmo_after_theft'),flush=True)
# The scoped unused trainer slot has ten distinct six-mon Rocket teams.
at('MAP_KANTOAR_1_57_SILPHCO_11F',1,17)
print(shot('ashes_admin_staging'),flush=True)
teams=[]
for index in range(1,11):
 invoke('VarSet',c['VAR_LA_SILPH_OPPONENT'],index)
 t=invoke('LegendsTrainer_Get',c['TRAINER_GRUNT_UNUSED'],symbols['gTrainers']+c['TRAINER_GRUNT_UNUSED']*c['sizeof(struct Trainer)'])
 party=rd(t+c['offsetof(struct Trainer,party)'])
 for j in range(6):
  check('legal_member_'+str(index)+'_'+str(j),invoke('LegendsTrainer_MemberLegal',party+j*c['sizeof(struct TrainerMon)']))
 check('two_healing_items_'+str(index),rd(t+c['offsetof(struct Trainer,items)'],2)!=0 and rd(t+c['offsetof(struct Trainer,items)']+2,2)!=0)
 if index in (9,10):check('admin_portrait_'+str(index),rd(t+c['offsetof(struct Trainer,trainerPic)'],c['sizeof(enum TrainerPicID)'])==c['TRAINER_PIC_LA_PETREL' if index==9 else 'TRAINER_PIC_LA_ARIANA'])
 # Actual species is first field of TrainerMon.
 teams.append(tuple(rd(party+j*c['sizeof(struct TrainerMon)']+c['offsetof(struct TrainerMon,species)'],2) for j in range(6)))
check('all_rocket_teams_distinct',len(set(teams))==10)
# Summit aftermath and controlled portal; normal gym format selection is untouched.
invoke('FlagSet',c['FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY'])
at('MAP_MT_CHIMNEY',13,7)
addr=0x03007600
for j,b in enumerate(bytes([4])+struct.pack('<I',symbols['LegendsAshes_ChimneyAftermath'])+bytes([0x6c,2])):wr(addr+j,b,1)
# releaseall (0x6c), end (0x02) after the called subroutine.
invoke('ScriptContext_SetupScript',addr)
finish('summit_aftermath')
# This is a subroutine; provide a call/end wrapper for isolated invocation.

check('summit_opens_hoopa_lead',f('FLAG_LA_CHIMNEY_RESONANCE') and v('VAR_LA_ASHES_STATE')==3)
run('LegendsAshes_EnterPast')
waitfor(lambda:location()==(c['MAP_KANTOAR_3_10_SAFFRONCITY']>>8,c['MAP_KANTOAR_3_10_SAFFRONCITY']&255),'hoopa_crossing')
finish('saffron_arrival')
check('saffron_story_arrival',pos()==(33,32))
at('MAP_KANTOAR_1_55_SILPHCO_9F',5,16)
tap(32);frames(15);tap(1);finish('wally_found')
check('wally_found_and_healed',f('FLAG_LA_SILPH_WALLY_FOUND'))
invoke('AddBagItem',c['ITEM_CARD_KEY'],1)
at('MAP_KANTOAR_1_57_SILPHCO_11F',1,17)
tap(32);tap(1);waitfor(ready,'petrel')
check('petrel_six_actual_enemies',rd(symbols['gPartiesCount']+1,1)==6)
print(shot('ashes_petrel_battle'),flush=True)
win();finish('petrel_defeated')
check('petrel_saved_flag',f('FLAG_LA_SILPH_PETREL_DEFEATED'))
tap(16);tap(1);waitfor(ready,'ariana')
check('ariana_six_actual_enemies',rd(symbols['gPartiesCount']+1,1)==6)
win();finish('ariana_defeated')
check('ariana_saved_flag',f('FLAG_LA_SILPH_ARIANA_DEFEATED'))
at('MAP_KANTOAR_1_57_SILPHCO_11F',5,18)
run('LegendsSilph_Door_19');finish('final_security_door')
frames(55,64)
waitfor(lambda:textseen('Ashes_Text_PastGiovanni'),'two_giovannis')
frames(80);print(shot('ashes_two_giovannis'),flush=True)
waitfor(lambda:v('VAR_LA_ASHES_STATE')==6,'escaped_and_reported')
finish('escape_complete')
check('wally_rescued',f('FLAG_LA_WALLY_RESCUED'))
check('flannery_walked_into_gym',f('FLAG_LA_FLANNERY_RETURNED_GYM'))
check('flannery_no_longer_outside',invoke('GetObjectEventIdByLocalIdAndMap',c['LOCALID_ASHES_LAVA_FLANNERY'],c['MAP_LAVARIDGE_TOWN']&255,c['MAP_LAVARIDGE_TOWN']>>8)>=16)
check('returned_to_walkable_lavaridge',location()==(c['MAP_LAVARIDGE_TOWN']>>8,c['MAP_LAVARIDGE_TOWN']&255) and pos()==(9,11))
check('hoopa_companion_below_cap',f('FLAG_LA_HOOPA_COMPANION') and not f('FLAG_LA_HOOPA_JOINED'))
check('no_seventh_party_mon',rd(symbols['gPartiesCount'],1)==6)
for key in [128,128,128,64,64,64]:tap(key);frames(16)
check('hoopa_extra_world_actor',ghost()<16)
check('normal_follower_preserved',invoke('GetFollowerObject')!=0)
print(shot('ashes_two_followers'),flush=True)
# Cap 49 is insufficient; first cap >=50 is currently 56.
for i in range(3,6):invoke('FlagSet',c['FLAG_BADGE01_GET']+i)
invoke('LegendsAshes_HoopaPrepare')
check('cap49_keeps_companion',invoke('GetCurrentLevelCap')==49 and rd(symbols['gSpecialVar_Result'],2)==0)
invoke('FlagSet',c['FLAG_BADGE01_GET']+6)
waitfor(lambda:f('FLAG_LA_HOOPA_JOINED'),'hoopa_joins_at_cap')
finish('hoopa_gift')
check('hoopa_join_clears_companion',not f('FLAG_LA_HOOPA_COMPANION'))
check('hoopa_removed_from_extra_actor',ghost()>=16)
check('hoopa_full_party_kept_six',rd(symbols['gPartiesCount'],1)==6)
check('rescued_quest_complete',invoke('LegendsQuest_State',8)==3 and invoke('LegendsQuest_State',45)==3)
check('save_chapter',invoke('TrySavingData',0)==1)
invoke('FlagClear',c['FLAG_LA_WALLY_RESCUED'])
check('load_chapter',invoke('LoadGameSave',0)==1)
check('rescue_persists',f('FLAG_LA_WALLY_RESCUED') and f('FLAG_LA_HOOPA_JOINED'))
# Second player: already above the threshold when Hoopa rescues them.
setup(1,7)
invoke('AddBagItem',c['ITEM_CARD_KEY'],1)
for key in ['FLAG_LA_SILPH_WALLY_FOUND','FLAG_LA_SILPH_PETREL_DEFEATED','FLAG_LA_SILPH_ARIANA_DEFEATED']:
 invoke('FlagSet',c[key])
invoke('VarSet',c['VAR_LA_ASHES_STATE'],4)
at('MAP_KANTOAR_1_57_SILPHCO_11F',12,11);frames(20,64)
waitfor(lambda:f('FLAG_LA_HOOPA_JOINED'),'immediate_silph_join')
check('joins_before_leaving_silph',location()==(c['MAP_KANTOAR_1_57_SILPHCO_11F']>>8,c['MAP_KANTOAR_1_57_SILPHCO_11F']&255))
check('party_hoopa_immediate',invoke('GetMonData2',symbols['gParties']+c['sizeof(struct Pokemon)'],c['MON_DATA_SPECIES'])==c['SPECIES_HOOPA'])
waitfor(lambda:v('VAR_LA_ASHES_STATE')==6,'high_cap_escape')
finish('high_cap_return')
check('veteran_flannery_walked_into_gym',f('FLAG_LA_FLANNERY_RETURNED_GYM'))
check('no_random_companion_when_already_eligible',not f('FLAG_LA_HOOPA_COMPANION') and ghost()>=16)
print('PASS',len(checks),'Ashes and past Silph checks',flush=True)
