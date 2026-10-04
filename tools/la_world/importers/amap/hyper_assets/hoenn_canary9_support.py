"""Reuse recovered extra graphics bank and story-switched geometry, never donor logic."""
import hashlib,json,re,struct,zipfile
from pathlib import Path
import port_hyper_assets as A
ROM_SHA=A.ROM_SHA
ALTERNATES={
 'LAYOUT_SOOTOPOLIS_CITY_LEGENDS_BATTLE':(357,'SootopolisCity'),
 'LAYOUT_ROUTE131_SKY_PILLAR':(319,'Route131'),
 **{f'LAYOUT_SKY_PILLAR_{i}F_CLEAN':(432+i,f'SkyPillar_{i}F') for i in range(1,6)},
 'LAYOUT_SKY_PILLAR_TOP_CLEAN':(438,'SkyPillar_Top')}
def extra_bank(root):
 key='secondary_08305DE0';base=Path('data/tilesets/secondary/hyper_secondary_08305de0');prior=root.parent/'Legends-Awakening/data/tilesets/secondary/amap_secondary_08305de0';export=root/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export/tilesets'/key
 raw=(export/'tiles.4bpp').read_bytes();padded=(prior/'tiles.4bpp').read_bytes();compressed=(prior/'tiles.4bpp.lz').read_bytes();assert padded.startswith(raw) and not any(padded[len(raw):]);assert A.decompress_lz(compressed)==padded;assert (prior/'metatiles.bin').read_bytes()==(export/'metatiles.bin').read_bytes()
 behaviors=A.enums(root/'include/constants/metatile_behaviors.h');names={x['source_id']:x['baseline_name'] for x in A.load(Path(__file__).parent/'reference/hyper_behavior_source_catalog.json')['behaviors']};attrs=A.u16s(export/'metatile_attributes.bin');translated=[(v&0xff00)|behaviors[names[v&255]] for v in attrs];files={str(base/p.name):p.read_bytes() for p in prior.iterdir() if p.is_file() and p.name!='metatile_attributes.bin'};files[str(base/'metatile_attributes.bin')]=struct.pack('<'+'H'*len(translated),*translated)
 for p in (prior/'palettes').iterdir():
  if p.is_file():files[str(base/'palettes'/p.name)]=p.read_bytes()
 for i in range(13):
  p=prior/f'palettes/{i:02}.gbapal';assert p.stat().st_size==32
  if not (export/f'palettes/{i:02}.pal').exists():continue
  rgb=[tuple(map(int,line.split())) for line in (export/f'palettes/{i:02}.pal').read_text().splitlines()[3:19]];assert struct.pack('<16H',*(a//8|b//8<<5|c//8<<10 for a,b,c in rgb))==p.read_bytes()
 symbol='Hyper_Secondary_08305DE0';graphics=f'\nconst u16 ALIGNED(4) gTilesetPalettes_{symbol}[][16] =\n{{\n'+''.join(f'    INCBIN_U16("{base}/palettes/{i:02}.gbapal"),\n' for i in range(13))+'};\n'+f'const u32 gTilesetTiles_{symbol}[] = INCBIN_U32("{base}/tiles.4bpp.lz");\n';meta=f'\nconst u16 gMetatiles_{symbol}[] = INCBIN_U16("{base}/metatiles.bin");\nconst u16 gMetatileAttributes_{symbol}[] = INCBIN_U16("{base}/metatile_attributes.bin");\n';header=f'\nconst struct Tileset gTileset_{symbol} = {{\n    .isCompressed = TRUE,\n    .isSecondary = TRUE,\n    .tiles = gTilesetTiles_{symbol},\n    .palettes = gTilesetPalettes_{symbol},\n    .metatiles = gMetatiles_{symbol},\n    .metatileAttributes = gMetatileAttributes_{symbol},\n    .callback = NULL,\n}};\n'
 assignments=A.load(root.parent/'Legends-Awakening/amap_tileset_animation_integration_report.json')['callback_assignments'];assert assignments.get('gTileset_AMap_Secondary_08305DE0','NULL')=='NULL'
 row={'source_id':key,'symbol':'gTileset_'+symbol,'path':str(base),'callback':'NULL','metadata':A.load(export/'tileset.json'),'source_graphics_sha256':hashlib.sha256(raw).hexdigest(),'recovered_graphics_sha256':hashlib.sha256(padded).hexdigest(),'translated_attributes_sha256':hashlib.sha256(files[str(base/'metatile_attributes.bin')]).hexdigest(),'prior_component':'Previously recovered Hyper Distortion/Ancient Retreat graphics bank'}
 return files,graphics,meta,header,row,translated

def alternate_layouts(root,layouts,files):
 archive=Path('/mnt/c/Users/aadair/Downloads/HypEm v5.7 EN+QoL.zip');blob=zipfile.ZipFile(archive).read('HypEm v5.7 EN+QoL.gba');assert hashlib.sha256(blob).hexdigest()==ROM_SHA;manifest=A.load(root/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export/manifest.json');known={m['layout_id']:int(m['layout_pointer'],16) for m in manifest['maps']};table=0xcfd124;assert sum(struct.unpack_from('<I',blob,table+(k-1)*4)[0]==v for k,v in known.items())==804
 rows=[]
 for lid,(idx,owner) in ALTERNATES.items():
  l=next(z for z in layouts if z['id']==lid);ptr=struct.unpack_from('<I',blob,table+(idx-1)*4)[0];w,h,border,blocks,primary,secondary=struct.unpack_from('<IIIIII',blob,ptr-0x08000000);assert (w,h)==(l['width'],l['height']);path=Path('data/hyper_assets/canary9_layouts')/lid
  l.update(primary_tileset=f'gTileset_Hyper_Primary_{primary:08X}',secondary_tileset=f'gTileset_Hyper_Secondary_{secondary:08X}',border_filepath=str(path/'border.bin'),blockdata_filepath=str(path/'map.bin'));files[l['border_filepath']]=blob[border-0x08000000:border-0x08000000+8];files[l['blockdata_filepath']]=blob[blocks-0x08000000:blocks-0x08000000+w*h*2]
  rows.append({'canonical_layout':lid,'native_owner':owner,'donor_layout_index':idx,'donor_layout_pointer':f'0x{ptr:08X}','width':w,'height':h,'primary_tileset':l['primary_tileset'],'secondary_tileset':l['secondary_tileset'],'blockdata_sha256':hashlib.sha256(files[l['blockdata_filepath']]).hexdigest(),'reason':'Native story callback keeps canonical layout identity and state; only referenced Hyper geometry/assets are copied.'})
 return rows

def semantic_cells(root,maps,layouts,grids,header,metatiles,files,derivatives,patches):
 ids={m['id']:n for n,m in maps.items()};requests={};counts={}
 for n,m in maps.items():
  if n not in grids:continue
  g=grids[n]
  for co in m['connections'] or []:
   if co['direction'] not in ['dive','emerge'] or ids.get(co['map']) not in grids:continue
   dn=ids[co['map']];dg=grids[dn]
   for y in range(g.h):
    for x in range(g.w):
     v=g.cell(x,y)
     if v['collision']:continue
     dv=dg.cell(x,y);wanted=None;reason=''
     if co['direction']=='dive' and v['translated_behavior'] in [0x11,0x12,0x14] and dv['collision']:
      wanted=0x15;reason='Reviewed Dive pair would land inside donor underwater wall; retain identical Surfable artwork with ocean behavior.'
     if co['direction']=='emerge' and v['translated_behavior'] not in [0x19,0x2A,0x6C] and (dv['collision'] or dv['translated_behavior'] not in [0x10,0x11,0x12,0x13,0x14,0x15]):
      wanted=0x2A if v['translated_behavior']==0x22 else 0x19;reason='Reviewed emerge pair has blocked/nonwater surface above; identical underwater artwork uses native no-surfacing behavior.'
     if wanted is not None:requests.setdefault(n,[]).append((x,y,wanted,reason))
 for n,rows in requests.items():
  g=grids[n];l=next(z for z in layouts if z['id']==maps[n]['layout']);meta=[]
  for role in ['primary_tileset','secondary_tileset']:
   body=re.search(r'const struct Tileset\s+'+l[role]+r'\s*=\s*\{(.*?)\};',header,re.S)[1];sy=re.search(r'\.metatiles\s*=\s*(\w+)',body)[1];path=re.search(re.escape(sy)+r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"\)',metatiles)[1];meta.append(files[path] if path in files else (root/path).read_bytes())
  base=l['secondary_tileset'];body=re.search(r'const struct Tileset\s+'+base+r'\s*=\s*\{(.*?)\};',header,re.S)[1];attrs=list(g.attrs[1]);out=bytearray(meta[1]);used={v&1023 for v in g.blocks};border=files.get(l['border_filepath']) or (root/l['border_filepath']).read_bytes();used.update(v&1023 for v in struct.unpack('<'+'H'*(len(border)//2),border));free=[i for i in reversed(range(min(len(attrs),len(out)//16))) if i+512 not in used];cache={}
  for x,y,want,reason in rows:
   v=g.cell(x,y);tile=v['metatile'];key=(tile,want)
   if key not in cache:
    assert free;idx=free.pop();cache[key]=idx+512;attrs[idx]=(g.attrs[tile//512][tile%512]&0xff00)|want;out[idx*16:idx*16+16]=meta[tile//512][(tile%512)*16:(tile%512+1)*16]
   after=(v['block']&0xfc00)|cache[key];g.blocks[y*g.w+x]=after;patches.append({'map':n,'x':x,'y':y,'before':v['block'],'after':after,'reason':reason})
  name='gTileset_Hyper_Canary9_'+n+'_Dive';ms='gMetatiles_Hyper_Canary9_'+n+'_Dive';ats='gMetatileAttributes_Hyper_Canary9_'+n+'_Dive';mp=f'data/hyper_assets/canary9_layouts/{n}/dive_metatiles.bin';ap=f'data/hyper_assets/canary9_layouts/{n}/dive_attributes.bin';body=re.sub(r'(\.metatiles\s*=\s*)\w+',lambda m:m[1]+ms,body);body=re.sub(r'(\.metatileAttributes\s*=\s*)\w+',lambda m:m[1]+ats,body);header+='\nconst struct Tileset '+name+' = {'+body+'};\n';metatiles+=f'\nconst u16 {ms}[] = INCBIN_U16("{mp}");\nconst u16 {ats}[] = INCBIN_U16("{ap}");\n';files[mp]=bytes(out);files[ap]=struct.pack('<'+'H'*len(attrs),*attrs);l['secondary_tileset']=name;derivatives[name]={'base':base,'attributes_path':ap,'metatiles_path':mp};g.attrs[1]=attrs;files[l['blockdata_filepath']]=struct.pack('<'+'H'*len(g.blocks),*g.blocks);counts[n]=len(rows)
 return header,metatiles,counts
