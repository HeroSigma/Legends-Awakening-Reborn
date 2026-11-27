"""Gold-inspired long jacket and Lyra-inspired bib overalls on player identities."""
from pathlib import Path
from PIL import Image, ImageDraw
R=Path(__file__).resolve().parents[3]
ns={"__file__":str(R/"tools/la_world/art/build_classic_wardrobe.py")};exec(compile((R/'tools/la_world/art/build_classic_wardrobe.py').read_text().split("\nfor name,female in")[0],'garment_helpers','exec'),ns)
skin_face=ns['skin_face']
OUT=R/'graphics/player_outfits/johto'
def palette(im,female):
 p=im.getpalette();colors=[(65,123,213),(32,65,131),(246,82,82),(164,41,57)] if female else [(246,197,65),(172,115,32),(49,49,57),(16,24,32)]
 for i,c in enumerate(colors,10):p[i*3:i*3+3]=c
 im.putpalette(p);return im

def frame(src,female):
 out=src.copy();face=skin_face(src);occupied=[(x,y) for y in range(32) for x in range(src.width) if src.getpixel((x,y))]
 if not occupied:return out
 if face:cx=round(sum(x for x,y in face)/len(face));chest=max(y for x,y in face)+1;fw=max(x for x,y in face)-min(x for x,y in face)+1
 else:cx=round((min(x for x,y in occupied)+max(x for x,y in occupied))/2);chest=max(y for x,y in occupied)-7;fw=0
 chest=min(chest,27)
 cloth=[x for y in range(max(0,chest),min(32,chest+3)) for x in range(max(0,cx-5),min(src.width,cx+6)) if src.getpixel((x,y)) in [10,11,12,13]]
 if cloth:cx=round((min(cloth)+max(cloth))/2)
 for y in range(max(0,chest),min(32,chest+5)):
  for x in range(max(0,cx-4),min(src.width,cx+5)):
   n=src.getpixel((x,y))
   if n in [0,15] or (female and n in [7,8]):continue
   skin=n in [1,2,3,4]
   if skin and not (abs(x-cx)>=2 and y<chest+2):continue
   if female:
    bib=(abs(x-cx)<=1 and y>=chest+1) or (abs(x-cx)==2 and y<=chest+2) or (y>=chest+3 and abs(x-cx)<=3)
    out.putpixel((x,y),(10 if x<=cx+1 else 11) if bib else (12 if n%2==0 else 13))
   else:
    center=fw>0 and x in [cx,cx+1]
    out.putpixel((x,y),(12 if y%2 else 13) if center else (10 if x<=cx+2 else 11))
 if female and fw>=6:
  for x in [cx-2,cx+2]:
   if 0<=x<src.width and chest+1<32 and src.getpixel((x,chest+1)) not in [0,7,8]:out.putpixel((x,chest+1),14)
 return out

def sheet(src,female,width):
 out=src.copy()
 for yy in range(0,src.height,32):
  for xx in range(0,src.width,width):out.paste(frame(src.crop((xx,yy,xx+width,yy+32)),female),(xx,yy))
 return palette(out,female)

def portrait(src,female,back):
 out=src.copy()
 for start in range(0,src.height,64):
  if back:
   for y in range(start+43,min(start+64,src.height)):
    for x in range(18,53):
     n=src.getpixel((x,y))
     if n in [0,15] or (female and n in [7,8]):continue
     if n in [1,2,3,4] and not (not female and y<start+58 and (x<28 or x>44)):continue
     if female:
      straps=x in [28,29,38,39] or (y>=start+55 and 29<=x<=40)
      out.putpixel((x,y),(10 if x<38 else 11) if straps else (12 if n%2==0 else 13))
     else:out.putpixel((x,y),12 if y<start+46 or (29<=x<=32) else (10 if x<44 else 11))
   continue
  if female:
   # Red blouse, blue shoulder straps and chest bib; blue divided shorts below.
   for y in range(25,43):
    for x in range(22,35):
     n=src.getpixel((x,y))
     if n not in [5,6,10,11,12,13]:continue
     straps=(x in [25,26,31,32] and y<=34)
     bib=(26<=x<=31 and 30<=y<=37) or y>=37
     out.putpixel((x,y),(10 if x<31 else 11) if straps or bib else (12 if n%2==0 else 13))
   for x in [25,31]:out.putpixel((x,30),14)
   for x in [27,28,29]:
    if src.getpixel((x,35)) not in [0,1,2,3,4,15]:out.putpixel((x,35),11)
  else:
   for y in range(26,39):
    for x in range(22,37):
     n=src.getpixel((x,y))
     if n not in [5,6,7,8,10,11,12,13]:continue
     out.putpixel((x,y),(12 if x<30 else 13) if x in [28,29,30] else (10 if x<33 else 11))
   sleeves=Image.new('1',src.size);dr=ImageDraw.Draw(sleeves)
   dr.polygon([(24,27),(25,31),(20,38),(16,37),(19,32)],fill=1)
   dr.polygon([(34,27),(39,29),(44,34),(42,36),(36,32)],fill=1)
   for y in range(27,39):
    for x in range(15,45):
     n=src.getpixel((x,y))
     if sleeves.getpixel((x,y)) and n in [1,2,3,4,5,6,7,8,10,11,12,13]:out.putpixel((x,y),10 if x%3 else 11)
   for y in range(28,38,2):
    if src.getpixel((29,y)) not in [0,1,2,3,4,15]:out.putpixel((29,y),9)
 return palette(out,female)

for name,female in [('brendan',False),('may',True)]:
 dest=OUT/name;dest.mkdir(parents=True,exist_ok=True);source=R/f'graphics/object_events/pics/people/{name}'
 for state in ['walking','running','mach_bike','acro_bike','surfing','underwater','field_move','fishing','watering','decorating','riding']:
  im=Image.open(source/(state+'.png'));width=16 if state in ['walking','running','decorating','riding'] else 32
  sheet(im,female,width).save(dest/(state+'.png'),bits=4,transparency=0)
 walk=Image.open(dest/'walking.png');run=Image.open(dest/'running.png');normal=Image.new('P',(walk.width+run.width,32));normal.putpalette(walk.getpalette());normal.paste(walk,(0,0));normal.paste(run,(walk.width,0));normal.save(dest/'normal_running.png',bits=4,transparency=0)
 for side in ['front','back']:
  im=Image.open(R/f'graphics/trainers/{side}_pics/{name}.png');portrait(im,female,side=='back').save(dest/(side+'.png'),bits=4,transparency=0)
print('Built Gold jacket and Lyra overalls')
