from pathlib import Path
import subprocess,struct,json,hashlib
P=Path(__file__).resolve().parents[2];rom=(P/'pokeemerald.gba').read_bytes();syms={}
for line in subprocess.check_output(['arm-none-eabi-nm','--defined-only',str(P/'pokeemerald.elf')],text=True).splitlines():
 z=line.split()
 if len(z)==3:syms[z[2]]=int(z[0],16)
def blob(name,size):
 i=syms[name]-0x8000000;assert 0<=i<i+size<=len(rom);return rom[i:i+size]
def lz(name):
 i=syms[name]-0x8000000;assert rom[i]==16;size=int.from_bytes(rom[i+1:i+4],'little');i+=4;out=bytearray()
 while len(out)<size:
  flags=rom[i];i+=1
  for bit in range(7,-1,-1):
   if flags&(1<<bit):
    a,b=rom[i:i+2];i+=2;length=(a>>4)+3;back=((a&15)<<8|b)+1
    for _ in range(length):out.append(out[-back])
   else:out.append(rom[i]);i+=1
   if len(out)>=size:break
 return bytes(out[:size])
for dirname,name in [('primary/unova_general','UnovaGeneral_Primary'),('secondary/unova_nuvema','UnovaNuvema_Secondary')]:
 d=P/'data/tilesets'/dirname
 assert lz('gTilesetTiles_'+name)==(d/'tiles.4bpp').read_bytes()
 for prefix,file in [('gMetatiles_','metatiles.bin'),('gMetatileAttributes_','metatile_attributes.bin')]:
  raw=(d/file).read_bytes();assert blob(prefix+name,len(raw))==raw
 palettes=b''.join((d/'palettes'/f'{i:02}.gbapal').read_bytes() for i in range(16));assert blob('gTilesetPalettes_'+name,len(palettes))==palettes
for suffix,filename in [('Blockdata','map.bin'),('Border','border.bin')]:
 raw=(P/'data/layouts/AMap_3_0_Nuvema_Town_Layout'/filename).read_bytes();assert blob('AMap_3_0_Nuvema_Town_Layout_'+suffix,len(raw))==raw
for i in range(4):assert blob(f'sUnovaOceanFrame{i}',512)==(P/f'data/tilesets/primary/unova_general/anim/water/{i}.4bpp').read_bytes()
for s in ['InitTilesetAnim_UnovaGeneral','sUnovaRoute1BoundaryToNuvema','sUnovaNuvemaBoundaryToRoute1']:assert s in syms
v=json.loads((P/'docs/la_world/unova_wesley/validation.json').read_text());v['linked_rom_assets_verified']=True;v['rom_sha256']=hashlib.sha256(rom).hexdigest();(P/'docs/la_world/unova_wesley/validation.json').write_text(json.dumps(v,indent=2)+'\n');print('PASS: linked ROM graphics, metatiles, attributes, palettes and four ocean frames match source assets byte-for-byte.')

