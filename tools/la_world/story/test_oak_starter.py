from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
names=['MAP_GROUP(MAP_MAUVILLE_CITY_GYM)','MAP_NUM(MAP_MAUVILLE_CITY_GYM)','MAP_GROUP(MAP_KANTO_POWER_PLANT_RIFT)','MAP_NUM(MAP_KANTO_POWER_PLANT_RIFT)','VAR_LA_MAUVILLE_RIFT','VAR_LA_POWERPLANT_STATE','FLAG_DEFEATED_WALLY_MAUVILLE','FLAG_ENABLE_FIRST_WALLY_POKENAV_CALL','FLAG_HIDE_MAUVILLE_GYM_WATTSON','LOCALID_MAUVILLE_RIFT_GATE','LOCALID_MAUVILLE_GYM_WATTSON','MAP_GROUP(MAP_MAUVILLE_CITY)','MAP_NUM(MAP_MAUVILLE_CITY)','FLAG_HIDE_MAUVILLE_CITY_WALLY','FLAG_HIDE_MAUVILLE_CITY_WALLYS_UNCLE','TRAINER_WALLY_MAUVILLE','SPECIES_MIRAIDON','MON_DATA_SPECIES','MON_DATA_LEVEL','FLAG_LA_MIRAIDON_BATTLE','sizeof(struct Pokemon)','FLAG_HIDE_VERDANTURF_TOWN_WANDAS_HOUSE_WALLY','LOCALID_MAUVILLE_RIFT_WALLY','LOCALID_MAUVILLE_RIFT_KIRLIA','VAR_LA_PARADIGM_ARC','FLAG_BADGE03_GET','FLAG_BADGE01_GET','FLAG_LA_RED_DEX_GIFTS','FLAG_ENABLE_WALLY_MATCH_CALL','VAR_WALLY_CALL_STEP_COUNTER','MAP_GROUP(MAP_VERDANTURF_TOWN_WANDAS_HOUSE)','MAP_NUM(MAP_VERDANTURF_TOWN_WANDAS_HOUSE)','MAP_GROUP(MAP_HYPERHOENN_34_67_TIMELESS_WOODS)','MAP_NUM(MAP_HYPERHOENN_34_67_TIMELESS_WOODS)','FLAG_LA_TIMELESS_WOODS_ENTERED','FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN','FLAG_LA_TIMELESS_WOODS_ORB_TAKEN','LOCALID_TIMELESS_PARADIGM_MAY','LOCALID_TIMELESS_PARADIGM_TRIAD','LOCALID_VERDANTURF_PARADIGM_MAY']
names += ['FLAG_SYS_GAME_CLEAR','VAR_LA_RIFT_TRACKER', 'VAR_LA_RIFT_SURVEYED', 'VAR_LA_RIFT_RESOLVED', 'VAR_BIRCH_LAB_STATE', 'VAR_LA_LITTLEROOT_ARC', 'MAP_GROUP(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)', 'MAP_NUM(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)', 'FLAG_BADGE04_GET', 'FLAG_BADGE05_GET', 'FLAG_BADGE06_GET', 'FLAG_BADGE07_GET', 'MAP_GROUP(MAP_HYPERHOENN_34_45_DESERT_RUINS)', 'MAP_NUM(MAP_HYPERHOENN_34_45_DESERT_RUINS)', 'FONT_SMALL']
names += ['VAR_UNUSED_0x40F7','VAR_UNUSED_0x40F8','FLAG_TEMP_7','VAR_LA_OAK_STARTER', 'LOCALID_LA_TRACKER_OAK', 'MAP_GROUP(MAP_FALLARBOR_TOWN)', 'MAP_NUM(MAP_FALLARBOR_TOWN)', 'LOCALID_LA_FALLARBOR_BLUE', 'MON_DATA_SPECIES', 'MON_DATA_LEVEL', 'SPECIES_BULBASAUR', 'SPECIES_CHARMANDER', 'SPECIES_SQUIRTLE', 'sizeof(struct Pokemon)']
with tempfile.TemporaryDirectory() as td:
 td=Path(td)
 (td/'c.c').write_text('#include "global.h"\n#include "text.h"\n#include "constants/maps.h"\n#include "constants/map_event_ids.h"\n#include "constants/flags.h"\n#include "constants/opponents.h"\n#include "pokemon.h"\n#include <stddef.h>\n#include "constants/items.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
group,num=c[names[0]],c[names[1]]
def wait_for(pred,label):
 for i in range(14000):
  if pred():return
  frames(1,1 if i%24<3 else 0)
 print(shot('route110_timeout_'+label),flush=True)
 raise AssertionError((label,pos(),hex(rd(symbols['gMain']+4))))
def spoke(name):
 expected=bytes(rd(symbols[name]+i,1) for i in range(10))
 return expected in bytes(rd(symbols['gStringVar4']+i,1) for i in range(18))
def actor(name):
 return invoke('GetObjectEventIdByLocalIdAndMap',c[name],num,group)<16
def ready():
 return rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1 and rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1
def ended():
 return rd(symbols['sGlobalScriptContextStatus'],1)==2 and rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1 and rd(symbols['sLockFieldControls'],1)==0

def rift_stage():return rd(rd(symbols['gSaveBlock1Ptr'])+0x139c+2*(c['VAR_LA_MAUVILLE_RIFT']-0x4000),2)
def run(name):
 invoke('ScriptContext_SetupScript',symbols[name])
 frames(3)
def finish(label):
 wait_for(ended,label)
 frames(20)

def arc():return rd(rd(symbols['gSaveBlock1Ptr'])+0x139c+2*(c['VAR_LA_PARADIGM_ARC']-0x4000),2)
def setup():
 start(0)
 invoke('ScriptGiveMon',4,20,0)
 for key in ('FLAG_LA_RED_DEX_GIFTS','FLAG_BADGE03_GET'):
  invoke('FlagSet',c[key])
 invoke('VarSet',c['VAR_LA_LITTLEROOT_ARC'],5)
 invoke('VarSet',c['VAR_BIRCH_LAB_STATE'],5)
 invoke('VarSet',c['VAR_LA_RIFT_TRACKER'],1)
 invoke('VarSet',c['VAR_LA_PARADIGM_ARC'],2)
 warp(c['MAP_GROUP(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)'],c['MAP_NUM(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)'],6,5);frames(40)
 check('oak_present',invoke('GetObjectEventIdByLocalIdAndMap',c['LOCALID_LA_TRACKER_OAK'],c['MAP_NUM(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)'],c['MAP_GROUP(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)'])<16)
def choose(index):
 wait_for(lambda:active('Task_HandleMultichoiceInput') is not None,'oak_choice_menu')
 frames(20)
 for j in range(index):tap(128);frames(12)
 tap(1)
 wait_for(lambda:active('Task_HandleYesNoInput') is not None,'starter_confirmation')
 frames(30);tap(1)
 finish('oak_starter_awarded')
def party_species(slot):
 return invoke('GetMonData2',symbols['gParties']+slot*c['sizeof(struct Pokemon)'],c['MON_DATA_SPECIES'])
for index,species in enumerate(['SPECIES_BULBASAUR','SPECIES_CHARMANDER','SPECIES_SQUIRTLE']):
 setup()
 before=rd(symbols['gPartiesCount'],1)
 tap(64);frames(24);tap(1)
 choose(index)
 check('one_gift_'+species,rd(symbols['gPartiesCount'],1)==before+1)
 check('correct_gift_'+species,party_species(before)==c[species])
 check('gift_level5_'+species,invoke('GetMonData2',symbols['gParties']+before*c['sizeof(struct Pokemon)'],c['MON_DATA_LEVEL'])==5)
 check('choice_recorded_'+species,invoke('VarGet',c['VAR_LA_OAK_STARTER'])==index+2)
 check('tracker_upgrade_kept_'+species,invoke('RiftTracker_IsActive'))
 if index==0:
  print(shot('oak_starter_lab'),flush=True)
  invoke('VarSet',c['VAR_UNUSED_0x40F7'],4)
  invoke('VarSet',c['VAR_UNUSED_0x40F8'],c['SPECIES_SQUIRTLE'])
  invoke('ClearMysteryGiftVars')
  check('mystery_gift_reset_preserves_tracker',invoke('RiftTracker_IsActive'))
  check('mystery_gift_reset_preserves_oak_gift',invoke('VarGet',c['VAR_LA_OAK_STARTER'])==2)
  run('RiftResearch_OakCatchUp');finish('oak_repeat')
  check('repeat_does_not_duplicate_gift',rd(symbols['gPartiesCount'],1)==before+1)
  warp(c['MAP_GROUP(MAP_FALLARBOR_TOWN)'],c['MAP_NUM(MAP_FALLARBOR_TOWN)'],14,11);frames(40)
  check('blue_present_in_fallarbor',invoke('GetObjectEventIdByLocalIdAndMap',c['LOCALID_LA_FALLARBOR_BLUE'],c['MAP_NUM(MAP_FALLARBOR_TOWN)'],c['MAP_GROUP(MAP_FALLARBOR_TOWN)'])<16)
  check('menu_theme_independent',invoke('VarGet',c['VAR_UNUSED_0x40F7'])==4)
  check('dexnav_species_independent',invoke('VarGet',c['VAR_UNUSED_0x40F8'])==c['SPECIES_SQUIRTLE'])
  tap(64);frames(24);tap(1)
  wait_for(lambda:spoke('RiftResearch_Text_BlueReply'),'blue_introduction')
  frames(40);print(shot('blue_fallarbor_introduction'),flush=True)
  finish('blue_met')
  check('blue_meeting_saved',invoke('VarGet',c['VAR_LA_OAK_STARTER'])==10)
  tap(1);finish('blue_repeat')
  check('blue_introduction_not_repeated',invoke('VarGet',c['VAR_LA_OAK_STARTER'])==10)
 lib.shutdown()
# Full party routes the starter into storage and consumes the gift exactly once.
setup()
while rd(symbols['gPartiesCount'],1)<6:invoke('ScriptGiveMon',25,5,0)
tap(64);frames(24);tap(1);choose(2)
check('full_party_stays_six',rd(symbols['gPartiesCount'],1)==6)
check('full_party_gift_committed',invoke('VarGet',c['VAR_LA_OAK_STARTER'])==4)
check('gift_reached_pc',invoke('GetBoxMonDataAt',0,0,c['MON_DATA_SPECIES'])==c['SPECIES_SQUIRTLE'])
lib.shutdown()
setup()
while rd(symbols['gPartiesCount'],1)<6:invoke('ScriptGiveMon',25,5,0)
boxes=invoke('GetStorageBoxCount')
for box in range(boxes):
 for slot in range(30):invoke('SetBoxMonAt',box,slot,symbols['gParties'])
tap(64);frames(24);tap(1);choose(1)
check('full_storage_preserves_offer',invoke('VarGet',c['VAR_LA_OAK_STARTER'])==1)
invoke('ZeroBoxMonAt',0,0)
run('RiftResearch_OakCatchUp');choose(1)
check('retry_after_making_room',invoke('VarGet',c['VAR_LA_OAK_STARTER'])==3)
check('retry_delivers_correct_species',invoke('GetBoxMonDataAt',0,0,c['MON_DATA_SPECIES'])==c['SPECIES_CHARMANDER'])
lib.shutdown()

setup()
for name in ['RiftResearch_Text_OakIntroduction', 'RiftResearch_Text_OakGreeting', 'RiftResearch_Text_PlayerOak', 'RiftResearch_Text_OakReply', 'RiftResearch_Text_Offer', 'RiftResearch_Text_ConfirmStarter', 'RiftResearch_Text_Later', 'RiftResearch_Text_NoRoom', 'RiftResearch_Text_SentToPC', 'RiftResearch_Text_ReceivedStarter', 'RiftResearch_Text_ThanksOak', 'RiftResearch_Text_Grandson', 'RiftResearch_Text_FindBlue', 'RiftResearch_Text_OakAfterBlue', 'RiftResearch_Text_BlueFirst', 'RiftResearch_Text_PlayerBlue', 'RiftResearch_Text_BlueReply', 'RiftResearch_Text_PlayerEvidence', 'RiftResearch_Text_BlueEvidence', 'RiftResearch_Text_BlueRepeat']:
 data=[];addr=symbols[name]
 for k in range(2400):
  v=rd(addr+k,1)
  if v==255:break
  data.append(v)
 for j,line in enumerate(bytes(data).replace(bytes([251]),bytes([254])).split(bytes([254]))):
  if 253 in line:continue
  buf=0x03007500
  for k,v in enumerate(line+bytes([255])):wr(buf+k,v,1)
  check('dialogue_fit_'+name+'_'+str(j),invoke('GetStringWidth',1,buf,0)<=208)
lib.shutdown()
print('PASS',len(checks),'Oak starter, Blue and dialogue checks')
