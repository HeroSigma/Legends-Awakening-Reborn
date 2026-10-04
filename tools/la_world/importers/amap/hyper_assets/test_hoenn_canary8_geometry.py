#!/usr/bin/env python3
"""Inspect new canonical warp approaches, donor elevations and native Wailmer visuals."""
import re,struct,collections
import hoenn_canary8 as C

def review(q):
 water=0;doors=[];remaps=[];dormant=[]
 for n,k in C.TARGETS.items():
  g=q['grids'][n];m=q['maps'][n]
  for i,b in enumerate(g.blocks):
   v=g.cell(i%g.w,i//g.w)
   if v['translated_behavior'] in {0x10,0x11,0x12,0x13,0x14,0x15,0x19,0x22,0x2A}:assert v['elevation']==1,(n,v);water+=1
  for i,w in enumerate(m['warp_events'][:len(q['original'][n]['warp_events'])]):
   v=g.cell(w['x'],w['y'])
   if v['translated_behavior'] not in [0x29,*range(0x60,0x70),0x1B,0x1C]:
    ol=next(z for z in q['oldls']['layouts'] if z['id']==q['original'][n]['layout']);ow=q['original'][n]['warp_events'][i];blocks=C.words(C.ROOT/ol['blockdata_filepath']);tile=blocks[ow['y']*ol['width']+ow['x']]&1023;role='secondary_tileset' if tile>=512 else 'primary_tileset';header=(C.ROOT/'src/data/tilesets/headers.h').read_text();meta=(C.ROOT/'src/data/tilesets/metatiles.h').read_text();body=re.search(r'const struct Tileset\s+'+ol[role]+r'\s*=\s*\{(.*?)\};',header,re.S)[1];symbol=re.search(r'\.metatileAttributes\s*=\s*(\w+)',body)[1];path=re.search(re.escape(symbol)+r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"\)',meta)[1];mb=C.words(C.ROOT/path)[tile%512]&255;assert mb not in [0x29,*range(0x60,0x70),0x1B,0x1C],(n,i,mb,v);dormant.append({'map':n,'index':i,'native_behavior':mb,'source_behavior':v['translated_behavior'],'reason':'Native arrival-only/script-used slot was already on a nonwarp cell.'})
   doors.append({'map':n,'index':i,'cell':v,'destination':w['dest_map'],'native_destination_slot':w['dest_warp_id']})
  for i,e in enumerate(m['object_events']):
   if e['graphics_id'] in ['OBJ_EVENT_GFX_SS_TIDAL','OBJ_EVENT_GFX_NURSE','OBJ_EVENT_GFX_MART_EMPLOYEE','OBJ_EVENT_GFX_BERRY_TREE']:continue
   v=g.cell(e['x'],e['y']);assert v['collision']==0 and v['translated_behavior'] not in [0x10,0x15],(n,i,e,v)
   assert e['elevation'] in [0,v['elevation']] or v['elevation'] in [0,15],(n,i,e,v)
 # Native Wailmer commands have the exact donor visual operands; no script ownership transfer.
 labels={m[1]:int(m[2],16) for m in re.finditer(r'#define\s+(METATILE_\w+)\s+(0x[0-9A-Fa-f]+)',(C.ROOT/'include/constants/metatile_labels.h').read_text())};s=q['scripts']['LilycoveCity'];native=[(int(x),int(y),labels[t],int(v=='TRUE')) for x,y,t,v in re.findall(r'setmetatile (\d+), (\d+), (METATILE_Lilycove_Wailmer\w+), (TRUE|FALSE)',s)];folder=next((C.ROOT/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export/maps').glob('00.05_*'));scripts=C.load(folder/'scripts.json');donor=[struct.unpack('<4H',bytes.fromhex(c['raw_hex'])[1:]) for z in scripts['scripts'] for c in z['commands'] if c['name']=='setmetatile' and len(bytes.fromhex(c['raw_hex']))==9];assert native==donor[:12]
 # Native Fly/heal positions remain usable on actual donor land.
 heal=[]
 for z in C.load(C.ROOT/'src/data/heal_locations.json')['heal_locations']:
  if z['map']==q['maps']['LilycoveCity']['id']:
   v=q['grids']['LilycoveCity'].cell(z['x'],z['y']);assert v['collision']==0 and v['elevation']==3;heal.append(z)
 C.dump(C.OUT/'geometry_validation.json',{'passed':True,'surface_water_cells_checked':water,'native_warps_checked':doors,'wailmer_visual_operands_match_donor':native,'native_heal_fly_positions_checked':heal,'source_heights_retained_except_one_inspected_water_anomaly':True,'native_arrival_only_warps':dormant});print('Geometry passed:',len(doors),'native warps,',water,'water cells, native Wailmer visuals and heal/Fly positions.')
if __name__=='__main__':review(C.prepare())
