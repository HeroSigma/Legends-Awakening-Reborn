"""Saved outfit preview: actual soft reset and Continue OBJ palette."""
from pathlib import Path
import json,hashlib,shutil
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/player-outfits/continue';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
def snap(n):shutil.copy2(shot('continue_outfit_'+n),D/(n+'.png'))
for gender in [0,1]:
 start(gender)
 for style in range(5):
  for colors in [0,0x121]:
   tag=f'g{gender}_style{style}_colors{colors:03x}'
   invoke('PlayerOutfit_Set',style);invoke('DynamicPal_SetSelection',colors)
   check(tag+'_saved',invoke('TrySavingData',0)==1)
   frames(20,15);frames(600)
   for i in range(5000):
    if active('Task_MainMenuMain') is not None:break
    frames(1,8 if i%120==0 else 0)
   else:raise AssertionError('Continue screen timeout')
   frames(45)
   check(tag+'_loaded_style',invoke('PlayerOutfit_Get')==style)
   check(tag+'_loaded_colors',invoke('DynamicPal_GetSelection')==colors)
   slot=invoke('IndexOfSpritePaletteTag',30012)
   check(tag+'_palette_slot',slot<16)
   if style:
    pic=invoke('GetPlayerTrainerPic',gender,3)
    ptr=invoke('DynamicPal_TrainerPalette',pic,1)
   else:
    ptr=invoke('DynamicPal_MugshotPalette',symbols['sMayMugshot_Pal' if gender else 'sBrendanMugshot_Pal'],gender)
   expected=bytes(rd(ptr+i,1) for i in range(32))
   actual=bytes(rd(symbols['gPlttBufferUnfaded']+0x200+slot*32+i,1) for i in range(32))
   check(tag+'_exact_outfit_palette',actual==expected)
   snap(tag)
   tap(1)
   for i in range(1800):
    if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
    frames(1)
   else:raise AssertionError('Continue handoff timeout')
   frames(120)
   check(tag+'_continue_to_field',invoke('PlayerOutfit_Get')==style)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'Continue outfit checks',flush=True)
