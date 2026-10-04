"""Keep Hyper portal artwork and give static project warps native behavior, in map-local banks."""
import re,struct

def integrate(root, maps, layouts, extras, grids, header, metatiles, files, derivatives, patches, stage="canary5"):
 for n in extras.values():
  m=maps[n];l=next(x for x in layouts if x['id']==m['layout']);g=grids[n];a=g.attrs;body=re.search(r'const struct Tileset\s+'+l['secondary_tileset']+r'\s*=\s*\{(.*?)\};',header,re.S)[1]
  def binary(role):
   b=re.search(r'const struct Tileset\s+'+l[role]+r'\s*=\s*\{(.*?)\};',header,re.S)[1];sy=re.search(r'\.metatiles\s*=\s*(\w+)',b)[1];p=re.search(re.escape(sy)+r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"\)',metatiles)[1];return files[p] if p in files else (root/p).read_bytes()
  metas=[binary('primary_tileset'),binary('secondary_tileset')];newattrs=list(a[1]);newmeta=bytearray(metas[1]);cache={};border=files.get(l['border_filepath'],(root/l['border_filepath']).read_bytes() if (root/l['border_filepath']).exists() else b'');borderwords=struct.unpack('<'+'H'*(len(border)//2),border);used={v&1023 for v in [*g.blocks,*borderwords]};free=[i for i in reversed(range(min(len(newattrs),len(newmeta)//16))) if i+512 not in used]
  for e in m['warp_events']:
   at=e['y']*g.w+e['x'];v=g.blocks[at];tile=v&1023;attr=a[tile//512][tile%512];mb=attr&255
   if mb in [0x29,*range(0x60,0x70)]:continue
   want=0x67 if n=='AquaHideout_B1F' else (0x6D if m['map_type']=='MAP_TYPE_UNDERWATER' else 0x60);key=(tile,want)
   if key not in cache:
    assert free,(n,'No unused metatile for local portal behavior');idx=free.pop(0);cache[key]=idx+512;newattrs[idx]=(attr&0xFF00)|want;newmeta[idx*16:idx*16+16]=metas[tile//512][(tile%512)*16:(tile%512+1)*16]
   g.blocks[at]=(v&0xF000)|cache[key];patches.append({'map':n,'x':e['x'],'y':e['y'],'before':v,'after':g.blocks[at],'reason':'Static project-owned portal uses duplicated identical Hyper artwork in an otherwise unused map-local metatile slot with native warp behavior; donor gameplay callback not copied.'})
  if not cache:continue
  base=l['secondary_tileset'];tag=stage.replace('canary','Canary');derived='gTileset_Hyper_'+tag+'_'+n+'_Portals';ms='gMetatiles_Hyper_'+tag+'_'+n+'_Portals';ats='gMetatileAttributes_Hyper_'+tag+'_'+n+'_Portals';folder='data/hyper_assets/'+stage+'_layouts/'+n;mp=folder+'/portal_metatiles.bin';ap=folder+'/portal_attributes.bin';body=re.sub(r'(\.metatiles\s*=\s*)\w+',lambda x:x[1]+ms,body);body=re.sub(r'(\.metatileAttributes\s*=\s*)\w+',lambda x:x[1]+ats,body);header+='\nconst struct Tileset '+derived+' = {'+body+'};\n';metatiles+='\nconst u16 '+ms+'[] = INCBIN_U16("'+mp+'");\nconst u16 '+ats+'[] = INCBIN_U16("'+ap+'");\n';files[mp]=bytes(newmeta);files[ap]=struct.pack('<'+'H'*len(newattrs),*newattrs);files[l['blockdata_filepath']]=struct.pack('<'+'H'*len(g.blocks),*g.blocks);l['secondary_tileset']=derived;g.attrs[1]=newattrs;derivatives[derived]={'base':base,'attributes_path':ap,'metatiles_path':mp}
 return header,metatiles
