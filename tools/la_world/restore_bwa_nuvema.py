from pathlib import Path
import json,shutil,re,struct
P=Path('/home/allan/projects/Legends-Awakening-Reborn');old=P/'.la_work/unova_wesley/original';save=P/'.la_work/unova_wesley/archived-before-bwa-revert';save.mkdir(exist_ok=True)
rels=['data/maps/Unova_NuvemaTown/map.json','data/layouts/layouts.json','data/layouts/AMap_3_0_Nuvema_Town_Layout/map.bin','data/layouts/AMap_3_0_Nuvema_Town_Layout/border.bin','data/maps/Unova_Route1/map.json','src/fieldmap.c','data/scripts/la_teleport_scientist.inc']
for rel in rels:
 d=save/rel;d.parent.mkdir(parents=True,exist_ok=True)
 if not d.exists():shutil.copy2(P/rel,d)
layouts=json.loads((P/'data/layouts/layouts.json').read_text());original=json.loads((old/'data/layouts/layouts.json').read_text());lid='LAYOUT_AMAP_3_0_NUVEMA_TOWN_LAYOUT';layout=next(v for v in original['layouts'] if v['id']==lid)
layouts['layouts']=[layout if v['id']==lid else v for v in layouts['layouts']];(P/'data/layouts/layouts.json').write_text(json.dumps(layouts,indent=2)+'\n')
for rel in ['data/maps/Unova_NuvemaTown/map.json',layout['blockdata_filepath'],layout['border_filepath']]:shutil.copy2(old/rel,P/rel);assert (P/rel).read_bytes()==(old/rel).read_bytes()
rfile=P/'data/maps/Unova_Route1/map.json';route=json.loads(rfile.read_text());oldroute=json.loads((old/'data/maps/Unova_Route1/map.json').read_text());mapid='MAP_AMAP_3_0_NUVEMA_TOWN'
for c in route.get('connections',[]):
 if c['map']==mapid:
  oc=next(v for v in oldroute['connections'] if v['map']==mapid);c.update(oc)
rfile.write_text(json.dumps(route,indent=2)+'\n')
f=P/'src/fieldmap.c';s=f.read_text();s=s.replace('#include "unova_connection_blocks.inc"\n','');s=re.sub(r'    // Wesley Nuvema: extend each edge.*?\n    if \(mapLayout->isFrlg\)', '    if (mapLayout->isFrlg)',s,flags=re.S);s=re.sub(r'        // Each map keeps its own tileset; adapt only the visible connection strip\..*?\n        dest \+=', '        dest +=',s,flags=re.S);f.write_text(s)
f=P/'data/scripts/la_teleport_scientist.inc';f.write_text(f.read_text().replace('warp MAP_AMAP_3_0_NUVEMA_TOWN, 19, 23','warp MAP_AMAP_3_0_NUVEMA_TOWN, 16, 22'))
words=struct.unpack('<'+str((P/layout['blockdata_filepath']).stat().st_size//2)+'H',(P/layout['blockdata_filepath']).read_bytes());assert len(words)==layout['width']*layout['height'];arrival=words[22*layout['width']+16];assert arrival&0xC00==0,hex(arrival)
print('BWA Nuvema restored byte-for-byte:',layout['width'],layout['height'],layout['primary_tileset'],layout['secondary_tileset']);print('Route connection restored; Wesley border/connection hooks removed; travel arrival walkable.')
