#!/usr/bin/env python3
"""Register approved Aesthetic Red visual maps in Reborn for Porymap editing."""
import hashlib,json,re,shutil,struct
from pathlib import Path
from hyper_assets.port_hyper_assets import enums
R=Path(__file__).resolve().parents[4]
def dump(p,o):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2)+"\n")
def main():
 source=R/".la_work/amap/aestheticred_full_v11";doc=R/"docs/la_world/kanto_aestheticred"
 assert not (doc/"import_ledger.json").exists(),"Already imported"
 manifest=json.loads((source/"manifest.json").read_text());rom=Path(manifest["rom"]["path"])
 assert hashlib.sha256(rom.read_bytes()).hexdigest()==manifest["rom"]["sha256"]
 shared={"data/layouts/layouts.json","data/maps/map_groups.json","data/event_scripts.s","src/data/region_map/region_map_sections.json","src/data/tilesets/headers.h","src/data/tilesets/graphics.h","src/data/tilesets/metatiles.h"}
 protected={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for root in ["data","src","include"] for p in (R/root).rglob("*") if p.is_file() and str(p.relative_to(R)) not in shared}
 native=enums(R/"include/constants/metatile_behaviors.h");donor={int(v,16):n for n,v in re.findall(r"#define (MB_\w+) (0x[0-9A-Fa-f]+)",(R/".la_work/amap/firered_behaviors_reference.h").read_text())}
 aliases={"MB_ROCK_STAIRS":"MB_NORMAL","MB_SAND_CAVE":"MB_CAVE","MB_RUNNING_DISALLOWED":"MB_NO_RUNNING"}
 declarations={k:[] for k in ["headers","graphics","metatiles"]};labels={};behaviors=[]
 for folder in sorted((source/"tilesets").iterdir()):
  meta=json.loads((folder/"tileset.json").read_text());key=meta["id"];label="gTileset_KantoAR_"+key;labels[key]=label
  target=R/"data/kanto_ar_assets/tilesets"/key;shutil.copytree(folder,target);base=target.relative_to(R).as_posix();attrs=bytearray((target/"metatile_attributes.bin").read_bytes());raw=(target/"source_frlg_metatile_attributes.bin").read_bytes()
  for i in range(512):
   b=struct.unpack_from("<I",raw,4*i)[0]&511;name=aliases.get(donor.get(b),donor.get(b));status="TRANSLATED"
   if name and any(t in name for t in ["WARP","DOOR","LADDER"]):name="MB_NORMAL";status="UNWIRED_TRAVEL"
   if name not in native:name="MB_NORMAL";status="REVIEW_REQUIRED"
   a=struct.unpack_from("<H",attrs,2*i)[0];struct.pack_into("<H",attrs,2*i,(a&0xf000)|native[name]);behaviors.append(dict(tileset=key,metatile=i,source_behavior=b,target=name,status=status))
  (target/"metatile_attributes.bin").write_bytes(attrs)
  for i in range(16):
   pal=target/"palettes"/f"{i:02}.pal";binary=pal.with_suffix(".gbapal")
   if not pal.exists():pal.write_text("JASC-PAL\n0100\n16\n"+"0 0 0\n"*16)
   colors=[tuple(map(int,line.split())) for line in pal.read_text().splitlines()[3:19]]
   binary.write_bytes(b"".join(struct.pack("<H",(a>>3)|((b>>3)<<5)|((c>>3)<<10)) for a,b,c in colors))
  declarations["graphics"].append(f'const u32 {label}_Tiles[] = INCBIN_U32("{base}/tiles.4bpp.lz");\nconst u16 {label}_Palettes[][16] = {{\n'+"".join(f' INCBIN_U16("{base}/palettes/{i:02}.gbapal"),\n' for i in range(16))+"};")
  declarations["metatiles"].append(f'const u16 {label}_Metatiles[] = INCBIN_U16("{base}/metatiles.bin");\nconst u16 {label}_Attributes[] = INCBIN_U16("{base}/metatile_attributes.bin");')
  declarations["headers"].append(f'const struct Tileset {label} = {{ .isCompressed=TRUE, .isSecondary={"TRUE" if meta["role"]=="secondary" else "FALSE"}, .tiles={label}_Tiles, .palettes={label}_Palettes, .metatiles={label}_Metatiles, .metatileAttributes={label}_Attributes, .callback=NULL }};')
 for kind,lines in declarations.items():
  p=R/f"src/data/tilesets/{kind}.h";p.write_text(p.read_text().rstrip()+"\n\n"+"\n\n".join(lines)+"\n")
 lp=R/"data/layouts/layouts.json";layouts=json.loads(lp.read_text());gp=R/"data/maps/map_groups.json";groups=json.loads(gp.read_text());old_groups=json.loads(gp.read_text());ref=json.loads((R/"tools/la_world/importers/amap/firered_map_reference.json").read_text())["maps"];ledger=[];scripts=[]
 for folder in sorted((source/"maps").iterdir()):
  m=json.loads((folder/"map.json").read_text());readable=ref.get(m["id"],{}).get("name",m["name"]);name=f'KantoAR_{m["group"]}_{m["map"]}_'+re.sub("[^A-Za-z0-9]+","_",readable).strip("_");lid="LAYOUT_"+name.upper();target=R/"data/kanto_ar_assets/layouts"/name;target.mkdir(parents=True);base=target.relative_to(R).as_posix()
  shutil.copy2(folder/"blockdata.bin",target/"map.bin");shutil.copy2(folder/"border.bin",target/"border.bin")
  assert not any(l["id"]==lid for l in layouts["layouts"])
  layouts["layouts"].append(dict(id=lid,name=name+"_Layout",width=m["width"],height=m["height"],primary_tileset=labels[m["primary_tileset"]],secondary_tileset=labels[m["secondary_tileset"]],blockdata_filepath=base+"/map.bin",border_filepath=base+"/border.bin",border_width=m["border"]["width"],border_height=m["border"]["height"]))
  # WarpData uses signed bytes: append to existing safe banks, never groups >=127.
  slots=[k for k in groups["group_order"] if "AMap_Bank" in k]+["gMapGroup_HyperHoenn_Dragonspiral_Tower"]
  group=next(k for k in slots if groups["group_order"].index(k)<127 and len(groups[k])<127)
  groups[group].append(name)
  obj=dict(id="MAP_"+name.upper(),name=name,layout=lid,music="MUS_DUMMY",region_map_section="MAPSEC_KANTO_AR",requires_flash=False,weather="WEATHER_NONE",map_type="MAP_TYPE_INDOOR",allow_cycling=False,allow_escaping=False,allow_running=True,show_map_name=False,battle_scene="MAP_BATTLE_SCENE_NORMAL",connections=None,object_events=[],warp_events=[],coord_events=[],bg_events=[])
  dump(R/"data/maps"/name/"map.json",obj);(R/"data/maps"/name/"scripts.inc").write_text(name+"_MapScripts::\n\t.byte 0\n");scripts.append(f'.include "data/maps/{name}/scripts.inc"')
  ledger.append(dict(donor_id=m["id"],name=m["name"],project_name=name,layout=lid,source_blockdata_sha256=hashlib.sha256((folder/"blockdata.bin").read_bytes()).hexdigest()))
 assert len(ledger)==425 and len(groups["group_order"])<=127
 for k,v in old_groups.items():assert groups[k][:len(v)]==v
 dump(lp,layouts);dump(gp,groups);p=R/"data/event_scripts.s";p.write_text(p.read_text().rstrip()+"\n"+"\n".join(scripts)+"\n")
 p=R/"src/data/region_map/region_map_sections.json";sections=json.loads(p.read_text());sections["map_sections"].append(dict(id="MAPSEC_KANTO_AR",name="Kanto (Aesthetic Red)",x=0,y=0,width=1,height=1));dump(p,sections)
 for rel,h in protected.items():assert hashlib.sha256((R/rel).read_bytes()).hexdigest()==h,rel
 dump(doc/"import_ledger.json",ledger);dump(doc/"behavior_translation.json",behaviors);dump(doc/"validation.json",dict(maps=len(ledger),tilesets=len(labels),protected_files=len(protected),existing_map_ids_unchanged=True,donor_gameplay_imported=False,travel_enabled=False,animations="STATIC_PENDING_PORT"))
 (doc/"review.md").write_text("# Aesthetic Red Kanto maps\n\n425 approved visual maps and 62 tileset banks registered in the main project. Open Porymap Locations > Kanto (Aesthetic Red), or filter KantoAR. Original donor geometry is preserved. Existing Johto and other region files were checksum protected.\n\nBlank asset maps: no donor NPCs, scripts, warps or connections activated. Tileset animations and unknown donor behavior translation remain pending. Johto Routes 27 and 28 have not been replaced.\n")
 print("Registered",len(ledger),"maps and",len(labels),"tilesets; protected",len(protected),"existing files")
if __name__=="__main__":main()
