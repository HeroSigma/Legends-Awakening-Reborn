"""Reuse validated prior assets for additional regions; no script extraction."""
import hashlib,re,struct
import port_hyper_assets as A

def recover(root,keys,catalog):
 old=root.parent/'Legends-Awakening';donor=root/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export';files={};rows=[];headers=[];graphics=[];metatiles=[];assignments=A.load(old/'amap_tileset_animation_integration_report.json')['callback_assignments'];source_names={x['source_id']:x['baseline_name'] for x in A.load(__import__('pathlib').Path(__file__).parent/'reference/hyper_behavior_source_catalog.json')['behaviors']};target=A.enums(root/'include/constants/metatile_behaviors.h')
 for key in sorted(keys):
  role,addr=key.split('_');prior=old/f'data/tilesets/{role}/amap_{key.lower()}';export=donor/'tilesets'/key;base=__import__('pathlib').Path(f'data/tilesets/{role}/hyper_{key.lower()}');raw=(export/'tiles.4bpp').read_bytes();padded=(prior/'tiles.4bpp').read_bytes();compressed=(prior/'tiles.4bpp.lz').read_bytes();assert padded.startswith(raw) and not any(padded[len(raw):]);assert A.decompress_lz(compressed)==padded;assert (prior/'metatiles.bin').read_bytes().startswith((export/'metatiles.bin').read_bytes());assert A.u16s(prior/'metatile_attributes.bin')==A.u16s(export/'metatile_attributes.bin') or len(A.u16s(prior/'metatile_attributes.bin'))>=len(A.u16s(export/'metatile_attributes.bin'))
  attrs=[]
  sourceattrs=A.u16s(export/'metatile_attributes.bin');oldnames={v:k for k,v in A.enums(old/'include/constants/metatile_behaviors.h').items()}
  for index,v in enumerate(A.u16s(prior/'metatile_attributes.bin')):
   sourcevalue=sourceattrs[index]&255 if index<len(sourceattrs) else v&255
   v=(v&0xff00)|sourcevalue
   assert v&255 not in [0x1f,0x2d],(key,'Unreviewed custom behavior');name=source_names.get(sourcevalue,oldnames.get(v&255));assert name in target;attrs.append((v&0xff00)|target[name])
  for p in prior.rglob('*'):
   if p.is_file():files[str(base/p.relative_to(prior))]=p.read_bytes()
  files[str(base/'metatile_attributes.bin')]=struct.pack('<'+'H'*len(attrs),*attrs)
  sym='Hyper_'+role.title()+'_'+addr;cb=assignments.get('gTileset_AMap_'+role.title()+'_'+addr,'NULL').replace('AMap','HyperAsset');graphics.append(f'const u16 ALIGNED(4) gTilesetPalettes_{sym}[][16] =\n{{\n'+''.join(f'    INCBIN_U16("{base}/palettes/{i:02}.gbapal"),\n' for i in range(13))+'};\n'+f'const u32 gTilesetTiles_{sym}[] = INCBIN_U32("{base}/tiles.4bpp.lz");\n');metatiles.append(f'const u16 gMetatiles_{sym}[] = INCBIN_U16("{base}/metatiles.bin");\nconst u16 gMetatileAttributes_{sym}[] = INCBIN_U16("{base}/metatile_attributes.bin");\n');headers.append(f'const struct Tileset gTileset_{sym} = {{\n .isCompressed = TRUE,\n .isSecondary = {"FALSE" if role=="primary" else "TRUE"},\n .tiles = gTilesetTiles_{sym},\n .palettes = gTilesetPalettes_{sym},\n .metatiles = gMetatiles_{sym},\n .metatileAttributes = gMetatileAttributes_{sym},\n .callback = {cb},\n}};\n')
  for i in range(13):
   pal=prior/f'palettes/{i:02}.gbapal';assert pal.stat().st_size==32 and pal.with_suffix('.pal').exists()
   if (export/f'palettes/{i:02}.pal').exists():
    rgb=[tuple(map(int,l.split())) for l in (export/f'palettes/{i:02}.pal').read_text().splitlines()[3:19]];assert struct.pack('<16H',*(a//8|b//8<<5|c//8<<10 for a,b,c in rgb))==pal.read_bytes()
  rows.append({'source_id':key,'symbol':'gTileset_'+sym,'path':str(base),'callback':cb,'metadata':A.load(export/'tileset.json'),'source_graphics_sha256':hashlib.sha256(raw).hexdigest(),'recovered_graphics_sha256':hashlib.sha256(padded).hexdigest(),'translated_attributes_sha256':hashlib.sha256(files[str(base/'metatile_attributes.bin')]).hexdigest(),'prior_component':'Previously proven Hyper Sinnoh asset bank'})
 for name,lines in [('headers',headers),('graphics',graphics),('metatiles',metatiles)]:files[f'src/data/tilesets/{name}.h']=((root/f'src/data/tilesets/{name}.h').read_text()+'\n/* Additional recovered Hyper asset banks. */\n'+''.join(lines)).encode()
 callbacks=sorted({x['callback'].replace('HyperAsset','AMap') for x in catalog['tilesets']+rows if x['callback'].startswith('InitTilesetAnim_HyperAsset_')});runtime,summary=A.runtime_subset((old/'src/amap_tileset_anims_generated.inc').read_text(),callbacks);files['src/hyper_tileset_anims.inc']=runtime.encode();files['include/hyper_tileset_anims.h']=('#ifndef GUARD_HYPER_TILESET_ANIMS_H\n#define GUARD_HYPER_TILESET_ANIMS_H\n'+''.join(f'void {c.replace("AMap","HyperAsset")}(void);\n' for c in callbacks)+'#endif\n').encode()
 return files,rows,summary
