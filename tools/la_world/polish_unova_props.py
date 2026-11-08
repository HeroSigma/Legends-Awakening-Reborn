from pathlib import Path
import json,os,struct
P=Path(__file__).resolve().parents[2];f=P/'tools/la_world/rebuild_unova_wesley.py';s=f.read_text()
s=s.replace("(88,18,104,64),'Hedge',True),16,48,(0,2)","(89,17,105,64),'Hedge',True),16,48,(0,1)")
s=s.replace("9:finish_colors(quant_colors([assets['mailbox'],assets['board_sign'],assets['dock_rail']],15)),","9:finish_colors(sorted({c[:3] for c in assets['mailbox'].getdata() if c[3]})+quant_colors([assets['board_sign'],assets['dock_rail']],5)),")
s=s.replace("11:finish_colors(greens+quant_colors([assets['hedge']],5)+[(255,255,239),(255,239,115),(214,230,255)]),","11:finish_colors(greens+sorted({c[:3] for c in assets['hedge'].getdata() if c[3]})),")
f.write_text(s)
# Repack graphics without executing the map rebuilding portion: editor changes remain untouched.
paths=[P/'data/tilesets/primary/unova_general',P/'data/tilesets/secondary/unova_nuvema'];before={p:(p.read_bytes(),p.stat().st_atime_ns,p.stat().st_mtime_ns) for d in paths for p in d.rglob('*') if p.is_file()}
mapfiles=[P/'data/maps/Unova_NuvemaTown/map.json',P/'data/layouts/layouts.json',P/'data/layouts/AMap_3_0_Nuvema_Town_Layout/map.bin'];mapbefore={p:p.read_bytes() for p in mapfiles}
ns={'__file__':str(f),'__name__':'unova_props_only'};exec(compile(s[:s.index('layoutfile=P/')],str(f),'exec'),ns)
exec("rockwater=pack.add(assets['rock'],'CoastalRockWater',[3,4],background=prefabs['Ocean'][0][0])",ns)
old=json.loads((P/'docs/la_world/unova_wesley/prefabs.json').read_text());assert ns['prefabs']==old,'Metatile IDs must remain stable'
start=s.index('for bank,directory in enumerate([PRI,SEC]):');end=s.index('layout.update(width=W,height=H')
exec(compile(s[start:end],str(f),'exec'),ns)
for p,(data,at,mt) in before.items():
 if p.read_bytes()==data:os.utime(p,ns=(at,mt))
for p,data in mapbefore.items():assert p.read_bytes()==data,'Map edits must remain untouched'
pack=ns['pack'];D=P/'docs/la_world/unova_wesley';r=json.loads((D/'report.json').read_text());r.update(primary_graphics_tiles=pack.next[0]+16,secondary_graphics_tiles=pack.next[1]-512,primary_graphics_free=512-pack.next[0]-16,secondary_graphics_free=1024-pack.next[1]);r['source_crops'].update(ns['crops']);r['prop_polish']={'hedge':'Full 16x47 native crop, 1px top padding; all original hedge colors retained after RGB5 conversion.','mailbox':'All ten original opaque source colors prioritized in palette 9.','map_files_preserved':True};(D/'report.json').write_text(json.dumps(r,indent=2)+'\n')
for name in ['hedge','mailbox']:ns['assets'][name].save(P/f'.la_work/unova_wesley/{name}-native.png')
print('Repacked hedge and mailbox; metatile IDs and map files unchanged. Graphics tiles:',r['primary_graphics_tiles'],r['secondary_graphics_tiles'])
