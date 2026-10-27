"""Validate the linked roster and role resolution using an isolated native core."""
from pathlib import Path
import json,hashlib,re,struct
from PIL import Image
helpers=Path(__file__).with_name('test_timeless_call.py').read_text().split('\nfor gender in [0,1]:')[0]
exec(compile(helpers,'roster_helpers','exec'))
D=R/'docs/art/npc_roster';(D/'screenshots').mkdir(exist_ok=True);checks=[]
manifest=json.loads((D/'manifest.json').read_text());rom=(R/'pokeemerald.gba').read_bytes()
header=(R/'include/constants/event_objects.h').read_text();clean=re.sub(r'/\*.*?\*/|//[^\n]*','',header,flags=re.S);body=re.search(r'enum\s*\{(.*?)NUM_OBJ_EVENT_GFX',clean,re.S)[1];names=[n.strip() for n in body.split(',') if n.strip()];ids={n:i for i,n in enumerate(names)}
for line in (R/'include/constants/hns_object_graphics.h').read_text().splitlines():
 match=re.fullmatch(r'#define\s+(OBJ_EVENT_GFX_\w+)\s+(0x[0-9a-fA-F]+)',line)
 if match:ids[match[1]]=int(match[2],16)
def rombytes(ptr,n):assert 0x08000000<=ptr<0x0a000000;return rom[ptr-0x08000000:ptr-0x08000000+n]
def packed(im):
 out=bytearray();p=im.load()
 for ty in range(0,im.height,8):
  for tx in range(0,im.width,8):
   for y in range(8):
    for x in range(0,8,2):out.append(p[tx+x,ty+y]|p[tx+x+1,ty+y]<<4)
 return bytes(out)
_historical_protected=json.loads((R/'.la_work/amap/npc_roster/protected_before.json').read_text())
_save_before={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in _historical_protected if Path(p).suffix=='.sav'}
start(0);setflag(0x860);warp(1,4,6,12);frames(60)
for row in manifest['characters']:
 name=row['name'];info=symbols[row['info_symbol']];result=invoke('GetObjectEventGraphicsInfo',ids[row['graphics_id']]);check('named_graphics_'+name,result==info)
 check('dimensions_'+name,rd(info+8,2)==row['width'] and rd(info+10,2)==row['height'] and rd(info+6,2)==row['width']*row['height']//2)
 images=rd(info+0x1c);sheet=Image.open(R/row['editor_sheet']);all_frames=True
 for i in range(row['frames']):
  im=sheet.crop(((i%3)*row['width'],(i//3)*row['height'],(i%3+1)*row['width'],(i//3+1)*row['height']))
  frame=packed(im);entry=images+i*8;all_frames &= rd(entry+4,2)==len(frame) and rombytes(rd(entry),len(frame))==frame
 check('linked_frames_'+name,all_frames)
 pal=symbols['sObjectEventSpritePalettes'];found=False
 for i in range(512):
  ptr=rd(pal+i*8);tag=rd(pal+i*8+4,2)
  if tag==row['palette_tag']:
   found=hashlib.sha256(rombytes(ptr,32)).hexdigest()==row['palette_sha256'];break
 check('linked_palette_'+name,found)
 for alias in row['aliases']:check('role_alias_'+alias,invoke('GetObjectEventGraphicsInfo',ids[alias])==info)
# Hoopa and its ring are one graphic with safe visual-only donor animations.
h=next(x for x in manifest['characters'] if x['name']=='HoopaRing');info=symbols[h['info_symbol']];table=rd(info+0x18);reference=json.loads((D/'hoopa_visual_animations.json').read_text())
for animation in reference['donor_animations']:
 ptr=rd(table+animation['index']*4);actual=[list(struct.unpack('<HH',rombytes(ptr+j*4,4))) for j in range(len(animation['commands']))]
 check('hoopa_donor_animation_'+str(animation['index']),actual==animation['commands'])
sprite_id=invoke('CreateObjectGraphicsSprite',ids[h['graphics_id']],symbols['SpriteCallbackDummy']|1,120,72,0)
check('hoopa_combined_sprite_created',sprite_id<64);sprite=symbols['gSprites']+sprite_id*68
invoke('StartSpriteAnim',sprite,20);observed=set()
for tick in range(110):
 index=rd(sprite+0x2b,1);ptr=rd(table+20*4);frame=rd(ptr+index*4,2)
 if frame<7:observed.add(frame)
 if tick==12:capture('hoopa_ring_opening')
 if tick==65:capture('hoopa_emerged')
 frames(1)
check('ring_then_hoopa_single_sprite',set([0,1,3,4,5,6]).issubset(observed) and rd(sprite+0x2a,1)==20)
check('hoopa_emergence_finishes',bool(rd(sprite+0x3f,1)&16))
invoke('DestroySprite',sprite)
for gender,name in [(0,'Brendan'),(1,'May')]:
 gfx='OBJ_EVENT_GFX_'+name.upper()+'_NORMAL'
 check('player_avatar_unchanged_'+str(gender),invoke('GetObjectEventGraphicsInfo',ids[gfx])==symbols['gObjectEventGraphicsInfo_'+name+'Normal'])
# Older native enum identities remain numerically stable.
before=json.loads((R/'.la_work/amap/npc_roster/protected_before.json').read_text());check('protected_maps_player_art_save_unchanged',all(Path(p).exists() and hashlib.sha256(Path(p).read_bytes()).hexdigest()==digest for p,digest in before.items() if Path(p).suffix!='.sav') and all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==digest for p,digest in _save_before.items()))
old=(R/'.la_work/amap/npc_roster/before/include/constants/event_objects.h').read_text();old=re.sub(r'/\*.*?\*/|//[^\n]*','',old,flags=re.S);oldbody=re.search(r'enum\s*\{(.*?)NUM_OBJ_EVENT_GFX',old,re.S)[1];oldnames=[n.strip() for n in oldbody.split(',') if n.strip()];check('existing_graphics_ids_unchanged',names[:len(oldnames)]==oldnames)
lib.shutdown()
(D/'runtime_validation.json').write_text(json.dumps(dict(checks=checks,all_passed=all(c['passed'] for c in checks),user_save_loaded=False),indent=2)+'\n');print('NPC roster checks:',len(checks),flush=True)
