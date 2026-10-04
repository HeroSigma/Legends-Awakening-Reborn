#!/usr/bin/env python3
"""Restore source water elevation without changing donor art or expansion gameplay."""
import copy,struct
import hoenn_canary1 as C
ROOT=C.ROOT;OUT=ROOT/'.la_work/amap/hyper_hoenn_route114_water_fix'
WATER={0x10,0x11,0x12,0x13,0x14,0x15,0x19,0x22,0x2A}
def apply():
 if (OUT/'receipt.json').exists():raise SystemExit('Already applied; validate the existing correction receipt.')
 OUT.mkdir(parents=True,exist_ok=True)
 cat=C.load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');g=C.Grid(next(z for z in cat['layouts'] if z['donor_id']=='0.29'))
 mp='data/maps/Route114/map.json';m=C.load(ROOT/mp);old=copy.deepcopy(m);l=next(z for z in C.load(ROOT/'data/layouts/layouts.json')['layouts'] if z['id']==m['layout']);bp=l['blockdata_filepath'];blocks=C.words(ROOT/bp);changes=[];events=[];before={}
 for f in [mp,bp]:
  before[f]=C.digest(ROOT/f);p=OUT/'original'/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/f).read_bytes())
 for y in range(g.h):
  for x in range(g.w):
   v=g.cell(x,y);i=y*g.w+x;b=blocks[i]
   if v['translated_behavior'] not in WATER:continue
   assert b&4095==v['block']&4095,(x,y,'Unexpected artwork/collision edit; inspect manually before changing.')
   n=(b&4095)|(v['elevation']<<12)
   if b!=n:changes.append({'x':x,'y':y,'before':b,'after':n,'behavior':v['translated_behavior']});blocks[i]=n
 for kind,i,x,y in [('object_events',15,20,27),('bg_events',1,30,6)]:
  e=m[kind][i];before_event=copy.deepcopy(e);e['x'],e['y']=x,y;cell=g.cell(x,y)
  assert cell['translated_behavior'] not in WATER
  assert (g.walk(x,y) if kind=='object_events' else cell['collision']==1 and g.walk(x,y+1))
  events.append({'kind':kind,'index':i,'before':before_event,'after':copy.deepcopy(e),'source_cell':cell,'reason':'Matched donor event role/index and inspected actual shoreline/bridge or sign cell; retain all expansion gameplay fields.'})
 assert len(changes)==119
 (ROOT/bp).write_bytes(struct.pack('<'+'H'*len(blocks),*blocks));C.dump(ROOT/mp,m)
 receipt={'schema':'hyper-route114-water-fix-v1','donor_id':'0.29','map':'Route114','water_cells_corrected':len(changes),'cells':changes,'events':events,'changed_files':{f:{'before':before[f],'after':C.digest(ROOT/f)} for f in before},'reason':'Canary5 native elevation reconciliation copied old land elevations into relocated Hyper water. Restore donor water elevation1.','runtime_verified':False}
 C.dump(OUT/'receipt.json',receipt);print('Restored 119 water cells; reconciled fisherman and house sign.')
if __name__=='__main__':apply()
