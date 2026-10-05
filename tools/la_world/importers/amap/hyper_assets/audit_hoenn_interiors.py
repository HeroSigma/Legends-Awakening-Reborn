#!/usr/bin/env python3
"""Check static door and NPC approaches in rendered Hoenn interior batches."""
import argparse,re
import hoenn_finalization as F
R=F.R

def audit(batch):
 O=R/f'.la_work/amap/hoenn_interior_polish{batch}';rows=F.load(O/'inventory.json');maps={p.parent.name:F.load(p) for p in (R/'data/maps').glob('*/map.json')};ids={m['id']:n for n,m in maps.items()};ls={l['id']:l for l in F.load(R/'data/layouts/layouts.json')['layouts']};h=(R/'src/data/tilesets/headers.h').read_text();a=(R/'src/data/tilesets/metatiles.h').read_text();issues=[];doors=actors=0;dynamic=[];signs=[];conditional=[]
 for z in rows:
  n=z['map'];m=maps[n];g=F.grid(ls[m['layout']],h,a);roots={(w['x'],w['y']) for w in m['warp_events']};seen=set(roots);todo=list(roots)
  while todo:
   x,y=todo.pop()
   for xx,yy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
    if (xx,yy) not in seen and 0<=xx<g.w and 0<=yy<g.h and g.cell(xx,yy)['collision']==0:seen.add((xx,yy));todo.append((xx,yy))
  for w in m['warp_events']:
   if w['dest_map']=='MAP_DYNAMIC':dynamic.append({'map':n,'warp':w,'owner':'Native runtime system'});continue
   assert w['dest_map'] in ids;dn=ids[w['dest_map']];dest=maps[dn];di=int(w['dest_warp_id']);assert di<len(dest['warp_events']);dw=dest['warp_events'][di];dg=F.grid(ls[dest['layout']],h,a);free=[(xx,yy) for xx,yy in [(dw['x']+1,dw['y']),(dw['x']-1,dw['y']),(dw['x'],dw['y']+1),(dw['x'],dw['y']-1)] if 0<=xx<dg.w and 0<=yy<dg.h and dg.cell(xx,yy)['collision']==0]
   if not free:
    scriptpath=R/f'data/maps/{dn}/scripts.inc';text=scriptpath.read_text() if scriptpath.exists() else '';alternatives=[]
    for layout_id in re.findall(r'\bsetmaplayoutindex\s+(LAYOUT_\w+)',text):
     if layout_id not in ls:continue
     alternate=F.grid(ls[layout_id],h,a)
     if any(0<=xx<alternate.w and 0<=yy<alternate.h and alternate.cell(xx,yy)['collision']==0 for xx,yy in [(dw['x']+1,dw['y']),(dw['x']-1,dw['y']),(dw['x'],dw['y']+1),(dw['x'],dw['y']-1)]):alternatives.append(layout_id)
    if alternatives:conditional.append({'map':n,'warp':w,'destination':dn,'runtime_layouts_with_clear_arrival':alternatives,'status':'Requires native scripted layout state; runtime testing pending'})
    else:issues.append({'map':n,'kind':'WARP_NO_FREE_NEIGHBOR','warp':w,'destination':dn})
   doors+=1
  for actor in z['actors']:
   e=actor['event'];x,y=e['x'],e['y'];virtual=actor['virtual_or_decorative'] or 'graphics_id' not in e or any(t in e.get('graphics_id','') for t in ['DOLL','ITEM_BALL'])
   if virtual:continue
   available=False
   for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
    if (x+dx,y+dy) in seen:available=True
    elif 0<=x+dx<g.w and 0<=y+dy<g.h and g.cell(x+dx,y+dy)['translated_behavior']==128 and (x+2*dx,y+2*dy) in seen:available=True
   if not available:issues.append({'map':n,'kind':'NPC_NO_TALK_APPROACH','event':e,'cell':actor['cell']})
   actors+=1
  for e in m['bg_events']:
   if not (0<=e['x']<g.w and 0<=e['y']<g.h):
    issues.append({'map':n,'kind':'BG_OUT_OF_BOUNDS','event':e});continue
   signs.append({'map':n,'event':e,'cell':g.cell(e['x'],e['y'])})
 result={'rooms':len(rows),'warp_arrivals':doors,'native_dynamic_warps':dynamic,'conditional_layout_warps':conditional,'active_actors':actors,'bg_events':len(signs),'issues':issues,'scope':'Static floor/counter reachability; native flags and script-controlled movement retained; runtime story/service testing remains necessary.'};F.dump(O/'access_audit.json',result);print('Rooms',len(rows),'static warp arrivals',doors,'actors',actors,'issues',len(issues));print(issues);return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--batch',type=int,choices=[1,2,3,4,5,6,7,8,9,10],default=1);audit(p.parse_args().batch)
