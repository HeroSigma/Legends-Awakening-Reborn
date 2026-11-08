from pathlib import Path
import json
from PIL import Image
P=Path('/home/allan/projects/Legends-Awakening-Reborn');f=P/'tools/la_world/rebuild_unova_wesley.py';s=f.read_text();ns={'__file__':str(f)}
exec(s[:s.index('# Small native materials')],ns)
sheets=[Image.open(P/'graphics/unova_wesley/source'/n).convert('RGBA') for n in ['Nuvema.png','Nuvema Second.png']];found={}
for key,im in ns['assets'].items():
 bbox=im.getbbox();t=im.crop(bbox);pix=t.load();opaque=[(x,y,pix[x,y][:3]) for y in range(t.height) for x in range(t.width) if pix[x,y][3]]
 anchors=opaque[::max(1,len(opaque)//20)]
 for si,sheet in enumerate(sheets):
  a=sheet.load();done=False
  for y in range(sheet.height-t.height+1):
   for x in range(sheet.width-t.width+1):
    if not all(a[x+dx,y+dy][:3]==c and a[x+dx,y+dy][3] for dx,dy,c in anchors):continue
    if all(a[x+dx,y+dy][:3]==c and a[x+dx,y+dy][3] for dx,dy,c in opaque):
     found[key]={'sheet':['Nuvema.png','Nuvema Second.png'][si],'box':[x,y,x+t.width,y+t.height],'offset':[bbox[0],bbox[1]],'size':list(im.size)};done=True;break
   if done:break
  if done:break
(P/'docs/la_world/unova_wesley/user_sheet_crops.json').write_text(json.dumps(found,indent=2)+'\n');print(json.dumps(found,indent=2))
