from pathlib import Path
from PIL import Image
import json,shutil,zipfile
R=Path(__file__).resolve().parents[4];D=Path(__file__).parent;A=D/'actions';report=[]
for action in ['walking','running','mach_bike','acro_bike','surfing','fishing','watering','field_move','decorating']:
 im=Image.open(A/(action+'.png'));old=Image.open(R/'graphics/object_events/pics/people/brendan'/(action+'.png'));w=16 if action in ['walking','running','decorating'] else 32
 for fi in range(im.width//w):
  fr=old.crop((fi*w,0,(fi+1)*w,32));seen=set();comps=[]
  for y in range(32):
   for x in range(w):
    if (x,y) in seen or fr.getpixel((x,y)) not in [5,9,10,11,14]:continue
    q=[(x,y)];seen.add((x,y));comp=[]
    while q:
     pt=q.pop();comp.append(pt);xx,yy=pt
     for adj in [(xx-1,yy),(xx+1,yy),(xx,yy-1),(xx,yy+1)]:
      ax,ay=adj
      if 0<=ax<w and 0<=ay<32 and adj not in seen and fr.getpixel(adj) in [5,9,10,11,14]:seen.add(adj);q.append(adj)
    comps.append(comp)
  if not comps:continue
  cap=max(comps,key=lambda c:sum(fr.getpixel(p) in [9,14] for p in c))
  fixes=[]
  for x,y in cap:
   if im.getpixel((fi*w+x,y)) in [10,11]:im.putpixel((fi*w+x,y),15);fixes.append([x,y])
  if fixes:report.append(dict(action=action,frame=fi,pixels=fixes))
 im.info['transparency']=0;im.save(A/(action+'.png'))
 if action=='walking':im.save(D/'walking.png')
 # Rebuild matching previews so stale images do not suggest unfixed hair.
 n=im.width//w;cols=min(9,n);contact=Image.new('P',(cols*w,((n+cols-1)//cols)*32),0);contact.putpalette(im.getpalette());fs=[]
 for fi in range(n):
  fr=im.crop((fi*w,0,(fi+1)*w,32));contact.paste(fr,((fi%cols)*w,(fi//cols)*32));fs.append(fr.resize((w*6,192),Image.Resampling.NEAREST))
 contact.resize((contact.width*4,contact.height*4),Image.Resampling.NEAREST).save(A/(action+'_preview_4x.png'))
 fs[0].save(A/(action+'_frames.gif'),save_all=True,append_images=fs[1:],duration=180,loop=0,transparency=0,disposal=2)
approved=Image.open(D/'walking_Aren_user_original.png');walk=Image.open(A/'walking.png')
assert walk.crop((0,0,16,32)).tobytes()==approved.crop((0,0,16,32)).tobytes()
walk.resize((1152,256),Image.Resampling.NEAREST).save(D/'walking_preview_8x.png')
(A/'hair_cleanup.json').write_text(json.dumps(dict(method='Native cap/hair component mask; replace green with approved black only within the source crown component',changed_pixels=sum(len(x['pixels']) for x in report),frames=report,approved_front_unchanged=True,rom_changed=False),indent=2)+'\n')
win=Path('/mnt/c/Users/aadair/Downloads/Legends-Awakening-Reborn/protagonist-previews/Your-Aren/Approved-Front-Revision');dest=win/'Aren-actions';dest.mkdir(exist_ok=True)
for p in A.iterdir():
 if p.is_file():shutil.copy2(p,dest/p.name)
shutil.copy2(D/'walking_preview_8x.png',win/'walking_preview_8x.png')
with zipfile.ZipFile(win/'Aren-approved-front-actions.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in A.iterdir():
  if p.is_file():z.write(p,'Aren-actions/'+p.name)
print('Hair pixels corrected:',sum(len(x['pixels']) for x in report))
