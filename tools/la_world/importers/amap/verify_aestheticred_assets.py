#!/usr/bin/env python3
"""Verify Kanto editor declarations and linked blank asset maps."""
import hashlib,json,re,struct,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[4];D=R/"docs/la_world/kanto_aestheticred"
symbols={z[2]:int(z[0],16) for line in subprocess.check_output(["arm-none-eabi-nm","--defined-only",str(R/"pokeemerald-sinnoh-assets.elf")],text=True).splitlines() if len(z:=line.split())==3}
rom=(R/"pokeemerald-sinnoh-assets.gba").read_bytes()
def blob(a,n):
 assert 0x8000000<=a<=a+n<=0x8000000+len(rom);return rom[a-0x8000000:a-0x8000000+n]
def u(a):return struct.unpack("<I",blob(a,4))[0]
ls={l["id"]:l for l in json.loads((R/"data/layouts/layouts.json").read_text())["layouts"]};g=json.loads((R/"data/maps/map_groups.json").read_text());headers=(R/"src/data/tilesets/headers.h").read_text();checked=[]
changes_by_map={}
if (D/"travel_cell_changes.json").exists():
 for change in json.loads((D/"travel_cell_changes.json").read_text()):changes_by_map.setdefault(change["map"],[]).append(change)
ledger=json.loads((D/"import_ledger.json").read_text());allmaps={z["project_name"]:json.loads((R/"data/maps"/z["project_name"]/"map.json").read_text()) for z in ledger};numeric={m["id"]:next((i,g[k].index(name)) for i,k in enumerate(g["group_order"]) if name in g[k]) for name,m in allmaps.items()}
for item in ledger:
 name=item["project_name"];m=json.loads((R/"data/maps"/name/"map.json").read_text());l=ls[m["layout"]];gi,mi=next((i,g[k].index(name)) for i,k in enumerate(g["group_order"]) if name in g[k]);assert 0<=gi<127 and 0<=mi<127, (name,gi,mi,"signed warp ID overflow");hp=u(u(symbols["gMapGroups"]+4*gi)+4*mi);assert hp==symbols[name];lp=u(hp);assert lp==symbols[l["name"]];assert (u(lp),u(lp+4))==(l["width"],l["height"])
 for off,key in [(8,"border_filepath"),(12,"blockdata_filepath")]:
  b=(R/l[key]).read_bytes();assert blob(u(lp+off),len(b))==b
 original=bytearray((R/l["blockdata_filepath"]).read_bytes())
 for change in reversed(changes_by_map.get(name,[])):
  off=2*(change["y"]*l["width"]+change["x"]);assert struct.unpack_from("<H",original,off)[0]==change["after"];struct.pack_into("<H",original,off,change["before"])
 assert hashlib.sha256(original).hexdigest()==item["source_blockdata_sha256"]
 for off,key in [(16,"primary_tileset"),(20,"secondary_tileset")]:
  label=l[key];ts=u(lp+off);assert ts==symbols[label];assert u(ts+20)==0;body=re.search(re.escape(label)+r"\s*=\s*\{(.*?)\};",headers,re.S)[1]
  for po,field in [(4,"tiles"),(8,"palettes"),(12,"metatiles"),(16,"metatileAttributes")]:assert u(ts+po)==symbols[re.search(r"\."+field+r"\s*=\s*(\w+)",body)[1]]
  folder=R/"data/kanto_ar_assets/tilesets"/label.replace("gTileset_KantoAR_","")
  palette=b""
  for i in range(13):
   pal=folder/"palettes"/f"{i:02}.pal"
   colors=[tuple(map(int,line.split())) for line in pal.read_text().splitlines()[3:19]]
   expected=b"".join(struct.pack("<H",(a>>3)|((b>>3)<<5)|((c>>3)<<10)) for a,b,c in colors)
   assert pal.with_suffix(".gbapal").read_bytes()==expected, (label,i,"palette conversion")
   palette+=expected
  assert blob(u(ts+8),len(palette))==palette, (label,"linked palette")
  address=u(ts+4);size=int.from_bytes(blob(address+1,3),"little");out=bytearray();pos=address+4
  while len(out)<size:
   flags=blob(pos,1)[0];pos+=1
   for bit in range(7,-1,-1):
    if len(out)>=size:break
    if flags & (1<<bit):
     a,b=blob(pos,2);pos+=2;length=(a>>4)+3;distance=((a&15)<<8|b)+1
     assert distance<=len(out)
     for _ in range(length):out.append(out[-distance])
    else:out.extend(blob(pos,1));pos+=1
  assert bytes(out)==(folder/"tiles.4bpp").read_bytes(), (label,"lossless graphics")
  for po,file in [(12,"metatiles.bin"),(16,"metatile_attributes.bin")]:
   b=(folder/file).read_bytes();assert blob(u(ts+po),len(b))==b
 assert u(hp+8)==symbols[name+"_MapScripts"] and blob(u(hp+8),1)==b"\0";ep=u(hp+4);assert blob(ep,4)==bytes([len(m["object_events"]),len(m["warp_events"]),0,0])
 for j,z in enumerate(m["warp_events"]):
  ob=blob(u(ep+8)+8*j,8);assert struct.unpack_from("<hh",ob)==(z["x"],z["y"]);assert ob[4]==z["elevation"] and ob[5]==int(z["dest_warp_id"])
  if z["dest_map"]=="MAP_DYNAMIC":assert (ob[7],ob[6])==(127,127)
  else:assert (ob[7],ob[6])==numeric[z["dest_map"]]
 for j,z in enumerate(m["object_events"]):
  ob=blob(u(ep+4)+24*j,24);assert struct.unpack_from("<hh",ob,4)==(z["x"],z["y"]);assert struct.unpack_from("<I",ob,16)[0]==symbols[z["script"]]
 if m["connections"]:
  cp=u(hp+12);assert u(cp)==len(m["connections"])
  for j,z in enumerate(m["connections"]):
   ob=blob(u(cp+4)+12*j,12);assert struct.unpack_from("<I",ob)[0]=={"down":1,"up":2,"left":3,"right":4,"dive":5,"emerge":6}[z["direction"]];assert struct.unpack_from("<i",ob,4)[0]==z["offset"];assert (ob[8],ob[9])==numeric[z["map"]]
 checked.append(name)
assert len(checked)==425
(D/"linked_validation.json").write_text(json.dumps(dict(linked_maps=len(checked),rom_sha256=hashlib.sha256(rom).hexdigest(),runtime_verified=False),indent=2)+"\n");print("PASS: 425 Kanto maps, preserved artwork, scoped travel cells, linked warps, objects and connections")
