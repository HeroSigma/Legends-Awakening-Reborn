"""Require visible scientist pixels in every functional upstairs room."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_training_scientist.py').read_text().split('for mode in [0,1]:')[0],'training_helpers','exec'))
from PIL import Image,ImageChops
D=R/'.la_work/training-visibility';D.mkdir(exist_ok=True)
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'v.c').write_text('#include "global.h"\n#include "sprite.h"\n#include "constants/event_objects.h"\n#include <stddef.h>\nconst unsigned v[]={sizeof(struct ObjectEvent),offsetof(struct ObjectEvent,graphicsId),offsetof(struct ObjectEvent,spriteId),sizeof(struct Sprite),offsetof(struct Sprite,x),offsetof(struct Sprite,y),offsetof(struct Sprite,x2),offsetof(struct Sprite,y2),OBJ_EVENT_GFX_SCIENTIST,OBJ_EVENT_GFX_SCIENTIST_1};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-c',str(td/'v.c'),'-o',str(td/'v.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'v.o'),str(td/'v.bin')],check=True)
 osize,gfxoff,sidoff,ssize,xoff,yoff,x2off,y2off,legacy,native=struct.unpack('<10I',(td/'v.bin').read_bytes())
def signed(v):return v-65536 if v&0x8000 else v
mg=json.loads((R/'data/maps/map_groups.json').read_text())
start(0);invoke('ScriptGiveMon',4,5,0)
check('legacy_saved_id_resolves',invoke('GetObjectEventGraphicsInfo',legacy)==invoke('GetObjectEventGraphicsInfo',native)!=0)
proof=[]
for index,row in enumerate(json.loads((R/'docs/features/training-scientist-locations.json').read_text())):
 if index:
  lib.shutdown();start(0);invoke('ScriptGiveMon',4,5,0)
 for group,gname in enumerate(mg['group_order']):
  if row['map'] in mg[gname]:mid=mg[gname].index(row['map']);break
 warp(group,mid,4,4)
 obj=invoke('GetObjectEventIdByLocalIdAndMap',row['local_id'],mid,group)
 check('actor_'+row['map'],obj<16)
 a=symbols['gObjectEvents']+obj*osize
 info=invoke('GetObjectEventGraphicsInfo',rd(a+gfxoff,2))
 check('resolved_graphics_'+row['map'],info!=0)
 sp=symbols['gSprites']+rd(a+sidoff,1)*ssize
 x=signed(rd(sp+xoff,2))+signed(rd(sp+x2off,2))+signed(rd(symbols['gSpriteCoordOffsetX'],2))
 y=signed(rd(sp+yoff,2))+signed(rd(sp+y2off,2))+signed(rd(symbols['gSpriteCoordOffsetY'],2))
 frames(15)
 visible=Image.open(shot('visible_'+row['map'])).convert('RGB').copy()
 invoke('SetObjectInvisibility',row['local_id'],mid,group,1);frames(2)
 hidden=Image.open(shot('hidden_'+row['map'])).convert('RGB').copy()
 area=(max(0,x-10),max(0,y-18),min(240,x+10),min(160,y+17))
 diff=ImageChops.difference(visible.crop(area),hidden.crop(area))
 changed=sum(any(px) for px in diff.getdata())
 print(row['map'],x,y,changed,flush=True)
 check('visible_pixels_'+row['map'],changed>=40)
 invoke('SetObjectInvisibility',row['local_id'],mid,group,0)
 proof.append(dict(map=row['map'],pixels=changed))
 if row['map']=='OldaleTown_PokemonCenter_2F':visible.save(R/'docs/features/training-scientist-visible.png')
lib.shutdown()
(R/'docs/features/training-scientist-visibility-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),maps=proof,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'scientist pixel-visibility checks')
