"""Native character colors: live PC UI, cancellation, persistence and intro."""
from pathlib import Path
import tempfile,struct,json,hashlib,shutil,subprocess
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/dynamic-palettes';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
def capture(n):shutil.copy2(shot('dynpal_'+n),D/(n+'.png'))
def until(task,limit=30000):
 for i in range(limit):
  if active(task) is not None:return active(task)
  frames(1,1 if i%13==0 else 0)
 raise AssertionError(('task',task,hex(rd(symbols['gMain']+4))))
names=['VAR_LA_PLAYER_COLORS','OBJ_EVENT_PAL_TAG_AREN','OBJ_EVENT_PAL_TAG_ARIA','OBJ_EVENT_PAL_TAG_BRENDAN','OBJ_EVENT_PAL_TAG_MAY','TRAINER_PIC_BRENDAN','TRAINER_PIC_MAY','offsetof(struct Sprite,oam)','offsetof(struct Sprite,images)','offsetof(struct ObjectEventGraphicsInfo,images)','ITEM_POKEVIAL','ITEM_POTION']
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
for gender,mode in [(0,0),(1,1)]:
 tag=f'g{gender}_mode{mode}'
 start(gender);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',4,16,0)
 invoke('AddBagItem',c['ITEM_POKEVIAL'],1);invoke('AddBagItem',c['ITEM_POTION'],17)
 invoke('StorageWriteMon',59 if mode else 13,29,symbols['gParties'])
 check(tag+'_old_save_default',invoke('DynamicPal_GetSelection')==0)
 base=symbols['gObjectEventPal_May' if gender else 'gObjectEventPal_Brendan']
 owtag=c['OBJ_EVENT_PAL_TAG_ARIA' if gender else 'OBJ_EVENT_PAL_TAG_AREN']
 rivaltag=c['OBJ_EVENT_PAL_TAG_MAY' if gender else 'OBJ_EVENT_PAL_TAG_BRENDAN']
 pic=c['TRAINER_PIC_MAY' if gender else 'TRAINER_PIC_BRENDAN']
 original=pal(base)
 check(tag+'_default_exact',pal(invoke('DynamicPal_ObjectPalette',owtag,base))==original)
 for skin in range(4):
  for outfit in range(8):
   for accent in range(8):
    choice=skin|(outfit<<4)|(accent<<8);invoke('DynamicPal_SetSelection',choice)
    got=pal(invoke('DynamicPal_ObjectPalette',owtag,base))
    check(tag+f'_combination_{choice}',all(0<=v<=0x7fff for v in got) and all(got[i]==original[i] for i in [0,5,6,7,8,9,14,15]))
 check(tag+'_rival_unchanged',pal(invoke('DynamicPal_ObjectPalette',rivaltag,base))==original)
 invoke('DynamicPal_SetSelection',0);capture(tag+'_field_before');openpc();capture(tag+'_original')
 tap(16);tap(16);tap(128);tap(16);tap(16);tap(16);tap(128);tap(16);tap(16);tap(16);tap(16);frames(30)
 check(tag+'_live_choices',invoke('DynamicPal_GetSelection')==0x432)
 capture(tag+'_preview')
 finishpc(2);check(tag+'_cancel_restores',invoke('DynamicPal_GetSelection')==0)
 openpc();tap(16);tap(128);tap(16);tap(128);tap(16);finishpc(1)
 check(tag+'_accepted',invoke('DynamicPal_GetSelection')==0x111)
 # Repeated opens/cancels must not leak palette tags, sprites or control state.
 for repeat in range(3):openpc();tap(16);finishpc(2);check(tag+f'_repeat_{repeat}',invoke('DynamicPal_GetSelection')==0x111)
 invoke('MoveSaveBlocks_ResetHeap');check(tag+'_relocation',invoke('DynamicPal_GetSelection')==0x111)
 check(tag+'_save',invoke('TrySavingData',0)==1)
 invoke('DynamicPal_SetSelection',0);check(tag+'_load',invoke('LoadGameSave',0)==1)
 check(tag+'_saved_colors',invoke('DynamicPal_GetSelection')==0x111)
 check(tag+'_saved_boxes',invoke('GetStorageBoxCount')==(60 if mode else 14) and invoke('GetBoxMonDataAt',59 if mode else 13,29,18)==4)
 check(tag+'_vial_kept',invoke('CountTotalItemQuantityInBag',c['ITEM_POKEVIAL'])==1)
 check(tag+'_potions_kept',invoke('CountTotalItemQuantityInBag',c['ITEM_POTION'])==17)
 invoke('VarSet',c['VAR_LA_PLAYER_COLORS'],0xffff);check(tag+'_invalid_clamped',invoke('DynamicPal_GetSelection')==0)
 invoke('DynamicPal_SetSelection',0xfff);check(tag+'_invalid_parts_clamped',invoke('DynamicPal_GetSelection')==0)
 invoke('DynamicPal_SetSelection',0x432);check(tag+'_save_again',invoke('TrySavingData',0)==1);check(tag+'_reload_again',invoke('LoadGameSave',0)==1)
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
 tap(16);tap(16);tap(128);tap(16);tap(16);tap(16);tap(128);tap(16);frames(30);capture(tag+'_intro')
 check(tag+'_intro_live',invoke('DynamicPal_GetSelection')==0x132)
 tap(2);until('Task_NewGameBirchSpeech_ChooseGender');frames(360)
 check(tag+'_intro_cancel',invoke('DynamicPal_GetSelection')==0)
 prompt_ptr=invoke('GetWindowAttribute',0,7)
 check(tag+'_cancel_restores_entire_prompt',bytes(rd(prompt_ptr+i,1) for i in range(27*4*32))==prompt_before)
 capture(tag+'_back_to_gender')
 if gender:tap(128);frames(360)
 tap(1);until('Task_DynamicPalMenu');tap(16);tap(128);tap(16);tap(128);tap(16);tap(1)
 until('Task_NewGameBirchSpeech_WaitPressBeforeNameChoice');tap(1);wait('Task_NamingScreen',1800);frames(100);capture(tag+'_naming')
 tap(8);frames(90);tap(1);until('Task_NewGameBirchSpeech_ProcessNameYesNoMenu');tap(1)
 for i in range(18000):
  if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
  frames(1,1 if i%13==0 else 0)
 else:raise AssertionError('intro handoff timeout')
 frames(120)
 check(tag+'_intro_commits_to_new_save',invoke('DynamicPal_GetSelection')==0x111 and not invoke('DynamicPal_IsIntro'))
 capture(tag+'_new_game_field')
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'dynamic palette checks',flush=True)
