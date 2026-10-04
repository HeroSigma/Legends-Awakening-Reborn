#!/usr/bin/env python3
"""Read applied assets and verify sea/land connection boundaries without modifying them."""
import re,struct
import hoenn_canary9 as C

def check():
 ls={z['id']:z for z in C.load(C.ROOT/'data/layouts/layouts.json')['layouts']};maps={p.parent.name:C.load(p) for p in (C.ROOT/'data/maps').glob('*/map.json')};ids={m['id']:n for n,m in maps.items()};header=(C.ROOT/'src/data/tilesets/headers.h').read_text();meta=(C.ROOT/'src/data/tilesets/metatiles.h').read_text();cache={}
 def grid(n):
  if n in cache:return cache[n]
  l=ls[maps[n]['layout']];g=C.P.C.Grid.__new__(C.P.C.Grid);g.w,g.h=l['width'],l['height'];g.blocks=C.words(C.ROOT/l['blockdata_filepath']);g.attrs=[]
  for role in ['primary_tileset','secondary_tileset']:
   body=re.search(r'const struct Tileset\s+'+l[role]+r'\s*=\s*\{(.*?)\};',header,re.S)[1];sy=re.search(r'\.metatileAttributes\s*=\s*(\w+)',body)[1];path=re.search(re.escape(sy)+r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"\)',meta)[1];g.attrs.append(C.words(C.ROOT/path))
  cache[n]=g;return g
 results=[]
 for n in C.TARGETS:
  g=grid(n)
  for co in maps[n]['connections'] or []:
   direction=co['direction']
   if direction not in ['up','down','left','right']:continue
   dn=ids[co['map']];dg=grid(dn);pairs=[]
   for i in range(g.h if direction in ['left','right'] else g.w):
    j=i-co['offset']
    if not 0<=j<(dg.h if direction in ['left','right'] else dg.w):continue
    if direction=='left':xy=(0,i);dxy=(dg.w-1,j)
    elif direction=='right':xy=(g.w-1,i);dxy=(0,j)
    elif direction=='up':xy=(i,0);dxy=(j,dg.h-1)
    else:xy=(i,g.h-1);dxy=(j,0)
    a=g.cell(*xy);b=dg.cell(*dxy)
    if a['collision'] or b['collision']:continue
    if not (a['elevation']==b['elevation'] or a['elevation'] in [0,15] or b['elevation'] in [0,15]):continue # Separate shore/elevation barrier; only compatible transition cells are counted.
    pairs.append({'source':a,'destination':b})
   dormant=False
   if not pairs:
    oldls={z['id']:z for z in C.load(C.OUT/'original/data/layouts/layouts.json')['layouts']};oldmaps={z:C.load(C.OUT/f'original/data/maps/{z}/map.json') for z in [n,dn]};sl=oldls[oldmaps[n]['layout']];dl=oldls[oldmaps[dn]['layout']];sb=C.words(C.ROOT/sl['blockdata_filepath']);db=C.words(C.ROOT/dl['blockdata_filepath']);oldpairs=0
    for i in range(sl['height'] if direction in ['left','right'] else sl['width']):
     j=i-co['offset']
     if not 0<=j<(dl['height'] if direction in ['left','right'] else dl['width']):continue
     if direction=='left':aa=i*sl['width'];bb=j*dl['width']+dl['width']-1
     elif direction=='right':aa=i*sl['width']+sl['width']-1;bb=j*dl['width']
     elif direction=='up':aa=i;bb=(dl['height']-1)*dl['width']+j
     else:aa=(sl['height']-1)*sl['width']+i;bb=j
     oldpairs+=((sb[aa]>>10)&3)==0 and ((db[bb]>>10)&3)==0
    assert oldpairs==0,(n,dn,'Lost native traversable boundary');dormant=True
   results.append({'map':n,'destination':dn,'direction':direction,'offset':co['offset'],'compatible_pairs':len(pairs),'native_already_closed_boundary':dormant,'cells':pairs})
 result={'passed':True,'directed_boundaries':len(results),'boundaries':results};C.dump(C.OUT/'connection_boundary_validation.json',result);print('Validated',len(results),'directed boundaries.');return result
if __name__=='__main__':check()
