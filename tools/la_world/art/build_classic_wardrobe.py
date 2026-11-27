"""Native indexed garment edits; preserve original protagonist heads and poses.
All source art is existing project player art. No generated concept is imported.
"""
from pathlib import Path
from PIL import Image, ImageDraw
R=Path(__file__).resolve().parents[3]
OUT=R/'graphics/player_outfits/classic'

def palette(im, female):
 p=im.getpalette()
 colors=[(82,180,230),(41,106,172),(255,98,90),(197,65,65)] if female else [(238,74,65),(164,41,49),(255,255,255),(197,205,222)]
 for i,c in enumerate(colors,10):p[i*3:i*3+3]=c
 im.putpalette(p)
 return im

def skin_face(im):
 todo={(x,y) for y in range(im.height) for x in range(im.width) if im.getpixel((x,y)) in [1,2,3,4]};groups=[]
 while todo:
  seed=todo.pop();group={seed};stack=[seed]
  while stack:
   x,y=stack.pop()
   for n in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
    if n in todo:todo.remove(n);group.add(n);stack.append(n)
  xs=[x for x,y in group];ys=[y for x,y in group]
  if max(xs)-min(xs)>=2 and max(ys)-min(ys)>=2:groups.append(group)
 return max(groups,key=len) if groups else None

def field_frame(im, female, swimming=False):
 src=im.copy();face=skin_face(src)
 occupied=[(x,y) for y in range(im.height) for x in range(im.width) if src.getpixel((x,y))]
 if not occupied:return im
 if face:
  cx=round(sum(x for x,y in face)/len(face));chest=max(y for x,y in face)+1
  face_width=max(x for x,y in face)-min(x for x,y in face)+1
 else:
  cx=round((min(x for x,y in occupied)+max(x for x,y in occupied))/2);chest=max(y for x,y in occupied)-7;face_width=0
 chest=min(chest,im.height-5)
 cloth_x=[x for y in range(max(0,chest),min(im.height,chest+3)) for x in range(max(0,cx-5),min(im.width,cx+6)) if src.getpixel((x,y)) in [10,11,12,13]]
 if cloth_x:cx=round((min(cloth_x)+max(cloth_x))/2)
 # Garment panels replace the original chest pattern, including its diagonal sash.
 for y in range(max(0,chest),min(im.height,chest+4)):
  for x in range(max(0,cx-3),min(im.width,cx+4)):
   n=src.getpixel((x,y))
   if n in ([0,1,2,3,4,7,8,15] if female else [0,1,2,3,4,15]):continue
   if female:im.putpixel((x,y),10 if n%2==0 else 11)
   else:
    shirt=(face_width>=6 and x in [cx,cx+1]) or (0<face_width<6 and x==cx-2)
    im.putpixel((x,y),(12 if y%2 else 13) if shirt else (10 if x<cx+2 else 11))
 if female and not swimming:
  # A real skirt silhouette and filled hem, rather than recolored shorts.
  for row,half in ([(3,1),(4,2),(5,2)] if 0<face_width<6 else [(3,2),(4,3),(5,3)]):
   y=chest+row
   if y>=im.height-2:continue
   for x in range(max(0,cx-half),min(im.width,cx+half+1)):
    if src.getpixel((x,y)) in [7,8] and y<chest+4:continue
    im.putpixel((x,y),15 if abs(x-cx)==half or row==5 else (12 if x<cx+2 else 13))
 return im

def field_sheet(src, female, width=32, swimming=False):
 out=src.copy()
 for yy in range(0,src.height,32):
  for xx in range(0,src.width,width):
   frame=field_frame(src.crop((xx,yy,xx+width,yy+32)),female,swimming)
   out.paste(frame,(xx,yy))
 return palette(out,female)

def portrait(src,female,back=False):
 out=src.copy()
 for start in range(0,src.height,64):
  if back:
   for y in range(start+35,min(start+64,src.height)):
    for x in range(12,53):
     n=src.getpixel((x,y))
     if n in [10,11,12,13]:out.putpixel((x,y),10 if n%2==0 else 11)
   if not female:
    # Vest back panel and white undershirt sleeves replace the original dark
    # short-sleeved shirt/backpack pattern; the complete head stays untouched.
    for y in range(start+43,min(start+64,src.height)):
     for x in range(18,53):
      n=src.getpixel((x,y))
      if n not in [5,6,7,8,10,11,12,13]:continue
      if 29<=x<=44:out.putpixel((x,y),11 if x>=41 or x==35 else 10)
      elif y<start+56:out.putpixel((x,y),12 if n in [5,6,10,12] else 13)
   continue
  if female:
   for y in range(25,35):
    for x in range(23,34):
     n=src.getpixel((x,y))
     if n in [10,11,12,13]:out.putpixel((x,y),10 if n%2==0 else 11)
   skirt=Image.new('1',src.size);ImageDraw.Draw(skirt).polygon([(24,34),(31,34),(35,42),(21,42)],fill=1)
   for y in range(34,43):
    for x in range(20,37):
     if skirt.getpixel((x,y)):
      edge=any(not (0<=xx<src.width and 0<=yy<src.height) or not skirt.getpixel((xx,yy)) for xx,yy in [(x-1,y),(x+1,y),(x,y+1)])
      out.putpixel((x,y),15 if edge else (12 if x<31 else 13))
   for x in range(23,34):out.putpixel((x,41),13)
  else:
   for y in range(26,38):
    for x in range(22,37):
     n=src.getpixel((x,y))
     if n not in [5,6,7,8,10,11,12,13]:continue
     if x in [28,29,30]:out.putpixel((x,y),12 if x<30 else 13)
     else:out.putpixel((x,y),10 if x<33 else 11)
   # Pockets and stitch lines are garment pixels, not a global recolor.
   for x in [24,25,32,33]:
    if src.getpixel((x,34)) not in [0,1,2,3,4,15]:out.putpixel((x,34),11)
 return palette(out,female)

for name,female in [('brendan',False),('may',True)]:
 dest=OUT/name;dest.mkdir(parents=True,exist_ok=True)
 source=R/f'graphics/object_events/pics/people/{name}'
 for state in ['walking','running','mach_bike','acro_bike','surfing','underwater','field_move','fishing','watering','decorating','riding']:
  im=Image.open(source/(state+'.png'))
  width=16 if state in ['walking','running','decorating','riding'] else 32
  out=field_sheet(im,female,width,state in ['surfing','underwater','riding'])
  out.save(dest/(state+'.png'),bits=4,transparency=0)
 walk=Image.open(dest/'walking.png');run=Image.open(dest/'running.png')
 normal=Image.new('P',(walk.width+run.width,walk.height));normal.putpalette(walk.getpalette());normal.paste(walk,(0,0));normal.paste(run,(walk.width,0));normal.save(dest/'normal_running.png',bits=4,transparency=0)
 for side in ['front','back']:
  im=Image.open(R/f'graphics/trainers/{side}_pics/{name}.png')
  portrait(im,female,side=='back').save(dest/(side+'.png'),bits=4,transparency=0)
print('Built both classic garment sets')
