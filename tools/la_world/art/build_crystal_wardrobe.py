"""Silver high-collar jacket and Kris cropped jacket / cycling shorts on player identities."""
from pathlib import Path
from PIL import Image, ImageDraw
R=Path(__file__).resolve().parents[3]
ns={"__file__":str(R/"tools/la_world/art/build_classic_wardrobe.py")};exec(compile((R/'tools/la_world/art/build_classic_wardrobe.py').read_text().split("\nfor name,female in")[0],'garment_helpers','exec'),ns)
skin_face=ns['skin_face']
OUT=R/'graphics/player_outfits/crystal'
def palette(im,female):
 p=im.getpalette();colors=[(246,246,255),(172,180,205),(213,82,148),(82,106,189)] if female else [(49,49,66),(16,24,41),(197,49,74),(115,24,49)]
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
    if y>=chest+3:out.putpixel((x,y),13 if n%2==0 else 6)
    else:out.putpixel((x,y),12 if abs(x-cx)<=1 else (10 if n%2==0 else 11))
   else:
    piping=(y==chest or y==chest+4 or (x==cx+2 and y<chest+3))
    out.putpixel((x,y),(12 if x<=cx else 13) if piping else (10 if x<=cx+2 else 11))
 if female:
  y=chest+5
  if y<30:
   for x in range(max(0,cx-2),min(src.width,cx+3)):
    if src.getpixel((x,y)) in [1,2,3,4,5,6]:out.putpixel((x,y),13 if x<=cx else 6)
 elif fw>=6 and chest+3<32 and 0<=cx+2<src.width:
  if src.getpixel((cx+2,chest+3)) not in [0,15]:out.putpixel((cx+2,chest+3),14)
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
     if n in [1,2,3,4] and not (y<start+56 and (x<28 or x>44)):continue
     if female:out.putpixel((x,y),12 if y>=start+59 else (10 if x<42 else 11))
     else:
      trim=y in [start+44,start+45,start+60,start+61] or (x==43 and y>start+47)
      out.putpixel((x,y),(12 if x<40 else 13) if trim else (10 if x<42 else 11))
   if female:
    # Puffy jacket sleeves also cover the upper shoulder in battle back poses.
    for y in range(start+45,min(start+52,src.height)):
     for x in range(39,51):
      n=src.getpixel((x,y))
      if n in [1,2,3,4]:out.putpixel((x,y),10 if n in [1,2] else 11)
   continue
  if female:
   # Cropped open jacket, pink undershirt and fitted cycling shorts.
   for y in range(25,38):
    for x in range(22,35):
     n=src.getpixel((x,y))
     if n not in [5,6,10,11,12,13]:continue
     center=27<=x<=30
     out.putpixel((x,y),12 if center or y>=34 else (10 if x<31 else 11))
   sleeves=Image.new('1',src.size);dr=ImageDraw.Draw(sleeves)
   dr.polygon([(23,27),(25,29),(22,33),(19,31)],fill=1)
   dr.polygon([(32,28),(36,30),(37,33),(33,34)],fill=1)
   for y in range(26,35):
    for x in range(18,38):
     n=src.getpixel((x,y))
     if sleeves.getpixel((x,y)) and n in [1,2,3,4,5,6,10,11,12,13]:out.putpixel((x,y),10 if x%3 else 11)
   for y in range(38,46):
    for x in range(22,37):
     n=src.getpixel((x,y))
     if n in [1,2,3,4,5,6,10,11,12,13]:out.putpixel((x,y),13 if n in [1,2,5,10,12] else 6)
  else:
   # Closed jacket, raised collar, red piping and a ribbed waistband.
   for y in range(25,41):
    for x in range(22,37):
     n=src.getpixel((x,y))
     if n not in [5,6,7,8,10,11,12,13] and not (y==25 and n in [1,2,3,4]):continue
     trim=(y in [26,27,37,38,39]) or (x==33 and y>29)
     out.putpixel((x,y),(12 if x<31 else 13) if trim else (10 if x<32 else 11))
   sleeves=Image.new('1',src.size);dr=ImageDraw.Draw(sleeves)
   dr.polygon([(24,27),(25,31),(20,38),(16,37),(19,32)],fill=1)
   dr.polygon([(34,27),(39,29),(44,34),(42,36),(36,32)],fill=1)
   for y in range(27,39):
    for x in range(15,45):
     n=src.getpixel((x,y))
     if sleeves.getpixel((x,y)) and n in [1,2,3,4,5,6,7,8,10,11,12,13]:out.putpixel((x,y),10 if x%3 else 11)
   for x in [32,34]:
    if src.getpixel((x,36)) not in [0,1,2,3,4,15]:out.putpixel((x,36),14)
 return palette(out,female)

for name,female in [('brendan',False),('may',True)]:
 dest=OUT/name;dest.mkdir(parents=True,exist_ok=True);source=R/f'graphics/object_events/pics/people/{name}'
 for state in ['walking','running','mach_bike','acro_bike','surfing','underwater','field_move','fishing','watering','decorating','riding']:
  im=Image.open(source/(state+'.png'));width=16 if state in ['walking','running','decorating','riding'] else 32
  sheet(im,female,width).save(dest/(state+'.png'),bits=4,transparency=0)
 walk=Image.open(dest/'walking.png');run=Image.open(dest/'running.png');normal=Image.new('P',(walk.width+run.width,32));normal.putpalette(walk.getpalette());normal.paste(walk,(0,0));normal.paste(run,(walk.width,0));normal.save(dest/'normal_running.png',bits=4,transparency=0)
 for side in ['front','back']:
  im=Image.open(R/f'graphics/trainers/{side}_pics/{name}.png');portrait(im,female,side=='back').save(dest/(side+'.png'),bits=4,transparency=0)
print('Built Silver jacket and Kris sports outfit')
