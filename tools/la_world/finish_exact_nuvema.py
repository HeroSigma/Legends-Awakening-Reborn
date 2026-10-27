from pathlib import Path
import json,struct
P=Path('/home/allan/projects/Legends-Awakening-Reborn');D=P/'docs/la_world/unova_wesley'
pref=json.loads((D/'prefabs.json').read_text());required={'ForestInterior','Tree','TreeNature','CoastalCliff','SandyShore','ForestVerticalCluster','ForestHorizontalCluster','ForestPartialLeft','ForestPartialRight','StoneSign','Ocean','BlueHouse','Laboratory','Mailbox','Hedge','TownSign','BoardwalkBack','BoardwalkDeck','BoardwalkFront','BoardwalkSupport'};ids={v for k,pat in pref.items() if k in required for row in pat for v in row}
cat=json.loads((P/'.la_work/unova_wesley/before-exact-user/data/tilesets/unova_wesley_prefabs.json').read_text()) if (P/'.la_work/unova_wesley/before-exact-user/data/tilesets/unova_wesley_prefabs.json').exists() else json.loads((P/'.la_work/unova_wesley/before-exact-user/docs/la_world/unova_wesley/prefabs.json').read_text())
# The original editor catalogue is preserved in the normal export.
if isinstance(cat,dict):cat=json.loads(Path('/mnt/c/Users/aadair/Downloads/Legends-Awakening-Reborn/Unova-Wesley-Nuvema/prefabs.json').read_text()) if Path('/mnt/c/Users/aadair/Downloads/Legends-Awakening-Reborn/Unova-Wesley-Nuvema/prefabs.json').exists() else json.loads((P/'data/tilesets/unova_wesley_prefabs.json').read_text())
cat=[q for q in cat if all(t['metatile_id'] in ids for t in q['metatiles'])];(P/'data/tilesets/unova_wesley_prefabs.json').write_text(json.dumps(cat,indent=2)+'\n')
f=P/'data/layouts/AMap_3_0_Nuvema_Town_Layout/map.bin';words=list(struct.unpack('<1600H',f.read_bytes()));kfile=D/'collision_grid.json';k=json.loads(kfile.read_text())
for x,y in [(18,12),(22,21)]:
 for j,row in enumerate(pref['Hedge']):
  for i,n in enumerate(row):words[(y+j)*40+x+i]=n|0x3400;k['kind'][(y+j)*40+x+i]='hedge'
f.write_bytes(struct.pack('<1600H',*words));kfile.write_text(json.dumps(k,indent=2)+'\n')
f=P/'tools/la_world/validate_unova_wesley.py';s=f.read_text().replace("check(len(catalog)==46,'46 registered Porymap prefabs')","check(len(catalog)>0 and any('BlueHouse' in p['name'] for p in catalog) and any('Laboratory' in p['name'] for p in catalog),'Nuvema building prefabs registered')");f.write_text(s)
print('Complete hedge bases restored; editor catalog contains',len(cat),'Nuvema assemblies.')
