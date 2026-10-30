"""Allocate local title/rift animation palette bands; no runtime framebuffer."""
from pathlib import Path
from PIL import Image
import struct
R=Path(__file__).resolve().parents[3]
D=R/'graphics/title_screen/legends_awakening'
source=R/'docs/art/title_screen/rift_preview/concept-source.png'
im=Image.open(source).convert('RGB').resize((240,160),Image.Resampling.LANCZOS)
base=im.quantize(colors=192,dither=Image.Dither.NONE)
pal=base.getpalette()[:576]+[0]*(768-576)
pixels=bytearray(base.tobytes());groups=[[] for _ in range(56)]
for y in range(160):
 for x in range(240):
  r,g,b=im.getpixel((x,y));group=None
  # Bright logo lettering only; keep its dark outline and the forest untouched.
  if 5<=y<=49 and 43<=x<203 and max(r,g,b)>175 and min(r,g,b)>78:
   band=min(15,(x-43)//10)
   group=band*2+(1 if r+g+b>620 else 0)
  # Follow luminous fractured edges, excluding Iron Valiant's central body.
  elif 50<=y<127 and 112<=x<=186 and not (143<=x<=166 and 61<=y<=121) and max(r,g,b)>175 and r>g*1.12 and b>g*1.08:
   band=min(11,(y-50)*12//77)
   group=32+band*2+(1 if r+g+b>585 else 0)
  if group is not None:
   groups[group].append((r,g,b));pixels[y*240+x]=192+group
for group,colors in enumerate(groups):
 c=tuple(round(sum(z[i] for z in colors)/len(colors)) for i in range(3)) if colors else (0,0,0)
 pal[(192+group)*3:(193+group)*3]=c
out=Image.frombytes('P',(240,160),bytes(pixels));out.putpalette(pal);out.save(D/'title.png')
(D/'title.bin').write_bytes(pixels)
(D/'title.gbapal').write_bytes(b''.join(struct.pack('<H',(pal[i]>>3)|((pal[i+1]>>3)<<5)|((pal[i+2]>>3)<<10)) for i in range(0,768,3)))
print('Animation pixels:',sum(map(len,groups)),'palette bands:',sum(bool(g) for g in groups))
