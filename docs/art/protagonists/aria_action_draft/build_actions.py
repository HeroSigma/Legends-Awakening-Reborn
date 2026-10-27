"""Native May-pose Aria action draft. Never modifies playable assets."""
from pathlib import Path
from PIL import Image,ImageOps
import json
R=Path(__file__).resolve().parents[4];D=Path(__file__).parent;O=D/'Aria-actions';O.mkdir(exist_ok=True)
N=R/'graphics/object_events/pics/people/may';base=Image.open(N/'walking.png');aria=Image.open(R/'docs/art/protagonists/pixel_authored_trial/aria_walking.png')
palette=aria.getpalette()
mapping={0:0,1:1,2:2,3:3,4:4,5:13,6:12,7:6,8:7,9:9,10:10,11:11,12:10,13:11,14:14,15:15}
directions={'running':[0,1,2,0,0,1,1,2,2],'mach_bike':[0,1,2,0,0,1,1,2,2],'acro_bike':[0,1,2,0,0,1,1,2,2]+[0]*4+[1]*4+[2]*4+[0,0,1,1,2,2],'surfing':[0,0,1,1,2,2],'fishing':[2]*4+[1]*4+[0]*4,'watering':[0,0,1,1,2,2],'field_move':[0]*5,'decorating':[2],'underwater':[0,0,2,2]}
seeds=[]
for fi,di in enumerate([0,1,2,0,0,1,1,2,2]):
 old=base.crop((fi*16,0,fi*16+16,32));top=min(y for y in range(32) for x in range(16) if old.getpixel((x,y)))
 for flip in [False,True]:
  h=old.crop((0,top,16,top+8));h=ImageOps.mirror(h) if flip else h
  coords=[(x,y,h.getpixel((x,y))) for y in range(8) for x in range(16) if h.getpixel((x,y))]
  seeds.append((di,flip,coords))
report=[]
aria.save(O/'walking.png')
for action in directions:
 width=16 if action in ['running','decorating'] else 32
 src=Image.open(N/(action+'.png'));out=Image.new('P',src.size,0);out.putpalette(src.getpalette() if action=='underwater' else palette);out.info['transparency']=0
 records=[]
 for fi in range(src.width//width):
  raw=src.crop((fi*width,0,(fi+1)*width,32));di=directions[action][fi];best=None
  for sd,flip,coords in seeds:
   if sd!=di:continue
   for y in range(25):
    for x in range(width-15):
     score=sum(raw.getpixel((x+xx,y+yy))==c for xx,yy,c in coords)/len(coords)
     if best is None or score>best[0]:best=(score,x,y,flip)
  score,x,y,flip=best
  fr=Image.new('P',(width,32),0)
  for yy in range(32):
   for xx in range(width):
    c=raw.getpixel((xx,yy));fr.putpixel((xx,yy),c if action=='underwater' else mapping[c])
  if action=='underwater':
   # Draw Aria's crown in the native underwater blue palette, removing May's bow.
   crown=aria.crop((di*16,10,di*16+16,18))
   tint={0:0,1:9,2:5,3:6,4:7,5:5,6:6,7:7,8:8,9:9,10:6,11:7,12:7,13:6,14:9,15:15}
   for yy in range(8):
    for xx in range(16):fr.putpixel((8+xx,5+yy),tint[crown.getpixel((xx,yy))])

  else:
   # Use the authored Aria crown with pale streak/clip; restore native face beneath.
   crown=aria.crop((di*16,10,di*16+16,18));crown=ImageOps.mirror(crown) if flip else crown
   target_y=max(0,y-1)
   for yy in range(8):
    for xx in range(16):fr.putpixel((x+xx,target_y+yy),crown.getpixel((xx,yy)))
   # Long locks frame the native face without covering eyes or hands.
   for yy in range(target_y+8,min(target_y+14,29)):
    positions=[1,2,13,14] if di<2 else ([1,2,3] if flip else [12,13,14])
    for xx in positions:
     if x+xx<width:
      c=fr.getpixel((x+xx,yy))
      if c in [0,6,7,8,13]:fr.putpixel((x+xx,yy),7 if xx in [1,14] else 6)
   if di==1:
    for yy in range(target_y+8,min(target_y+12,29)):
     for xx in range(4,12):
      if fr.getpixel((x+xx,yy)) not in [1,2,3]:fr.putpixel((x+xx,yy),6 if xx<10 else 7)
    for yy in range(target_y+8,min(target_y+11,29)):fr.putpixel((x+(5 if flip else 10),yy),9)
   # Shoulder whites and dark shorts/green trim stay on existing body pixels.
   for xx,yy in [(5,13),(10,13),(5,14),(10,14),(6,14),(9,14)]:
    tx=x+xx;ty=target_y+yy
    if tx<width and ty<32 and fr.getpixel((tx,ty)) not in [0,1,2,3,15]:fr.putpixel((tx,ty),14 if xx in [5,10] else 9)
  out.paste(fr,(fi*width,0));records.append(dict(frame=fi,head_match=round(score,3),direction=di,mirrored=flip,review=score<.7 or action in ['field_move','underwater']))
 out.save(O/(action+'.png'))
 report.append(dict(action=action,frames=records,frame_count=len(records),frame_size=[width,32]))
# Export contact sheets and inspection GIFs. GIFs cycle source frames, not game timing.
for p in sorted(O.glob('*.png')):
 im=Image.open(p);width=16 if p.stem in ['walking','running','decorating'] else 32;count=im.width//width;cols=min(9,count);rows=(count+cols-1)//cols
 contact=Image.new('P',(cols*width,rows*32),0);contact.putpalette(im.getpalette());frames=[]
 for fi in range(count):
  fr=im.crop((fi*width,0,(fi+1)*width,32));contact.paste(fr,((fi%cols)*width,(fi//cols)*32));frames.append(fr.resize((width*6,192),Image.Resampling.NEAREST))
 contact.resize((contact.width*4,contact.height*4),Image.Resampling.NEAREST).save(O/(p.stem+'_preview_4x.png'))
 frames[0].save(O/(p.stem+'_frames.gif'),save_all=True,append_images=frames[1:],duration=180,loop=0,transparency=0,disposal=2)
(O/'action_audit.json').write_text(json.dumps(report,indent=2)+'\n')
print('Aria draft action sheets prepared')
