from pathlib import Path
from PIL import Image, ImageFilter, ImageChops, ImageStat
import json,struct,shutil
P=Path('/home/allan/projects/Legends-Awakening-Reborn')
A=P/'data/tilesets/nuvema_recreation';A.mkdir(parents=True,exist_ok=True)
B=P/'.la_work/nuvema_recreation_backup';B.mkdir(parents=True,exist_ok=True)
def backup(f):
 q=B/f;q.parent.mkdir(parents=True,exist_ok=True)
 if not q.exists():shutil.copy2(P/f,q)
def edit(f,s):backup(f);(P/f).write_text(s)
source=A/'reference.png'


im=Image.open(source).convert('RGB').resize((320,240),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=0.6,percent=130,threshold=3))
# Tile palettes follow materials; each 8x8 tile uses one hardware palette.
groups=[[] for _ in range(13)];tileinfo=[]
for y in range(30):
 for x in range(40):
  tile=im.crop((x*8,y*8,x*8+8,y*8+8));r,g,b=tuple(sum(c[i] for c in tile.getdata())//64 for i in range(3))
  if y>=24:k=0 if b>g else 1
  elif r>g*1.15:k=2
  elif b>r*1.35:k=3 if g<b*.8 else 4
  elif r>g*.92:k=5 if r>155 else 6
  elif g>r*1.45:k=7 if g<100 else 8 if g<145 else 9
  else:k=10 if g<110 else 11 if g<165 else 12
  groups[k].append(tile);tileinfo.append((x,y,k,tile))
pals=[]
for group in groups:
 canvas=Image.new('RGB',(8,max(8,len(group)*8)))
 for i,t in enumerate(group):canvas.paste(t,(0,i*8))
 q=canvas.quantize(colors=15,method=Image.Quantize.MEDIANCUT)
 colors=[tuple(v&248 for v in q.getpalette()[i:i+3]) for i in range(0,45,3)]
 pals.append([(0,0,0)]+colors)

# Match each tile to the palette with the least actual colour error.
encoded=[]
palette_images=[]
for colors in pals:
 pal=Image.new('P',(1,1));pal.putpalette(sum((list(c) for c in colors[1:]),[])+list(colors[-1])*(256-15));palette_images.append(pal)
for x,y,_,t in tileinfo:
 options=[]
 for k,pal in enumerate(palette_images):
  q=t.quantize(palette=pal,dither=Image.Dither.NONE)
  error=sum(ImageStat.Stat(ImageChops.difference(t,q.convert('RGB'))).sum2)
  options.append((error,k,q))
 _,k,q=min(options,key=lambda e:e[0]);pix=bytes(min(v,14)+1 for v in q.getdata())
 encoded.append((x,y,k,pix))
# Keep buildings, fences and water exact. Spend approximation only on vegetation.
def important(e):
 x,y,k,pix=e
 return not (x<6 or x>=34 or y<3 or (y<9 and x>=18))
encoded.sort(key=lambda e:(not important(e),e[1],e[0]))
tiles=[bytes(64)];lookup={bytes(64):0};refs={};approximated=0;by_palette={k:[] for k in range(13)}
for x,y,k,pix in encoded:
 if pix not in lookup:
  if len(tiles)<1024:
   lookup[pix]=len(tiles);tiles.append(pix);by_palette[k].append(len(tiles)-1)
  else:
   candidates=by_palette[k] or list(range(1,len(tiles)))
   candidates=sorted(candidates,key=lambda i:abs(sum(tiles[i])-sum(pix)))[:96]
   colors=pals[k]
   def distance(i):
    return sum(sum((colors[a][j]-colors[b][j])**2 for j in range(3)) for a,b in zip(tiles[i],pix))
   lookup[pix]=min(candidates,key=distance);approximated+=1
 idx=lookup[pix];refs[x,y]=idx|(k<<12)
preview=Image.new('RGB',(320,240))
for (x,y),ref in refs.items():
 t=Image.new('RGB',(8,8));t.putdata([pals[ref>>12][v] for v in tiles[ref&1023]]);preview.paste(t,(x*8,y*8))
preview.resize((960,720),Image.Resampling.NEAREST).save(A/'preview.png')
meta=[]
for y in range(15):
 for x in range(20):meta.extend([refs[x*2,y*2],refs[x*2+1,y*2],refs[x*2,y*2+1],refs[x*2+1,y*2+1],0,0,0,0])
meta.extend([0]*(4096-len(meta)))
attr=list(struct.unpack('<512H',(A/'primary/metatile_attributes.bin').read_bytes()))
print('Improved conversion:',len(tiles),'tiles;',approximated,'vegetation approximations')
for secondary in [False,True]:
 name='secondary' if secondary else 'primary';d=A/name;(d/'palettes').mkdir(parents=True,exist_ok=True)
 chunk=tiles[512:1024] if secondary else tiles[:512];chunk+= [bytes(64)]*(512-len(chunk))
 raw=bytes(a|(b<<4) for t in chunk for a,b in zip(t[::2],t[1::2]));(d/'tiles.4bpp').write_bytes(raw)
 png=Image.new('P',(128,256));png.putpalette([i*17 for i in range(16) for _ in range(3)]+[0]*720)
 for i,t in enumerate(chunk):tt=Image.new('P',(8,8));tt.putdata(t);png.paste(tt,((i%16)*8,(i//16)*8))
 png.save(d/'tiles.png')
 (d/'metatiles.bin').write_bytes(struct.pack('<4096H',*(meta if not secondary else [0]*4096)))
 (d/'metatile_attributes.bin').write_bytes(struct.pack('<512H',*(attr if not secondary else [0]*512)))
 for i,colors in enumerate(pals):
  (d/f'palettes/{i:02}.gbapal').write_bytes(struct.pack('<16H',*[r//8|((g//8)<<5)|((b//8)<<10) for r,g,b in colors]))
  (d/f'palettes/{i:02}.pal').write_text('JASC-PAL\n0100\n16\n'+'\n'.join(' '.join(map(str,c)) for c in colors)+'\n')
