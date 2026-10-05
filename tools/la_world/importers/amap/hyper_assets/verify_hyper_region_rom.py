#!/usr/bin/env python3
"""Check current editor assets, linked ROM bytes and native ownership receipts."""
import argparse,re,struct,subprocess,json
import hoenn_finalization as F
R=F.R

def verify(stem):
 rec=F.load(F.O/'receipt.json');data=F.load(F.O/'reconciliation.json');F.audit();maps={p.parent.name:F.load(p) for p in (R/'data/maps').glob('*/map.json') if F.load(p).get('warp_events') is not None};ids={m['id']:n for n,m in maps.items()};groups=F.load(R/'data/maps/map_groups.json');numeric={maps[n]['id']:(gi,mi) for gi,g in enumerate(groups['group_order']) for mi,n in enumerate(groups[g]) if n in maps};layouts={x['id']:x for x in F.load(R/'data/layouts/layouts.json')['layouts']};header=(R/'src/data/tilesets/headers.h').read_text();meta=(R/'src/data/tilesets/metatiles.h').read_text();graphics=(R/'src/data/tilesets/graphics.h').read_text();decl=dict(re.findall(r'const struct Tileset\s+(\w+)\s*=\s*\{(.*?)\};',header,re.S));cache={}
 def assets(s):
  if s in cache:return cache[s]
  body=decl[s];a={}
  for field,text in [('tiles',graphics),('metatiles',meta),('metatileAttributes',meta)]:
   sy=re.search(r'\.'+field+r'\s*=\s*(\w+)',body)[1];path=re.search(re.escape(sy)+r'\[\]\s*=\s*INCBIN_U(?:16|32)\("([^"]+)"\)',text)[1];a[field]=(R/path).read_bytes()
   if field=='tiles':assert (R/path).parent.joinpath('tiles.png').exists()
  sy=re.search(r'\.palettes\s*=\s*(\w+)',body)[1];pb=re.search(re.escape(sy)+r'\[\]\[16\]\s*=\s*\{(.*?)\};',graphics,re.S)[1];paths=re.findall(r'INCBIN_U16\("([^"]+)"\)',pb);assert len(paths)==13
  for path in paths:assert (R/path).with_suffix('.pal').exists()
  a['palettes']=b''.join((R/p).read_bytes() for p in paths);a['callback']=re.search(r'\.callback\s*=\s*(\w+)',body)[1];cache[s]=a;return a
 raw=subprocess.check_output(['arm-none-eabi-nm','-n','--defined-only',str(R/(stem+'.elf'))],text=True);symbols={s[2]:int(s[0],16) for line in raw.splitlines() if len(s:=line.split())==3};rom=(R/(stem+'.gba')).read_bytes()
 def blob(a,n):assert 0x08000000<=a<=a+n<=0x08000000+len(rom);return rom[a-0x08000000:a-0x08000000+n]
 def u32(a):return struct.unpack('<I',blob(a,4))[0]
 checked=[];objects=warps=connections=0
 for n,m in maps.items():
  l=layouts[m['layout']]
  if not l['primary_tileset'].startswith('gTileset_Hyper_'):continue
  gi,mi=numeric[m['id']];hp=u32(u32(symbols['gMapGroups']+gi*4)+mi*4);assert hp==symbols[n];lp=u32(hp);assert lp==symbols[l['name']];assert (u32(lp),u32(lp+4))==(l['width'],l['height']);assert u32(hp+8)==symbols[n+'_MapScripts']
  for off,key in [(8,'border_filepath'),(12,'blockdata_filepath')]:expected=(R/l[key]).read_bytes();assert blob(u32(lp+off),len(expected))==expected
  blocks=F.words(R/l['blockdata_filepath']);assert len(blocks)==l['width']*l['height'];attrs=[]
  for off,key in [(16,'primary_tileset'),(20,'secondary_tileset')]:
   s=l[key];a=assets(s);ts=u32(lp+off);assert ts==symbols[s]
   for po,field in [(4,'tiles'),(8,'palettes'),(12,'metatiles'),(16,'metatileAttributes')]:assert blob(u32(ts+po),len(a[field]))==a[field],(n,field)
   assert u32(ts+20)==(0 if a['callback']=='NULL' else symbols[a['callback']]|1);attrs.append(list(struct.unpack('<'+'H'*(len(a['metatileAttributes'])//2),a['metatileAttributes'])))
  for v in blocks:
   t=v&1023;assert t%512<len(attrs[t//512]),(n,t);assert t%512<len(assets(l[['primary_tileset','secondary_tileset'][t//512]])['metatiles'])//16,(n,t,'metatile graphics bounds')
  ep=u32(hp+4);assert list(blob(ep,4))==[len(m[k]) for k in ['object_events','warp_events','coord_events','bg_events']];op=u32(ep+4);wp=u32(ep+8)
  for i,e in enumerate(m['object_events']):
   v=blob(op+i*24,24);assert struct.unpack_from('<hh',v,4)==(e['x'],e['y']);assert v[8]==e['elevation'];expected=int(e['script'],16) if e['script'].startswith('0x') else symbols[e['script']];assert struct.unpack_from('<I',v,16)[0]==expected;objects+=1
  for i,e in enumerate(m['warp_events']):
   v=blob(wp+i*8,8);assert struct.unpack_from('<hh',v)==(e['x'],e['y']);assert v[4]==e['elevation']
   if e['dest_map']=='MAP_DYNAMIC':assert v[6:8]==bytes([127,127]);warps+=1;continue
   assert v[5]==int(e['dest_warp_id']);assert (v[7],v[6])==numeric[e['dest_map']];dest=maps[ids[e['dest_map']]];assert 0<=int(e['dest_warp_id'])<len(dest['warp_events']),(n,i,e);warps+=1
  if m['connections']:
   cp=u32(hp+12);assert u32(cp)==len(m['connections']);table=u32(cp+4)
   for i,e in enumerate(m['connections']):v=blob(table+i*12,12);assert struct.unpack_from('<i',v,4)[0]==e['offset'];assert (v[8],v[9])==numeric[e['map']];connections+=1
  else:assert u32(hp+12)==0
  checked.append(n)
 # Every indoor asset port retains the complete native collision/elevation/behavior grid.
 oldls={x['id']:x for x in F.load(F.O/'original/data/layouts/layouts.json')['layouts']};native_cells=0
 for n in rec['donor_ids']:
  before=F.load(F.O/f'original/data/maps/{n}/map.json');m=maps[n];assert m['id']==before['id'];assert m['connections']==before['connections'];path=f'data/maps/{n}/scripts.inc';assert F.digest(R/path)==rec['baseline'][path],(n,'Native script changed')
  for k in ['object_events','warp_events','coord_events','bg_events']:
   assert len(m[k])==len(before[k]);assert all({a:b for a,b in e.items() if a not in ['x','y','elevation']}=={a:b for a,b in o.items() if a not in ['x','y','elevation']} for e,o in zip(m[k],before[k])),(n,k)
  if n in ['BattleFrontier_OutsideWest','BattleFrontier_OutsideEast']:continue
  ng=F.grid(oldls[before['layout']],header,meta);dg=F.grid(layouts[m['layout']],header,meta);assert (ng.w,ng.h)==(dg.w,dg.h)
  assert all((a&0xfc00)==(b&0xfc00) and (ng.attrs[(a&1023)//512][a&511]&255)==(dg.attrs[(b&1023)//512][b&511]&255) for a,b in zip(ng.blocks,dg.blocks)),n;native_cells+=len(dg.blocks)
 sections=F.load(R/'src/data/region_map/region_map_sections.json')['map_sections'];assert sections[218]['id']=='MAPSEC_NONE';assert len(sections)<253
 import test_hyper_assets as T
 plan=F.load(R/'.la_work/amap/hyper_asset_integration/reborn_hyper_asset_integration_plan.json');sinnoh_path=R/'.la_work/amap/hyper_sinnoh_asset_travel/receipt.json'
 if sinnoh_path.exists():
  sinnoh=F.load(sinnoh_path);plan=__import__('copy').deepcopy(plan);plan['tilesets']+=sinnoh['asset_banks'];manifest=F.load(R/'.la_work/amap/hyper_sinnoh_asset_travel/manifest.json');plan['layouts'] += [{'primary_tileset':z['tilesets'][0],'secondary_tileset':z['tilesets'][1]} for z in manifest['maps']]
 # Include previously recovered side-system banks absent from the historical Hoenn plan.
 plan['tilesets']=[{'symbol':s,'callback':re.search(r'\.callback\s*=\s*(\w+)',b)[1]} for s,b in decl.items() if s.startswith('gTileset_Hyper_')]
 plan['layouts']=[l for l in layouts.values() if l['primary_tileset'].startswith('gTileset_Hyper_') and l['secondary_tileset'].startswith('gTileset_Hyper_')]
 animation=T.animation_host_test(plan)
 result={'passed':True,'linked_maps':len(checked),'linked_tilesets':len(cache),'linked_objects':objects,'linked_warps':warps,'linked_connections':connections,'native_cell_contracts_checked':native_cells,'canonical_asset_ports':len(rec['donor_ids']),'animation':animation,'rom_sha256':F.digest(R/(stem+'.gba')),'rom_bytes':len(rom),'runtime_verified':False};F.dump(F.O/'validation.json',result);print(json.dumps(result,indent=2));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--rom-stem',default='pokeemerald-hoenn-finalization');a=p.parse_args();verify(a.rom_stem)
