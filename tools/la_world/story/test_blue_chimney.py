"""Blue briefing, directional gates, native cable-car ride and summit continuation."""
from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct,re,json,hashlib
names=['FLAG_LA_RED_DEX_GIFTS','FLAG_BADGE01_GET','FLAG_LA_BLUE_CHIMNEY_BRIEFED','FLAG_LA_BLUE_CABLE_MET','FLAG_LA_BLUE_CHIMNEY_BOARDED','FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY','FLAG_LA_CHIMNEY_RESONANCE','FLAG_LA_COZMO_BRIEFED','FLAG_LA_HEARD_GIOVANNI','FLAG_HIDE_ROUTE_112_TEAM_MAGMA','VAR_LA_OAK_STARTER','VAR_LA_ASHES_STATE','MAP_FALLARBOR_TOWN','MAP_ROUTE112_CABLE_CAR_STATION','MAP_MT_CHIMNEY_CABLE_CAR_STATION','MAP_MT_CHIMNEY','LOCALID_LA_FALLARBOR_BLUE','LOCALID_LA_BLUE_CHIMNEY','LOCALID_ROUTE112_CABLE_CAR_ATTENDANT','DIR_NORTH']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/flags.h"\n#include "constants/vars.h"\n#include "constants/maps.h"\n#include "constants/map_event_ids.h"\n#include "constants/event_object_movement.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def flag(n):return invoke('FlagGet',c[n])
def at(n,x,y):
 m=c[n];warp(m>>8,m&255,x,y);frames(60)
def ended():return rd(symbols['sGlobalScriptContextStatus'],1)==2 and not rd(symbols['sLockFieldControls'],1) and rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1
def waitfor(predicate,label,limit=18000):
 for i in range(limit):
  if predicate():return
  frames(1,1 if i%24<3 else 0)
 print(shot('blue_timeout_'+label),flush=True)
 raise AssertionError((label,location(),pos(),hex(rd(symbols['gMain']+4))))
def finish(label):waitfor(ended,label);frames(15)
def run(n):invoke('ScriptContext_SetupScript',symbols[n]);frames(2)
start(0);invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
for i in range(3):invoke('FlagSet',c['FLAG_BADGE01_GET']+i)
for sp in [1,4,7,25,133,155]:invoke('ScriptGiveMon',sp,26,0)
invoke('VarSet',c['VAR_LA_OAK_STARTER'],2);invoke('VarSet',c['VAR_LA_ASHES_STATE'],1)
# Production-font checks for every new/revised conversation.
for n in sorted(symbols):
 if not (n.startswith('BlueChimney_Text_') or n.startswith('FallarborTown_CozmosHouse_Text_')):continue
 data=bytearray()
 for i in range(2200):
  b=rd(symbols[n]+i,1)
  if b==255:break
  data.append(b)
 for i,line in enumerate(re.split(b'[\xfe\xfb\xfa]',bytes(data))):
  if 253 in line:continue
  for j,b in enumerate(line+b'\xff'):wr(0x03007500+j,b,1)
  width=invoke('GetStringWidth',1,0x03007500,0)
  check('line_fit_'+n+'_'+str(i),width<=208)
# Leaving both sides is blocked, but walking into town is allowed.
at('MAP_FALLARBOR_TOWN',2,10);frames(40,32);finish('west_gate')
check('west_gate_keeps_player_in_town',location()==(c['MAP_FALLARBOR_TOWN']>>8,c['MAP_FALLARBOR_TOWN']&255) and pos()[0]>=2)
at('MAP_FALLARBOR_TOWN',17,10);frames(40,16);finish('east_gate')
check('east_gate_keeps_player_in_town',pos()[0]<=17)
at('MAP_FALLARBOR_TOWN',1,10);frames(40,16);finish('west_entry')
check('entering_fallarbor_not_blocked',pos()[0]>=2)
# Brief Blue through his real object interaction.
at('MAP_FALLARBOR_TOWN',14,11);invoke('FlagSet',c['FLAG_LA_HEARD_GIOVANNI'])
tap(64);tap(1);finish('blue_briefing')
check('blue_briefing_saved',flag('FLAG_LA_BLUE_CHIMNEY_BRIEFED'))
check('oak_introduction_retained',invoke('VarGet',c['VAR_LA_OAK_STARTER'])==10)
at('MAP_FALLARBOR_TOWN',17,10);frames(40,16);finish('east_open')
check('briefed_player_can_reach_edge',pos()[0]>=18)
# The existing Meteor Falls flag opens the route to the cable-car station.
invoke('FlagSet',c['FLAG_LA_COZMO_BRIEFED']);invoke('FlagSet',c['FLAG_HIDE_ROUTE_112_TEAM_MAGMA']);invoke('VarSet',c['VAR_LA_ASHES_STATE'],2)
at('MAP_ROUTE112_CABLE_CAR_STATION',6,10);frames(40,64);finish('station_teamup')
check('station_scene_automatic',flag('FLAG_LA_BLUE_CABLE_MET'))
print(shot('blue_cable_teamup'),flush=True)
at('MAP_ROUTE112_CABLE_CAR_STATION',6,7);tap(64);tap(1)
upper=c['MAP_MT_CHIMNEY_CABLE_CAR_STATION']
waitfor(lambda:location()==(upper>>8,upper&255),'native_cable_ride')
finish('cable_exit')
check('blue_boarded_same_cable_car',flag('FLAG_LA_BLUE_CHIMNEY_BOARDED'))
# Native Maxie battle and original postbattle/Hoopa scene still complete.
at('MAP_MT_CHIMNEY',13,7);tap(64);tap(1)
waitfor(lambda:rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1 and rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,'maxie_battle')
wr(symbols['gBattleOutcome'],1,1);wr(symbols['gBattleMainFunc'],symbols['HandleEndTurn_BattleWon']|1)
finish('summit_aftermath')
check('native_chimney_completion_preserved',flag('FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY'))
check('hoopa_aftermath_preserved',flag('FLAG_LA_CHIMNEY_RESONANCE'))
obj=invoke('GetObjectEventIdByLocalIdAndMap',c['LOCALID_LA_BLUE_CHIMNEY'],c['MAP_MT_CHIMNEY']&255,c['MAP_MT_CHIMNEY']>>8)
check('blue_rejoins_at_summit',obj<16)
print(shot('blue_summit_aftermath'),flush=True)
# Previously completed saves bypass the new briefing gate and do not loop.
invoke('FlagClear',c['FLAG_LA_BLUE_CHIMNEY_BRIEFED'])
at('MAP_FALLARBOR_TOWN',17,10);frames(40,16);finish('legacy_exit')
check('completed_saves_not_locked',pos()[0]>=18)
invoke('VarSet',c['VAR_LA_OAK_STARTER'],10)
run('RiftResearch_Blue');finish('legacy_blue_repeat')
check('legacy_blue_repeat_ends',ended())
report=dict(passed=True,checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest())
p=R/'docs/story/blue-chimney/validation.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(report,indent=2)+'\n')
print('PASS',len(checks),'Blue chapter checks',flush=True)
