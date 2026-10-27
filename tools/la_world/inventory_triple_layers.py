from pathlib import Path
import re,json,collections,struct
P=Path('/home/allan/projects/Legends-Awakening-Reborn');ms=(P/'src/data/tilesets/metatiles.h').read_text();paths=dict(re.findall(r'const u(?:16|32)\s+(\w+)\[\]\s*=\s*INCBIN_U(?:16|32)\("([^"]+)"\)',ms));hs=(P/'src/data/tilesets/headers.h').read_text();pairs={};symbols={};issues=[]
for name,body in re.findall(r'const struct Tileset\s+(\w+)\s*=\s*\{(.*?)\};',hs,re.S):
 m=re.search(r'\.metatiles\s*=\s*(\w+)',body);a=re.search(r'\.metatileAttributes\s*=\s*(\w+)',body)
 if not(m and a) or m[1] not in paths or a[1] not in paths:issues.append(name);continue
 pairs[paths[m[1]]]=paths[a[1]];symbols[name]=(paths[m[1]],paths[a[1]])
layouts=json.loads((P/'data/layouts/layouts.json').read_text())['layouts'];formats=collections.defaultdict(set)
for l in layouts:
 for name in [l['primary_tileset'],l['secondary_tileset']]:
  if name in symbols:formats[symbols[name][0]].add(4 if l.get('is_frlg',False) else 2)
print('Pair count',len(pairs),'symbols',len(symbols),'missing',issues[:10]);bad=[]
for m,a in pairs.items():
 n=(P/m).stat().st_size//16;data=(P/a).read_bytes();width=len(data)//n
 if width not in (2,4) or len(data)!=n*width:bad.append((m,n,len(data)));continue
 vals=struct.unpack('<'+str(n)+('H' if width==2 else 'I'),data);invalid=[(i,(v>>12)&15) for i,v in enumerate(vals) if width==2 and ((v>>12)&15)>2]
 if invalid:print(m,'invalid',len(invalid),'width',width,'formats',formats[m], 'example',invalid[:2])
print('Bad lengths:',bad);(P/'.la_work/triple-layer-inventory.json').write_text(json.dumps({'pairs':pairs,'symbols':symbols,'issues':issues},indent=2))
