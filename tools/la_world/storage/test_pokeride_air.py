"""Fly-gated low flight keeps native route collision and save semantics."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pokeride.py').read_text().split('for gender in [0,1]:')[0],'ride_helpers','exec'))
extra=['FLAG_BADGE01_GET','MOVE_FLY','ITEM_HM02','offsetof(__typeof__(sRide),airHeight)']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'a.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "constants/flags.h"\n#include "constants/items.h"\n#include <stddef.h>\n'+prefix+'const unsigned v[]={'+','.join(extra)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'a.c'),'-o',str(td/'a.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'a.o'),str(td/'a.bin')],check=True)
 c.update(zip(extra,struct.unpack('<4I',(td/'a.bin').read_bytes())))
D=R/'docs/features/pokeride-air';D.mkdir(exist_ok=True)
def height():return rd(symbols['sRide']+c['offsetof(__typeof__(sRide),airHeight)'],1)
def wallbank():
 for y in range(5,14):
  for x in range(2,18):
   if invoke('MapGridGetCollisionAt',x+7,y+7)!=0:continue
   for direction,dx,dy,key in [(2,0,-1,64),(3,-1,0,32),(4,1,0,16),(1,0,1,128)]:
    beh=invoke('MapGridGetMetatileBehaviorAt',x+dx+7,y+dy+7)
    if invoke('MapGridGetCollisionAt',x+dx+7,y+dy+7)==0:continue
    if invoke('MetatileBehavior_IsSurfableWaterOrUnderwater',beh):continue
    if invoke('MetatileBehavior_IsWarpDoor',beh):continue
    return x,y,key
 raise AssertionError('No wall edge')
for gender in [0,1]:
 start(gender);invoke('StorageChangeMode',gender,1);invoke('ScriptGiveMon',6,40,0);invoke('ScriptGiveMon',3,40,0)
 invoke('SetMonMoveSlot',symbols['gParties'],c['MOVE_FLY'],0);invoke('AddBagItem',c['ITEM_HM02'],1)
 invoke('FlagSet',c['FLAG_SYS_B_DASH']);warp(0,9,10,10)
 check('charizard_air_species_'+str(gender),invoke('PokeRide_IsAirSpecies',6)==1)
 check('venusaur_not_air_species_'+str(gender),invoke('PokeRide_IsAirSpecies',3)==0)
 check('mount_'+str(gender),invoke('PokeRide_Start',0)==1);frames(30)
 check('fly_locked_'+str(gender),invoke('PokeRide_CanFly')==0)
 check('takeoff_locked_'+str(gender),invoke('PokeRide_ToggleFlight')==0)
 for badge in range(6):invoke('FlagSet',c['FLAG_BADGE01_GET']+badge)
 check('fly_unlocked_'+str(gender),invoke('PokeRide_CanFly')==1)
 flags=rd(symbols['gPlayerAvatar']+c['offsetof(struct PlayerAvatar,flags)'],1)
 before=pos();tap(2);frames(30)
 check('b_takes_off_'+str(gender),invoke('PokeRide_IsAirborne')==1 and height()==12)
 check('takeoff_keeps_position_'+str(gender),pos()==before)
 check('takeoff_keeps_native_flags_'+str(gender),rd(symbols['gPlayerAvatar']+c['offsetof(struct PlayerAvatar,flags)'],1)==flags)
 check('air_dismount_blocked_'+str(gender),invoke('PokeRide_CanDismount')==0)
 check('air_switch_blocked_'+str(gender),invoke('PokeRide_Start',1)==0)
 tap(768);frames(20)
 check('shoulders_do_not_drop_rider_'+str(gender),invoke('PokeRide_IsAirborne')==1)
 check('no_control_lock_'+str(gender),invoke('ArePlayerFieldControlsLocked')==0)
 moved=False
 for key in [16,32,64,128]:
  p=pos();frames(18,key);frames(20);moved|=pos()!=p
 check('air_moves_on_paths_'+str(gender),moved)
 shutil.copy2(shot('air_'+str(gender)),D/('air-'+str(gender)+'.png'))
 invoke('FlagSet',c['FLAG_SYS_POKEMON_GET']);wr(symbols['sStartMenuPage'],0,1);wr(symbols['sStartMenuCursorPos'],0,1)
 tap(8);frames(40);tap(1);frames(150)
 check('party_open_'+str(gender),active('Task_HandleChooseMonInput') is not None)
 tap(2);frames(180);tap(2);frames(70)
 for i in range(3):
  if active('Task_ShowStartMenu') is None:break
  tap(2);frames(70)
 check('menu_keeps_air_'+str(gender),invoke('PokeRide_IsAirborne')==1 and height()==12)
 check('menu_keeps_gender_'+str(gender),playergfx()==c['OBJ_EVENT_GFX_LA_MAY_RIDING' if gender else 'OBJ_EVENT_GFX_LA_BRENDAN_RIDING'])
 check('save_in_air_'+str(gender),invoke('TrySavingData',0)==1)
 tap(2);frames(30)
 check('b_lands_'+str(gender),invoke('PokeRide_IsAirborne')==0 and height()==0)
 check('ground_dismount_allowed_'+str(gender),invoke('PokeRide_CanDismount')==1)
 invoke('PokeRide_Stop');frames(20)
 x,y,key=wallbank();warp(0,9,x,y);invoke('PokeRide_Start',0);frames(30)
 initial=pos();frames(18,key);frames(25)
 check('ground_wall_blocks_'+str(gender),pos()==initial)
 invoke('PokeRide_ToggleFlight');frames(30);frames(18,key);frames(25)
 check('air_wall_still_blocks_'+str(gender),pos()==initial)
 check('wall_does_not_cancel_air_'+str(gender),invoke('PokeRide_IsAirborne')==1)
 # Scripts and indoor maps can always safely land a low-flight rider.
 warp(1,4,6,8);frames(30)
 check('indoor_lands_'+str(gender),invoke('PokeRide_IsActive')==0 and height()==0)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'aerial ride checks')
