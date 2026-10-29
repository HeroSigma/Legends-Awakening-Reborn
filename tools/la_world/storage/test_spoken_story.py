"""Native spoken Rusturf/Briney exchanges and text-width checks; isolated saves only."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
names=['MAP_GROUP(MAP_RUSTURF_TUNNEL)','MAP_NUM(MAP_RUSTURF_TUNNEL)','MAP_GROUP(MAP_ROUTE104_MR_BRINEYS_HOUSE)','MAP_NUM(MAP_ROUTE104_MR_BRINEYS_HOUSE)','MAP_GROUP(MAP_ROUTE104)','MAP_NUM(MAP_ROUTE104)','VAR_RUSTURF_TUNNEL_STATE','VAR_RUSTBORO_CITY_STATE','VAR_BRINEY_HOUSE_STATE','VAR_ROUTE104_STATE','FLAG_LA_INTRO_ACTIVE','VAR_LITTLEROOT_INTRO_STATE','FLAG_LA_RED_DEX_GIFTS','FLAG_DEVON_GOODS_STOLEN','FLAG_RECOVERED_DEVON_GOODS','FLAG_HIDE_RUSTURF_TUNNEL_AQUA_GRUNT','FLAG_HIDE_RUSTURF_TUNNEL_PEEKO','FLAG_HIDE_RUSTURF_TUNNEL_BRINEY','FLAG_HIDE_BRINEYS_HOUSE_MR_BRINEY','FLAG_HIDE_BRINEYS_HOUSE_PEEKO','FLAG_MR_BRINEY_SAILING_INTRO','FLAG_HIDE_ROUTE_104_MR_BRINEY','LOCALID_RUSTURF_TUNNEL_GRUNT','LOCALID_BRINEYS_HOUSE_BRINEY','ITEM_DEVON_PARTS','ITEM_LETTER']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/maps.h"\n#include "constants/map_event_ids.h"\n#include "constants/items.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
proof=R/'docs/story/spoken_protagonist';proof.mkdir(parents=True,exist_ok=True)
seen=set();prefixes={}
def prepare_prefixes():
 prefixes.clear()
 for label in symbols:
  if label.startswith('LegendsVoice_'):
   invoke('StringExpandPlaceholders',symbols['gStringVar4'],symbols[label])
   prefixes[label]=bytes(rd(symbols['gStringVar4']+i,1) for i in range(12))
 wr(symbols['gStringVar4'],255,1)
def observe():
 current=[bytes(rd(symbols['gStringVar4']+offset+i,1) for i in range(12)) for offset in range(4)]
 seen.update(label for label,value in prefixes.items() if value in current)
def until(pred,limit=32000):
 for i in range(limit):
  observe()
  if pred():return
  frames(1,1 if i%31<4 else 0)
 raise AssertionError(('timeout',location(),pos(),hex(rd(symbols['sGlobalScriptContext']+8))))
def flag(name):return invoke('FlagGet',c[name])
def begin(script,local,group,num):
 wr(symbols['gSpecialVar_LastTalked'],local,2)
 wr(symbols['gSelectedObjectEvent'],invoke('GetObjectEventIdByLocalIdAndMap',local,group,num),1)
 invoke('ScriptContext_SetupScript',symbols[script]);frames(5)
for gender in [0,1]:
 start(gender);invoke('StorageChangeMode',gender,1);invoke('FlagClear',c['FLAG_LA_INTRO_ACTIVE']);invoke('VarSet',c['VAR_LITTLEROOT_INTRO_STATE'],7)
 invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS']);invoke('ScriptGiveMon',4,16,0);invoke('ScriptGiveMon',7,16,0)
 invoke('FlagSet',c['FLAG_DEVON_GOODS_STOLEN'])
 for name in ['FLAG_HIDE_RUSTURF_TUNNEL_AQUA_GRUNT','FLAG_HIDE_RUSTURF_TUNNEL_PEEKO']:invoke('FlagClear',c[name])
 invoke('FlagSet',c['FLAG_HIDE_RUSTURF_TUNNEL_BRINEY']);invoke('VarSet',c['VAR_RUSTURF_TUNNEL_STATE'],3)
 warp(c[names[0]],c[names[1]],13,5);prepare_prefixes();seen.clear()
 begin('RusturfTunnel_EventScript_Grunt',c['LOCALID_RUSTURF_TUNNEL_GRUNT'],c[names[0]],c[names[1]])
 until(lambda:rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1);frames(240)
 check('player_challenges_grunt_'+str(gender),'LegendsVoice_GruntChallenge' in seen)
 check('story_has_no_format_prompt_'+str(gender),active('Task_HandleYesNoInput') is None)
 wr(symbols['gBattleOutcome'],1,1);wr(symbols['gBattleMainFunc'],symbols['HandleEndTurn_BattleWon']|1)
 until(lambda:'LegendsVoice_PlayerIntroduction' in seen);frames(600)
 shutil.copy2(shot('spoken_player_'+str(gender)),proof/('introduction_'+str(gender)+'.png'))
 until(lambda:rd(symbols['sGlobalScriptContextStatus'],1)==2 and flag('FLAG_RECOVERED_DEVON_GOODS')==1)
 check('questions_grunt_'+str(gender),'LegendsVoice_GruntQuestion' in seen)
 check('introduces_self_'+str(gender),'LegendsVoice_PlayerIntroduction' in seen)
 check('thanks_briney_'+str(gender),'LegendsVoice_PeekoFarewell' in seen)
 check('parcel_obtained_'+str(gender),invoke('CheckBagHasItem',c['ITEM_DEVON_PARTS'],1)==1)
 check('rustboro_return_state_'+str(gender),invoke('VarGet',c['VAR_RUSTBORO_CITY_STATE'])==4)
 check('theft_flag_cleared_'+str(gender),not flag('FLAG_DEVON_GOODS_STOLEN'))
 check('tunnel_controls_return_'+str(gender),invoke('ArePlayerFieldControlsLocked')==0)
 # At the cottage the player explains the delivery and can decline departure.
 for name in ['FLAG_HIDE_BRINEYS_HOUSE_MR_BRINEY','FLAG_HIDE_BRINEYS_HOUSE_PEEKO','FLAG_MR_BRINEY_SAILING_INTRO']:invoke('FlagClear',c[name])
 warp(c[names[2]],c[names[3]],9,4);seen.clear()
 begin('Route104_MrBrineysHouse_EventScript_Briney',c['LOCALID_BRINEYS_HOUSE_BRINEY'],c[names[2]],c[names[3]])
 until(lambda:active('Task_HandleYesNoInput') is not None)
 check('asks_for_passage_'+str(gender),'LegendsVoice_BrineyRequest' in seen)
 check('explains_delivery_'+str(gender),'LegendsVoice_BrineyReason' in seen)
 frames(30);frames(4,2)
 until(lambda:rd(symbols['sGlobalScriptContextStatus'],1)==2)
 check('decline_is_spoken_'+str(gender),'LegendsVoice_BrineyNotYet' in seen)
 check('decline_stays_in_cottage_'+str(gender),location()==(c[names[2]],c[names[3]]))
 check('decline_controls_return_'+str(gender),invoke('ArePlayerFieldControlsLocked')==0)
 # Accept on the next visit: the original boat state/warp must still be set.
 begin('Route104_MrBrineysHouse_EventScript_Briney',c['LOCALID_BRINEYS_HOUSE_BRINEY'],c[names[2]],c[names[3]])
 until(lambda:active('Task_HandleYesNoInput') is not None);frames(30);frames(4,1)
 until(lambda:location()==(c[names[4]],c[names[5]]))
 check('departure_is_spoken_'+str(gender),'LegendsVoice_BrineyReady' in seen)
 check('boat_sequence_armed_'+str(gender),invoke('VarGet',c['VAR_ROUTE104_STATE'])==2)
 lib.shutdown()
# Font metrics for every new line, with the player's actual name expanded.
start(0)
for label in sorted(n for n in symbols if n.startswith('LegendsVoice_')):
 invoke('StringExpandPlaceholders',symbols['gStringVar4'],symbols[label]);lines=[[]]
 for i in range(1400):
  value=rd(symbols['gStringVar4']+i,1)
  if value==255:break
  if value in (250,251,254):lines.append([])
  else:lines[-1].append(value)
 for line_id,line in enumerate(lines):
  for i,value in enumerate(line+[255]):wr(0x0203fc00+i,value,1)
  check('fits_'+label+'_'+str(line_id),invoke('GetStringWidth',1,0x0203fc00,0)<=208)
lib.shutdown()
(proof/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),battle_outcome='injected native win to check continuation, not difficulty',checks=checks),indent=2)+'\n')
print('PASS',len(checks),'spoken story checks')
