from pathlib import Path
import re,collections,struct,json
P=Path('/home/allan/projects/Legends-Awakening-Reborn');s=(P/'src/data/tilesets/metatiles.h').read_text();files=sorted(set(re.findall(r'INCBIN_U16\("([^"]+)"\)',s)));metas=[v for v in files if 'attribute' not in v.lower()];problems=[];stats=collections.Counter();types=collections.Counter()
for rel in metas:
 f=P/rel;attr=f.with_name('metatile_attributes.bin')
 if not attr.exists():problems.append((rel,'missing attrs'));continue
 n=f.stat().st_size//16;data=attr.read_bytes();width=len(data)//n if n else 0
 if f.stat().st_size%16 or width not in (2,4):problems.append((rel,n,len(data),width));continue
 words=struct.unpack('<'+str(n)+('H' if width==2 else 'I'),data);types.update(((v>>12)&15 if width==2 else (v>>29)&3) for v in words);stats[width]+=1
print('Metatile files',len(metas),'attribute formats',dict(stats),'layer types',dict(types));print('Problems',problems[:20]);print('All files:',len(list((P/'data').rglob('metatiles.bin'))))
