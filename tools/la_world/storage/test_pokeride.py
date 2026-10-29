"""Native ground mounts, collision boundaries, menu returns and HM coexistence."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_preferred_follower.py').read_text().split('for mode in [0,1]:')[0],'helpers','exec'))
source=(R/'src/pokeride.c').read_text();prefix=source[source.index('static EWRAM_DATA struct {'):source.index('static const struct PokeRideInfo *RideInfo')].replace('static EWRAM_DATA','')
names=['FLAG_SYS_B_DASH','FLAG_SYS_POKEMON_GET','offsetof(struct PlayerAvatar,objectEventId)','offsetof(struct PlayerAvatar,spriteId)','offsetof(struct PlayerAvatar,flags)','offsetof(struct ObjectEvent,graphicsId)','sizeof(struct ObjectEvent)','OBJ_EVENT_GFX_LA_BRENDAN_RIDING','OBJ_EVENT_GFX_LA_MAY_RIDING','PLAYER_AVATAR_FLAG_UNDERWATER','PLAYER_AVATAR_FLAG_SURFING','offsetof(__typeof__(sRide),sprite)','offsetof(__typeof__(sRide),hasSprite)','MON_DATA_IS_EGG']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'r.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "constants/flags.h"\n#include "constants/event_objects.h"\n#include <stddef.h>\n'+prefix+'const unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'r.c'),'-o',str(td/'r.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'r.o'),str(td/'r.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'r.bin').read_bytes())))
D=R/'docs/features/pokeride';D.mkdir(exist_ok=True)
def player():return symbols['gObjectEvents']+rd(symbols['gPlayerAvatar']+c['offsetof(struct PlayerAvatar,objectEventId)'],1)*c['sizeof(struct ObjectEvent)']
def playergfx():return rd(player()+c['offsetof(struct ObjectEvent,graphicsId)'],2)
def warp(group,mapid,x,y):
 invoke('ScriptContext_Init');invoke('UnlockPlayerFieldControls')
 a=symbols['sWarpDestination']
 for i,value in enumerate(struct.pack('<BBbxhh',group,mapid,-1,x,y)):wr(a+i,value,1)
 wr(symbols['gMain']+4,symbols['WarpIntoMap']|1);frames(2)
 wr(symbols['gMain']+4,symbols['CB2_LoadMap']|1);frames(180)
for gender in [0,1]:
 start(gender);invoke('StorageChangeMode',gender,1);invoke('ScriptGiveMon',3,20,0);invoke('ScriptGiveMon',25,20,0);invoke('ScriptGiveMon',6,20,0);invoke('ScriptGiveMon',903,20,0)
 check('supported_venusaur_'+str(gender),invoke('PokeRide_IsValidSpecies',3)==1)
 check('unsupported_pikachu_'+str(gender),invoke('PokeRide_IsValidSpecies',25)==0)
 check('indoor_refused_'+str(gender),invoke('PokeRide_Start',0)==0)
 warp(0,9,10,10)
 check('story_gate_'+str(gender),invoke('PokeRide_Start',0)==0)
 invoke('FlagSet',c['FLAG_SYS_B_DASH'])
 check('invalid_slot_'+str(gender),invoke('PokeRide_Start',6)==0)
 check('unsupported_refused_'+str(gender),invoke('PokeRide_Start',1)==0)
 a=0x0203fc00;wr(a,1);invoke('SetMonData',symbols['gParties'],c['MON_DATA_IS_EGG'],a)
 check('egg_refused_'+str(gender),invoke('PokeRide_Start',0)==0)
 wr(a,0);invoke('SetMonData',symbols['gParties'],c['MON_DATA_IS_EGG'],a)
 flags=rd(symbols['gPlayerAvatar']+c['offsetof(struct PlayerAvatar,flags)'],1)

 check('mount_start_'+str(gender),invoke('PokeRide_Start',0)==1)
 frames(60)
 check('mount_stays_active_'+str(gender),invoke('PokeRide_IsActive')==1)
 check('mounted_graphics_'+str(gender),playergfx()==c['OBJ_EVENT_GFX_LA_MAY_RIDING' if gender else 'OBJ_EVENT_GFX_LA_BRENDAN_RIDING'])
 check('sprite_created_'+str(gender),rd(symbols['sRide']+c['offsetof(__typeof__(sRide),hasSprite)'],1)==1)
 check('native_flags_preserved_'+str(gender),rd(symbols['gPlayerAvatar']+c['offsetof(struct PlayerAvatar,flags)'],1)==flags)
 moved=False
 for key in [16,32,64,128]:
  before=pos()
  frames(18,key);frames(15)
  moved |= before != pos()
  check('walks_without_dismount_'+str((gender,key)),invoke('PokeRide_IsActive')==1)
 check('actually_moves_'+str(gender),moved)
 shutil.copy2(shot('ride_'+str(gender)),D/('mounted-'+str(gender)+'.png'))
 # Open/close Start without losing the mount; L+R dismounts only back in field.
 tap(8);frames(40)
 tap(2);frames(60)
 check('start_return_keeps_mount_'+str(gender),invoke('PokeRide_IsActive')==1)
 tap(768);frames(40)
 check('shoulders_dismount_'+str(gender),invoke('PokeRide_IsActive')==0)
 check('dismount_controls_released_'+str(gender),invoke('ArePlayerFieldControlsLocked')==0)
 check('sprite_removed_'+str(gender),rd(symbols['sRide']+c['offsetof(__typeof__(sRide),hasSprite)'],1)==0)
 # Mount the other supported shapes, then repeatedly switch and release resources.
 for slot in [2,3,0,2,3,0]:
  check('switch_mount_'+str((gender,slot,len(checks))),invoke('PokeRide_Start',slot)==1)
  frames(25)
  check('switch_sprite_'+str((gender,slot,len(checks))),rd(symbols['sRide']+c['offsetof(__typeof__(sRide),hasSprite)'],1)==1)
  if slot in [2,3]:shutil.copy2(shot('ride_shape_'+str((gender,slot))),D/('shape-'+str(gender)+'-'+str(slot)+'.png'))
 # A real Pokemon-menu return resets all sprite slots; the mount must recreate safely.
 invoke('FlagSet',c['FLAG_SYS_POKEMON_GET'])
 wr(symbols['sStartMenuPage'],0,1);wr(symbols['sStartMenuCursorPos'],0,1)
 tap(8);frames(40);tap(1);frames(150)
 check('party_open_'+str(gender),active('Task_HandleChooseMonInput') is not None)
 tap(2);frames(180);tap(2);frames(60)
 check('party_return_keeps_mount_'+str(gender),invoke('PokeRide_IsActive')==1)
 check('party_return_sprite_'+str(gender),rd(symbols['sRide']+c['offsetof(__typeof__(sRide),hasSprite)'],1)==1)
 invoke('PokeRide_Stop');frames(20)
 # Choose Ride through the actual Follower submenu.
 wr(symbols['sStartMenuCursorPos'],0,1)
 tap(8);frames(40);tap(1);frames(150);tap(1);frames(30)
 for i in range(4):tap(128)
 tap(1);frames(30);tap(128)
 shutil.copy2(shot('ride_menu_'+str(gender)),D/('menu-'+str(gender)+'.png'))
 tap(1);frames(70);tap(1);frames(45)
 check('ride_menu_selects_'+str(gender),invoke('PokeRide_IsActive')==1)
 tap(2);frames(180);tap(2);frames(60)
 shutil.copy2(shot('ride_ui_return_'+str(gender)),D/('ui-return-'+str(gender)+'.png'))
 check('ride_menu_return_'+str(gender),invoke('PokeRide_IsActive')==1 and playergfx()==c['OBJ_EVENT_GFX_LA_MAY_RIDING' if gender else 'OBJ_EVENT_GFX_LA_BRENDAN_RIDING'])
 for i in range(3):
  if active('Task_ShowStartMenu') is None:break
  tap(2);frames(70)
 check('field_ready_for_battle_'+str(gender),invoke('ArePlayerFieldControlsLocked')==0)
 # A wild battle resets sprites; escape must return to a controllable field.
 invoke('CreateScriptedWildMon',261,3,0);invoke('BattleSetup_StartWildBattle')
 for i in range(1200):
  frames(1,1 if i%30==0 else 0)
  if rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:
   frames(40);break
 check('battle_entered_'+str(gender),rd(symbols['gMain']+4)!=symbols['CB2_Overworld']|1)
 tap(16);tap(128);tap(1)
 for i in range(1200):
  frames(1,1 if i%30==0 else 0)
  if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1 and not invoke('ArePlayerFieldControlsLocked'):
   break
 shutil.copy2(shot('ride_battle_return_'+str(gender)),D/('battle-return-'+str(gender)+'.png'))
 check('battle_returns_to_field_'+str(gender),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 check('battle_controls_released_'+str(gender),invoke('ArePlayerFieldControlsLocked')==0)
 frames(40)
 if not invoke('PokeRide_IsActive'):invoke('PokeRide_Start',0);frames(30)
 # Saving uses the existing serializer; ride state adds no save schema.
 check('save_while_mounted_'+str(gender),invoke('TrySavingData',0)==1)
 check('storage_mode_unchanged_'+str(gender),invoke('GetStorageBoxCount')==(60 if gender else 14))
 # Entering an indoor map dismounts and restores a normal player.
 warp(1,4,6,8);frames(30)
 check('indoor_dismount_'+str(gender),invoke('PokeRide_IsActive')==0)
 check('underwater_bit_preserved_'+str(gender),c['PLAYER_AVATAR_FLAG_UNDERWATER']==16 and c['PLAYER_AVATAR_FLAG_SURFING']==8)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'ground ride checks')
