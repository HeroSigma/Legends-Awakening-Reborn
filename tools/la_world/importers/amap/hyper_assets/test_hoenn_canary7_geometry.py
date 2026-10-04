#!/usr/bin/env python3
"""Review native scene paths, bridge/water levels and canonical seams before apply."""
import re
import hoenn_canary7 as C

def review(q):
 scenes=[];water=0;wildcard_bypasses=[]
 def path(n,label,start):
  g=q['grids'][n];s=q['scripts'][n];body=s.split(label+':',1)[1].split('step_end',1)[0];x,y=start;cells=[g.cell(x,y)]
  for line in body.splitlines():
   cmd=line.strip().split()[0] if line.strip() else ''
   if not cmd.startswith(('walk_fast_','walk_down','walk_up','walk_left','walk_right')):continue
   direction=cmd.rsplit('_',1)[-1];dx,dy={'up':(0,-1),'down':(0,1),'left':(-1,0),'right':(1,0)}[direction];x+=dx;y+=dy;v=g.cell(x,y);assert v['collision']==0 and v['translated_behavior'] not in {0x10,0x15},(n,label,v);cells.append(v)
  scenes.append({'map':n,'movement':label,'start':start,'cells':cells});return x,y
 m=q['maps']['Route119'];rival=next(e for e in m['object_events'] if e['graphics_id']=='OBJ_EVENT_GFX_VAR_3')
 for branch in [1,2]:
  end=path('Route119','Route119_Movement_RivalEnter'+str(branch),(rival['x'],rival['y']));assert end==(24+branch,32),end
  path('Route119','Route119_Movement_RivalExit'+str(branch),end)
  end=path('Route119','Route119_Movement_ScottEnter',(26+branch,25));assert end==(24+branch,30)
  path('Route119','Route119_Movement_ScottExit'+str(branch),end)
 for n in ['Route119','Route120','FortreeCity']:
  g=q['grids'][n]
  for y in range(g.h):
   for x in range(g.w):
    v=g.cell(x,y)
    if v['translated_behavior'] not in {0x10,0x11,0x12,0x13,0x14,0x15,0x19,0x22,0x2A}:continue
    assert v['elevation']==1,(n,v);water+=1
    for xx,yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
     if not(0<=xx<g.w and 0<=yy<g.h):continue
     a=g.cell(xx,yy)
     if a['collision']==0 and a['elevation']==0 and a['translated_behavior'] not in [0x70,0x71,0x72,0x73]:wildcard_bypasses.append({'map':n,'land':a,'water':v})
 assert not wildcard_bypasses,wildcard_bypasses[:5]
 # Sliding-gate puzzle uses identical native numeric geometry; runtime logic remains untouched.
 n='FortreeCity_Gym';g=q['grids'][n];old=q['original'][n];ol=next(z for z in q['oldls']['layouts'] if z['id']==old['layout']);native=C.words(C.ROOT/ol['blockdata_filepath']);assert all((a&1023)==(b&1023) for a,b in zip(g.blocks,native))
 result={'passed':True,'native_scene_paths':scenes,'surface_water_cells_checked':water,'water_wildcard_bypasses':wildcard_bypasses,'gym_metatile_geometry_matches_native':True};C.dump(C.OUT/'geometry_validation.json',result);return result
if __name__=='__main__':q=C.prepare();print(review(q))
