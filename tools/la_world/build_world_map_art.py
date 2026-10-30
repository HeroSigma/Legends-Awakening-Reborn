"""Build the connected Hoenn / HnS Johto-Kanto artwork without donor code."""
from pathlib import Path
from PIL import Image
import struct
R=Path(__file__).resolve().parents[2]
A=R/'data/world_map';A.mkdir(exist_ok=True)
def decode(p):
 im=Image.open(p.with_suffix('.png'));b=p.with_suffix('.bin').read_bytes();assert len(b)==4096
 out=Image.new('RGB',(512,512));cols=im.width//8
 for i,t in enumerate(b):
  assert t<cols*(im.height//8)
  out.paste(im.crop((t%cols*8,t//cols*8,t%cols*8+8,t//cols*8+8)).convert('RGB'),(i%64*8,i//64*8))
 return out
hoenn=decode(R/'graphics/pokenav/region_map/map');jk=decode(R/'assets/regional_maps/hns/pokenav/map_jk')
world=Image.new('RGB',(512,512),(96,176,240));world.paste(jk.crop((0,0,240,160)),(248,24));world.paste(hoenn.crop((0,0,240,160)),(16,224))
# One ocean pattern joins the donor pieces without drawing false land connections.
pix=world.load()
for y in range(512):
 for x in range(512):
  r,g,b=pix[x,y]
  if b>r+15 and b>g+4:pix[x,y]=(112,192,248) if y%2 else (96,176,240)
world=world.quantize(colors=192,method=Image.Quantize.FASTOCTREE)
tiles=[];lookup={};grid=[]
for y in range(64):
 for x in range(64):
  b=world.crop((x*8,y*8,x*8+8,y*8+8)).tobytes()
  if b not in lookup:lookup[b]=len(tiles);tiles.append(b)
  grid.append(lookup[b])
assert len(tiles)<512, 'Atlas must stay below BG0 character data at 0x8000'
tm=[0]*4096
for y in range(64):
 for x in range(64):tm[(y//32*2+x//32)*1024+(y%32)*32+x%32]=grid[y*64+x]
(A/'tiles.bin').write_bytes(b''.join(tiles));(A/'tilemap.bin').write_bytes(struct.pack('<4096H',*tm));pal=world.getpalette();(A/'palette.bin').write_bytes(b''.join(struct.pack('<H',(pal[i]>>3)|((pal[i+1]>>3)<<5)|((pal[i+2]>>3)<<10)) for i in range(0,192*3,3)))
world.save(R/'docs/art/regional_maps/world-canvas.png')
print('Atlas:',len(tiles),'unique tiles; world palette reserves banks 12-15 for UI.')
