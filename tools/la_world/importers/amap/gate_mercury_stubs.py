#!/usr/bin/env python3
"""Keep unsafe/no-land donor stubs registered, with project construction gates."""
import json,collections
from replace_johto_mercury import R,D,load,dump

def main():
 assert not (D/'stub_gates.json').exists(),'Already gated'
 p=load(D/'replacement_plan.json');arrivals={r['source'] for r in load(D/'inspection_arrivals.json')};water_only={'3.46','3.108','3.109','3.110','3.111','3.112','3.113','3.114','3.115'};held=set(p['selected'])-arrivals-water_only;ids=p['ids'];names=p['names'];reverse={v:k for k,v in ids.items()};maps={k:load(R/'data/maps'/n/'map.json') for k,n in names.items()};events={k:m['warp_events'] for k,m in maps.items()};keep={k:set() if k in held else {i for i,e in enumerate(events[k]) if reverse[e['dest_map']] not in held} for k in maps}
 while True:
  remove=[(k,i) for k,indices in keep.items() for i in indices if int(events[k][i]['dest_warp_id']) not in keep[reverse[events[k][i]['dest_map']]]]
  if not remove:break
  for k,i in remove:keep[k].remove(i)
 lookup={(k,i):j for k,v in keep.items() for j,i in enumerate(sorted(v))};gates=[]
 for k,m in maps.items():
  out=[]
  for i,e in enumerate(events[k]):
   if i in keep[k]:
    target=reverse[e['dest_map']];e['dest_warp_id']=str(lookup[target,int(e['dest_warp_id'])]);out.append(e)
   elif k not in held and not any(o['x']==e['x'] and o['y']==e['y'] for o in m['object_events']):
    m['object_events'].append(dict(local_id='LOCALID_'+m['name'].upper()+'_MERCURY_GATE_'+str(i),graphics_id='OBJ_EVENT_GFX_SCIENTIST_1',x=e['x'],y=e['y'],elevation=3,movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script='MercuryJohto_ConstructionGate',flag='0'));gates.append(dict(source=k,map=m['name'],x=e['x'],y=e['y'],old_target=e['dest_map']))
  m['warp_events']=out;m['connections']=None if k in held else [e for e in m['connections'] or [] if reverse[e['map']] not in held] or None;dump(R/'data/maps'/m['name']/'map.json',m)
 script=R/'data/scripts/mercury_johto_construction.inc';script.write_text('MercuryJohto_ConstructionGate::\n\tlock\n\tfaceplayer\n\tmsgbox MercuryJohto_ConstructionGate_Text, MSGBOX_DEFAULT\n\trelease\n\tend\nMercuryJohto_ConstructionGate_Text:\n\t.string "This area is under construction.\\p"\n\t.string "Please explore the other Johto areas.$"\n');pfile=R/'data/event_scripts.s';pfile.write_text(pfile.read_text().rstrip()+'\n.include "data/scripts/mercury_johto_construction.inc"\n')
 dump(D/'stub_gates.json',dict(registered_stubs=[dict(source=k,map=names[k],id=ids[k]) for k in sorted(held)],construction_scientists=gates,water_only_sectors_retained=sorted(water_only),reason='No validated land-based arrival or inspector cell. Preserve for Porymap; prevent traversal until reconciled.'))
 print('Held',len(held),'registered stubs;',len(gates),'entrance scientists')
if __name__=='__main__':main()
