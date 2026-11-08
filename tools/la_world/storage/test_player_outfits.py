"""Native character colors: live PC UI, cancellation, persistence and intro."""
from pathlib import Path
import tempfile,struct,json,hashlib,shutil,subprocess
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/player-outfits';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
def capture(n):shutil.copy2(shot('dynpal_'+n),D/(n+'.png'))
def until(task,limit=30000):
 for i in range(limit):
  if active(task) is not None:return active(task)
  frames(1,1 if i%13==0 else 0)
 raise AssertionError(('task',task,hex(rd(symbols['gMain']+4))))
names=['VAR_LA_PLAYER_OUTFIT','VERSION_EMERALD','FLAG_SYS_B_DASH','offsetof(struct PlayerAvatar,objectEventId)','offsetof(struct PlayerAvatar,spriteId)','sizeof(struct ObjectEvent)','TRAINER_PIC_RS_BRENDAN','TRAINER_PIC_RS_MAY','OBJ_EVENT_GFX_LA_BRENDAN_RIDING','OBJ_EVENT_GFX_LA_MAY_RIDING','OBJ_EVENT_GFX_LA_BRENDAN_WATER_RIDING','OBJ_EVENT_GFX_LA_MAY_WATER_RIDING','OBJ_EVENT_GFX_BRENDAN_NORMAL','OBJ_EVENT_GFX_BRENDAN_MACH_BIKE','OBJ_EVENT_GFX_BRENDAN_ACRO_BIKE','OBJ_EVENT_GFX_BRENDAN_SURFING','OBJ_EVENT_GFX_BRENDAN_UNDERWATER','OBJ_EVENT_GFX_BRENDAN_FIELD_MOVE','OBJ_EVENT_GFX_BRENDAN_FISHING','OBJ_EVENT_GFX_BRENDAN_WATERING','OBJ_EVENT_GFX_BRENDAN_DECORATING','OBJ_EVENT_GFX_MAY_NORMAL','OBJ_EVENT_GFX_MAY_MACH_BIKE','OBJ_EVENT_GFX_MAY_ACRO_BIKE','OBJ_EVENT_GFX_MAY_SURFING','OBJ_EVENT_GFX_MAY_UNDERWATER','OBJ_EVENT_GFX_MAY_FIELD_MOVE','OBJ_EVENT_GFX_MAY_FISHING','OBJ_EVENT_GFX_MAY_WATERING','OBJ_EVENT_GFX_MAY_DECORATING','VAR_LA_PLAYER_COLORS','OBJ_EVENT_PAL_TAG_AREN','OBJ_EVENT_PAL_TAG_ARIA','OBJ_EVENT_PAL_TAG_BRENDAN','OBJ_EVENT_PAL_TAG_MAY','TRAINER_PIC_BRENDAN','TRAINER_PIC_MAY','offsetof(struct Sprite,oam)','offsetof(struct Sprite,images)','offsetof(struct ObjectEventGraphicsInfo,images)','ITEM_POKEVIAL','ITEM_POTION']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'a.c').write_text('#include "global.h"\n#include "sprite.h"\n#include "event_object_movement.h"\n#include "constants/event_objects.h"\n#include "constants/trainers.h"\n#include <stddef.h>\nconst unsigned values[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'a.c'),'-o',str(td/'a.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'a.o'),str(td/'a.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'a.bin').read_bytes())))
def pal(ptr):return tuple(rd(ptr+i*2,2) for i in range(16))
def openpc():
 invoke('PlayerPC');until('PlayerPCProcessMenuInput');frames(25);tap(128);tap(128);tap(1);until('Task_DynamicPalMenu');frames(45)
def finishpc(key):
 tap(key);until('PlayerPCProcessMenuInput');frames(20);tap(2);frames(90)

def player():return symbols['gObjectEvents']+rd(symbols['gPlayerAvatar']+c['offsetof(struct PlayerAvatar,objectEventId)'],1)*c['sizeof(struct ObjectEvent)']
def images(gfx):return rd(invoke('GetObjectEventGraphicsInfo',gfx)+c['offsetof(struct ObjectEventGraphicsInfo,images)'])
for gender,mode in [(0,0),(1,1)]:
 tag=f'g{gender}_mode{mode}';print('CASE',tag,flush=True)
 start(gender);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',3,20,0)
 invoke('StorageWriteMon',59 if mode else 13,29,symbols['gParties'])
 check(tag+'_legacy_defaults_emerald',invoke('PlayerOutfit_Get')==0)
 g='MAY' if gender else 'BRENDAN';name='May' if gender else 'Brendan'
 states=['NORMAL','MACH_BIKE','ACRO_BIKE','SURFING','UNDERWATER','FIELD_MOVE','FISHING','WATERING','DECORATING']
 old={state:images(c['OBJ_EVENT_GFX_'+g+'_'+state]) for state in states}
 # Real PC UI: select another style, then cancel; both visuals and data restore.
 openpc();tap(64);tap(16);frames(40);capture(tag+'_rs_preview')
 check(tag+'_live_style',invoke('PlayerOutfit_Get')==1)
 check(tag+'_style_keeps_colors',invoke('DynamicPal_GetSelection')==0)
 check(tag+'_walking_changes',images(c['OBJ_EVENT_GFX_'+g+'_NORMAL'])!=old['NORMAL'])
 finishpc(2)
 check(tag+'_cancel_restores_style',invoke('PlayerOutfit_Get')==0 and images(c['OBJ_EVENT_GFX_'+g+'_NORMAL'])==old['NORMAL'])
 openpc();tap(16);tap(128);tap(16);tap(128);tap(16);tap(128);tap(16);frames(40);capture(tag+'_custom_rs_preview');finishpc(1)
 check(tag+'_accepted_style_and_colors',invoke('PlayerOutfit_Get')==1 and invoke('DynamicPal_GetSelection')==0x111)
 for state in states:
  check(tag+'_alternate_'+state,images(c['OBJ_EVENT_GFX_'+g+'_'+state])!=old[state])
 pic=c['TRAINER_PIC_RS_MAY' if gender else 'TRAINER_PIC_RS_BRENDAN']
 check(tag+'_player_front_and_back',invoke('GetPlayerTrainerPic',gender,c['VERSION_EMERALD'])==pic)
 check(tag+'_save',invoke('TrySavingData',0)==1)
 invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],0);invoke('DynamicPal_SetSelection',0);invoke('MoveSaveBlocks_ResetHeap')
 check(tag+'_load',invoke('LoadGameSave',0)==1)
 check(tag+'_persist_both',invoke('PlayerOutfit_Get')==1 and invoke('DynamicPal_GetSelection')==0x111)
 check(tag+'_boxed_partner_preserved',invoke('GetBoxMonDataAt',59 if mode else 13,29,18)==3)
 # Native sprite creation for representative animation sizes.
 for state in ['NORMAL','MACH_BIKE','SURFING','FISHING']:
  invoke('ObjectEventSetGraphicsId',player(),c['OBJ_EVENT_GFX_'+g+'_'+state]);frames(10);capture(tag+'_'+state.lower())
 invoke('ObjectEventSetGraphicsId',player(),c['OBJ_EVENT_GFX_'+g+'_NORMAL'])
 warp(0,9,10,10);invoke('FlagSet',c['FLAG_SYS_B_DASH'])
 check(tag+'_mount_starts',invoke('PokeRide_Start',0)==1);frames(40);capture(tag+'_riding')
 check(tag+'_mount_uses_rs',images(c['OBJ_EVENT_GFX_LA_'+g+'_RIDING'])==symbols['sOutfitRsFrames_'+name+'Riding'])
 check(tag+'_water_mount_uses_rs',images(c['OBJ_EVENT_GFX_LA_'+g+'_WATER_RIDING'])==symbols['sOutfitRsFrames_'+name+'Riding'])
 move(16,1);invoke('PokeRide_Stop');frames(30)
 check(tag+'_dismount_keeps_rs',images(c['OBJ_EVENT_GFX_'+g+'_NORMAL'])==symbols['sOutfitRsFrames_'+name+'Normal'])
 # Invalid/new save values are safe defaults; only our signed value selects RS.
 invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],0xffff);check(tag+'_invalid_is_emerald',invoke('PlayerOutfit_Get')==0)
 invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],0xC101)
 for repeat in range(3):
  openpc();tap(64);tap(16);finishpc(2)
  check(tag+'_reopen_cancel_'+str(repeat),invoke('PlayerOutfit_Get')==1 and invoke('DynamicPal_GetSelection')==0x111)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'outfit checks',flush=True)
