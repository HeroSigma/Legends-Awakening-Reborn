from pathlib import Path
from PIL import Image
import collections,json
p=Path('/home/allan/projects/Legends-Awakening-Reborn');f=p/'tools/la_world/rebuild_unova_wesley.py';s=f.read_text();ns={'__file__':str(f)};exec(s[:s.index('class Pack:')],ns)
exec((p/'tools/la_world/nuvema_exact_assets.py').read_text(),ns)
sets=[];bad=[]
for n,im in ns['assets'].items():
 if n not in ns['active_assets']:continue
 for y in range(0,im.height,8):
  for x in range(0,im.width,8):
   cs=frozenset(tuple(v>>3 for v in c[:3]) for c in im.crop((x,y,x+8,y+8)).getdata() if c[3])
   if len(cs)>15:bad.append((n,x,y,len(cs)))
   elif cs:sets.append(cs)
sets=list(set(sets));sets=[c for c in sets if not any(c<d for d in sets)];bins=[]
for cs in sorted(sets,key=lambda c:(-len(c),sorted(c))):
 opts=[(len(cs-b),i) for i,b in enumerate(bins) if len(cs|b)<=15]
 if opts:bins[min(opts)[1]]|=cs
 else:bins.append(set(cs))
print('Oversized native 8x8 tiles:',bad);print('Exact greedy palette banks:',len(bins));print([len(b) for b in bins])
