"""Native character colors: live PC UI, cancellation, persistence and intro."""
from pathlib import Path
import tempfile,struct,json,hashlib,shutil,subprocess
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/player-outfits/intro';D.mkdir(parents=True,exist_ok=True)
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
for gender in [0,1]:
 tag='intro_'+str(gender);print('CASE',tag,flush=True)
 start(gender);invoke('ScriptGiveMon',4,16,0);invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],0xC101);invoke('DynamicPal_SetSelection',0x432)
 check(tag+'_save_setup',invoke('TrySavingData',0)==1)
 # Mugshot should pick up the player's colors on a real menu return.
 frames(20,15);frames(600)
 for i in range(2400):
  if active('Task_MainMenuMain') is not None:break
  frames(1,8 if i%120==0 else 0)
 else:raise AssertionError('reset Continue menu timeout')
 frames(40);capture(tag+'_continue')
 tap(128);tap(1);wait('Task_LegendsCreator_Update',1500)
 until('Task_NewGameBirchSpeech_ChooseGender');frames(40)
 prompt_ptr=invoke('GetWindowAttribute',0,7)
 prompt_before=bytes(rd(prompt_ptr+i,1) for i in range(27*4*32))
 if gender:tap(128);frames(360)
 tap(1);until('Task_DynamicPalMenu');frames(30)
 check(tag+'_new_game_original',invoke('DynamicPal_GetSelection')==0)
 tap(16);tap(16);tap(128);tap(16);tap(16);tap(16);tap(128);tap(16);tap(128);tap(16);frames(30);capture(tag+'_intro')
 check(tag+'_intro_live',invoke('DynamicPal_GetSelection')==0x132 and invoke('PlayerOutfit_Get')==1)
 tap(2);until('Task_NewGameBirchSpeech_ChooseGender');frames(360)
 check(tag+'_intro_cancel',invoke('DynamicPal_GetSelection')==0 and invoke('PlayerOutfit_Get')==0)
 prompt_ptr=invoke('GetWindowAttribute',0,7)
 check(tag+'_cancel_restores_entire_prompt',bytes(rd(prompt_ptr+i,1) for i in range(27*4*32))==prompt_before)
 capture(tag+'_back_to_gender')
 if gender:tap(128);frames(360)
 tap(1);until('Task_DynamicPalMenu');tap(16);tap(128);tap(16);tap(128);tap(16);tap(128);tap(16);tap(1)
 until('Task_NewGameBirchSpeech_WaitPressBeforeNameChoice');tap(1);wait('Task_NamingScreen',1800);frames(100);capture(tag+'_naming')
 tap(8);frames(90);tap(1);until('Task_NewGameBirchSpeech_ProcessNameYesNoMenu');tap(1)
 for i in range(18000):
  if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
  frames(1,1 if i%13==0 else 0)
 else:raise AssertionError('intro handoff timeout')
 frames(120)
 check(tag+'_intro_commits_to_new_save',invoke('DynamicPal_GetSelection')==0x111 and invoke('PlayerOutfit_Get')==1 and not invoke('DynamicPal_IsIntro'))
 capture(tag+'_new_game_field')
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'outfit intro checks',flush=True)
