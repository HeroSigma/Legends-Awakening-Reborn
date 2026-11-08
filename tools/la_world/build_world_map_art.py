"""Build the connected Hoenn / HnS Johto-Kanto artwork without donor code."""
from pathlib import Path
from PIL import Image
import struct
import json, re
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
# Each region has a dedicated 16-color GBA bank. This leaves room for the UI
# while preserving the source image's original pixel resolution.
regions=[(0,0,512,512),(248,24,240,160),(16,224,240,160)]
quant=[];palette=[];preview=Image.new('RGB',(512,512));
for ox,oy,w,h in regions:
 im=world.crop((ox,oy,ox+w,oy+h)).quantize(colors=16,method=Image.Quantize.MAXCOVERAGE,dither=Image.Dither.NONE)
 quant.append(im);palette+=(im.getpalette()+[0]*48)[:48];preview.paste(im.convert('RGB'),(ox,oy))
tiles=[];lookup={};grid=[]
for y in range(64):
 for x in range(64):
  bank=0
  for j,(ox,oy,w,h) in enumerate(regions[1:],1):
   if ox<=x*8<ox+w and oy<=y*8<oy+h:bank=j
  ox,oy,w,h=regions[bank];tile=quant[bank].crop((x*8-ox,y*8-oy,x*8-ox+8,y*8-oy+8));raw=tile.tobytes();b=bytes(raw[i]|raw[i+1]<<4 for i in range(0,64,2))
  if b not in lookup:lookup[b]=len(tiles);tiles.append(b)
  grid.append(lookup[b]|bank<<12)
assert len(tiles)<1024, '4bpp atlas must fit before the UI character bank'
tm=[0]*4096
for y in range(64):
 for x in range(64):tm[(y//32*2+x//32)*1024+(y%32)*32+x%32]=grid[y*64+x]
(A/'tiles.bin').write_bytes(b''.join(tiles));(A/'tilemap.bin').write_bytes(struct.pack('<4096H',*tm));(A/'palette.bin').write_bytes(b''.join(struct.pack('<H',(palette[i]>>3)|((palette[i+1]>>3)<<5)|((palette[i+2]>>3)<<10)) for i in range(0,len(palette),3)))
preview.save(R/'docs/art/regional_maps/world-canvas.png')
print('Atlas:',len(tiles),'unique 4bpp tiles; three palette banks.')
