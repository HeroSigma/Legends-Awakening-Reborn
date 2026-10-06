"""Repair project-owned static Johto travel without donor gameplay scripts."""
import json,struct,sys
from pathlib import Path
from port_gs_johto import enums
R=Path(__file__).resolve().parents[4]
def main():
 n=enums(R/'include/constants/metatile_behaviors.h')
 layouts={l['id']:l for l in json.loads((R/'data/layouts/layouts.json').read_text())['layouts']}
 rows=[];used={};banks={};ledger=[]
 for p in (R/'data/maps').glob('GSJohto_*/map.json'):
  m=json.loads(p.read_text());l=layouts[m['layout']];keys=[l[k].replace('gTileset_GSJohto_','') for k in ['primary_tileset','secondary_tileset']]
  data=bytearray((R/l['blockdata_filepath']).read_bytes());rows.append((m,l,keys,data))
  for blob in [data,(R/l['border_filepath']).read_bytes()]:
   for v, in struct.iter_unpack('<H',blob):used.setdefault(keys[(v&1023)//512],set()).add(v&511)
 for key in used:
  root=R/'data/gs_johto_assets/tilesets'/key;attrs=bytearray((root/'metatile_attributes.bin').read_bytes());meta=bytearray((root/'metatiles.bin').read_bytes());raw=(root/'source_frlg_metatile_attributes.bin').read_bytes()
  for i in range(512):
   v=struct.unpack_from('<I',raw,i*4)[0]&511
   name={0x60:'MB_NON_ANIMATED_DOOR',0x69:'MB_ANIMATED_DOOR',0x67:'MB_NON_ANIMATED_DOOR'}.get(v)
   if name:struct.pack_into('<H',attrs,i*2,(struct.unpack_from('<H',attrs,i*2)[0]&0xf000)|n[name])
  if key.endswith('P082D4A94S082D4B9C'):
   for i in [0x47,0xca,0xc9,0xd4]:struct.pack_into('<H',attrs,i*2,(struct.unpack_from('<H',attrs,i*2)[0]&0xf000)|n['MB_WEST_ARROW_WARP'])
  if key=='primary_f2e_GS_CHRONICLES_276_082D4A94':
   for i in [0x15b,0x15f,0x15c,0x162]:struct.pack_into('<H',attrs,i*2,(struct.unpack_from('<H',attrs,i*2)[0]&0xf000)|n['MB_WEST_ARROW_WARP' if i in [0x15b,0x15f] else 'MB_EAST_ARROW_WARP'])
  banks[key]=(root,attrs,meta)
 seam=json.loads((R/'docs/la_world/gs_johto/goldenrod_seam_fix.json').read_text());clones={}
 for m,l,keys,data in rows:
  for z in seam:
   if z['map']==m['name']:struct.pack_into('<H',data,(z['y']*l['width']+z['x'])*2,int(z['before'],16))
  warps={(z['x'],z['y']) for z in m['warp_events']}
  for z in m['warp_events']:
   off=(z['y']*l['width']+z['x'])*2;v=struct.unpack_from('<H',data,off)[0];mid=v&1023;key=keys[mid//512];root,attrs,meta=banks[key];beh=struct.unpack_from('<H',attrs,(mid%512)*2)[0]&255
   if beh in [n['MB_NORMAL'],n['MB_CAVE'],n['MB_IMPASSABLE_NORTHEAST']]:
    pair=(key,mid%512);slot=clones.get(pair)
    if slot is None:
     slot=next(i for i in range(511,-1,-1) if i not in used[key]);used[key].add(slot);clones[pair]=slot
     meta[slot*16:slot*16+16]=meta[(mid%512)*16:(mid%512)*16+16]
     struct.pack_into('<H',attrs,slot*2,(struct.unpack_from('<H',attrs,(mid%512)*2)[0]&0xf000)|n['MB_NON_ANIMATED_DOOR'])
    v=(v&0xfc00)|(mid//512*512+slot)
   new=(v&0x3ff)|0x3000;struct.pack_into('<H',data,off,new);ledger.append(dict(map=m['name'],x=z['x'],y=z['y'],entry=hex(new)))
  # Non-warp outdoor stairs use ordinary ground traversal, matching Hyper assets.
  if keys[0]=='primary_f2e_GS_CHRONICLES_276_082D4A94':
   for i,(v,) in enumerate(struct.iter_unpack('<H',bytes(data))):
    mid=v&1023
    if mid in [0x15b,0x15f,0x15c,0x162] and (i%l['width'],i//l['width']) not in warps and v>>10&3==0:
     pair=(keys[0],mid,'floor');slot=clones.get(pair);root,attrs,meta=banks[keys[0]]
     if slot is None:
      slot=next(j for j in range(511,-1,-1) if j not in used[keys[0]]);used[keys[0]].add(slot);clones[pair]=slot;meta[slot*16:slot*16+16]=meta[mid*16:mid*16+16];struct.pack_into('<H',attrs,slot*2,struct.unpack_from('<H',attrs,mid*2)[0]&0xf000)
     struct.pack_into('<H',data,i*2,slot)
  (R/l['blockdata_filepath']).write_bytes(data)
 for root,attrs,meta in banks.values():(root/'metatile_attributes.bin').write_bytes(attrs);(root/'metatiles.bin').write_bytes(meta)
 (R/'docs/la_world/gs_johto/travel_repair.json').write_text(json.dumps(dict(warps=ledger,cloned_metatiles=len(clones)),indent=2)+'\n');print('Repaired',len(ledger),'static warp cells;',len(clones),'scoped art-preserving tiles')
if __name__=='__main__':main()
