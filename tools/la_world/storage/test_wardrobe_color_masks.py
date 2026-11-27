"""Regression for skin-colored garment outlines and wrist-selected torso anchors."""
from pathlib import Path
import sys
from PIL import Image
R=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(R/'tools/la_world/art'))
from wardrobe_pixels import garment_pose,skin_face
checks=0
for gender in ['brendan','may']:
 source=Image.open(R/f'graphics/object_events/pics/people/{gender}/walking.png')
 rear=source.crop((16,0,32,32))
 assert skin_face(rear) is None, 'Back-facing wrists must not be interpreted as a face'
 assert garment_pose(rear)[0]==8
 checks+=2
 for theme in ['classic','johto','crystal']:
  for pose in ['walking','running','decorating','riding']:
   im=Image.open(R/f'graphics/player_outfits/{theme}/{gender}/{pose}.png')
   for x0 in range(0,im.width,16):
    frame=im.crop((x0,0,x0+16,32))
    for y in range(24,32):
     for x in range(3,13):
      if frame.getpixel((x,y))!=4:continue
      near=[frame.getpixel((xx,yy)) for yy in range(max(0,y-1),min(32,y+2)) for xx in range(max(0,x-1),min(16,x+2))]
      assert any(n in [1,2,3] for n in near) or (gender=='may' and any(n in [7,8] for n in near)), (theme,gender,pose,x0,x,y)
    checks+=1
rear=Image.open(R/'graphics/player_outfits/classic/brendan/walking.png').crop((16,0,32,32))
assert sum(rear.getpixel((x,y)) in [10,11] for y in range(22,26) for x in range(5,11))>=10, 'Red vest back must be red'
print(f'PASS {checks+1} outfit color-mask regressions')
