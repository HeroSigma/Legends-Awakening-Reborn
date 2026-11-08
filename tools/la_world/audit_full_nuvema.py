from pathlib import Path
from PIL import Image
P=Path('/home/allan/projects/Legends-Awakening-Reborn');sets=[]
for name in ['Nuvema.png','Nuvema Second.png']:
 im=Image.open(P/'graphics/unova_wesley/source'/name).convert('RGBA');bad=[];unique=set()
 for y in range(0,im.height,8):
  for x in range(0,im.width,8):
   cs=frozenset(tuple(v>>3 for v in c[:3]) for c in im.crop((x,y,x+8,y+8)).getdata() if c[3]);unique.add(cs)
   if len(cs)>15:bad.append((x,y,len(cs)))
 print(name,im.size,'oversized tiles',bad,'opaque colours',len(set().union(*unique)))
 sets+=list(unique)
sets=list(set(sets));sets=[c for c in sets if c and not any(c<d for d in sets)];bins=[]
for cs in sorted(sets,key=lambda c:(-len(c),sorted(c))):
 opts=[(len(cs-b),i) for i,b in enumerate(bins) if len(cs|b)<=15]
 if opts:bins[min(opts)[1]]|=cs
 else:bins.append(set(cs))
print('Full-sheet exact palettes:',len(bins))
