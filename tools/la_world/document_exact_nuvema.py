from pathlib import Path
import json
P=Path('/home/allan/projects/Legends-Awakening-Reborn');D=P/'docs/la_world/unova_wesley';r=json.loads((D/'report.json').read_text());r['limitations']=['Source colours are preserved after the required RGB888-to-RGB555 hardware conversion; no palette reduction or nearest-colour substitution for packed Nuvema art.','Original reference shoreline and repeating boardwalk supply pieces missing from the user sheet.','Unused city stairs, fences, rocks and other previous prefabs are not packed in the Nuvema pair; original source sheets remain intact.','Interior warps are not yet activated.'];(D/'report.json').write_text(json.dumps(r,indent=2)+'\n')
pref=json.loads((D/'prefabs.json').read_text());f=P/'data/tilesets/unova_wesley_prefabs.json';cat=json.loads(f.read_text());names={v['name'] for v in cat}
for name in ['Tree','TreeNature','Grass','ForestInterior','BlueHouse','Laboratory','Hedge','Mailbox','TownSign','StoneSign','Ocean']:
 if name=='Grass':pat=[[0]]
 else:pat=pref[name]
 title='Unova - '+name
 if title in names:continue
 cat.append({'name':title,'width':len(pat[0]),'height':len(pat),'primary_tileset':'gTileset_UnovaGeneral_Primary','secondary_tileset':'gTileset_UnovaNuvema_Secondary','metatiles':[{'x':x,'y':y,'metatile_id':n,'collision':0 if name in ['Grass','Ocean'] or (name=='BlueHouse' and (x,y)==(2,5)) or (name=='Laboratory' and (x,y)==(5,6)) else 1,'elevation':1 if name=='Ocean' else 3} for y,row in enumerate(pat) for x,n in enumerate(row)]})
f.write_text(json.dumps(cat,indent=2)+'\n')
(D/'EXACT-USER-SHEETS.md').write_text('Nuvema exact source colours\n\nUse tools/la_world/build_nuvema_exact.py to repack the native user artwork. Do not run the older general rebuild/polish scripts: they use the former reduced material palettes.\n\n11 GBA palettes; 932 tile-source comparisons passed with RGB555 values preserved exactly. No nearest-colour substitution. Native user tree, mailbox, sign and building crops are used. Shoreline and repeating boardwalk retain original reference pixels for the pieces absent from the user sheets.\n\nExisting layout retained with two hedge positions moved one metatile upward to expose their complete bases. Interior warps remain pending.\n')
