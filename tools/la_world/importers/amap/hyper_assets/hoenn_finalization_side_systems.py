#!/usr/bin/env python3
"""Complete indoor native-cell reconciliation; never copy donor gameplay."""
import copy,re,struct
import hoenn_finalization as F
R=F.R;O=F.O

def prepare():
 rec=F.load(O/'receipt.json');j=F.load(O/'reconciliation.json');assert not j.get('side_system_closure_completed'),'Already applied'
 ls=F.load(R/'data/layouts/layouts.json');oldls=copy.deepcopy(ls);header=(R/'src/data/tilesets/headers.h').read_text();meta=(R/'src/data/tilesets/metatiles.h').read_text();by={x['donor_id']:x for x in F.load(R/'.la_work/amap/hyper_asset_integration/asset_catalog.json')['layouts']};files={};maps={};original={};kept=[];notices=[]
 for z in j['kept_original']:
  n=z['map'];k=z['donor_id'];candidate=n.startswith(('ArtisanCave_','AlteringCave','Route110_TrickHouse','SouthernIsland_','FarawayIsland_','SSTidal')) or n.startswith('NavelRock_') and n!='NavelRock_Harbor' or n in ['SootopolisCity_MysteryEventsHouse_B1F','InsideOfTruck']
  if n in ['NavelRock_Top','NavelRock_Bottom']:
   candidate=False;z['reason']='Canonical legendary scene references native numeric art slots absent from the donor bank; keep original geometry/assets and gameplay.'
  if not candidate:kept.append(z);continue
  m=F.load(R/f'data/maps/{n}/map.json');original[n]=copy.deepcopy(m);maps[n]=m;l=next(x for x in ls['layouts'] if x['id']==m['layout']);ng=F.grid(l,header,meta);dg=F.C.P.C.Grid(by[k]);assert (ng.w,ng.h)==(dg.w,dg.h)
  if len([p for p in (R/'data/maps').glob('*/map.json') if F.load(p).get('layout')==l['id']])>1:
   l=copy.deepcopy(l);l['id']='LAYOUT_HYPER_FINAL_'+F.C.P.const(n);l['name']='HyperFinal'+n+'_Layout';ls['layouts'].append(l);m['layout']=l['id']
  # Native numeric tile namespace is authoritative for all script-generated cells.
  for bi,role in enumerate(['primary_tileset','secondary_tileset']):
   attrs=list(dg.attrs[bi]);edits=[]
   for ti,a in enumerate(ng.attrs[bi]):
    if ti<len(attrs) and (a&255)!=(attrs[ti]&255):edits.append((ti,attrs[ti],a));attrs[ti]=(attrs[ti]&0xff00)|(a&255)
   base=by[k][role];l[role]=base
   if edits:
    sym=f'gMetatileAttributes_Hyper_Final_{n}_{bi}';derived=f'gTileset_Hyper_Final_{n}_{bi}';body=re.search(r'const struct Tileset\s+'+base+r'\s*=\s*\{(.*?)\};',header,re.S)[1];body=re.sub(r'(\.metatileAttributes\s*=\s*)\w+',lambda x:x[1]+sym,body);header+='\nconst struct Tileset '+derived+' = {'+body+'};\n';fp=f'data/hyper_assets/finalization_layouts/{n}/attributes{bi}.bin';files[fp]=struct.pack('<'+'H'*len(attrs),*attrs);meta+='\nconst u16 '+sym+'[] = INCBIN_U16("'+fp+'");\n';l[role]=derived;j['attribute_derivatives'][derived]={'base':base,'attributes_path':fp,'reason':'Native numeric metatile behavior namespace; Hyper graphics/palettes/metatiles/animation.'}
   dg.attrs[bi]=attrs
  for at,(a,b) in enumerate(zip(ng.blocks,dg.blocks)):
   if (a&0xfc00)!=(b&0xfc00) or (ng.attrs[(a&1023)//512][a&511]&255)!=(dg.attrs[(b&1023)//512][b&511]&255):
    dg.blocks[at]=a;j['geometry_patches'].append({'map':n,'x':at%ng.w,'y':at//ng.w,'before':b,'after':a,'reason':'Restore canonical indoor scripted cell role, collision and elevation at the native coordinate with Hyper artwork.'})
  assert all((a&0xfc00)==(b&0xfc00) and (ng.attrs[(a&1023)//512][a&511]&255)==(dg.attrs[(b&1023)//512][b&511]&255) for a,b in zip(ng.blocks,dg.blocks)),n
  l.update(border_filepath=by[k]['border_path'],blockdata_filepath=f'data/hyper_assets/finalization_layouts/{n}/map.bin');files[l['blockdata_filepath']]=struct.pack('<'+'H'*len(dg.blocks),*dg.blocks);rec['donor_ids'][n]=k;j['asset_ports'].append({'map':n,'donor_id':k,'mode':'LAYOUT_REPLACEMENT_WITH_NATIVE_CELL_RECONCILIATION','full_grid_contract_equal':True,'events_and_scripts_unchanged':True})
 j['kept_original']=kept
 for p in (R/'data/maps').glob('HyperHoenn_*/map.json'):
  m=F.load(p);before=copy.deepcopy(m);l=next(x for x in ls['layouts'] if x['id']==m['layout']);g=F.grid(l,header,meta);occupied={(e['x'],e['y']) for e in m['object_events']};warps={(e['x'],e['y']) for e in m['warp_events']};remove=[]
  for e in m['object_events']:
   if 'Construction' not in e['script'] or (e['x'],e['y']) not in warps:continue
   x,y=e['x'],e['y'];cells=[]
   for yy in range(max(0,y-4),min(g.h,y+5)):
    for xx in range(max(0,x-4),min(g.w,x+5)):
     v=g.cell(xx,yy)
     if (xx,yy) not in occupied|warps and v['collision']==0 and v['translated_behavior'] in [0,2,6,0x21] and (v['elevation']==g.cell(x,y)['elevation'] or v['elevation'] in [0,3]):cells.append((abs(xx-x)+abs(yy-y),yy,xx,v))
   if not cells:
    remove.append(e);notices.append({'map':p.parent.name,'before':copy.deepcopy(e),'after':None,'reason':'Redundant interior exit guard removed: no safe nearby standing cell. Parent construction gate and regional notices remain.'});continue
   _,yy,xx,v=min(cells);old=copy.deepcopy(e);e['x'],e['y'],e['elevation']=xx,yy,v['elevation'] if v['elevation'] not in [0,15] else 0;occupied.add((xx,yy));notices.append({'map':p.parent.name,'before':old,'after':copy.deepcopy(e),'inspected_floor':v,'reason':'Interior notice moved off static return slot; canonical entrance scientists stay.'})
  m['object_events']=[e for e in m['object_events'] if e not in remove]
  if m!=before:maps[p.parent.name]=m;original[p.parent.name]=before
 j['interior_notice_moves']=notices;j['side_system_closure_completed']=True
 return locals()

def apply():
 q=prepare();rec=q['rec'];j=q['j']
 allowed=set(rec['changed_baseline_files'])|{f'data/maps/{n}/map.json' for n in q['maps']}
 for f,h in rec['baseline'].items():
  expected=rec['changed_baseline_files'].get(f,{}).get('after',h);assert F.digest(R/f)==expected,('Protected baseline changed',f)
 for n,m in q['maps'].items():
  op=O/f'original/data/maps/{n}/map.json'
  if not op.exists():F.dump(op,q['original'][n])
  F.dump(R/f'data/maps/{n}/map.json',m)
 for f,data in q['files'].items():p=R/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data);rec['new_files'][f]=F.digest(p)
 F.dump(R/'data/layouts/layouts.json',q['ls']);(R/'src/data/tilesets/headers.h').write_text(q['header']);(R/'src/data/tilesets/metatiles.h').write_text(q['meta'])
 for f,h in rec['baseline'].items():
  actual=F.digest(R/f)
  if actual!=h:rec['changed_baseline_files'][f]={'before':h,'after':actual}
 rec['touched_maps']=sorted(set(rec['touched_maps'])|set(q['maps']));F.dump(O/'receipt.json',rec);F.dump(O/'reconciliation.json',j);print('Completed',len(rec['donor_ids']),'asset ports and moved',len(q['notices']),'interior notices.')
if __name__=='__main__':
 import sys
 if '--apply' in sys.argv:apply()
 else:q=prepare();print('Prepared side systems',len(q['maps']))
