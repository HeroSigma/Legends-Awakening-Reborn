"""Idempotently register the free scientist in functional PC upstairs rooms."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
groups=json.loads((R/'data/maps/map_groups.json').read_text())
manifest=[]
for name in sorted({n for group in groups['group_order'] for n in groups[group]}):
 if not name.endswith('PokemonCenter_2F'):continue
 path=R/'data/maps'/name/'map.json';data=json.loads(path.read_text())
 # Old donor inspection copies are staged underground maps, not working centers.
 if data['map_type']!='MAP_TYPE_INDOOR':continue
 objects=data['object_events']
 matches=[i for i,obj in enumerate(objects) if obj['script']=='LegendsTraining_Scientist']
 if not matches:
  assert not any(obj['x']==4 and obj['y']==2 for obj in objects),(name,'requested tile occupied')
  assert len(objects)<16,(name,'object limit')
  objects.append(dict(graphics_id='OBJ_EVENT_GFX_SCIENTIST_1',x=4,y=2,elevation=3,movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script='LegendsTraining_Scientist',flag='0'))
  path.write_text(json.dumps(data,indent=2)+'\n');matches=[len(objects)-1]
 assert len(matches)==1
 if objects[matches[0]]['graphics_id']!='OBJ_EVENT_GFX_SCIENTIST_1':
  objects[matches[0]]['graphics_id']='OBJ_EVENT_GFX_SCIENTIST_1'
  path.write_text(json.dumps(data,indent=2)+'\n')
 manifest.append(dict(map=name,local_id=matches[0]+1,x=4,y=2))
(R/'docs/features/training-scientist-locations.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Training scientists:',len(manifest))
