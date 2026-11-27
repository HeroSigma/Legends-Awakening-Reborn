"""Shared native outfit masks: separate exposed skin/head pixels from garments."""
def components(points):
 points=set(points)
 while points:
  seed=points.pop();group={seed};stack=[seed]
  while stack:
   x,y=stack.pop()
   for p in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
    if p in points:points.remove(p);group.add(p);stack.append(p)
  yield group

def cap_bottom(im):
 groups=[]
 for g in components((x,y) for y in range(im.height) for x in range(im.width) if im.getpixel((x,y)) in [9,14]):
  xs=[x for x,y in g];ys=[y for x,y in g]
  if len(g)>=8 and max(xs)-min(xs)>=2 and min(ys)<=20:groups.append(g)
 if not groups:return None
 g=max(groups,key=lambda g:len(g)-abs(sum(x for x,y in g)/len(g)-im.width/2))
 return max(y for x,y in g)

def skin_face(im):
 # Index 4 is ALSO a brown clothing outline in the original Emerald art.
 # Never flood through it: that joins chins to collars, waistbands and gloves.
 cap=cap_bottom(im);groups=[]
 for g in components((x,y) for y in range(im.height) for x in range(im.width) if im.getpixel((x,y)) in [1,2,3]):
  xs=[x for x,y in g];ys=[y for x,y in g];center=sum(xs)/len(xs)
  if len(g)<9 or max(xs)-min(xs)<2 or max(ys)-min(ys)<2 or min(ys)>20:continue
  if center<im.width*.2 or center>im.width*.8:continue
  if cap is not None and max(ys)<cap:continue
  groups.append(g)
 if not groups:return None
 face=max(groups,key=len)
 # Add one outline pixel around real skin, without transitive body expansion.
 halo={(xx,yy) for x,y in face for xx,yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if 0<=xx<im.width and 0<=yy<im.height and im.getpixel((xx,yy))==4}
 return face|halo

def garment_pose(src):
 face=skin_face(src)
 occupied=[(x,y) for y in range(src.height) for x in range(src.width) if src.getpixel((x,y))]
 if not occupied:return src.width//2,src.height,0
 if face:
  fw=max(x for x,y in face)-min(x for x,y in face)+1
  cx=round(sum(x for x,y in face)/len(face))+(2 if fw<6 else 0)
  chest=max(y for x,y in face)+1
 else:cx=src.width//2;chest=max(y for x,y in occupied)-7;fw=0
 # All 16px avatar frames share a centered body; wrists must not reposition it.
 if src.width==16:cx=8
 else:
  cloth=[x for y in range(max(0,chest),min(src.height,chest+3)) for x in range(max(0,cx-3),min(src.width,cx+4)) if src.getpixel((x,y)) in [10,11,12,13]]
  if cloth:cx=round((min(cloth)+max(cloth))/2)
 cap=cap_bottom(src)
 if cap is not None:chest=max(chest,cap+3)
 return min(src.width-1,max(0,cx)),min(src.height,max(0,chest)),fw

def clean_shadows(src,out,female,start):
 before=out.copy()
 for y in range(max(0,start),out.height):
  for x in range(out.width):
   if before.getpixel((x,y))!=4:continue
   near=[(xx,yy) for yy in range(max(0,y-1),min(out.height,y+2)) for xx in range(max(0,x-1),min(out.width,x+2)) if (xx,yy)!=(x,y)]
   skin=any(before.getpixel(p) in [1,2,3] for p in near)
   hair=female and any(src.getpixel(p) in [7,8] for p in near)
   if not skin and not hair:out.putpixel((x,y),15)
 return out

def finish_field_frame(src,out,female):
 return clean_shadows(src,out,female,min(24,garment_pose(src)[1]))

def finish_portrait(src,out,female,back):
 # Work per native 64x64 frame, keeping every original head pixel intact.
 for y in range(0,src.height,64):
  frame=clean_shadows(src.crop((0,y,src.width,y+64)),out.crop((0,y,out.width,y+64)),female,43 if back else 25)
  out.paste(frame,(0,y))
 return out
