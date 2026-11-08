from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
names=['MAP_GROUP(MAP_MAUVILLE_CITY_GYM)','MAP_NUM(MAP_MAUVILLE_CITY_GYM)','MAP_GROUP(MAP_KANTO_POWER_PLANT_RIFT)','MAP_NUM(MAP_KANTO_POWER_PLANT_RIFT)','VAR_LA_MAUVILLE_RIFT','VAR_LA_POWERPLANT_STATE','FLAG_DEFEATED_WALLY_MAUVILLE','FLAG_ENABLE_FIRST_WALLY_POKENAV_CALL','FLAG_HIDE_MAUVILLE_GYM_WATTSON','LOCALID_MAUVILLE_RIFT_GATE','LOCALID_MAUVILLE_GYM_WATTSON','MAP_GROUP(MAP_MAUVILLE_CITY)','MAP_NUM(MAP_MAUVILLE_CITY)','FLAG_HIDE_MAUVILLE_CITY_WALLY','FLAG_HIDE_MAUVILLE_CITY_WALLYS_UNCLE','TRAINER_WALLY_MAUVILLE','SPECIES_MIRAIDON','MON_DATA_SPECIES','MON_DATA_LEVEL','FLAG_LA_MIRAIDON_BATTLE','sizeof(struct Pokemon)','FLAG_HIDE_VERDANTURF_TOWN_WANDAS_HOUSE_WALLY','LOCALID_MAUVILLE_RIFT_WALLY','LOCALID_MAUVILLE_RIFT_KIRLIA','VAR_LA_PARADIGM_ARC','FLAG_BADGE03_GET','FLAG_BADGE01_GET','FLAG_LA_RED_DEX_GIFTS','FLAG_ENABLE_WALLY_MATCH_CALL','VAR_WALLY_CALL_STEP_COUNTER','MAP_GROUP(MAP_VERDANTURF_TOWN_WANDAS_HOUSE)','MAP_NUM(MAP_VERDANTURF_TOWN_WANDAS_HOUSE)','MAP_GROUP(MAP_HYPERHOENN_34_67_TIMELESS_WOODS)','MAP_NUM(MAP_HYPERHOENN_34_67_TIMELESS_WOODS)','FLAG_LA_TIMELESS_WOODS_ENTERED','FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN','FLAG_LA_TIMELESS_WOODS_ORB_TAKEN','LOCALID_TIMELESS_PARADIGM_MAY','LOCALID_TIMELESS_PARADIGM_TRIAD','LOCALID_VERDANTURF_PARADIGM_MAY']
names += ['FLAG_SYS_GAME_CLEAR','VAR_LA_RIFT_TRACKER', 'VAR_LA_RIFT_SURVEYED', 'VAR_LA_RIFT_RESOLVED', 'VAR_BIRCH_LAB_STATE', 'VAR_LA_LITTLEROOT_ARC', 'MAP_GROUP(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)', 'MAP_NUM(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)', 'FLAG_BADGE04_GET', 'FLAG_BADGE05_GET', 'FLAG_BADGE06_GET', 'FLAG_BADGE07_GET', 'MAP_GROUP(MAP_HYPERHOENN_34_45_DESERT_RUINS)', 'MAP_NUM(MAP_HYPERHOENN_34_45_DESERT_RUINS)', 'FONT_SMALL']
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
start(0)
invoke('ScriptGiveMon',4,45,0)
for key in ('FLAG_LA_RED_DEX_GIFTS','FLAG_LA_TIMELESS_WOODS_ENTERED','FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN','FLAG_LA_TIMELESS_WOODS_ORB_TAKEN'):
 invoke('FlagSet',c[key])
invoke('VarSet',c['VAR_LA_LITTLEROOT_ARC'],5)
invoke('VarSet',c['VAR_BIRCH_LAB_STATE'],5)
invoke('VarSet',c['VAR_LA_MAUVILLE_RIFT'],3)
invoke('VarSet',c['VAR_LA_PARADIGM_ARC'],2)
for i in range(3):invoke('FlagSet',c['FLAG_BADGE01_GET']+i)
check('no_tracker_before_lab',not invoke('RiftTracker_IsActive'))
warp(group,num,5,18);frames(30)
finish('existing_save_invitation')
check('invitation_queued_for_existing_save',invoke('VarGet',c['VAR_LA_RIFT_TRACKER'])==1)
count=invoke('RiftTracker_Count')
check('native_wormholes_and_travel_catalogued',count==24)
for i in range(count):
 wr(symbols['gSpecialVar_0x8004'],i,2);invoke('RiftTracker_Check')
 check('no_detector_gate_'+str(i),rd(symbols['gSpecialVar_Result'],2)==0)
check('locations_not_recorded_early',invoke('VarGet',c['VAR_LA_RIFT_SURVEYED'])==0)
warp(c['MAP_GROUP(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)'],c['MAP_NUM(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)'],6,5);frames(40)
tap(64);frames(24);tap(1)
wait_for(lambda:invoke('RiftTracker_IsActive'),'lab_upgrade')
frames(35);print(shot('rift_tracker_lab_upgrade'),flush=True)
finish('briefing_end')
check('detector_installed_in_lab',invoke('VarGet',c['VAR_LA_RIFT_TRACKER'])==2)
def gate(i):
 wr(symbols['gSpecialVar_0x8004'],i,2);invoke('RiftTracker_Check')
 return rd(symbols['gSpecialVar_Result'],2)
for i in range(count):check('natural_wormholes_require_league_'+str(i),gate(i)==5)
for j in range(3,8):invoke('FlagSet',c['FLAG_BADGE01_GET']+j)
for i in range(count):check('eight_badges_are_not_league_victory_'+str(i),gate(i)==5)
invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])
for i in range(count):check('league_victory_preserves_story_seals_'+str(i),gate(i)==2)
invoke('VarSet',c['VAR_LA_PARADIGM_ARC'],5)
# The three original statistics pages are replaced only after the lab upgrade.
invoke('AdventureJournal_Open');frames(30)
print(shot('rift_tracker_lead'),flush=True)
tap(256);frames(20);print(shot('rift_tracker_signals'),flush=True)
tap(128);tap(256);frames(20);print(shot('rift_tracker_notes'),flush=True)
tap(2);frames(30)
check('tracker_closes_to_field',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
# The native map wormhole retains its original artwork and destination.
invoke('FlagClear',c['FLAG_SYS_GAME_CLEAR'])
warp(c['MAP_GROUP(MAP_HYPERHOENN_34_67_TIMELESS_WOODS)'],c['MAP_NUM(MAP_HYPERHOENN_34_67_TIMELESS_WOODS)'],24,9);frames(40)
tap(64);frames(24);tap(1);finish('native_wormhole_league_gate')
check('native_wormhole_requires_actual_league_win',spoke('RiftResearch_Text_League'))
invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])

warp(c['MAP_GROUP(MAP_HYPERHOENN_34_67_TIMELESS_WOODS)'],c['MAP_NUM(MAP_HYPERHOENN_34_67_TIMELESS_WOODS)'],24,9);frames(40)
tap(64);frames(24);tap(1)
finish('native_wormhole_sealed')
check('native_wormhole_uses_gate_dialogue',spoke('RiftResearch_Text_Sealed'))
check('native_wormhole_does_not_warp_early',location()==(c['MAP_GROUP(MAP_HYPERHOENN_34_67_TIMELESS_WOODS)'],c['MAP_NUM(MAP_HYPERHOENN_34_67_TIMELESS_WOODS)']))
print(shot('rift_tracker_native_wormhole'),flush=True)
for name in ['RiftResearch_Text_Invite','RiftResearch_Text_Answer','RiftResearch_Text_Priority','RiftResearch_Text_Welcome','RiftResearch_Text_Question','RiftResearch_Text_Signatures','RiftResearch_Text_Strength','RiftResearch_Text_Explain','RiftResearch_Text_Upgrade','RiftResearch_Text_Resolve','RiftResearch_Text_LastAdvice','RiftResearch_Text_NoDetector','RiftResearch_Text_Repelled','RiftResearch_Text_Sealed','RiftResearch_Text_Travel','RiftResearch_Text_League']:
 data=[];addr=symbols[name]
 for k in range(2400):
  v=rd(addr+k,1)
  if v==255:break
  data.append(v)
 for j,line in enumerate(bytes(data).replace(bytes([251]),bytes([254])).split(bytes([254]))):
  # placeholders expand according to player/destination; check fixed authored lines here
  if 253 in line:continue
  buf=0x03007500
  for k,v in enumerate(line+bytes([255])):wr(buf+k,v,1)
  check('dialogue_fit_'+name+'_'+str(j),invoke('GetStringWidth',1,buf,0)<=208)
lib.shutdown()
print('PASS' ,len(checks),'Rift research checks')
