"""Extract BWA's masked Shadow Triad trainer portrait, visual assets only."""
from pathlib import Path
import struct,hashlib,json
from PIL import Image
R=Path(__file__).resolve().parents[4]
source=Path('/mnt/c/Users/aadair/Downloads/tools/Donor Roms/Pokemon Black & White Advanced (Demo v2).gba')
b=source.read_bytes()
assert hashlib.sha256(b).hexdigest()=='12a2e11285b5a4c57ede151d78ad3308b9a96b406b0d41fdade6f6da57b3fef4'
def decompress(off):
 assert b[off]==16
 n=int.from_bytes(b[off+1:off+4],'little');out=bytearray();off+=4
 while len(out)<n:
  flags=b[off];off+=1
  for bit in range(7,-1,-1):
   if len(out)>=n:break
   if flags&(1<<bit):
    a,c=b[off:off+2];off+=2;distance=((a&15)<<8|c)+1
    for _ in range((a>>4)+3):out.append(out[-distance])
   else:out.append(b[off]);off+=1
 return out[:n]
index=99
pic=struct.unpack_from('<I',b,0x23957c+index*8)[0]-0x8000000
pal=struct.unpack_from('<I',b,0x239a1c+index*8)[0]-0x8000000
raw=decompress(pic);colors=decompress(pal)
assert len(raw)==2048 and len(colors)==32
palette=[tuple(((v>>s)&31)*255//31 for s in [0,5,10]) for v in struct.unpack('<16H',colors)]
im=Image.new('P',(64,64));im.putpalette(sum((list(c) for c in palette),[])+[0]*720)
for y in range(64):
 for x in range(64):im.putpixel((x,y),raw[((y//8)*8+x//8)*32+(y%8)*4+x%8//2]>>(4*(x%2))&15)
im.save(R/'graphics/trainers/front_pics/shadow_triad.png',bits=4,transparency=0)
(R/'docs/art/npc_roster/shadow-triad-portrait.json').write_text(json.dumps(dict(source_sha256=hashlib.sha256(b).hexdigest(),donor='bwa',trainer_pic_index=index,picture_offset=hex(pic),palette_offset=hex(pal),graphics_only=True),indent=2)+'\n')
