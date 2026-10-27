"""Adapt native action poses to user-edited Aren; draft assets only."""
from pathlib import Path
from PIL import Image,ImageOps
import json,shutil
R=Path(__file__).resolve().parents[4];D=Path(__file__).parent;O=D/'actions';O.mkdir(exist_ok=True)
native=R/'graphics/object_events/pics/people/brendan'
base=Image.open(native/'walking.png');user=Image.open(D/'seed_standing.png');walk=Image.open(D/'walking.png')
seeds=[]
for i,di in enumerate([0,1,2,0,0,1,1,2,2]):
 old=base.crop((16*i,0,16*i+16,32));ys=[y for y in range(32) for x in range(16) if old.getpixel((x,y))!=0];top=min(ys)
 oldhead=old.crop((0,top,16,top+8));newhead=user.crop((di*16,10,di*16+16,18))
 for flip in [False,True]:
  seeds.append((ImageOps.mirror(oldhead) if flip else oldhead,ImageOps.mirror(newhead) if flip else newhead,di,flip))
report=[]
for action,width in [('running',16),('mach_bike',32),('acro_bike',32),('surfing',32),('fishing',32),('watering',32),('field_move',32),('underwater',32),('decorating',16)]:
 src=Image.open(native/(action+'.png'));out=src.copy();out.info['transparency']=0;records=[];gifs=[]
 directions={'running':[0,1,2,0,0,1,1,2,2],'mach_bike':[0,1,2,0,0,1,1,2,2],'acro_bike':[0,1,2,0,0,1,1,2,2]+[0]*4+[1]*4+[2]*4+[0,0,1,1,2,2],'surfing':[0,0,1,1,2,2],'fishing':[2]*4+[1]*4+[0]*4,'watering':[0,0,1,1,2,2],'field_move':[0]*5,'decorating':[2],'underwater':[0,0,2,2]}
 for fi in range(src.width//width):
  fr=src.crop((fi*width,0,(fi+1)*width,32));best=None
  for old,new,di,flip in seeds:
   if di!=directions[action][fi]:continue
   coords=[(x,y,old.getpixel((x,y))) for y in range(8) for x in range(16) if old.getpixel((x,y))!=0]
   for yy in range(25):
    for xx in range(width-15):
     same=sum(fr.getpixel((xx+x,yy+y))==c for x,y,c in coords)
     # Require the hat highlights, avoiding accidental matches on dark clothing.
     highlights=[(x,y,c) for x,y,c in coords if c in [5,9,14]]
     hs=sum(fr.getpixel((xx+x,yy+y))==c for x,y,c in highlights)/max(1,len(highlights))
     score=same/len(coords)*.7+hs*.3
     if best is None or score>best[0]:best=(score,xx,yy,old,new,di,flip)
  score,xx,yy,old,new,di,flip=best
  matched=score>=.62
  if action=='running' and di==2:
   xx=0;yy=min(y for y in range(32) for x in range(width) if fr.getpixel((x,y))!=0);matched=True
  if action=='field_move':matched=True
  if action=='acro_bike' and fi==16:matched=True
  if matched:
   # Recolor clothing locally below the head, leaving bikes/rods/water outside the torso intact.
   for y in range(yy+13,min(yy+20,32)):
    for x in range(max(0,xx+2),min(width,xx+14)):
     c=fr.getpixel((x,y))
     if c in [12,13]:fr.putpixel((x,y),10 if c==12 else 11)
   for y in range(8):
    for x in range(16):
     oldc=old.getpixel((x,y));newc=new.getpixel((x,y));actual=fr.getpixel((xx+x,yy+y))
     # Explicit native head rectangle: preserve equipment beyond its bounds.
     if oldc!=0 or newc!=0:fr.putpixel((xx+x,yy+y),newc)
   # Carry the edited jacket panels and rear satchel through the native body when geometry agrees.
   for sy in range(23,31):
    for sx in range(16):
     tx=xx+(15-sx if flip else sx);ty=yy+(sy-10)
     if 0<=tx<width and 0<=ty<32:
      a=base.getpixel((di*16+sx,sy));b=user.getpixel((di*16+sx,sy))
      if a!=b and fr.getpixel((tx,ty))==a:fr.putpixel((tx,ty),b)
  if action=='underwater':
   # Preserve the special diving pose and its dedicated blue palette.
   # Repaint its crown only, retaining face/air-bubble and swim silhouette.
   for y in range(0,12):
    for x in range(width):
     c=fr.getpixel((x,y))
     if c in [5,6,9]:fr.putpixel((x,y),8)
   pts=[(x,y) for y in range(0,12) for x in range(width) if fr.getpixel((x,y))==8]
   if pts:
    left=min(x for x,y in pts);top=min(y for x,y in pts)
    for y in range(top+1,min(top+7,12)):
     x=left+5+(y-top)//3
     if x<width and fr.getpixel((x,y))!=0:fr.putpixel((x,y),9)
    matched=True
  out.paste(fr,(fi*width,0));records.append(dict(frame=fi,head_match=round(score,3),adapted=matched,direction=di,mirrored=flip))
  fr.putpalette(src.getpalette());fr.info['transparency']=0;gifs.append(fr.resize((width*6,192),Image.Resampling.NEAREST))
 out.save(O/(action+'.png'))
 # Contact sheet uses exact native pixels, not interpolation.
 columns=min(9,src.width//width);rows=(src.width//width+columns-1)//columns
 contact=Image.new('P',(columns*width,rows*32),0);contact.putpalette(src.getpalette())
 for fi in range(src.width//width):contact.paste(out.crop((fi*width,0,(fi+1)*width,32)),((fi%columns)*width,(fi//columns)*32))
 contact.resize((contact.width*4,contact.height*4),Image.Resampling.NEAREST).save(O/(action+'_preview_4x.png'))
 gifs[0].save(O/(action+'_frames.gif'),save_all=True,append_images=gifs[1:],duration=180,loop=0,transparency=0,disposal=2)
 report.append(dict(action=action,frame_size=[width,32],frame_count=len(records),adapted=sum(x['adapted'] for x in records),review_frames=[x['frame'] for x in records if not x['adapted']],frames=records))
shutil.copy2(D/'walking.png',O/'walking.png')
(O/'action_audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps([{k:v for k,v in a.items() if k!='frames'} for a in report],indent=2))
