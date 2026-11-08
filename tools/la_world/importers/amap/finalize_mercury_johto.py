#!/usr/bin/env python3
"""Finish regional presentation and editor grouping without moving original IDs."""
import re,json,shutil
from replace_johto_mercury import R,S,D,B,load,dump,sid

def main():
 plan=load(D/'replacement_plan.json');old=load(B/'before.json')['groups'];groups=load(R/'data/maps/map_groups.json');new=set(plan['new_maps']);source={m['id']:m for m in load(S/'manifest.json')['maps']};maps={k:load(R/'data/maps'/name/'map.json') for k,name in plan['names'].items()}
 for group in old['group_order']:
  assert groups[group][:len(old[group])]==old[group]
  assert set(groups[group][len(old[group]):])<=new
  groups[group]=list(old[group])
 addedgroups=[]
 for k in sorted(plan['selected'],key=sid):
  name=plan['names'][k]
  if name not in new:continue
  m=source[k];label=m['name'];t=m['map_type'];area=m['width']*m['height']
  if t in [8,0,9] or area<400:
   candidates=[g for g in groups['group_order'] if g.startswith('gMapGroup_Johto_Interiors') and len(groups[g])<127]
   if not candidates:
    group='gMapGroup_Johto_Interiors_03';assert group not in groups;assert len(groups['group_order'])<127;groups['group_order'].append(group);groups[group]=[];addedgroups.append(group);candidates=[group]
   group=min(candidates,key=lambda g:len(groups[g]))
  elif 'Forest' in label:group='gMapGroup_Johto_Forests'
  elif t==4:group='gMapGroup_Johto_Caves'
  elif ('Town' in label or 'City' in label) and label!='Pallet Town':group='gMapGroup_Johto_TownsAndCities'
  elif 'Route' in label or label in ['Lake of Rage','Sea Bridge']:group='gMapGroup_Johto_Routes'
  else:group='gMapGroup_Johto_SpecialAreas'
  assert len(groups[group])<127,(group,len(groups[group]));groups[group].append(name)
 dump(R/'data/maps/map_groups.json',groups)
 shared=R/'src/regional_map_names.c';backup=B/'src/regional_map_names.c';backup.parent.mkdir(parents=True,exist_ok=True);assert not backup.exists();shutil.copy2(shared,backup)
 ls={l['id']:l for l in load(R/'data/layouts/layouts.json')['layouts']};byname={};cases=[];rows=[]
 for k,m in maps.items():
  label=source[k]['name'].replace('’',"'").replace('‘',"'")
  if label=='Pallet Town':label='Johto Area'
  elif label=='Celadon Dept.':label='Johto Dept. Store'
  if label not in byname:byname[label]='sMercuryLocationName'+str(len(byname))
  cases.append(f'    case {m["layout"]}: return {byname[label]};');rows.append(dict(source=k,map=m['name'],layout=m['layout'],label=label))
 lines=['// Johto-only visual labels; canonical map-section/save IDs are preserved.']
 for label,sym in byname.items():lines.append(f'static const u8 {sym}[] = _("{label}");')
 lines+=['static const u8 *MercuryJohtoDisplayName(u16 layout)','{','    switch (layout)','    {']+cases+['    default: return NULL;','    }','}']
 (R/'src/mercury_johto_names.inc').write_text('\n'.join(lines)+'\n')
 text=shared.read_text();include='#include "mercury_johto_names.inc"';text=text.replace('const u8 *RegionalMapDisplayName',include+'\n\nconst u8 *RegionalMapDisplayName');anchor='    u32 i;\n';assert text.count(anchor)==1;text=text.replace(anchor,'    const u8 *mercuryName = MercuryJohtoDisplayName(header->mapLayoutId);\n    u32 i;\n    if (mercuryName != NULL)\n        return mercuryName;\n');shared.write_text(text)
 dump(D/'display_names.json',rows);dump(D/'editor_groups.json',dict(groups={g:groups[g] for g in groups['group_order'] if 'Johto' in g},added_groups=addedgroups,previous_numeric_ids_preserved=True))
 recovery=load(D/'asset_recovery.json');unique={json.dumps(x,sort_keys=True):x for x in recovery};dump(D/'asset_recovery.json',list(unique.values()))
 print('Grouped',len(new),'new maps; Johto label count',len(rows),'new groups',addedgroups)
if __name__=='__main__':main()
