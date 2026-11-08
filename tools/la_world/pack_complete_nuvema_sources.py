from pathlib import Path
from PIL import Image
import json,struct,copy
P=Path(__file__).resolve().parents[2];SRC=P/'graphics/unova_wesley/source';D=P/'docs/la_world/unova_wesley';OUT=P/'.la_work/unova_wesley';pages=[];records=[];current=None
for filename in ['Nuvema.png','Nuvema Second.png']:
 im=Image.open(SRC/filename).convert('RGBA')
 for y in range(0,im.height,16):
  for x in range(0,im.width,16):
   cell=im.crop((x,y,x+16,y+16))
   if not cell.getbbox():continue
   pieces=[cell.crop((j%2*8,j//2*8,j%2*8+8,j//2*8+8)) for j in range(4)]
   cs=[set(tuple(v>>3 for v in c[:3]) for c in q.getdata() if c[3]) for q in pieces]
   assert all(len(c)<=15 for c in cs)
   def extend(bins):
    bins=copy.deepcopy(bins);slots=[]
    for colors in cs:
     options=[(len(colors-b),i) for i,b in enumerate(bins) if len(colors|b)<=15]
     if options:i=min(options)[1];bins[i]|=colors
     else:i=len(bins);bins.append(set(colors))
     slots.append(i)
    return bins,slots
   options=[]
   for pi,page in enumerate(pages):
    bins,slots=extend(page['bins'])
    if len(bins)<=13 and len(page['cells'])<200:options.append((len(bins),pi,bins,slots))
   if options:_,pi,bins,slots=min(options,key=lambda q:q[:2]);page=pages[pi];page['bins']=bins
   else:
    bins,slots=extend([]);pi=len(pages);page={'bins':bins,'cells':[]};pages.append(page)
   page['cells'].append((filename,x,y,pieces,slots));records.append((filename,x,y,pi))
cat=json.loads((P/'data/tilesets/unova_wesley_prefabs.json').read_text());cat=[v for v in cat if not v['name'].startswith('Original sheet -')];mapping=[];graphics=[];metas=[];headers=[];checks=0
for pi,page in enumerate(pages):
 palettes=[[(0,0,0)]+[tuple(v<<3 for v in c) for c in sorted(b)]+[(0,0,0)]*(15-len(b)) for b in page['bins']];palettes += [[(0,0,0)]*16]*(16-len(palettes));tiles={0:bytes(64)};lookup={bytes(64):0};nexttile=1;bankmetas=[[],[]];symbols=[f'UnovaNuvemaOriginal{pi+1}_Primary',f'UnovaNuvemaOriginal{pi+1}_Secondary']
 for filename,x,y,pieces,slots in page['cells']:
  refs=[]
  for q,slot in zip(pieces,slots):
   colours=palettes[slot];indices={tuple(v>>3 for v in c):i for i,c in enumerate(colours) if i};pix=bytes(indices[tuple(v>>3 for v in c[:3])] if c[3] else 0 for c in q.getdata())
   if pix not in lookup:lookup[pix]=nexttile;tiles[nexttile]=pix;nexttile+=1
   refs.append(lookup[pix]|slot<<12)
  bank=int(any((v&1023)>=512 for v in refs));mid=len(bankmetas[bank])+bank*512;bankmetas[bank].append(refs+[0]*4)
  mapping.append({'sheet':filename,'x':x,'y':y,'page':pi+1,'metatile_id':mid})
  cat.append({'name':f'Original sheet - {filename} ({x},{y}) page {pi+1}','width':1,'height':1,'primary_tileset':'gTileset_'+symbols[0],'secondary_tileset':'gTileset_'+symbols[1],'metatiles':[{'x':0,'y':0,'metatile_id':mid,'collision':0,'elevation':3}]})
  for q,ref in zip(pieces,refs):
   decoded=[(*palettes[ref>>12][n],255 if n else 0) for n in tiles[ref&1023]]
   for c,got in zip(q.getdata(),decoded):assert (not c[3] and not got[3]) or (c[3] and got[3] and tuple(v>>3 for v in c[:3])==tuple(v>>3 for v in got[:3]));checks+=1
 assert nexttile<=1024
 for bank,symbol in enumerate(symbols):
  directory=P/'data/tilesets'/('secondary' if bank else 'primary')/f'unova_nuvema_original{pi+1}';directory.mkdir(parents=True,exist_ok=True);(directory/'palettes').mkdir(exist_ok=True);rel=directory.relative_to(P).as_posix();raw=bytearray();png=Image.new('P',(128,256));png.putpalette([i*17 for i in range(16) for _ in range(3)]+[0]*720)
  for i in range(512):
   pix=tiles.get(bank*512+i,bytes(64));raw.extend(a|b<<4 for a,b in zip(pix[::2],pix[1::2]));q=Image.new('P',(8,8));q.putdata(pix);png.paste(q,((i%16)*8,(i//16)*8))
  (directory/'tiles.4bpp').write_bytes(raw);png.save(directory/'tiles.png');m=bankmetas[bank]+[[0]*8]*(512-len(bankmetas[bank]));(directory/'metatiles.bin').write_bytes(struct.pack('<4096H',*(v for row in m for v in row)));(directory/'metatile_attributes.bin').write_bytes(bytes(1024))
  for slot,colours in enumerate(palettes):
   (directory/f'palettes/{slot:02}.pal').write_text('JASC-PAL\n0100\n16\n'+'\n'.join(' '.join(map(str,c)) for c in colours)+'\n');(directory/f'palettes/{slot:02}.gbapal').write_bytes(struct.pack('<16H',*[sum((c[k]>>3)<<(5*k) for k in range(3)) for c in colours]))
  graphics.append(f'const u32 gTilesetTiles_{symbol}[] = INCBIN_U32("{rel}/tiles.4bpp.lz");\nconst u16 gTilesetPalettes_{symbol}[][16] = {{\n'+''.join(f'    INCBIN_U16("{rel}/palettes/{i:02}.gbapal"),\n' for i in range(16))+'};')
  metas.append(f'const u16 gMetatiles_{symbol}[] = INCBIN_U16("{rel}/metatiles.bin");\nconst u16 gMetatileAttributes_{symbol}[] = INCBIN_U16("{rel}/metatile_attributes.bin");')
  headers.append(f'const struct Tileset gTileset_{symbol} = {{ .isCompressed=TRUE, .isSecondary={"TRUE" if bank else "FALSE"}, .tiles=gTilesetTiles_{symbol}, .palettes=gTilesetPalettes_{symbol}, .metatiles=gMetatiles_{symbol}, .metatileAttributes=gMetatileAttributes_{symbol}, .callback=NULL }};')
 print('Original page',pi+1,':',len(page['bins']),'palettes,',nexttile,'tiles,',len(page['cells']),'native 16px pieces')
for file,content in [('graphics.h',graphics),('metatiles.h',metas),('headers.h',headers)]:
 f=P/'src/data/tilesets'/file;s=f.read_text();a='// BEGIN NUVEMA_COMPLETE_ORIGINALS';b='// END NUVEMA_COMPLETE_ORIGINALS'
 if a in s:s=s[:s.index(a)]+s[s.index(b)+len(b):]
 f.write_text(s.rstrip()+'\n\n'+a+'\n'+'\n\n'.join(content)+'\n'+b+'\n')
(P/'data/tilesets/unova_wesley_prefabs.json').write_text(json.dumps(cat,indent=2)+'\n');(D/'complete_source_mapping.json').write_text(json.dumps({'pages':len(pages),'pixel_checks':checks,'colour_reduction':False,'pieces':mapping},indent=2)+'\n')
# Reconstruct both sheets from serialized GBA bank files, not the input pixels.
for filename in ['Nuvema.png','Nuvema Second.png']:
 source=Image.open(SRC/filename).convert('RGBA');rebuilt=Image.new('RGBA',source.size)
 for v in mapping:
  if v['sheet']!=filename:continue
  pi=v['page'];mid=v['metatile_id'];bank=mid//512;directory=P/'data/tilesets'/('secondary' if bank else 'primary')/f'unova_nuvema_original{pi}';refs=struct.unpack('<8H',(directory/'metatiles.bin').read_bytes()[(mid%512)*16:(mid%512+1)*16])
  for j,ref in enumerate(refs[:4]):
   ti=ref&1023;td=P/'data/tilesets'/('secondary' if ti>=512 else 'primary')/f'unova_nuvema_original{pi}';raw=(td/'tiles.4bpp').read_bytes()[(ti%512)*32:(ti%512+1)*32];pal=struct.unpack('<16H',(directory/f'palettes/{ref>>12:02}.gbapal').read_bytes());q=Image.new('RGBA',(8,8));q.putdata([((pal[n]&31)<<3,((pal[n]>>5)&31)<<3,((pal[n]>>10)&31)<<3,255 if n else 0) for b in raw for n in [b&15,b>>4]]);rebuilt.paste(q,(v['x']+j%2*8,v['y']+j//2*8))
 for c,got in zip(source.getdata(),rebuilt.getdata()):assert (not c[3] and not got[3]) or (c[3] and got[3] and tuple(x>>3 for x in c[:3])==tuple(x>>3 for x in got[:3]))
 rebuilt.save(OUT/(filename.replace('.png','-exact-GBA.png')))
print('Every opaque pixel from both complete sheets preserved and verified from serialized files.',checks,'pixel checks')
