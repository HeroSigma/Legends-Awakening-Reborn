#!/usr/bin/env python3
"""Verify Mercury replacement ownership, identities, linked assets and static travel."""
import argparse,hashlib,json,re,struct,subprocess,collections
from pathlib import Path
from replace_johto_mercury import R,D,B,S,load,dump
from hyper_assets.port_hyper_assets import enums

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--rom-stem',default='pokeemerald');a=ap.parse_args();plan=load(D/'replacement_plan.json');before=load(B/'before.json');groups=load(R/'data/maps/map_groups.json');layouts={l['id']:l for l in load(R/'data/layouts/layouts.json')['layouts']};maps={p.parent.name:load(p) for p in (R/'data/maps').glob('*/map.json')};allids={m['id']:m for m in maps.values()};numeric={maps[name]['id']:(i,j) for i,g in enumerate(groups['group_order']) for j,name in enumerate(groups[g])};oldgroups=before['groups'];n=enums(R/'include/constants/metatile_behaviors.h')
 assert groups['group_order'][:len(oldgroups['group_order'])]==oldgroups['group_order']
 for g in oldgroups['group_order']:assert groups[g][:len(oldgroups[g])]==oldgroups[g]
 for g in groups['group_order']:assert len(groups[g])<=127 and groups['group_order'].index(g)<127
 # Build-generated metadata is allowed to grow; hand-authored non-Johto sources aren't.
 derived=lambda rel: rel in ['data/layouts/layouts_table.inc','data/layouts/layouts.inc','data/maps/groups.inc','src/data/map_group_count.h','include/constants/map_groups.h','include/constants/layouts.h','include/constants/map_event_ids.h','data/maps/events.inc','data/maps/headers.inc','data/maps/connections.inc'] or (rel.startswith('data/maps/') and Path(rel).name in ['events.inc','header.inc','connections.inc'])
 changes=[]
 for rel,h in before['protected'].items():
  if hashlib.sha256((R/rel).read_bytes()).hexdigest()!=h:
   if rel=='src/regional_map_names.c':
    text=(R/rel).read_text().replace('#include "mercury_johto_names.inc"\n\n','').replace('    const u8 *mercuryName = MercuryJohtoDisplayName(header->mapLayoutId);\n    u32 i;\n    if (mercuryName != NULL)\n        return mercuryName;\n','    u32 i;\n');assert text==(B/rel).read_text()
   elif rel=='src/new_game.c' and (R/'docs/la_world/mercury_johto/exploration_start.json').exists():
    exploration=load(R/'docs/la_world/mercury_johto/exploration_start.json')
    assert hashlib.sha256((R/'.la_work/amap/mercury_exploration_backup/new_game.c').read_bytes()).hexdigest()==h
    assert hashlib.sha256((R/rel).read_bytes()).hexdigest()==exploration['new_game_sha256']
   elif rel=='src/tileset_anims.c':
    assert (R/rel).read_text().replace('\n#include \"hns_canary_anims.inc\"\n','')==(R/'.la_work/amap/hns_canary_backup'/rel).read_text()
   elif not derived(rel):changes.append(rel)
 assert not changes,('Protected source modifications',changes)
 rom=(R/(a.rom_stem+'.gba')).read_bytes();elf=R/(a.rom_stem+'.elf');symbols={z[2]:int(z[0],16) for line in subprocess.check_output(['arm-none-eabi-nm','--defined-only',str(elf)],text=True).splitlines() if len(z:=line.split())==3}
 def blob(ptr,count):
  assert 0x8000000<=ptr<=ptr+count<=0x8000000+len(rom),(hex(ptr),count)
  return rom[ptr-0x8000000:ptr-0x8000000+count]
 def u(ptr):return struct.unpack('<I',blob(ptr,4))[0]
 checkedbanks={};warps=cons=water=objects=visual_cells=0;heldids={maps[name]['id'] for name in plan['unmatched_registered']};native_source=load(S/'manifest.json');source={m['id']:m for m in native_source['maps']};sourcefolders={load(p)['id']:p.parent for p in (S/'maps').glob('*/map.json')};headers=(R/'src/data/tilesets/mercury_johto_headers.h').read_text();defs='\n'.join((R/f'src/data/tilesets/mercury_johto_{x}.h').read_text() for x in ['graphics','metatiles']);warp_cells=set()
 for k,name in plan['names'].items():
  m=maps[name];l=layouts[m['layout']];gi,mi=numeric[m['id']];gp=u(symbols['gMapGroups']+gi*4);assert gp,(name,m['id'],gi,mi,'empty native group');hp=u(gp+mi*4);assert hp==symbols[name];lp=u(hp);assert lp==symbols[l['name']];assert (u(lp),u(lp+4))==(l['width'],l['height']);assert l['width']==source[k]['width'] and l['height']==source[k]['height']
  for off,key in [(8,'border_filepath'),(12,'blockdata_filepath')]:
   data=(R/l[key]).read_bytes();assert blob(u(lp+off),len(data))==data,(name,key)
  for off,key in [(16,'primary_tileset'),(20,'secondary_tileset')]:
   label=l[key];ptr=u(lp+off);assert ptr==symbols[label];assert u(ptr+20)==0
   if label not in checkedbanks:
    body=re.search(re.escape(label)+r' = \{(.*?)\};',headers,re.S)[1]
    for po,field in [(4,'tiles'),(8,'palettes'),(12,'metatiles'),(16,'metatileAttributes')]:
     sy=re.search(r'\.'+field+r'=(\w+)',body)[1];assert u(ptr+po)==symbols[sy]
     if field!='palettes':
      path=re.search(r'const u(?:16|32) '+re.escape(sy)+r'\[\] = INCBIN_U(?:16|32)\("([^"\n]+)"\)',defs)[1];expected=(R/path).read_bytes();assert blob(symbols[sy],len(expected))==expected,(label,field)
     else:
      palette_body=re.search(r'const u16 '+re.escape(sy)+r'\[\]\[16\] = \{(.*?)\};',defs,re.S)[1];paths=re.findall(r'INCBIN_U16\("([^"\n]+)"\)',palette_body);expected=b''.join((R/p).read_bytes() for p in paths);assert len(expected)==512 and blob(symbols[sy],512)==expected
    checkedbanks[label]=ptr
  assert u(hp+8)==symbols[name+'_MapScripts'];assert blob(u(hp+8),1)==b'\0';assert not m['coord_events'] and not m['bg_events'];ep=u(hp+4);assert blob(ep,4)==bytes([len(m['object_events']),len(m['warp_events']),0,0]);cells=[v[0] for v in struct.iter_unpack('<H',(R/l['blockdata_filepath']).read_bytes())];attrs=b''.join(blob(u(checkedbanks[l[f]]+16),1024) for f in ['primary_tileset','secondary_tileset'])
  for index,e in enumerate(m['object_events']):
   assert e['graphics_id']=='OBJ_EVENT_GFX_SCIENTIST_1' and e['flag']=='0' and e['trainer_type']=='TRAINER_TYPE_NONE';assert 0<=e['x']<l['width'] and 0<=e['y']<l['height'];pos=e['y']*l['width']+e['x'];assert cells[pos]>>10&3==0 and cells[pos]>>12 in [0,3];assert cells[(e['y']+1)*l['width']+e['x']]>>10&3==0
   event=blob(u(ep+4)+index*24,24);assert struct.unpack_from('<H',event,20)[0]==0 and struct.unpack_from('<H',event,12)[0]==0;assert struct.unpack_from('<hh',event,4)==(e['x'],e['y']);assert u(u(ep+4)+index*24+16)==symbols[e['script']];objects+=1
  for index,e in enumerate(m['warp_events']):
   assert e['dest_map'] not in heldids;dest=allids[e['dest_map']];assert 0<=int(e['dest_warp_id'])<len(dest['warp_events']);record=blob(u(ep+8)+index*8,8);assert struct.unpack_from('<hh',record)==(e['x'],e['y']);assert record[5]==int(e['dest_warp_id']);assert (record[7],record[6])==numeric[e['dest_map']];assert record[4]==3;warp_cells.add((k,e['x'],e['y']));warps+=1
  con=m['connections'] or [];cp=u(hp+12)
  if con:
   assert u(cp)==len(con);records=u(cp+4)
   for index,e in enumerate(con):
    assert e['map'] not in heldids and e['map'] in allids;record=blob(records+index*12,12);assert record[0]=={'down':1,'up':2,'left':3,'right':4,'dive':5,'emerge':6}[e['direction']];assert struct.unpack_from('<i',record,4)[0]==e['offset'];assert (record[8],record[9])==numeric[e['map']];cons+=1
  else:assert cp==0
  script=(R/'data/maps'/name/'scripts.inc').read_text()
  commands={line.strip().split()[0] for line in script.splitlines() if line.startswith('\t')};assert commands<={'.byte','.string','lock','faceplayer','msgbox','goto_if_eq','closemessage','warp','waitstate','release','end'},(name,commands)
  # Every cell retains its original normalized art, including scoped warp clones.
  source_defs=b''.join((S/'tilesets'/source[k][f]/'metatiles.bin').read_bytes() for f in ['primary_tileset','secondary_tileset'])
  source_attrs=b''.join((S/'tilesets'/source[k][f]/'metatile_attributes.bin').read_bytes() for f in ['primary_tileset','secondary_tileset'])
  native_defs=b''.join(blob(u(checkedbanks[l[f]]+12),512*24) for f in ['primary_tileset','secondary_tileset'])
  original=(sourcefolders[k]/'blockdata.bin').read_bytes();artcache={}
  for i,(v,) in enumerate(struct.iter_unpack('<H',original)):
   pair=(v&1023,cells[i]&1023)
   if pair not in artcache:
    mid,newmid=pair;lo=list(struct.unpack_from('<4H',source_defs,mid*16));hi=list(struct.unpack_from('<4H',source_defs,mid*16+8));layer=struct.unpack_from('<H',source_attrs,mid*2)[0]>>12
    expected=([0x3014]*4+lo+hi) if layer==0 else (lo+[0]*4+hi) if layer==2 else (lo+hi+[0]*4)
    assert struct.pack('<12H',*expected)==native_defs[newmid*24:newmid*24+24],(name,pair,'changed art');artcache[pair]=True
   visual_cells+=1
  # Water must remain native Surf water unless this cell is an explicit travel warp.
  orig=(sourcefolders[k]/'blockdata.bin').read_bytes();aa=b''.join((S/'tilesets'/source[k][f]/'source_frlg_metatile_attributes.bin').read_bytes() for f in ['primary_tileset','secondary_tileset'])
  for i,(v,) in enumerate(struct.iter_unpack('<H',orig)):
   raw=struct.unpack_from('<I',aa,(v&1023)*4)[0]&511;new=cells[i]
   if raw in [0x10,0x11,0x12,0x13,0x15,0x1a,0x1b,0x50,0x51,0x52,0x53] and new>>10&3==0 and (k,i%l['width'],i//l['width']) not in warp_cells:
    assert new>>12 in [1,15],(name,i,raw,hex(new));water+=1
 for name in plan['unmatched_registered']:assert not maps[name]['warp_events'] and not maps[name]['connections']
 # Compare every pre-existing map identity directly with its exact pre-replacement JSON.
 for rel in before['backups']:
  if rel.startswith('data/maps/') and rel.endswith('/map.json'):
   old=load(B/rel);now=load(R/rel);assert old['id']==now['id'] and old['name']==now['name']
 for g in oldgroups['group_order']:
  for i,name in enumerate(oldgroups[g]):assert numeric[maps[name]['id']]==(oldgroups['group_order'].index(g),i)
 # A native-section GC change must retain every registered region's layout.
 table=(R/'data/maps/groups.inc').read_text().split('gMapGroups::',1)[1];entries=re.findall(r'\.4byte\s+(\w+)',table);assert len(entries)==len(groups['group_order']);disabled_groups=[]
 registered=0
 for group in groups['group_order']:
  gi=groups['group_order'].index(group)
  if entries[gi]=='NULL':
   assert u(symbols['gMapGroups']+gi*4)==0;disabled_groups.append(group);continue
  assert u(symbols['gMapGroups']+gi*4)==symbols[entries[gi]]
  for name in groups[group]:
   m=maps[name]
   if m['layout'] not in layouts:continue
   l=layouts[m['layout']];gi,mi=numeric[m['id']];gp=u(symbols['gMapGroups']+gi*4);assert gp,(name,m['id'],gi,mi,'empty native group');hp=u(gp+mi*4);assert hp==symbols[name];lp=u(hp);assert lp==symbols[l['name']];assert (u(lp),u(lp+4))==(l['width'],l['height'])
   for off,key in [(8,'border_filepath'),(12,'blockdata_filepath')]:
    expected=(R/l[key]).read_bytes();assert blob(u(lp+off),len(expected))==expected,(name,key,'region regression')
   for off,key in [(16,'primary_tileset'),(20,'secondary_tileset')]:assert u(lp+off)==symbols[l[key]]
   registered+=1
 result=dict(rom_sha256=hashlib.sha256(rom).hexdigest(),rom_size=len(rom),maps=len(plan['selected']),tilesets=len(checkedbanks),objects=objects,warps=warps,connections=cons,native_water_cells=water,visual_cells_preserved=visual_cells,all_active_region_layouts_verified=registered,configured_inactive_groups=disabled_groups,old_numeric_map_ids_preserved=True,other_region_sources_preserved=True,held_areas_have_no_active_entrances=True,donor_gameplay_imported=False,source_scripts='project-owned inspection only',runtime_verified=False)
 dump(D/'validation.json',result);print('PASS',result)
if __name__=='__main__':main()
