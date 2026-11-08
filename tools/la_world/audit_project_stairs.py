from pathlib import Path
import json,re,struct,collections
R=Path(__file__).resolve().parents[2];O=R/'docs/la_world/project_stairs';O.mkdir(parents=True,exist_ok=True)
defs={};sets={}
for f in sorted((R/'src/data/tilesets').glob('*.h'),key=lambda f:(f.name!='headers.h',f.name)):
 s=f.read_text()
 defs.update({sym:path for sym,path in re.findall(r'const u(?:16|32)\s+(\w+)\[\]\s*=\s*INCBIN_U(?:16|32)\("([^"]+)"\)',s)})
 for name,b in re.findall(r'const struct Tileset\s+(\w+)\s*=\s*\{(.*?)\};',s,re.S):
  a=re.search(r'\.metatileAttributes\s*=\s*(\w+)',b)
  if a and name not in sets:sets[name]=a[1]
ls={l['id']:l for l in json.loads((R/'data/layouts/layouts.json').read_text())['layouts']};groups=json.loads((R/'data/maps/map_groups.json').read_text());rows=[];candidates=[];unknown=[]
for gi,g in enumerate(groups['group_order']):
 for mi,name in enumerate(groups[g]):
  m=json.loads((R/'data/maps'/name/'map.json').read_text());l=ls[m['layout']];arrays=[]
  for k in ['primary_tileset','secondary_tileset']:
   path=defs.get(sets.get(l[k],''))
   if path is None:break
   raw=(R/path).read_bytes();arrays.append(list(struct.unpack('<'+'H'*(len(raw)//2),raw)))
  if len(arrays)!=2:unknown.append(name);continue
  # Native Emerald and normalized donor banks have 512 primary definitions.
  attrs=arrays[0]+arrays[1];W,H=l['width'],l['height'];raw=(R/l['blockdata_filepath']).read_bytes();cells=struct.unpack('<'+'H'*(len(raw)//2),raw)
  if len(cells)!=W*H:continue
  counts=collections.Counter();sample=[]
  for i,v in enumerate(cells):
   id=v&1023
   if id>=len(attrs):continue
   b=attrs[id]&255
   if b not in range(0x49,0x50):continue
   counts[b]+=1;x,y=i%W,i//W
   if v&0xc00 or not(1<=x<W-1 and 1<=y<H-1):continue
   if b==0x4f and not cells[i-W]&0xc00 and not cells[i+W]&0xc00:
    sample.append(dict(x=x,y=y,kind='vertical',behavior=b))
   elif b in [0x49,0x4a]:sample.append(dict(x=x,y=y,kind='sideways',behavior=b))
  if counts:
   rows.append(dict(map=name,group=gi,num=mi,layout=m['layout'],counts={hex(k):v for k,v in counts.items()}))
   if sample:candidates.append(dict(map=name,group=gi,num=mi,region=g,samples=sample[:12]))
report=dict(registered_maps=sum(len(groups[g]) for g in groups['group_order']),maps_with_tagged_stairs=len(rows),stair_cells=sum(sum(r['counts'].values()) for r in rows),unresolved_maps=unknown,maps=rows,candidates=candidates)
(O/'coverage.json').write_text(json.dumps(report,indent=2));print({k:v for k,v in report.items() if k not in ['maps','candidates']});print('candidate maps',len(candidates));print([(r['map'],r['samples'][0]) for r in candidates][:15])

