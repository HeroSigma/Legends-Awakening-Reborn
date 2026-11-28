"""Native icon menu lifecycle, options palette choice, and save compatibility."""
from pathlib import Path
import tempfile,struct
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/custom-start-menu/store-return';D.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/flags.h"\n#include "dexnav.h"\nconst unsigned v[]={FLAG_SYS_POKEDEX_GET,FLAG_SYS_POKEMON_GET,FLAG_SYS_POKENAV_GET,DN_FLAG_DEXNAV_GET};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True);flags=struct.unpack('<4I',(td/'c.bin').read_bytes())
def openmenu(page=0):
 wr(symbols['sStartMenuPage'],page,1);wr(symbols['sStartMenuCursorPos'],0,1);tap(8);frames(50)
 check('icon menu active',rd(symbols['sCustomMenu'])!=0)

from PIL import Image
sheet=Image.open(R/'graphics/legends_start_menu/icons.png')
def packed_frame(frame):
 im=sheet.crop((0,frame*32,32,frame*32+32));out=[]
 for ty in range(4):
  for tx in range(4):
   for y in range(8):
    for x in range(0,8,2):out.append(im.getpixel((tx*8+x,ty*8+y)) | im.getpixel((tx*8+x+1,ty*8+y))<<4)
 return bytes(out)
def icons_ok(tag):
 p=rd(symbols['sCustomMenu']);count=rd(p+16,1);cursor=rd(symbols['sStartMenuCursorPos'],1)
 check(tag+'_active',p!=0 and count>0)
 for i in range(count):
  check(tag+'_sprite'+str(i),rd(p+i,1)<64 and invoke('GetSpriteTileStartByTag',0x7e30+i)!=0xffff)
  icon=rd(p+8+i,1);frame=icon+(0 if i==cursor else 1 if icon>=14 else 7)
  tile=invoke('GetSpriteTileStartByTag',0x7e30+i)
  actual=bytes(rd(0x06010000+tile*32+j,1) for j in range(512))
  check(tag+'_exact_pixels'+str(i),actual==packed_frame(frame))
def store_from_menu(tag):
 openmenu(1);frames(30)
 icons_ok(tag+'_before')
 # Locate STORE by its action icon instead of assuming unlock-dependent rows.
 p=rd(symbols['sCustomMenu']);row=next(i for i in range(rd(p+16,1)) if rd(p+8+i,1)==16)
 for i in range(row):tap(128)
 tap(1);wait('Task_LegendsStore');frames(30)
 check(tag+'_store_clears_menu',rd(symbols['sCustomMenu'])==0)
 # Browse categories, enter/cancel quantity, then exit through both B/Start.
 tap(16);tap(1);tap(2);tap(8 if tag.endswith('1') else 2);frames(60)
 check(tag+'_field_unlocked',invoke('ArePlayerFieldControlsLocked')==0)
 openmenu(1);frames(30);icons_ok(tag+'_after')
 for i in range(rd(rd(symbols['sCustomMenu'])+16,1)):tap(128);icons_ok(tag+'_cursor'+str(i))
 shutil.copy2(shot(tag),D/(tag+'.png'))
 tap(2);frames(30)
for gender in [0,1]:
 start(gender);invoke('ScriptGiveMon',25,16,0)
 for f in flags:invoke('FlagSet',f)
 for repeat in range(3):store_from_menu(f'g{gender}_visit{repeat}')
 # Force noncontiguous 512-byte gaps in sprite VRAM: the old whole-sheet
 # allocation must fail, while every visible menu row must still load.
 buf=invoke('AllocZeroed_',11264,0);S=0x03007400
 tags=[]
 for i in range(100):
  wr(S,buf);wr(S+4,512,2);wr(S+6,0x7100+i,2)
  invoke('LoadSpriteSheet',S)
  if invoke('GetSpriteTileStartByTag',0x7100+i)==0xffff:break
  tags.append(0x7100+i)
 for tag in tags[::2]:invoke('FreeSpriteTilesByTag',tag)
 wr(S,buf);wr(S+4,11264,2);wr(S+6,0x7200,2)
 invoke('LoadSpriteSheet',S)
 check(f'g{gender}_old_sheet_cannot_fit',invoke('GetSpriteTileStartByTag',0x7200)==0xffff)
 store_from_menu(f'g{gender}_fragmented1')
 openmenu(0);frames(30);icons_ok(f'g{gender}_fragmented_adventure')
 tap(16);frames(30);icons_ok(f'g{gender}_fragmented_services')
 tap(2);frames(30)
 for tag in tags:invoke('FreeSpriteTilesByTag',tag)
 invoke('Free',buf)
 check(f'g{gender}_tile_tags_released',all(invoke('GetSpriteTileStartByTag',0x7e30+i)==0xffff for i in range(8)))
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'Store/menu icon regressions',flush=True)
