#!/usr/bin/env python3
"""Register vertical Hyper climb strips without changing native or donor story state."""
import re
import hoenn_finalization as F
R=F.R;O=R/'.la_work/amap/hyper_sinnoh_id_correction'
def prepare():
 ls={l['id']:l for l in F.load(R/'data/layouts/layouts.json')['layouts']};h=(R/'src/data/tilesets/headers.h').read_text();a=(R/'src/data/tilesets/metatiles.h').read_text();rows=[];held=[]
 for p in sorted((R/'data/maps').glob('HyperSinnoh_*/map.json')):
  m=F.load(p);l=ls[m['layout']];g=F.grid(l,h,a)
  def eligible(x,y):
   c=g.cell(x,y);t=c['metatile']
   return c['translated_behavior']==209 and ((t in [0x166,0x167] and l['primary_tileset']=='gTileset_Hyper_Primary_089CBC6C') or (t==0x244 and l['secondary_tileset'].startswith('gTileset_Hyper_Secondary_08A5FEB4')) or (t==0x302 and l['secondary_tileset']=='gTileset_Hyper_Secondary_089CD34C'))
  for x in range(g.w):
   y=0
   while y<g.h:
    if not eligible(x,y):y+=1;continue
    top=y
    while y<g.h and eligible(x,y):y+=1
    row={'map':p.parent.name,'map_id':m['id'],'x':x,'top':top,'bottom':y-1,'steps':y-top+1,'tilesets':[l['primary_tileset'],l['secondary_tileset']],'cells':[g.cell(x,i) for i in range(top,y)]}
    if top==0 or y==g.h:held.append(dict(row,reason='No in-bounds landing'));continue
    row['upper_landing']=g.cell(x,top-1);row['lower_landing']=g.cell(x,y)
    forbidden={16,17,18,19,20,21,64,65,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111}
    occupied={(e['x'],e['y']) for e in m['object_events']}|{(w['x'],w['y']) for w in m['warp_events']}
    if any(c['collision']!=0 or c['translated_behavior'] in forbidden for c in [row['upper_landing'],row['lower_landing']]) or any((x,i) in occupied for i in range(top-1,y+1)):held.append(dict(row,reason='Landing water/blocked/portal or occupied path'));continue
    rows.append(row)
 assert any(z['map']=='HyperSinnoh_36_48_Acuity_Lakefront' and (z['x'],z['top'],z['bottom'])==(19,35,38) for z in rows)
 return rows,held

def apply():
 fix=F.load(O/'receipt.json');assert not fix.get('vertical_climb'),'Already applied';rows,held=prepare();entries=[];scripts='@ Project vertical traversal on inspected Hyper rock strips.\n'
 for i,z in enumerate(rows):
  for direction,y,move in [('NORTH',z['bottom']+1,'walk_up'),('SOUTH',z['top']-1,'walk_down')]:
   label=f'HyperSinnoh_VerticalClimb_{i}_{direction}';entries.append((z['map_id'],z['x'],y,direction,label));scripts+=f'{label}::\n\tlockall\n\tcall HyperSinnoh_RockClimbPrompt\n\tgoto_if_eq VAR_RESULT, NO, HyperSinnoh_RockClimbEnd\n\tapplymovement OBJ_EVENT_ID_PLAYER, {label}_Movement\n\twaitmovement OBJ_EVENT_ID_PLAYER\n\tgoto HyperSinnoh_RockClimbEnd\n{label}_Movement:\n'+('\t'+move+'\n')*z['steps']+'\tstep_end\n'
 c='/* Map-scoped inspected vertical routes; preserve source cell attributes. */\n'+''.join(f'extern const u8 {e[4]}[];\n' for e in entries)+'static const struct { u16 map; s16 x,y; u8 direction; const u8 *script; } sVerticalClimbRoutes[] = {\n'+''.join(f' {{{mid}, {x}, {y}, DIR_{d}, {label}}},\n' for mid,x,y,d,label in entries)+'};\nstatic const u8 *HyperSinnoh_GetVerticalClimbInteraction(s16 x, s16 y, u8 direction)\n{\n u32 i;\n for (i=0;i<ARRAY_COUNT(sVerticalClimbRoutes);i++)\n  if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(sVerticalClimbRoutes[i].map) && gSaveBlock1Ptr->location.mapNum == MAP_NUM(sVerticalClimbRoutes[i].map) && x == sVerticalClimbRoutes[i].x + MAP_OFFSET && y == sVerticalClimbRoutes[i].y + MAP_OFFSET && direction == sVerticalClimbRoutes[i].direction)\n   return sVerticalClimbRoutes[i].script;\n return NULL;\n}\n'
 source=(R/'src/hyper_sinnoh_climb.c').read_text();source=source.replace('const u8 *HyperSinnoh_GetRockClimbInteraction', '#include "hyper_sinnoh_vertical_climb.inc"\n\nconst u8 *HyperSinnoh_GetRockClimbInteraction',1);source=source.replace('    u32 i;\n    for (i = 0;', '    u32 i;\n    const u8 *vertical = HyperSinnoh_GetVerticalClimbInteraction(x,y,direction);\n    if (vertical != NULL)\n        return vertical;\n    for (i = 0;',1)
 files={'src/hyper_sinnoh_climb.c':source,'src/hyper_sinnoh_vertical_climb.inc':c,'data/scripts/hyper_sinnoh_vertical_climb.inc':scripts,'data/event_scripts.s':(R/'data/event_scripts.s').read_text()+'\n\t.include "data/scripts/hyper_sinnoh_vertical_climb.inc"\n'}
 for f,text in files.items():
  p=R/f
  if p.exists():
   snap=O/'vertical_original'/f;snap.parent.mkdir(parents=True,exist_ok=True);snap.write_bytes(p.read_bytes());before=F.digest(p)
   if f in fix.get('added_files',{}):target=fix['added_files'];p.write_text(text);target[f]=F.digest(p)
   else:
    old=fix['changed_files'].get(f);p.write_text(text);fix['changed_files'][f]={'before':old['before'] if old else before,'after':F.digest(p)}
  else:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text);fix.setdefault('added_files',{})[f]=F.digest(p)
 fix['vertical_climb']={'strips':rows,'held':held,'approach_triggers':len(entries),'runtime_verified':False};F.dump(O/'receipt.json',fix);F.dump(O/'vertical_climb_ledger.json',fix['vertical_climb']);print('Registered',len(rows),'vertical strips and',len(entries),'bidirectional A-button triggers;',len(held),'held.')
if __name__=='__main__':apply()
