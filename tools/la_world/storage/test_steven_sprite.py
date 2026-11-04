"""Selected Steven art, stable existing IDs and native role override."""
from pathlib import Path
import json,re,hashlib,subprocess
from PIL import Image
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/art/npc_roster/steven';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
def ids(text):
 clean=re.sub(r'/\*.*?\*/|//[^\n]*','',text,flags=re.S)
 return [n.strip() for n in re.search(r'enum\s*\{(.*?)NUM_OBJ_EVENT_GFX',clean,re.S)[1].split(',') if n.strip()]
old=ids(subprocess.check_output(['git','show','8c1c173ce3:include/constants/event_objects.h'],cwd=R,text=True));new=ids((R/'include/constants/event_objects.h').read_text())
check('all_existing_graphics_ids_preserved',new[:len(old)]==old)
manifest=json.loads((R/'docs/art/npc_roster/manifest.json').read_text());prior=json.loads(subprocess.check_output(['git','show','8c1c173ce3:docs/art/npc_roster/manifest.json'],cwd=R,text=True))
check('prior_roster_preserved',manifest['characters'][:len(prior['characters'])]==prior['characters'])
row=next(x for x in manifest['characters'] if x['name']=='Steven');check('selected_hyper_134',row['donor']=='hyper' and row['source_id']==134)
start(0)
info=symbols[row['info_symbol']]
check('registered_steven',invoke('GetObjectEventGraphicsInfo',new.index(row['graphics_id']))==info)
check('existing_steven_role',invoke('GetObjectEventGraphicsInfo',new.index('OBJ_EVENT_GFX_STEVEN'))==info)
check('native_dimensions',rd(info+8,2)==16 and rd(info+10,2)==32)
sheet=Image.open(R/row['editor_sheet']);images=rd(info+0x1c);rom=(R/'pokeemerald.gba').read_bytes();folder=R/'assets/donor_npcs/hyper/sprites/gfx_134'
for i in range(9):
 im=sheet.crop((i%3*16,i//3*32,(i%3+1)*16,(i//3+1)*32));src=Image.open(folder/'frames'/f'frame_{i:02}.png').convert('RGBA')
 check('donor_pixels_'+str(i),im.convert('RGBA').tobytes()==src.tobytes())
 raw=bytearray();px=im.load()
 for ty in range(0,32,8):
  for tx in range(0,16,8):
   for y in range(8):
    for x in range(0,8,2):raw.append(px[tx+x,ty+y]|px[tx+x+1,ty+y]<<4)
 ptr=rd(images+i*8)-0x08000000;check('linked_frame_'+str(i),rom[ptr:ptr+256]==raw and rd(images+i*8+4,2)==256)
for group,mid in [(24,10),(0,33),(0,35),(14,7)]:
 warp(group,mid,5,5);frames(60)
 check('role_override_'+str((group,mid)),invoke('GetObjectEventGraphicsInfo',new.index('OBJ_EVENT_GFX_STEVEN'))==info)
# Preview the selected sheet on a real field, including directional animations.
sprite=invoke('CreateObjectGraphicsSprite',new.index(row['graphics_id']),symbols['SpriteCallbackDummy']|1,180,70,0)
check('native_sprite_created',sprite<64)
for animation in range(4):
 invoke('StartSpriteAnim',symbols['gSprites']+sprite*68,animation);frames(20)
 shutil.copy2(shot('steven_'+str(animation)),D/('facing_'+str(animation)+'.png'))
lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'Steven sprite checks')
