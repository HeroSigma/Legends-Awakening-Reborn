from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
names=['MAP_GROUP(MAP_MAUVILLE_CITY_GYM)','MAP_NUM(MAP_MAUVILLE_CITY_GYM)','MAP_GROUP(MAP_KANTOAR_1_95_POWERPLANT)','MAP_NUM(MAP_KANTOAR_1_95_POWERPLANT)','VAR_LA_MAUVILLE_RIFT','VAR_LA_POWERPLANT_STATE','FLAG_DEFEATED_WALLY_MAUVILLE','FLAG_ENABLE_FIRST_WALLY_POKENAV_CALL','FLAG_HIDE_MAUVILLE_GYM_WATTSON','LOCALID_MAUVILLE_RIFT_GATE','LOCALID_MAUVILLE_GYM_WATTSON','MAP_GROUP(MAP_MAUVILLE_CITY)','MAP_NUM(MAP_MAUVILLE_CITY)','FLAG_HIDE_MAUVILLE_CITY_WALLY','FLAG_HIDE_MAUVILLE_CITY_WALLYS_UNCLE','TRAINER_WALLY_MAUVILLE','SPECIES_MIRAIDON','MON_DATA_SPECIES','MON_DATA_LEVEL','FLAG_LA_MIRAIDON_BATTLE','sizeof(struct Pokemon)','FLAG_HIDE_VERDANTURF_TOWN_WANDAS_HOUSE_WALLY','LOCALID_MAUVILLE_RIFT_WALLY','LOCALID_MAUVILLE_RIFT_KIRLIA','MAP_GROUP(MAP_KANTOAR_3_28_ROUTE10)','MAP_NUM(MAP_KANTOAR_3_28_ROUTE10)','FLAG_LA_KANTO_RIFT_ARRIVAL','VAR_REPEL_STEP_COUNT','WILD_AREA_LAND','TIME_DAY','FLAG_TEMP_1','FLAG_TEMP_2','FLAG_TEMP_3','FLAG_TEMP_5','FLAG_LA_HEARD_GIOVANNI','SP_NAME_ROCKET_CONTROL']
with tempfile.TemporaryDirectory() as td:
 td=Path(td)
 (td/'c.c').write_text('#include "global.h"\n#include "constants/speaker_names.h"\n#include "constants/maps.h"\n#include "constants/map_event_ids.h"\n#include "constants/flags.h"\n#include "constants/opponents.h"\n#include "pokemon.h"\n#include <stddef.h>\n#include "constants/items.h"\n#include "wild_encounter.h"\n#include "constants/rtc.h"\nconst unsigned v[]={'+','.join(names)+'};')
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
def heard_report_text():
 expected=bytes(rd(symbols['MauvilleRift_Text_GiovanniReport']+i,1) for i in range(28))
 return expected in bytes(rd(symbols['gStringVar4']+i,1) for i in range(40))
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

from collections import deque
import json
route=(c['MAP_GROUP(MAP_KANTOAR_3_28_ROUTE10)'],c['MAP_NUM(MAP_KANTOAR_3_28_ROUTE10)'])
plant=(c['MAP_GROUP(MAP_KANTOAR_1_95_POWERPLANT)'],c['MAP_NUM(MAP_KANTOAR_1_95_POWERPLANT)'])
def loc():return location()
def step(key,target):
 for i in range(48):
  frames(1,key)
  if pos()==target:
   frames(24)
   return
 raise AssertionError(('step blocked',pos(),target))
def walk_to(name,target):
 d=json.loads((R/'data/maps'/name/'map.json').read_text())
 l=next(l for l in json.loads((R/'data/layouts/layouts.json').read_text())['layouts'] if l['id']==d['layout'])
 w=l['width'];a=struct.unpack('<'+'H'*(w*l['height']),(R/l['blockdata_filepath']).read_bytes())
 blocked={(o['x'],o['y']) for o in d['object_events'] if o['flag']=='0' or not flag(c[o['flag']])}
 blocked|={(z['x'],z['y']) for z in d['warp_events'] if (z['x'],z['y'])!=target}
 q=deque([pos()]);paths={pos():[]}
 while q:
  x,y=q.popleft()
  if (x,y)==target:break
  for dx,dy,key in [(0,-1,64),(0,1,128),(-1,0,32),(1,0,16)]:
   p=(x+dx,y+dy)
   if not(0<=p[0]<w and 0<=p[1]<l['height']) or a[p[1]*w+p[0]]&0xc00 or p in blocked or p in paths:continue
   paths[p]=paths[(x,y)]+[(key,p)];q.append(p)
 assert target in paths,('no path',name,pos(),target)
 for key,p in paths[target]:step(key,p)
def encounters(label):
 h=invoke('GetCurrentMapWildMonHeaderId');check(label+'_has_encounter_header',h!=65535)
 types=invoke('GetEffectiveWildEncounterTypes',h,c['TIME_DAY']);land=rd(types)
 check(label+'_has_land_table',land!=0)
 for i in range(4):check(label+'_wild_generation_'+str(i),invoke('TryGenerateWildMon',land,c['WILD_AREA_LAND'],0))
start(0)
invoke('ScriptGiveMon',4,30,0)
invoke('FlagSet',c['FLAG_DEFEATED_WALLY_MAUVILLE'])
invoke('VarSet',c['VAR_REPEL_STEP_COUNT'],4000)
warp(group,num,5,20)
wait_for(lambda:rift_stage()==1,'gym_open')
finish('gym_scene')
warp(group,num,4,17);frames(30);tap(64);frames(24);tap(1)
wait_for(lambda:loc()==route and flag(c['FLAG_LA_KANTO_RIFT_ARRIVAL']),'route_arrival')
finish('route_arrival_finished')
check('requested_arrival',pos()==(9,44))
print(shot('route10_rift_arrival'),flush=True)
encounters('route10')
walk_to('Kanto_Route10',(6,43))
tap(64);frames(24);tap(1)
wait_for(lambda:spoke('PowerPlantRift_Text_Player'),'read_actual_sign')
frames(40);print(shot('route10_sign'),flush=True)
finish('sign_read')
walk_to('Kanto_Route10',(7,41))
frames(40,64);frames(60)
wait_for(lambda:loc()==plant,'enter_actual_plant')
finish('plant_entry')
encounters('full_powerplant')
check('plant_floor_supports_encounters',invoke('MetatileBehavior_IsLandWildEncounter',invoke('MapGridGetMetatileBehaviorAt',5+7,37+7)))
walk_to('Kanto_PowerPlant',(2,11))
tap(64);frames(24);tap(1);finish('wattson_found')
check('wattson_story_position',invoke('VarGet',c['VAR_LA_POWERPLANT_STATE'])==1)
print(shot('fullplant_wattson'),flush=True)
walk_to('Kanto_PowerPlant',(8,12))
tap(64);frames(24);tap(1)
wait_for(lambda:active('Task_HandleYesNoInput') is not None,'shutdown_confirmation')
frames(10);tap(2);finish('decline_shutdown')
check('declining_preserves_reactor',invoke('VarGet',c['VAR_LA_POWERPLANT_STATE'])==1)
check('declining_does_not_reveal_name',not flag(c['FLAG_LA_HEARD_GIOVANNI']))
tap(1)
wait_for(lambda:spoke('PowerPlantRift_Text_GiovanniOrders'),'giovanni_radio_reveal')
check('name_not_known_before_radio_completed',not flag(c['FLAG_LA_HEARD_GIOVANNI']))
check('radio_has_rocket_speaker',rd(symbols['gSpeakerName'])==rd(symbols['gSpeakerNamesTable']+4*c['SP_NAME_ROCKET_CONTROL']))
frames(40)
print(shot('giovanni_kanto_transmission'),flush=True)
wait_for(lambda:spoke('PowerPlantRift_Text_Miraidon'),'miraidon_visible')
check('transmission_records_knowledge',flag(c['FLAG_LA_HEARD_GIOVANNI']))
frames(40)
print(shot('miraidon_regular_overworld'),flush=True)
wait_for(ready,'miraidon')
enemy=symbols['gParties']+6*c['sizeof(struct Pokemon)']
check('miraidon_level70',invoke('GetMonData2',enemy,c['MON_DATA_SPECIES'])==c['SPECIES_MIRAIDON'] and invoke('GetMonData2',enemy,c['MON_DATA_LEVEL'])==70)
wait_for(lambda:invoke('VarGet',c['VAR_LA_POWERPLANT_STATE'])==2,'miraidon_loss')
finish('miraidon_finished')
walk_to('Kanto_PowerPlant',(2,11))
tap(64);frames(24);tap(1);finish('wattson_after')
check('wattson_heads_outside',invoke('VarGet',c['VAR_LA_POWERPLANT_STATE'])==3)
frames(64,32);frames(100)
wait_for(lambda:loc()==route,'exit_actual_plant')
finish('route_return')
check('left_exit_reaches_courtyard',loc()==route)
walk_to('Kanto_Route10',(8,45))
tap(64);frames(24);tap(1);finish('wally_ready')
check('return_ready',invoke('VarGet',c['VAR_LA_POWERPLANT_STATE'])==4)
walk_to('Kanto_Route10',(11,45))
check('courtyard_path_to_rift',pos()==(11,45))
tap(64);frames(24);tap(1)
wait_for(heard_report_text,'player_reports_radio')
frames(40)
print(shot('giovanni_paradigm_report'),flush=True)
wait_for(lambda:rift_stage()==3,'gym_return')
finish('chapter_return')
check('returned_to_gym',loc()==(group,num))

# Check all changed/new dialogue lines using the actual normal font.
import re
text_labels = ['TimelessWoods_Text_Plan','TimelessWoods_Text_Secrecy',
 'LegendsParadigm_Text_AskGiovanni','LegendsParadigm_Text_ScoutWarning',
 'SlateportCity_OceanicMuseum_2F_Text_ArchieWarning']
text_labels += [n for n in symbols if n.startswith('PowerPlantRift_Text_') or n in
 ['MauvilleRift_Text_GiovanniReport','MauvilleRift_Text_GiovanniConnection','MauvilleRift_Text_SharedOperation']]
for name in text_labels:
 data=bytearray()
 for i in range(2000):
  b=rd(symbols[name]+i,1)
  if b==255:break
  data.append(b)
 for j,line in enumerate(re.split(b'[\xfe\xfb\xfa]',bytes(data))):
  if 0xfd in line:continue
  for k,b in enumerate(line+b'\xff'):wr(0x03007500+k,b,1)
  check('text_fit_'+name+'_'+str(j),invoke('GetStringWidth',1,0x03007500,0)<=208)
check('knowledge_save',invoke('TrySavingData',0)==1)
invoke('FlagClear',c['FLAG_LA_HEARD_GIOVANNI'])
check('knowledge_load',invoke('LoadGameSave',0)==1)
check('knowledge_persists',flag(c['FLAG_LA_HEARD_GIOVANNI']))
# Older completed-rescue saves do not invent memories of the new radio.
invoke('FlagClear',c['FLAG_LA_HEARD_GIOVANNI'])
invoke('VarSet',c['VAR_LA_MAUVILLE_RIFT'],2)
warp(group,num,5,19);frames(10)
saw_legacy_report=False
for frame in range(14000):
 if heard_report_text():saw_legacy_report=True
 if rift_stage()==3 and ended():break
 frames(1,1 if frame%24<3 else 0)
else:raise AssertionError('legacy return did not finish')
check('old_save_no_invented_radio_memory',not saw_legacy_report and not flag(c['FLAG_LA_HEARD_GIOVANNI']))

lib.shutdown()
print('PASS' ,len(checks),'Route 10 rescue checks')
