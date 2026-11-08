"""Native Surf-gated water mounts, shoreline transitions and menu/battle state."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_preferred_follower.py').read_text().split('for mode in [0,1]:')[0],'helpers','exec'))
names=['FLAG_SYS_B_DASH','FLAG_BADGE01_GET','FLAG_SYS_POKEMON_GET','MOVE_SURF','ITEM_HM03','offsetof(struct PlayerAvatar,flags)','offsetof(struct PlayerAvatar,objectEventId)','offsetof(struct PlayerAvatar,preventStep)','offsetof(struct ObjectEvent,graphicsId)','offsetof(struct ObjectEvent,fieldEffectSpriteId)','sizeof(struct ObjectEvent)','OBJ_EVENT_GFX_LA_BRENDAN_WATER_RIDING','OBJ_EVENT_GFX_LA_MAY_WATER_RIDING','PLAYER_AVATAR_FLAG_SURFING','PLAYER_AVATAR_FLAG_ON_FOOT','MON_DATA_HP','MOVE_FLY','ITEM_HM02']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'w.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "constants/flags.h"\n#include "constants/items.h"\n#include "constants/event_objects.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'w.c'),'-o',str(td/'w.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'w.o'),str(td/'w.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'w.bin').read_bytes())))
D=R/'docs/features/pokeride-water';D.mkdir(exist_ok=True)
def player():return symbols['gObjectEvents']+rd(symbols['gPlayerAvatar']+c['offsetof(struct PlayerAvatar,objectEventId)'],1)*c['sizeof(struct ObjectEvent)']
def flags():return rd(symbols['gPlayerAvatar']+c['offsetof(struct PlayerAvatar,flags)'],1)
def playergfx():return rd(player()+c['offsetof(struct ObjectEvent,graphicsId)'],2)
def surf():return bool(flags() & c['PLAYER_AVATAR_FLAG_SURFING'])
def realwarp(group,mid,x,y):
 invoke('ScriptContext_Init');invoke('UnlockPlayerFieldControls')
 a=symbols['sWarpDestination']
 for i,value in enumerate(struct.pack('<BBbxhh',group,mid,-1,x,y)):wr(a+i,value,1)
 wr(symbols['gMain']+4,symbols['WarpIntoMap']|1);frames(2)
 wr(symbols['gMain']+4,symbols['CB2_LoadMap']|1);frames(180)
def water(x,y):return invoke('MetatileBehavior_IsSurfableFishableWater',invoke('MapGridGetMetatileBehaviorAt',x+7,y+7))!=0
def bank():
 for y in range(6,15):
  for x in range(6,17):
   if water(x,y) or invoke('MapGridGetCollisionAt',x+7,y+7)!=0:continue
   for direction,dx,dy,key,opposite in [(1,0,1,128,64),(2,0,-1,64,128),(3,-1,0,32,16),(4,1,0,16,32)]:
    if water(x+dx,y+dy) and water(x+2*dx,y+2*dy):return x,y,direction,key,opposite
 raise AssertionError('No valid shoreline')
for gender in [0,1]:
 start(gender);invoke('StorageChangeMode',gender,1);invoke('ScriptGiveMon',131,25,0);invoke('ScriptGiveMon',6,25,0);invoke('ScriptGiveMon',249,25,0)
 invoke('SetMonMoveSlot',symbols['gParties'],c['MOVE_SURF'],0)
 invoke('SetMonMoveSlot',symbols['gParties']+200,c['MOVE_SURF'],0);invoke('SetMonMoveSlot',symbols['gParties']+200,c['MOVE_FLY'],1)
 invoke('AddBagItem',c['ITEM_HM03'],1);invoke('FlagSet',c['FLAG_SYS_B_DASH'])
 for tid in [318,333,603,615]:invoke('SetTrainerFlag',tid)
 realwarp(0,17,5,12)
 check('lapras_swims_'+str(gender),invoke('PokeRide_IsWaterSpecies',131)==1)
 check('charizard_not_swimmer_'+str(gender),invoke('PokeRide_IsWaterSpecies',6)==0)
 original=flags();wr(symbols['gPlayerAvatar']+c['offsetof(struct PlayerAvatar,flags)'],32|c['PLAYER_AVATAR_FLAG_SURFING'],1)
 check('badge_gate_'+str(gender),invoke('PokeRide_BeginSurf',0)==0)
 wr(symbols['gPlayerAvatar']+c['offsetof(struct PlayerAvatar,flags)'],original,1)
 for badge in range(5):invoke('FlagSet',c['FLAG_BADGE01_GET']+badge)
 x,y,direction,key,opposite=bank();print('BANK',gender,x,y,direction,flush=True)
 realwarp(0,17,x,y);invoke('PlayerFaceDirection',direction);frames(30)
 check('starts_on_land_'+str(gender),not surf())
 tap(1)
 for i in range(1500):
  frames(1,1 if i%45==0 else 0)
  if surf() and invoke('PokeRide_IsWaterMode') and not invoke('ArePlayerFieldControlsLocked'):
   frames(40);break
 check('native_surf_started_'+str(gender),surf())
 check('automatic_water_mount_'+str(gender),invoke('PokeRide_IsWaterMode')==1)
 check('water_rider_graphics_'+str(gender),playergfx()==c['OBJ_EVENT_GFX_LA_MAY_WATER_RIDING' if gender else 'OBJ_EVENT_GFX_LA_BRENDAN_WATER_RIDING'])
 check('blob_hidden_'+str(gender),invoke('PokeRide_HidesSurfBlob')==1)
 check('cannot_dismount_offshore_'+str(gender),invoke('PokeRide_CanDismount')==0)
 tap(768);frames(30)
 check('shoulders_stay_on_water_mount_'+str(gender),invoke('PokeRide_IsWaterMode')==1 and surf())
 check('controls_not_locked_'+str(gender),invoke('ArePlayerFieldControlsLocked')==0)
 startpos=pos();frames(18,key);frames(20)
 check('moves_on_water_'+str(gender),pos()!=startpos and surf())
 shutil.copy2(shot('water_ride_'+str(gender)),D/('water-'+str(gender)+'.png'))
 # Menu return must retain Surf, rather than interpreting riding as on-foot.
 invoke('FlagSet',c['FLAG_SYS_POKEMON_GET']);wr(symbols['sStartMenuPage'],0,1);wr(symbols['sStartMenuCursorPos'],0,1)
 tap(8);frames(40);tap(1);frames(150)
 check('party_open_'+str(gender),active('Task_HandleChooseMonInput') is not None)
 tap(2);frames(180);tap(2);frames(70)
 for i in range(3):
  if active('Task_ShowStartMenu') is None:break
  tap(2);frames(70)
 check('party_keeps_surf_'+str(gender),surf() and invoke('PokeRide_IsWaterMode')==1)
 check('party_keeps_gender_'+str(gender),playergfx()==c['OBJ_EVENT_GFX_LA_MAY_WATER_RIDING' if gender else 'OBJ_EVENT_GFX_LA_BRENDAN_WATER_RIDING'])
 # A supported swimmer/flier still needs Fly permission while over water.
 check('combined_water_mount_'+str(gender),invoke('PokeRide_Start',2)==1);frames(25)
 check('water_flight_locked_'+str(gender),invoke('PokeRide_CanFly')==0)
 invoke('FlagSet',c['FLAG_BADGE01_GET']+5);invoke('AddBagItem',c['ITEM_HM02'],1)
 tap(2);frames(30)
 check('water_low_flight_'+str(gender),invoke('PokeRide_IsAirborne')==1 and surf())
 tap(2);frames(30)
 check('land_on_water_mount_'+str(gender),invoke('PokeRide_IsAirborne')==0 and surf())
 check('still_no_offshore_dismount_'+str(gender),invoke('PokeRide_CanDismount')==0)
 check('restore_lapras_'+str(gender),invoke('PokeRide_Start',0)==1);frames(25)
 # A fainted mount must fall back to native Surf, never leave a walking avatar.
 scratch=0x0203fc00;wr(scratch,0);invoke('SetMonData',symbols['gParties'],c['MON_DATA_HP'],scratch);frames(30)
 check('faint_keeps_native_surf_'+str(gender),surf() and invoke('PokeRide_IsActive')==0)
 blob=rd(player()+c['offsetof(struct ObjectEvent,fieldEffectSpriteId)'],1)
 check('fallback_blob_visible_'+str(gender),not (rd(symbols['gSprites']+blob*68+62,1)&4))
 wr(scratch,40);invoke('SetMonData',symbols['gParties'],c['MON_DATA_HP'],scratch)
 check('remount_on_water_'+str(gender),invoke('PokeRide_Start',0)==1);frames(30)
 check('reject_land_species_on_water_'+str(gender),invoke('PokeRide_Start',1)==0)
 # Battle sprite resets must retain the Surf mode and seated avatar on return.
 invoke('CreateScriptedWildMon',261,3,0);invoke('BattleSetup_StartWildBattle')
 for i in range(1200):
  frames(1,1 if i%30==0 else 0)
  if rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:
   frames(40);break
 tap(16);tap(128);tap(1)
 for i in range(1200):
  frames(1,1 if i%30==0 else 0)
  if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1 and not invoke('ArePlayerFieldControlsLocked'):break
 frames(30)
 check('battle_returns_surfing_'+str(gender),surf() and rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 check('battle_keeps_water_mount_'+str(gender),invoke('PokeRide_IsWaterMode')==1)
 check('save_on_water_'+str(gender),invoke('TrySavingData',0)==1)
 # Reload without temporary ride state: native Surf remains safe on water.
 savedpos=pos();invoke('PokeRide_Stop')
 check('reload_battery_'+str(gender),invoke('LoadGameSave',0)==1)
 realwarp(0,17,*savedpos)
 check('reload_native_surf_'+str(gender),surf())
 check('reload_remount_'+str(gender),invoke('PokeRide_Start',0)==1);frames(30)
 # Return to the original bank through the native stop-Surf hop.
 for i in range(6):
  if not surf():break
  frames(16,opposite);frames(40)
 check('native_shore_exit_'+str(gender),not surf())
 check('shore_controls_released_'+str(gender),invoke('ArePlayerFieldControlsLocked')==0)
 check('land_dismount_allowed_'+str(gender),invoke('PokeRide_CanDismount')==1)
 tap(768);frames(30)
 check('land_dismounts_'+str(gender),invoke('PokeRide_IsActive')==0)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'water ride checks')
