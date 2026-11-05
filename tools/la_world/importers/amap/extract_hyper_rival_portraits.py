"""Extract Hyper Emerald's active ORAS Brendan/May portraits, graphics only."""
from pathlib import Path
import struct,hashlib,json
from PIL import Image
R=Path(__file__).resolve().parents[4]
source=Path('/mnt/c/Users/aadair/Downloads/tools/Donor Roms/HypEm v5.7 EN+QoL.gba')
b=source.read_bytes()
assert hashlib.sha256(b).hexdigest()=='73d6faeb29bcc15e1627a6f237e99e11ddea8429ed31ec30057560ee069a546f'
def lz(off):
 assert b[off]==16
 n=int.from_bytes(b[off+1:off+4],'little');out=bytearray();off+=4
 while len(out)<n:
  flags=b[off];off+=1
  for bit in range(7,-1,-1):
   if len(out)>=n:break
   if flags>>bit&1:
    a,c=b[off:off+2];off+=2;distance=((a&15)<<8|c)+1
    for _ in range((a>>4)+3):out.append(out[-distance])
   else:out.append(b[off]);off+=1
 return bytes(out[:n])
records=[]
for name,index in [('brendan',71),('may',72)]:
 pic=struct.unpack_from('<I',b,0x101be90+index*8)[0]-0x8000000
 pal=struct.unpack_from('<I',b,0x101c660+index*8)[0]-0x8000000
 raw= lz(pic);colors=lz(pal)
 assert len(raw)==2048 and len(colors)==32
 rgb=[tuple((v>>s&31)*255//31 for s in [0,5,10]) for v in struct.unpack('<16H',colors)]
 im=Image.new('P',(64,64));im.putpalette(sum((list(c) for c in rgb),[])+[0]*720)
 for y in range(64):
  for x in range(64):im.putpixel((x,y),raw[((y//8)*8+x//8)*32+(y%8)*4+x%8//2]>>(4*(x%2))&15)
 dest=R/f'graphics/trainers/front_pics/hyper_rival_{name}.png';im.save(dest,bits=4,transparency=0)
 records.append(dict(character=name,donor_index=index,picture_offset=hex(pic),palette_offset=hex(pal),raw_sha256=hashlib.sha256(raw).hexdigest(),palette_sha256=hashlib.sha256(colors).hexdigest()))
d=R/'docs/art/hyper-rival-portraits';d.mkdir(parents=True,exist_ok=True)
(d/'source.json').write_text(json.dumps(dict(donor=source.name,donor_sha256=hashlib.sha256(b).hexdigest(),front_table='0x101be90',palette_table='0x101c660',graphics_only=True,portraits=records),indent=2)+'\n')
print('Extracted both Hyper portraits.')
