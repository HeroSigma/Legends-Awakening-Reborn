#!/usr/bin/env python3
"""Dewford–Mauville canonical assets. Expansion owns all gameplay and destinations."""
import argparse,collections,copy,csv,importlib.util,json,re,struct
from pathlib import Path
s=importlib.util.spec_from_file_location('rustboro',Path(__file__).with_name('hoenn_canary3.py'));P=importlib.util.module_from_spec(s);s.loader.exec_module(P)
ROOT=P.ROOT;load=P.load;dump=P.dump;digest=P.digest;words=P.words;OUT=ROOT/'.la_work/amap/hyper_hoenn_canary4'
TARGETS={'DewfordTown':'0.11','Route106':'0.21','GraniteCave_1F':'24.7','GraniteCave_B1F':'24.8','GraniteCave_B2F':'24.9','GraniteCave_StevensRoom':'24.10','DewfordTown_Gym':'3.3','DewfordTown_PokemonCenter_1F':'3.1','Route109':'0.24','Route109_SeashoreHouse':'28.0','SlateportCity':'0.1','SlateportCity_SternsShipyard_1F':'9.0','SlateportCity_SternsShipyard_2F':'9.1','SlateportCity_OceanicMuseum_1F':'9.7','SlateportCity_OceanicMuseum_2F':'9.8','SlateportCity_Harbor':'9.9','SlateportCity_PokemonCenter_1F':'9.11','SlateportCity_Mart':'9.13','Route110':'0.25','Route110_SeasideCyclingRoadSouthEntrance':'29.11','Route110_SeasideCyclingRoadNorthEntrance':'29.12','MauvilleCity':'0.2','MauvilleCity_Gym':'10.0','MauvilleCity_BikeShop':'10.1','MauvilleCity_House1':'10.2','MauvilleCity_House2':'10.4','MauvilleCity_PokemonCenter_1F':'10.5','MauvilleCity_Mart':'10.7'}
# Explicit event-role correspondence reviewed against native/donor records and actual cells.
REMAP={'DewfordTown':{'object_events':{4:(5,4)},'bg_events':{0:(13,13),1:(1,10),4:(1,4)}},'Route106':{'object_events':{4:(31,13)},'bg_events':{0:(37,12),2:(65,16)}},'Route109':{'object_events':{3:(22,45),9:(27,45),12:(20,56),15:(30,31),18:(32,5),19:(31,5)},'bg_events':{3:(8,42),6:(32,4),7:(21,56)}},'SlateportCity':{'object_events':{0:(22,11),6:(20,38),14:(17,46),16:(14,30)},'warp_events':{1:(14,26),2:(27,38),4:(5,26),6:(6,19),10:(30,44)},'bg_events':{0:(4,19),1:(21,19),2:(18,19),3:(13,26),5:(16,26),8:(16,23),10:(7,12)}},'Route110':{'object_events':{4:(11,7),6:(9,14),12:(31,16),19:(25,52),30:(10,77),31:(7,77)},'bg_events':{3:(21,95),4:(6,68),5:(4,14),10:(8,66)}},'MauvilleCity':{'object_events':{0:(30,16),1:(32,7),2:(20,10),3:(20,7),4:(22,13),7:(28,9),8:(27,19),9:(12,7)},'warp_events':{2:(37,5),3:(19,14),5:(8,14),6:(24,14)},'bg_events':{1:(21,5),2:(20,14),3:(18,14)}},'MauvilleCity_House1':{'warp_events':{0:(4,7),1:(5,7)}},'MauvilleCity_House2':{'object_events':{0:(5,5)},'warp_events':{0:(2,8),1:(3,8)}},'GraniteCave_1F':{'warp_events':{2:(12,5)}},'GraniteCave_B1F':{'object_events':{0:(27,21)},'warp_events':{0:(4,14),1:(16,21),2:(28,15),3:(7,16)}},'GraniteCave_B2F':{'object_events':{1:(21,12),2:(21,14),3:(9,15),4:(8,14),5:(18,22),6:(22,13),8:(5,21)},'warp_events':{0:(8,13),4:(29,5)},'bg_events':{0:(20,3),1:(18,19)}}}
EXTRAS={'GraniteCave_B2F':[5],'GraniteCave_StevensRoom':[1],'MauvilleCity_BikeShop':[2],'Route110':[6],'SlateportCity':[11]}
SCRIPT_MAPS=list(TARGETS)
CHANGED=['data/layouts/layouts.json',*[f'data/maps/{n}/map.json' for n in TARGETS],*[f'data/maps/{n}/scripts.inc' for n in {*EXTRAS,'MauvilleCity'}],'src/hyper_asset_graphics_bindings.inc','src/data/object_events/hyper_assets.inc']
class Grid(P.Grid):
 def walk(self,x,y):
  v=self.cell(x,y);return v['collision']==0 and v['translated_behavior'] not in range(0x10,0x16)

def baseline():
 OUT.mkdir(parents=True,exist_ok=True)
 if (OUT/'baseline.json').exists():return load(OUT/'baseline.json')
 b={str(f.relative_to(ROOT)):digest(f) for d in ['data','src','include','graphics'] for f in (ROOT/d).rglob('*') if f.is_file() and not P.C.C.derived(str(f.relative_to(ROOT)))}
 for f in set(CHANGED+[f'data/maps/{n}/scripts.inc' for n in TARGETS]):
  p=OUT/'original'/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/f).read_bytes())
 dump(OUT/'baseline.json',b);return b

def original_grid(n):
 m=load(OUT/'original'/f'data/maps/{n}/map.json');l=next(x for x in load(OUT/'original/data/layouts/layouts.json')['layouts'] if x['id']==m['layout']);return l,words(ROOT/l['blockdata_filepath'])

def prepare():
 b=baseline();assert all(digest(ROOT/f)==b[f] for f in CHANGED),'Already applied or input changed: validate receipt.'
 cat=load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');by={x['donor_id']:x for x in cat['layouts']};ls=load(ROOT/'data/layouts/layouts.json');grids={n:Grid(by[k]) for n,k in TARGETS.items()};maps={};ledger=[];donors={n:P.C.donor(k)[0] for n,k in TARGETS.items()};scripts={n:(OUT/'original'/f'data/maps/{n}/scripts.inc').read_text() for n in TARGETS}
 # Native Scott exits along the inspected open row 8; row 7 now ends at a Hyper hedge.
 label='MauvilleCity_Movement_ScottExitNorth';match=re.search(r'^'+label+r':\n(.*?)(?=^\w+:|\Z)',scripts['MauvilleCity'],re.M|re.S);scripts['MauvilleCity']=scripts['MauvilleCity'][:match.start(1)]+'\twalk_down\n'+match[1]+scripts['MauvilleCity'][match.end(1):]
 patches=[]
 # Canonical sea routes use default elevation3; Hyper water1 cannot cross unchanged native ocean seams.
 for n in ['DewfordTown','Route106','Route109','SlateportCity','Route110','GraniteCave_1F','GraniteCave_B1F','GraniteCave_B2F','GraniteCave_StevensRoom']:
  g=grids[n];native_layout,native_blocks=original_grid(n)
  for y in range(g.h):
   for x in range(g.w):
    v=g.cell(x,y)
    if v['collision']==0 and (n!='Route110' and v['translated_behavior'] in range(0x10,0x16) and v['elevation'] in [1,3] or (n=='Route109' or n.startswith('GraniteCave')) and v['elevation']==4 and v['translated_behavior'] not in range(0x10,0x16)):
     elev=native_blocks[y*g.w+x]>>12 if v['translated_behavior'] in range(0x10,0x16) and native_blocks[y*g.w+x]>>12 in [1,3] else 3
     after=(v['block']&4095)|(elev<<12)
     if after==v['block']:continue
     g.blocks[y*g.w+x]=after;patches.append({'map':n,'x':x,'y':y,'before':v['block'],'after':after,'reason':'Canonical native Surf/ocean/beach/cave elevation compatibility; art/metatile/collision preserved.'})
 # Preserve native closed sea-border corners instead of opening incompatible elevation seams.
 allmaps={load(f)['id']:f.parent.name for f in (ROOT/'data/maps').glob('*/map.json')}
 oldls=load(OUT/'original/data/layouts/layouts.json')['layouts']
 for n,g in grids.items():
  m=load(OUT/'original'/f'data/maps/{n}/map.json');ol,ob=original_grid(n)
  for conn in m['connections'] or []:
   dest=allmaps[conn['map']];dm=load((OUT/'original' if dest in TARGETS else ROOT)/f'data/maps/{dest}/map.json');dl=next(z for z in oldls if z['id']==dm['layout']);db=words(ROOT/dl['blockdata_filepath']);dg=grids.get(dest);direction=conn['direction'];off=conn['offset']
   for x,y in ([(x,0 if direction=='up' else g.h-1) for x in range(g.w)] if direction in ['up','down'] else [(0 if direction=='left' else g.w-1,y) for y in range(g.h)]):
    dx,dy=(x-off,dl['height']-1 if direction=='up' else 0) if direction in ['up','down'] else (dl['width']-1 if direction=='left' else 0,y-off)
    if not(0<=dx<dl['width'] and 0<=dy<dl['height']):continue
    v=g.cell(x,y);z=dg.cell(dx,dy)['block'] if dg else db[dy*dl['width']+dx];a=ob[y*g.w+x]
    if v['collision']==0 and ((z>>10)&3)==0 and v['elevation'] not in [0,15,z>>12] and z>>12 not in [0,15] and ((a>>10)&3)!=0:
     after=v['block']|0x400;g.blocks[y*g.w+x]=after;patches.append({'map':n,'x':x,'y':y,'before':v['block'],'after':after,'reason':'Close newly opened incompatible sea-border corner that was closed natively; same Hyper artwork retained, native adjacent map untouched.'})
 dk={'object_events':'npcs','warp_events':'warps','coord_events':'coord_events','bg_events':'bg_events'}
 for n,k in TARGETS.items():
  m=load(OUT/'original'/f'data/maps/{n}/map.json');g=grids[n];ol,ob=original_grid(n)
  for kind,dkey in dk.items():
   probes={x['index']:x for x in donors[n][dkey]}
   for i,e in enumerate(m[kind]):
    old=copy.deepcopy(e);probe=probes.get(i);xy=REMAP.get(n,{}).get(kind,{}).get(i);reason='Native coordinate retained; actual Hyper cell inspected.'
    if xy:e['x'],e['y']=xy;reason='Reviewed native role and source geometry; x/y remap only, native state/script/destination unchanged.'
    x,y=e['x'],e['y'];off=not(0<=x<g.w and 0<=y<g.h)
    if off:
     assert (n,kind,i) in [('SlateportCity','warp_events',9),('SlateportCity_Harbor','warp_events',2),('SlateportCity_Harbor','warp_events',3)] and old==e
     v=None;near=[];reason='Pre-existing native out-of-bounds terminal warp slot, retained dormant for destination/index ABI; not an active Hyper entrance.'
    else:
     v=g.cell(x,y);near=g.neighbors(x,y)
     if kind=='object_events':
      gfx=e['graphics_id'];oldblock=ob[old['y']*ol['width']+old['x']]
      if gfx=='OBJ_EVENT_GFX_BERRY_TREE':assert v['translated_behavior']==0xA0 and near,(n,kind,i,v)
      elif gfx in ['OBJ_EVENT_GFX_SS_TIDAL','OBJ_EVENT_GFX_SUBMARINE_SHADOW','OBJ_EVENT_GFX_MR_BRINEYS_BOAT'] or gfx.startswith('OBJ_EVENT_GFX_SWIMMER'):
       assert v['translated_behavior'] in range(0x10,0x16) or gfx=='OBJ_EVENT_GFX_MR_BRINEYS_BOAT' and v['collision']==0,(n,kind,i,v)
      elif not g.walk(x,y):
       assert old==e and ((oldblock>>10)&3)==v['collision'] and (near or n=='SlateportCity_SternsShipyard_2F' and i==0 and e['script']=='0x0' and (oldblock&1023)==v['metatile'] or gfx in ['OBJ_EVENT_GFX_NURSE','OBJ_EVENT_GFX_MART_EMPLOYEE'] and g.walk(x,y+2)),(n,kind,i,v)
       reason+=' Native staged/counter/door object retains original collision class; spawn elevation is normalized by native runtime.'
      else:assert near or gfx in ['OBJ_EVENT_GFX_NURSE','OBJ_EVENT_GFX_MART_EMPLOYEE'] and g.walk(x,y+2),(n,kind,i,v)
     elif kind=='coord_events':assert g.walk(x,y) and v['elevation'] in [0,e['elevation']],(n,kind,i,v)
     elif kind=='warp_events':assert v['translated_behavior'] in [0x60,0x61,0x62,0x63,0x64,0x65,0x69,0x6A,0x6B,0x6C,0x6D,0x6E] and near,(n,kind,i,v)
     else:assert near,(n,kind,i,v)
    ledger.append({'map':n,'donor_id':k,'canonical_id':m['id'],'kind':kind,'index':i,'before':old,'after':copy.deepcopy(e),'donor_reference':probe,'cell':v,'interaction_neighbors':near,'reason':reason,'owner':'expansion/project'})
  source=by[k];l=next(x for x in ls['layouts'] if x['id']==m['layout']);users=[f.parent.name for f in (ROOT/'data/maps').glob('*/map.json') if load(f)['layout']==l['id']]
  if len(users)>1:
   l=copy.deepcopy(l);l['id']='LAYOUT_HYPER_CANARY4_'+re.sub(r'(?<!^)(?=[A-Z])','_',n).upper();l['name']='HyperCanary4'+n+'_Layout';ls['layouts'].append(l);m['layout']=l['id']
  assert [l['width'],l['height']]==source['dimensions'],(n,l,source)
  l.update(primary_tileset=source['primary_tileset'],secondary_tileset=source['secondary_tileset'],blockdata_filepath=source['blockdata_path'],border_filepath=source['border_path']);maps[n]=m
  if any(p['map']==n for p in patches):l['blockdata_filepath']=f'data/hyper_assets/canary4_layouts/{n}/map.bin'
 gates=[]
 for n,indices in EXTRAS.items():
  g=grids[n]
  for number,index in enumerate(indices,1):
   w=next(x for x in donors[n]['warps'] if x['index']==index);d,dp=P.C.donor(w['target_id']);label=f'{n}_EventScript_HyperConstruction_{number}';e=P.new_scientist(n,number,w['x'],w['y']+2 if n=='Route110' else w['y'],label);assert g.walk(e['x'],e['y']) or n=='SlateportCity' and g.cell(e['x'],e['y'])['translated_behavior']==0x69,(n,w,g.cell(e['x'],e['y']));assert g.neighbors(e['x'],e['y'])
   assert not any((z['x'],z['y'])==(e['x'],e['y']) for z in maps[n]['object_events']);maps[n]['object_events'].append(e)
   name='Harbor annex' if n=='SlateportCity' else d['name'];name=name if len(name)<=25 else 'This extra area'
   scripts[n]+=f'\n@ Project-owned reservation; no donor gameplay, flags or warp destination.\n{label}::\n\tlock\n\tfaceplayer\n\tmsgbox {n}_Text_HyperConstruction_{number}, MSGBOX_DEFAULT\n\trelease\n\tend\n\n{n}_Text_HyperConstruction_{number}:\n\t.string "{name} is\\n"\n\t.string "under construction.\\p"\n\t.string "Please check back later!$"\n'
   gates.append({'map':n,'donor_id':TARGETS[n],'scientist':e,'source_warp':w,'reserved_donor_name':d['name'],'reserved_donor_id':w['target_id'],'display_name':name,'destination_reference_json':dp,'source_cell':g.cell(e['x'],e['y']),'status':'ENTRANCE_RESERVED_BLOCKED_NO_WARP','reason':'Actual source entrance occupied by permanent project-owned scientist; destination is reference only, including Mt. Silver. No new region/map registration.'})
 return b,cat,ls,maps,ledger,grids,scripts,gates,patches

def trace(grids,scripts,n,start,labels,boat=False):
 x,y=start;records=[];blocks=P.C.movement_blocks(scripts[n]);l,old=original_grid(n)
 for label in labels:
  label=n+'_Movement_'+label
  for cmd in blocks[label]:
   r=re.search(r'_(up|down|left|right)$',cmd)
   if not r or not cmd.startswith(('walk_','jump_')) or 'in_place' in cmd:continue
   dx,dy={'up':(0,-1),'down':(0,1),'left':(-1,0),'right':(1,0)}[r[1]];x+=dx;y+=dy
   if not(0<=x<grids[n].w and 0<=y<grids[n].h):
    assert boat or n=='MauvilleCity' and 'Exit' in label and x<0,(n,label,x,y);records.append({'xy':[x,y],'native_offscreen':True});continue
   v=grids[n].cell(x,y);permit=grids[n].walk(x,y) or boat and v['collision']==0 or v['translated_behavior'] in [0x60,0x69]
   if not permit:
    a=old[y*l['width']+x];permit=((a>>10)&3)==v['collision'] and (boat or 'Exit' in label or n=='SlateportCity_Harbor' and 'Board' in label);v['native_original_block']=a
   assert permit,(n,label,cmd,v);records.append(v)
 return {'map':n,'start':list(start),'labels':labels,'end':[x,y],'cells':records}

def scenes(grids,scripts):
 out=[]
 def add(n,xy,labels,**kw):q=trace(grids,scripts,n,xy,labels,**kw);out.append(q);return q['end']
 for i,x in enumerate([33,34,35],1):
  p=add('Route110',(34,54),['RivalApproachPlayer'+str(i)]);assert p==[x,55];add('Route110',p,['RivalExit'+str(i)])
 for i in range(1,5):
  p=add('Route110',(9,79),['BirchEntrance','BirchApproachPlayer'+str(i)]);assert p==[6+i,84];add('Route110',p,['BirchExit'+str(i)])
 for side in ['North','East']:
  p=add('MauvilleCity',(8,6),['WallyExit'+side+'1']);add('MauvilleCity',p,['WallyExit'+side+'2'])
  p=add('MauvilleCity',(9,6),['WallysUncleExit'+side+'1','WallysUncleApproachPlayer'+side]);add('MauvilleCity',p,['WallysUncleExit'+side+'2'])
  p=add('MauvilleCity',(12,13),['ScottApproachPlayer'+side]);add('MauvilleCity',p,['ScottExit'+side])
 add('GraniteCave_StevensRoom',(7,8),['StevenExit']);add('GraniteCave_StevensRoom',(7,8),['StevenExitSouth'])
 add('SlateportCity',(28,14),['GabbyExit']);add('SlateportCity',(29,13),['TyExit']);add('SlateportCity',(28,13),['SternWatchGabbyAndTyExit','SternEnterHarbor'])
 add('SlateportCity',(10,12),['ScottExitBattleTent','ScottExitAfterBattleTent'])
 for x in [22,23]:p=add('SlateportCity',(x,27),['ScottApproachPlayer']);add('SlateportCity',p,['ScottExit'])
 for i in ['0','1','']:add('SlateportCity_Harbor',(6,13),['SternApproachPlayer'+i])
 add('SlateportCity_Harbor',(7,10),['AquaBoardSub'],boat=True);add('SlateportCity_Harbor',(8,10),['ArchieBoardSub'],boat=True);add('SlateportCity_Harbor',(7,9),['SubmarineExit'],boat=True)
 for n,xy,labels in [('DewfordTown',(11,10),['PlayerBoardBoat']),('DewfordTown',(12,9),['BrineyBoardBoat']),('DewfordTown',(12,8),['BrineyExitBoat']),('DewfordTown',(12,11),['ExitBoatPetalburg']),('DewfordTown',(12,11),['ExitBoatSlateport']),('DewfordTown',(12,8),['SailToSlateport']),('DewfordTown',(12,8),['SailToPetalburg']),('Route109',(21,24),['BrineyEnterBoat']),('Route109',(21,26),['BrineyExitBoat']),('Route109',(21,26),['PlayerExitBoat']),('Route109',(21,26),['SailToDewford'])]:add(n,xy,labels,boat=True)
 for n,xy,labels in [('SlateportCity_OceanicMuseum_2F',(6,1),['FirstGruntEnter','FirstGruntApproach','GruntApproachToBattle','GruntDefeated']),('SlateportCity_OceanicMuseum_2F',(6,1),['SecondGruntEnter','SecondGruntApproach','GruntApproachToBattle','GruntDefeated','GruntMoveForArchie']),('SlateportCity_OceanicMuseum_2F',(6,1),['ArchieEnter','ArchieApproachPlayer']),('SlateportCity_OceanicMuseum_2F',(13,5),['PlayerApproachGruntSouth']),('SlateportCity_OceanicMuseum_2F',(14,6),['PlayerApproachGruntWest']),('SlateportCity_OceanicMuseum_1F',(9,4),['FamiliarGruntExit']),('SlateportCity_OceanicMuseum_1F',(9,4),['FamiliarGruntExitNorth'])]:add(n,xy,labels)
 # Museum actors are staged at the native stairs; full Aqua scene retains native byte ownership.
 for n in ['SlateportCity_OceanicMuseum_1F','SlateportCity_OceanicMuseum_2F']:
  m=load(OUT/'original'/f'data/maps/{n}/map.json');print('Museum native scene actors',n,[(x.get('local_id'),x['x'],x['y']) for x in m['object_events']])
 return out

def graphics(cat,maps,ledger):
 # Reuse the proven art-only adapter generator, but explicitly curate sprite roles.
 role={'OBJ_EVENT_GFX_SCIENTIST_1':46,'OBJ_EVENT_GFX_MAN_2':23,'OBJ_EVENT_GFX_STEVEN':129,'OBJ_EVENT_GFX_ARCHIE':195,'OBJ_EVENT_GFX_RIVAL_BRENDAN_NORMAL':100,'OBJ_EVENT_GFX_RIVAL_MAY_NORMAL':105}
 constants=(ROOT/'include/constants/event_objects.h').read_text();base=re.search(r'enum\s*\{(.*?)\};',constants,re.S)[1];symbols=re.findall(r'\bOBJ_EVENT_GFX_\w+',base);ordinary={name:i for i,name in enumerate(symbols[:70]) if not any(t in name for t in ['BRENDAN','QUINTY','RAYQUAZA','MAY','LINK_'])}
 safe=[];retained=[]
 for e in ledger:
  if e['kind']!='object_events':continue
  q=copy.deepcopy(e);gfx=q['after']['graphics_id'];p=q['donor_reference']
  if gfx.startswith('OBJ_EVENT_GFX_VAR_') or gfx in ['OBJ_EVENT_GFX_SS_TIDAL','OBJ_EVENT_GFX_SUBMARINE_SHADOW','OBJ_EVENT_GFX_ZIGZAGOON','OBJ_EVENT_GFX_WINGULL','OBJ_EVENT_GFX_WALLY','OBJ_EVENT_GFX_WATTSON','OBJ_EVENT_GFX_BRAWLY','OBJ_EVENT_GFX_SCOTT','OBJ_EVENT_GFX_LASS','OBJ_EVENT_GFX_HIKER','OBJ_EVENT_GFX_BLACK_BELT','OBJ_EVENT_GFX_SAILOR','OBJ_EVENT_GFX_CYCLING_TRIATHLETE_M','OBJ_EVENT_GFX_CYCLING_TRIATHLETE_F']:
   retained.append({'map':q['map'],'graphics_id':gfx,'reason':'Native story/species/dynamic/bike sprite contract retained; donor role not assumed.'});continue
  if gfx in role:q['donor_reference']={'graphics_id':role[gfx]}
  elif gfx in ordinary:q['donor_reference']={'graphics_id':ordinary[gfx]}
  elif not p or gfx in ['OBJ_EVENT_GFX_ITEM_BALL','OBJ_EVENT_GFX_BERRY_TREE','OBJ_EVENT_GFX_MR_BRINEYS_BOAT']:pass
  elif gfx not in ['OBJ_EVENT_GFX_NURSE','OBJ_EVENT_GFX_MART_EMPLOYEE']:
   # Source event indices are reference, never sufficient evidence for unrelated art roles.
   continue
  safe.append(q)
 for gfx,i in [('OBJ_EVENT_GFX_RIVAL_BRENDAN_NORMAL',100),('OBJ_EVENT_GFX_RIVAL_MAY_NORMAL',105)]:safe.append({'map':'Route110','kind':'object_events','after':{'graphics_id':gfx},'donor_reference':{'graphics_id':i}})
 # MAN_2 should be staff in shipyard/Bike Shop and gym guide116 in gyms.
 old=P.TARGETS;P.TARGETS=TARGETS
 try:
  text,bind,audit,other=P.graphics(cat,maps,safe)
 finally:P.TARGETS=old
 # Proven runtime adapters preserve native animation tables and dimensions. Replace staff role where needed.
 text=text.replace('Canary #3','Canary #4').replace('gHyperCanary3Graphics','gHyperCanary4Graphics');bind=bind.replace('gHyperCanary3Graphics','gHyperCanary4Graphics')
 for a in audit:
  if a['map'] in ['DewfordTown_Gym','MauvilleCity_Gym'] and a['graphics_id']=='OBJ_EVENT_GFX_MAN_2':
   symbol='gHyperCanary4Graphics_'+a['map']+'_MAN_2';pattern=r'(static const struct ObjectEventGraphicsInfo '+symbol+r' = \{)(.*?)(\};)';o=next(x for x in cat['object_graphics'] if x['source_graphics_id']==116)
   def guide(m):
    body=re.sub(r'(\.images\s*=\s*)\w+',lambda z:z[1]+'sPicTable_HyperAsset116',m[2]);body=re.sub(r'(\.paletteTag\s*=\s*)[^,]+',lambda z:z[1]+f'0x{o["palette_tag"]:04X}',body);a['source_graphics_id']=116;a['replacement']=body;return m[1]+body+m[3]
   text=re.sub(pattern,guide,text,flags=re.S)
 # Native runtime resolves gender/starter and bicycle GFX; preserve bike frames until proven compatible bank art exists.
 return text,bind,audit,retained+other

def geometry_checks(grids,maps):
 g=grids['Route110'];closed={(e['x'],e['y']) for e in maps['Route110']['coord_events'] if 'RivalTrigger' in e['script']}
 def reach(block):
  q=collections.deque([(17,99,3)]);seen=set(q)
  while q:
   x,y,e=q.popleft()
   for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
    if not(0<=a<g.w and 0<=b<g.h) or (a,b) in block:continue
    v=g.cell(a,b);el=v['elevation'];ne=e if el in [0,15] else el;state=(a,b,ne)
    if not g.walk(a,b) or el not in [0,15,e] or state in seen:continue
    seen.add(state);q.append(state)
  return seen
 full=reach(set());locked=reach(closed);assert any(y==0 for x,y,e in full) and not any(y==0 for x,y,e in locked),'Native rival can be bypassed on early land route.'
 l,old=original_grid('MauvilleCity_Gym');gym=grids['MauvilleCity_Gym'];assert all((a&4095)==(b&4095) for i,(a,b) in enumerate(zip(old,gym.blocks)) if 5<=i//gym.w<17 and i%gym.w<9),'Native puzzle metatile/collision grid differs.'
 seams=[];allmaps={load(f)['id']:f.parent.name for f in (ROOT/'data/maps').glob('*/map.json')};oldls=load(OUT/'original/data/layouts/layouts.json')['layouts']
 for n,m in maps.items():
  g=grids[n]
  for conn in m['connections'] or []:
   native_layout,native_blocks=original_grid(n)
   dest=allmaps[conn['map']];dm=maps.get(dest,load(ROOT/f'data/maps/{dest}/map.json'));dl=next(z for z in oldls if z['id']==load((OUT/'original' if dest in TARGETS else ROOT)/f'data/maps/{dest}/map.json')['layout']);db=words(ROOT/dl['blockdata_filepath']);dg=grids.get(dest);direction=conn['direction'];off=conn['offset'];cross=[]
   for x,y in ([(x,0 if direction=='up' else g.h-1) for x in range(g.w)] if direction in ['up','down'] else [(0 if direction=='left' else g.w-1,y) for y in range(g.h)]):
    dx,dy=(x-off,dl['height']-1 if direction=='up' else 0) if direction in ['up','down'] else (dl['width']-1 if direction=='left' else 0,y-off)
    if not(0<=dx<dl['width'] and 0<=dy<dl['height']):continue
    a=g.cell(x,y)['block'];b=dg.cell(dx,dy)['block'] if dg else db[dy*dl['width']+dx]
    if ((a>>10)&3)==0 and ((b>>10)&3)==0:
     compatible=a>>12==b>>12 or a>>12 in [0,15] or b>>12 in [0,15]
     original_a=native_blocks[y*g.w+x];original_b=db[dy*dl['width']+dx]
     assert compatible or (a>>12,b>>12)==(original_a>>12,original_b>>12),(n,dest,x,y,hex(a),hex(b))
     cross.append({'from':[x,y],'to':[dx,dy],'elevations':[a>>12,b>>12],'elevation_compatible':compatible,'native_elevation_pair':[original_a>>12,original_b>>12]})
   assert cross,(n,dest,'No crossable native connection boundary')
   seams.append({'from':n,'to':dest,'native_connection':conn,'crossing_cells':cross})
 return {'route110_rival_land_gate':{'start':[17,99,3],'open_reachable_states':len(full),'locked_reachable_states':len(locked),'north_reachable_without_rival_trigger':False,'model':'Collision/water/elevation-aware cardinal land traversal; elevation 0/15 inherit current elevation. Cycling entrances retain native bicycle checks.'},'mauville_puzzle':{'native_puzzle_grid_metatile_and_collision_exact':True,'puzzle_bounds':[0,5,8,16],'native_press_switch_default_alt_deactivation_code_preserved':True},'connection_checks':seams}

def apply():
 b,cat,ls,maps,ledger,grids,scripts,gates,patches=prepare();paths=scenes(grids,scripts);geometry=geometry_checks(grids,maps);text,bind,ga,ret=graphics(cat,maps,ledger)
 private={}
 for n in {p['map'] for p in patches}:
  f=f'data/hyper_assets/canary4_layouts/{n}/map.bin';p=ROOT/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(struct.pack('<'+'H'*len(grids[n].blocks),*grids[n].blocks));private[f]=digest(p)
 for n,m in maps.items():dump(ROOT/f'data/maps/{n}/map.json',m)
 dump(ROOT/'data/layouts/layouts.json',ls)
 for n in {*EXTRAS,'MauvilleCity'}:(ROOT/f'data/maps/{n}/scripts.inc').write_text(scripts[n])
 af='src/data/object_events/hyper_canary4_graphics.inc';(ROOT/af).write_text(text)
 p=ROOT/'src/hyper_asset_graphics_bindings.inc';p.write_text(p.read_text()+'\n/* Dewford–Mauville native gameplay ownership. */\n'+bind)
 p=ROOT/'src/data/object_events/hyper_assets.inc';p.write_text(p.read_text().replace('struct HyperAssetGraphicsBinding\n','#include "hyper_canary4_graphics.inc"\n\nstruct HyperAssetGraphicsBinding\n'))
 dump(OUT/'coordinate_remap_ledger.json',{'schema':1,'events':ledger,'geometry_compatibility_patches':patches,'construction_gates':gates,'geometry_script_edits':[{'map':'MauvilleCity','label':'MauvilleCity_Movement_ScottExitNorth','inserted_command':'walk_down','reason':'Exit along open row8 around Hyper west-boundary hedge; native flags/removal unchanged.'}],'geometry_checks':geometry,'native_scene_paths':paths,'graphics_adapters':ga,'native_graphics_retained':ret,'hyper_gameplay_imported':False})
 with (OUT/'coordinate_remap_ledger.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['map','kind','index','role','old_x','old_y','new_x','new_y','reason'])
  for e in ledger:w.writerow([e['map'],e['kind'],e['index'],e['after'].get('script',e['after'].get('dest_map',e['after'].get('item'))),e['before']['x'],e['before']['y'],e['after']['x'],e['after']['y'],e['reason']])
 dump(OUT/'receipt.json',{'schema':'hyper-hoenn-canary4-receipt-v1','canonical_maps_replaced':list(TARGETS),'donor_ids':TARGETS,'runtime_verified':False,'hyper_gameplay_imported':False,'graphics_binding_maps':sorted({x['map'] for x in ga}|{x['map'] for x in gates}),'changed_baseline_files':{f:{'before':b[f],'after':digest(ROOT/f)} for f in CHANGED},'new_files':{af:digest(ROOT/af),**private},'map_ids_header_sha256':digest(ROOT/'include/constants/map_groups.h'),'map_groups_json_sha256':digest(ROOT/'data/maps/map_groups.json'),'layout_count_before_after':[len(load(OUT/'original/data/layouts/layouts.json')['layouts']),len(ls['layouts'])]})
 manifest=[]
 for n,k in TARGETS.items():
  m=maps[n];d=P.C.donor(k)[0];l=next(x for x in ls['layouts'] if x['id']==m['layout']);manifest.append({'canonical_name':n,'canonical_id':m['id'],'donor_identity':'HYPER_EMERALD_V5_7_EN_QOL','donor_id':k,'donor_name':d['name'],'donor_header_reference':{key:v for key,v in d.items() if 'pointer' in key},'dimensions':[l['width'],l['height']],'map_type':m['map_type'],'tilesets':[l['primary_tileset'],l['secondary_tileset']],'layout':l,'blockdata_sha256':digest(ROOT/l['blockdata_filepath']),'border_sha256':digest(ROOT/l['border_filepath']),'donor_event_counts':d['event_counts'],'donor_map_scripts_reference_only':d['map_scripts'],'event_counts':{key:len(m[key]) for key in ['object_events','warp_events','coord_events','bg_events']},'warps':m['warp_events'],'connections':m['connections'],'confidence':'HIGH','script_owner':n+'_MapScripts','runtime_verified':False,'reserved_extra_entrances':[g for g in gates if g['map']==n]})
 dump(OUT/'dewford_mauville_spine_manifest.json',{'schema':1,'maps':manifest,'hyper_gameplay_imported':False,'runtime_verified':False})
 print('Applied',len(TARGETS),'canonical maps;',len(gates),'construction gates')

def validate():
 b=load(OUT/'baseline.json');r=load(OUT/'receipt.json');assert set(r['changed_baseline_files'])==set(CHANGED)
 for f,h in b.items():assert digest(ROOT/f)==P.C.C.editor_canary_hash(f,r['changed_baseline_files'].get(f,r.get('external_workspace_changes',{}).get(f,{})).get('after',h)),f
 for f,h in r['new_files'].items():assert digest(ROOT/f)==h,f
 assert digest(ROOT/'include/constants/map_groups.h')==r['map_ids_header_sha256'];assert digest(ROOT/'data/maps/map_groups.json')==r['map_groups_json_sha256']
 ledger=load(OUT/'coordinate_remap_ledger.json')
 for n in TARGETS:
  a=load(OUT/'original'/f'data/maps/{n}/map.json');z=load(ROOT/f'data/maps/{n}/map.json')
  for key in a:
   if key=='layout':continue
   if key.endswith('_events'):
    assert [{k:v for k,v in e.items() if k not in ['x','y']} for e in a[key]]==[{k:v for k,v in e.items() if k not in ['x','y']} for e in z[key][:len(a[key])]],(n,key)
    assert z[key][len(a[key]):]==([g['scientist'] for g in ledger['construction_gates'] if g['map']==n]+P.C.C.corridor_gates(n) if key=='object_events' else [])
   else:assert a[key]==z[key],(n,key)
  script=(ROOT/f'data/maps/{n}/scripts.inc').read_text().split('\n@ Project-owned reservation;')[0]
  if n=='MauvilleCity':script=script.replace('MauvilleCity_Movement_ScottExitNorth:\n\twalk_down\n','MauvilleCity_Movement_ScottExitNorth:\n',1)
  assert script==(OUT/'original'/f'data/maps/{n}/scripts.inc').read_text(),n
 old=load(OUT/'original/data/layouts/layouts.json')['layouts'];new=load(ROOT/'data/layouts/layouts.json')['layouts'];changedids={load(OUT/'original'/f'data/maps/{n}/map.json')['layout'] for n in TARGETS if load(ROOT/f'data/maps/{n}/map.json')['layout']==load(OUT/'original'/f'data/maps/{n}/map.json')['layout']}
 for a,z in zip(old,new):
  assert a['id']==z['id']
  if a['id'] not in changedids|set(P.C.C.corridor_layout_ids()):assert a==z
  else:assert {k:v for k,v in a.items() if k not in ['primary_tileset','secondary_tileset','blockdata_filepath','border_filepath']}=={k:v for k,v in z.items() if k not in ['primary_tileset','secondary_tileset','blockdata_filepath','border_filepath']}
 result={'passed':True,'protected_files_checked':len(b),'canonical_maps_replaced':len(TARGETS),'native_events':len(ledger['events']),'construction_scientists':len(ledger['construction_gates']),'canonical_map_ids_unchanged':True,'native_story_flags_vars_save_warp_connections_ownership_preserved':True,'hyper_gameplay_imported':False,'runtime_verified':False};dump(OUT/'validation.json',result);print(json.dumps(result,indent=2));return result

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--apply',action='store_true');a.add_argument('--validate',action='store_true');v=a.parse_args()
 if v.apply:apply()
 elif v.validate:validate()
 else:
  b,cat,ls,maps,ledger,grids,scripts,gates,patches=prepare();scenes(grids,scripts);geometry_checks(grids,maps);graphics(cat,maps,ledger);print('Preflight passed; no map writes.')
