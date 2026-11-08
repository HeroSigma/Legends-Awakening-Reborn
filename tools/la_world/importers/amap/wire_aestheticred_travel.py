#!/usr/bin/env python3
"""Wire Kanto asset exploration with native travel and project-owned inspection scripts."""
import json,re,struct,hashlib
from pathlib import Path
from hyper_assets.port_hyper_assets import enums
R=Path(__file__).resolve().parents[4];D=R/"docs/la_world/kanto_aestheticred";S=R/".la_work/amap/aestheticred_full_v11"
def dump(p,o):p.write_text(json.dumps(o,indent=2)+"\n")
def main():
 assert not (D/"travel_ledger.json").exists(),"Already wired"
 protected={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for root in ["data/gs_johto_assets","data/bwa_assets"] for p in (R/root).rglob("*") if p.is_file()}
 ledger=json.loads((D/"import_ledger.json").read_text());names={z["donor_id"]:z["project_name"] for z in ledger};source={m["id"]:m for p in (S/"maps").glob("*/map.json") if (m:=json.loads(p.read_text()))};layouts={l["id"]:l for l in json.loads((R/"data/layouts/layouts.json").read_text())["layouts"]};n=enums(R/"include/constants/metatile_behaviors.h");banks={};used={};rows={};clones={};changes=[];tour=[];travel=[]
 for key in (R/"data/kanto_ar_assets/tilesets").iterdir():banks[key.name]=(key,bytearray((key/"metatile_attributes.bin").read_bytes()),bytearray((key/"metatiles.bin").read_bytes()),(key/"source_frlg_metatile_attributes.bin").read_bytes())
 for did,name in names.items():
  m=json.loads((R/"data/maps"/name/"map.json").read_text());l=layouts[m["layout"]];keys=[l[k].replace("gTileset_KantoAR_","") for k in ["primary_tileset","secondary_tileset"]];cells=list(struct.unpack("<"+"H"*(l["width"]*l["height"]),(R/l["blockdata_filepath"]).read_bytes()));rows[did]=(m,l,keys,cells)
  for blob in [struct.pack("<"+"H"*len(cells),*cells),(R/l["border_filepath"]).read_bytes()]:
   for v, in struct.iter_unpack("<H",blob):used.setdefault(keys[(v&1023)//512],set()).add(v&511)
 def clone(keys,mid,beh):
  key=keys[mid//512];root,a,t,raw=banks[key];pair=(key,mid%512,beh)
  if pair not in clones:
   free=[i for i in range(511,-1,-1) if i not in used[key]];assert free,(key,"no free scoped metatiles");slot=free[0];used[key].add(slot);clones[pair]=slot;t[16*slot:16*slot+16]=t[16*(mid%512):16*(mid%512)+16];old=struct.unpack_from("<H",a,2*(mid%512))[0];struct.pack_into("<H",a,2*slot,(old&0xf000)|beh)
  return mid//512*512+clones[pair]
 raw_behavior=lambda keys,mid:struct.unpack_from("<I",banks[keys[mid//512]][3],4*(mid%512))[0]&511
 warpnames={0x60:"MB_NON_ANIMATED_DOOR",0x61:"MB_LADDER",0x62:"MB_EAST_ARROW_WARP",0x63:"MB_WEST_ARROW_WARP",0x64:"MB_NORTH_ARROW_WARP",0x65:"MB_SOUTH_ARROW_WARP",0x66:"MB_LADDER",0x67:"MB_AQUA_HIDEOUT_WARP",0x68:"MB_LADDER",0x69:"MB_NON_ANIMATED_DOOR",0x6a:"MB_UP_ESCALATOR",0x6b:"MB_DOWN_ESCALATOR",0x6c:"MB_UP_RIGHT_STAIR_WARP",0x6d:"MB_UP_LEFT_STAIR_WARP",0x6e:"MB_DOWN_RIGHT_STAIR_WARP",0x6f:"MB_DOWN_LEFT_STAIR_WARP",0x71:"MB_LADDER"}
 for did,(m,l,keys,cells) in rows.items():
  s=source[did];m["map_type"]={1:"MAP_TYPE_TOWN",2:"MAP_TYPE_CITY",3:"MAP_TYPE_ROUTE",4:"MAP_TYPE_UNDERWATER",5:"MAP_TYPE_OCEAN_ROUTE",6:"MAP_TYPE_INDOOR",7:"MAP_TYPE_SECRET_BASE",8:"MAP_TYPE_UNDERGROUND"}.get(s["map_type"],"MAP_TYPE_INDOOR");m["music"]="MUS_ROUTE104";m["allow_cycling"]=bool(s["allow_cycling"]);m["show_map_name"]=True;m["warp_events"]=[];m["connections"]=[]
  for z in s["connections"]:
   assert z["target_id"] in names;m["connections"].append(dict(map="MAP_"+names[z["target_id"]].upper(),offset=z["offset"],direction=z["direction"]))
  if not m["connections"]:m["connections"]=None
  for i,v in enumerate(cells):
   beh=raw_behavior(keys,v&1023)
   if beh in [0x10,0x11,0x12,0x13,0x15] and (v>>10&3)==0 and v>>12 not in [1,15]:
    new=(v&0xfff)|0x1000;cells[i]=new;changes.append(dict(map=m["name"],x=i%l["width"],y=i//l["width"],before=v,after=new,reason="native_water_elevation"))
  for z in s["warps"]:
   assert 0<=z["x"]<l["width"] and 0<=z["y"]<l["height"]
   if z["dynamic_target"]:dest="MAP_DYNAMIC";wid=0
   else:
    assert z["target_id"] in names and z["dest_warp_id"]<len(source[z["target_id"]]["warps"]);dest="MAP_"+names[z["target_id"]].upper();wid=z["dest_warp_id"]
   m["warp_events"].append(dict(x=z["x"],y=z["y"],elevation=3,dest_map=dest,dest_warp_id=str(wid)))
   pos=z["y"]*l["width"]+z["x"];v=cells[pos];mid=v&1023;desired=n[warpnames.get(raw_behavior(keys,mid),"MB_LADDER")];mid=clone(keys,mid,desired);new=mid|0x3000;cells[pos]=new;changes.append(dict(map=m["name"],x=z["x"],y=z["y"],before=v,after=new,reason="native_warp_trigger"))
  warppos={(z["x"],z["y"]) for z in m["warp_events"]};floor=set()
  for i,v in enumerate(cells):
   mid=v&1023;attr=struct.unpack_from("<H",banks[keys[mid//512]][1],2*(mid%512))[0]&255
   if (v>>10&3)==0 and v>>12 in [0,3] and attr==n["MB_NORMAL"] and (i%l["width"],i//l["width"]) not in warppos:floor.add(i)
  candidates=[i for i in floor if i%l["width"]>0 and i%l["width"]<l["width"]-1 and i-l["width"] in floor and i+l["width"] in floor and i-1 in floor and i+1 in floor]
  if candidates:
   pos=min(candidates,key=lambda i:abs(i%l["width"]-l["width"]//2)+abs(i//l["width"]-l["height"]//2));x,y=pos%l["width"],pos//l["width"];tour.append(dict(donor_id=did,map=m["name"],map_id=m["id"],spawn=[x,y]));m["object_events"]=[dict(local_id="LOCALID_"+m["name"].upper()+"_SCIENTIST",graphics_id="OBJ_EVENT_GFX_SCIENTIST_1",x=x,y=y-1,elevation=3,movement_type="MOVEMENT_TYPE_FACE_DOWN",movement_range_x=0,movement_range_y=0,trainer_type="TRAINER_TYPE_NONE",trainer_sight_or_berry_tree_id="0",script="KantoAR_TravelHub" if did=="3.0" else m["name"]+"_Inspect",flag="0")]
  (R/l["blockdata_filepath"]).write_bytes(struct.pack("<"+"H"*len(cells),*cells));dump(R/"data/maps"/m["name"]/"map.json",m);travel.append(dict(donor_id=did,map=m["name"],warps=len(m["warp_events"]),connections=len(m["connections"] or [])))
 for root,a,t,raw in banks.values():(root/"metatile_attributes.bin").write_bytes(a);(root/"metatiles.bin").write_bytes(t)
 tour.sort(key=lambda z:(0 if z["donor_id"]=="3.0" else 1,int(z["donor_id"].split(".")[0]),int(z["donor_id"].split(".")[1])))
 for i,z in enumerate(tour):
  name=z["map"];nxt=tour[(i+1)%len(tour)];text=f'{name}_MapScripts::\n\t.byte 0\n\n{name}_Inspect::\n\tlock\n\tfaceplayer\n\tmsgbox {name}_Text, MSGBOX_YESNO\n\tgoto_if_eq VAR_RESULT, YES, {name}_Next\n\tclosemessage\n\twarp MAP_LITTLEROOT_TOWN, 10, 17\n\twaitstate\n\trelease\n\tend\n{name}_Next::\n\tclosemessage\n\twarp {nxt["map_id"]}, {nxt["spawn"][0]}, {nxt["spawn"][1]}\n\twaitstate\n\trelease\n\tend\n{name}_Text:\n\t.string "Kanto map {z["donor_id"]}. Visit next?\\p"\n\t.string "YES: next. NO: Littleroot.$"\n';(R/"data/maps"/name/"scripts.inc").write_text(text)
 for rel,h in protected.items():assert hashlib.sha256((R/rel).read_bytes()).hexdigest()==h,rel
 dump(D/"travel_ledger.json",travel);dump(D/"travel_cell_changes.json",changes);dump(D/"inspection_arrivals.json",tour);dump(D/"travel_summary.json",dict(maps=len(travel),warps=sum(z["warps"] for z in travel),connections=sum(z["connections"] for z in travel),dynamic_returns=19,inspection_maps=len(tour),cloned_metatiles=len(clones),runtime_verified=False))
 print("Wired",len(travel),"maps;",len(tour),"safe inspection arrivals;",len(clones),"scoped warp graphics")
if __name__=="__main__":main()
