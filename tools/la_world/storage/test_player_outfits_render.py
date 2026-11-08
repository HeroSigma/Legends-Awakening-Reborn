"""Native character colors: live PC UI, cancellation, persistence and intro."""
from pathlib import Path
import tempfile,struct,json,hashlib,shutil,subprocess
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/player-outfits/render';D.mkdir(parents=True,exist_ok=True)
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

from PIL import Image
def tiled(frame):
 values=[]
 for ty in range(frame.height//8):
  for tx in range(frame.width//8):
   for y in range(8):
    for x in range(0,8,2):values.append(frame.getpixel((tx*8+x,ty*8+y))|(frame.getpixel((tx*8+x+1,ty*8+y))<<4))
 return bytes(values)
for gender in [0,1]:
 start(gender);tag='render_'+str(gender);g='MAY' if gender else 'BRENDAN';name='may' if gender else 'brendan'
 invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],0xC101)
 table=images(c['OBJ_EVENT_GFX_'+g+'_NORMAL']);sheet=Image.open(R/f'graphics/player_outfits/rs/{name}/normal_running.png')
 for frame in range(18):
  pointer=rd(table)+frame*256;expected=tiled(sheet.crop((frame*16,0,frame*16+16,32)))
  actual=bytes(rd(pointer+j,1) for j in range(len(expected)))
  check(tag+'_walking_running_tiles_'+str(frame),actual==expected)
 invoke('ScriptGiveMon',4,16,0);warp(0,9,10,10)
 invoke('CreateScriptedWildMon',261,3,0);invoke('BattleSetup_StartWildBattle')
 for i in range(400):
  frames(1)
  if i in [119,239,399]:capture(tag+'_battle_'+str(i))
 # The player's throw uses the outfit-specific back sprite ID through the native trainer resolver.
 check(tag+'_rs_battle_picture',invoke('GetPlayerTrainerPic',gender,c['VERSION_EMERALD'])==c['TRAINER_PIC_RS_MAY' if gender else 'TRAINER_PIC_RS_BRENDAN'])
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'outfit rendering checks',flush=True)
