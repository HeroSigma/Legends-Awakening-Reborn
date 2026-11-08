"""Source-native HnS asset conversion, graph-scoped animation and sprite recovery."""
from pathlib import Path
import json,re,struct,hashlib,subprocess
from PIL import Image
from stage_hns_canary import graphics,png
from hyper_assets.port_hyper_assets import enums
R=Path(__file__).resolve().parents[4]
S=Path('/home/allan/la-scratch/pokehns-canary-source')
A=R/'data/hns_region_assets'
def palette(p):
 lines=p.read_text().splitlines();rgb=[list(map(int,line.split())) for line in lines[3:] if line.strip()]
 assert 0<len(rgb)<=16,(p,len(rgb))
 rgb += [[0,0,0]]*(16-len(rgb))
 return b''.join(struct.pack('<H',(a>>3)|((b>>3)<<5)|((c>>3)<<10)) for a,b,c in rgb)
def dump(p,x):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+'\n')
def blob(p,b):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def c_defs(text):
 """Read constant initializers, preserving original source snippets."""
 result={}
 pattern=r'(?m)^(?:static\s+)?const\s+[^\n;=]+?\b(\w+)\s*(?:\[[^\]]*\]\s*)*\s*=\s*'
 for m in re.finditer(pattern,text):
  start=m.end()
  if text[start:start+1]=='{':
   depth=1;i=start+1
   while depth:
    depth+=(text[i]=='{')-(text[i]=='}');i+=1
   end=text.index(';',i)+1
  else:end=text.index(';',start)+1
  result[m[1]]=text[m.start():end]
 return result
def functions(text):
 result={}
 pattern=r'(?m)^(?:static\s+)?(?:void|u8|u16|u32|s8|s16|s32|bool8|bool32)\s+(\w+)\s*\([^;{]*\)\s*\{'
 for m in re.finditer(pattern,text):
  depth=1;i=m.end()
  while depth:
   depth+=(text[i]=='{')-(text[i]=='}');i+=1
  result[m[1]]=text[m.start():i]
 return result
def tokens(text):return set(re.findall(r'\b[A-Za-z_]\w*\b',text))
class AssetPort:
 def __init__(self):
  self.header=(S/'src/data/tilesets/headers.h').read_text()
  self.gfx=(S/'src/data/tilesets/graphics.h').read_text()+(S/'src/graphics.c').read_text()
  self.source={};self.banks={};self.decls={'headers':'','graphics':'','metatiles':''}
  self.native=enums(R/'include/constants/metatile_behaviors.h')
  self.donor={v:k for k,v in enums(S/'include/constants/metatile_behaviors.h').items()}
  self.aliases={'MB_HEADBUTT_TREE':'MB_NORMAL','MB_BOOKSHELF_GREEN':'MB_BOOKSHELF','MB_SHOP_SHELF_DEPARTMENT':'MB_SHOP_SHELF','MB_SHOP_SHELF_DEPARTMENT_FORWARD':'MB_SHOP_SHELF','MB_TALL_GRASS_IMPASSABLE_NORTH':'MB_TALL_GRASS','MB_CAVE_IMPASSABLE_NORTH':'MB_CAVE','MB_WATER_NORTH_ARROW_WARP':'MB_NORTH_ARROW_WARP','MB_BRIDGE_OVER_ICE':'MB_BRIDGE_OVER_POND_LOW'}
  self.behaviors=[];self.callbacks={512:set(),640:set()};self.payloads={}
 def source_bank(self,k):
  if k in self.source:return self.source[k]
  body=re.search(r'const struct Tileset '+re.escape(k)+r'\s*=\s*\{.*?\};',self.header,re.S)[0]
  sym=re.search(r'\.tiles\s*=\s*(\w+)',body)[1]
  match=re.search(re.escape(sym)+r'\[\].*?"([^"]+)"',self.gfx,re.S)
  assert match,(k,sym)
  path=match[1]
  folder=S/Path(path).parent
  raw=(folder/'metatile_attributes.bin').read_bytes()
  assert len(raw)%2==0
  attrs=[]
  for i,(v,) in enumerate(struct.iter_unpack('<H',raw)):
   code=v&255;label=self.donor.get(code,'UNUSED_PADDING_'+str(code))
   target='MB_NORMAL' if label.startswith('UNUSED_PADDING_') else self.aliases.get(label,label)
   assert target in self.native,(k,i,label,target)
   attrs.append((v&0xf000)|self.native[target])
   if target!=label:self.behaviors.append(dict(bank=k,index=i,source=label,target=target))
  result=dict(folder=folder,tiles=graphics(folder/'tiles.png'),defs=(folder/'metatiles.bin').read_bytes(),attrs=attrs,callback=re.search(r'\.callback\s*=\s*(\w+)',body)[1])
  self.source[k]=result;return result
 def payload(self,b,kind):
  digest=hashlib.sha256(b).hexdigest();key=(digest,kind)
  if key in self.payloads:return self.payloads[key]
  sym='gHnsRegion_'+kind+'_'+digest[:20];folder=A/'shared'/sym;folder.mkdir(parents=True,exist_ok=True)
  if kind=='Tiles':
   path=folder/'tiles.4bpp';blob(path,b);png(b,folder/'tiles.png')
   subprocess.run([str(R/'tools/gbagfx/gbagfx'),str(path),str(path)+'.lz'],check=True)
   path=Path(str(path)+'.lz');ctype='u32';inc='U32'
  else:path=folder/'data.bin';blob(path,b);ctype='u16';inc='U16'
  decl=f'const {ctype} {sym}[] = INCBIN_{inc}("{path.relative_to(R).as_posix()}");\n'
  self.decls['graphics' if kind=='Tiles' else 'metatiles']+=decl
  result=dict(symbol=sym,path=path.relative_to(R).as_posix(),raw_sha256=digest)
  self.payloads[key]=result;return result
 def bank(self,primary,secondary,base,role):
  key=(primary,secondary if role else '',base,role)
  if key in self.banks:return self.banks[key]
  p=self.source_bank(primary);s=self.source_bank(secondary) if role else None
  if role:
   tiles=p['tiles'][512*32:base*32].ljust((base-512)*32,b'\0')+s['tiles']
   defs=p['defs'][512*16:base*16].ljust((base-512)*16,b'\0')+s['defs']
   attrs=p['attrs'][512:base]+s['attrs']
   pals=[p['folder']/'palettes'/f'{i:02}.pal' if i<(7 if base==640 else 6) else s['folder']/'palettes'/f'{i:02}.pal' for i in range(16)]
   cb=s['callback']
  else:
   tiles=p['tiles'][:512*32];defs=p['defs'][:512*16];attrs=p['attrs'][:512];pals=[p['folder']/'palettes'/f'{i:02}.pal' for i in range(16)];cb=p['callback']
  # A map block and tile entry each address only 1024 slots. Source sheets may contain unused trailing art.
  tiles=tiles[:512*32];defs=defs[:512*16]
  tiles=tiles.ljust(512*32,b'\0');defs=defs.ljust(512*16,b'\0');attrs=(attrs+[0]*512)[:512];converted=bytearray()
  for i,v in enumerate(attrs):
   lo=list(struct.unpack_from('<4H',defs,i*16));hi=list(struct.unpack_from('<4H',defs,i*16+8));layer=v>>12
   out=([0x3014]*4+lo+hi) if layer==0 else (lo+[0]*4+hi) if layer==2 else (lo+hi+[0]*4)
   converted.extend(struct.pack('<12H',*out))
  t=self.payload(tiles,'Tiles');mt=self.payload(bytes(converted),'Metatiles');at=self.payload(struct.pack('<512H',*[v&0xfff for v in attrs]),'Attributes')
  identifier='B'+hashlib.sha256(repr(key).encode()).hexdigest()[:16];sym='gTileset_HnsRegion_'+identifier
  folder=A/'banks'/identifier;(folder/'palettes').mkdir(parents=True,exist_ok=True);palraw=b'';paths=[]
  for i,path in enumerate(pals):
   dest=folder/'palettes'/f'{i:02}.pal'
   text=path.read_text() if path.exists() else 'JASC-PAL\n0100\n16\n'+'0 0 0\n'*16
   dest.write_text(text);b=palette(path) if path.exists() else bytes(32);blob(dest.with_suffix('.gbapal'),b);palraw+=b;paths.append(dest.with_suffix('.gbapal'))
  psym='gHnsRegion_'+identifier+'_Palettes'
  self.decls['graphics']+=f'const u16 {psym}[][16] = {{\n'+''.join(f' INCBIN_U16("{x.relative_to(R).as_posix()}"),\n' for x in paths)+'};\n'
  if cb!='NULL':self.callbacks[base].add(cb);callback=f'HnsRegion{base}_{cb}';self.decls['headers']+=f'void {callback}(void);\n'
  else:callback='NULL'
  self.decls['headers']+=f'const struct Tileset {sym} = {{.isCompressed=TRUE, .isSecondary={"TRUE" if role else "FALSE"}, .tiles={t["symbol"]}, .palettes={psym}, .metatiles={mt["symbol"]}, .metatileAttributes={at["symbol"]}, .callback={callback}}};\n'
  result=dict(symbol=sym,identifier=identifier,path=str(folder.relative_to(R)),primary=primary,secondary=secondary if role else None,base=base,role='secondary' if role else 'primary',tiles=t,metatiles=mt,attributes=at,palette_symbol=psym,callback=callback)
  self.banks[key]=result;return result
 def animations(self):
  source=(S/'src/tileset_anims.c').read_text();fn=functions(source);const=c_defs(source)
  # Some vanilla frame arrays are declared in graphics.c; port only dependencies.
  const.update(c_defs((S/'src/graphics.c').read_text()))
  output='/* Graphical callbacks only, recovered from pinned HnS source. */\n';closure_report={}
  for base,roots in self.callbacks.items():
   needed=set();data=set();data_order=[]
   def walk(name):
    if name in needed:return
    needed.add(name)
    for token in tokens(fn[name]):
     if token in fn and token!='AppendTilesetAnimToBuffer':walk(token)
     if token in const:walkdata(token)
   def walkdata(name):
    if name in data:return
    data.add(name)
    for token in tokens(const[name]):
     if token!=name and token in const:walkdata(token)
    data_order.append(name)
   for name in sorted(roots):walk(name)
   names=needed|data;prefix=f'HnsRegion{base}_'
   def rename(text):
    for token in sorted(names,key=len,reverse=True):text=re.sub(r'\b'+re.escape(token)+r'\b',prefix+token,text)
    text=text.replace('sSecondaryTilesetBaseTile',str(base))
    text=text.replace('GetNumTilesInPrimary(gMapHeader.mapLayout)',str(base)).replace('NUM_TILES_IN_PRIMARY',str(base))
    return text
   # Preserve source order, with prototypes before every frame declaration.
   for name in sorted(needed):
    signature=fn[name][:fn[name].index('{')].strip();output+=rename(signature)+';\n'
   for name in data_order:
    text=const[name]
    for path in re.findall(r'"([^"]+\.(?:4bpp|gbapal))"',text):
     out=A/'animations'/Path(path)
     if not out.exists():
      if path.endswith('.4bpp'):blob(out,graphics((S/path).with_suffix('.png')))
      else:blob(out,palette((S/path).with_suffix('.pal')))
     text=text.replace(path,str(out.relative_to(R)))
    output+=rename(text)+'\n'
   for name in fn:
    if name in needed:output+=rename(fn[name])+'\n'
   closure_report[base]=dict(callbacks=sorted(roots),functions=len(needed),arrays=len(data))
  return output,closure_report
