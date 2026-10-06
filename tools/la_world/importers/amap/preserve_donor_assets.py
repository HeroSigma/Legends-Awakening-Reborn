#!/usr/bin/env python3
"""Preserve FRLG donor assets in isolated, non-buildable editor workspaces.
No live registry writes, donor events, scripts, flags or travel activation.
"""
import argparse, csv, hashlib, json, shutil, struct
from pathlib import Path
from sprite_catalog import ObjectSpriteCatalog
from prepare_donor_editor import prepare

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(x,indent=2)+'\n')
def csvout(p,rows):
    if rows:
        with p.open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def symbol(key): return 'gTileset_Preserve_'+key

def run(repo,donor):
    src=repo/'.la_work/amap'/f'{donor}_full_v11'
    out=repo/'.la_work/amap/donor_preservation'/donor
    editor=out/'editor';out.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((src/'manifest.json').read_text());rom=Path(manifest['rom']['path'])
    assert rom.exists(),rom
    assert sha(rom)==manifest['rom']['sha256'],'Wrong donor ROM'
    # Lossless recovery anchor. Never linked or executed in the editor/project.
    anchor=out/'reference/donor.gba';anchor.parent.mkdir(parents=True,exist_ok=True)
    if not anchor.exists():shutil.copy2(rom,anchor)
    assert sha(anchor)==sha(rom)
    data=rom.read_bytes()
    shutil.copytree(src,out/'reference/export',dirs_exist_ok=True)
    shutil.copytree(repo/'include/constants',editor/'include/constants',dirs_exist_ok=True)
    shutil.copy2(repo/'porymap.project.cfg',editor/'porymap.project.cfg')
    headers=[];graphics=[];metatiles=[];tilesets={};behaviors=[];callbacks={}
    for folder in sorted((src/'tilesets').iterdir()):
        meta=json.loads((folder/'tileset.json').read_text());key=meta['id'];tilesets[key]=meta
        target=editor/'data/tilesets'/meta['role']/key
        shutil.copytree(folder,target,dirs_exist_ok=True)
        # Porymap expects a complete palette array even for unused slots.
        pal=target/'palettes';pal.mkdir(exist_ok=True)
        for slot in range(16):
            p=pal/f'{slot:02}.pal'
            if not p.exists():p.write_text('JASC-PAL\n0100\n16\n'+'0 0 0\n'*16)
        label=symbol(key);base=target.relative_to(editor).as_posix()
        graphics.append(f'const u32 {label}_Tiles[] = INCGFX_U32("{base}/tiles.png", ".4bpp");')
        graphics.append(f'const u16 {label}_Palettes[][16] = {{\n'+''.join(f'    INCGFX_U16("{base}/palettes/{i:02}.pal", ".gbapal"),\n' for i in range(16))+'};')
        metatiles.extend([f'const u16 {label}_Metatiles[] = INCBIN_U16("{base}/metatiles.bin");',f'const u16 {label}_Attributes[] = INCBIN_U16("{base}/metatile_attributes.bin");'])
        headers.append(f'const struct Tileset {label} = {{\n .isCompressed = FALSE,\n .isSecondary = {"TRUE" if meta["role"]=="secondary" else "FALSE"},\n .tiles = {label}_Tiles,\n .palettes = {label}_Palettes,\n .metatiles = {label}_Metatiles,\n .metatileAttributes = {label}_Attributes,\n .callback = NULL,\n}};')
        raw=(folder/'source_frlg_metatile_attributes.bin').read_bytes()
        normalized=(folder/'metatile_attributes.bin').read_bytes()
        assert len(normalized)==1024 and len(raw)==2048
        for i in range(512):
            attr=struct.unpack_from('<I',raw,i*4)[0];compat=struct.unpack_from('<H',normalized,i*2)[0]
            behaviors.append(dict(tileset=key,metatile=i,raw_frlg_attribute=f'0x{attr:08X}',donor_behavior=attr&511,editor_behavior=compat&255,status='REFERENCE_ONLY' if (attr&511)<256 else 'HIGH_BEHAVIOR_REQUIRES_TRANSLATION',runtime_enabled=False))
        for field,value in meta['source'].items():
            if 'struct' not in field:continue
            ptr=int(value,16);offset=ptr-0x08000000
            assert 0<=offset<len(data)-24
            callback=struct.unpack_from('<I',data,offset+16)[0]
            callbacks[value]=dict(tileset_pointer=value,header_hex=data[offset:offset+24].hex(),callback=f'0x{callback:08X}',status='NO_CALLBACK' if not callback else 'SOURCE_PRESERVED_RUNTIME_PORT_PENDING',runtime_enabled=False)
    for filename,lines in [('headers.h',headers),('graphics.h',graphics),('metatiles.h',metatiles)]:
        p=editor/'src/data/tilesets'/filename;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('\n\n'.join(lines)+'\n')
    (editor/'src/tilesets.c').write_text('#include "data/tilesets/graphics.h"\n#include "data/tilesets/metatiles.h"\n#include "data/tilesets/headers.h"\n')
    (editor/'src/graphics.c').write_text('#include "data/tilesets/graphics.h"\n')
    cfg=(editor/'porymap.project.cfg').read_text().replace('use_custom_border_size=0','use_custom_border_size=1')
    prim=next(k for k,v in tilesets.items() if v['role']=='primary');sec=next(k for k,v in tilesets.items() if v['role']=='secondary')
    cfg=cfg.replace('default_primary_tileset=gTileset_General','default_primary_tileset='+symbol(prim)).replace('default_secondary_tileset=gTileset_Petalburg','default_secondary_tileset='+symbol(sec))
    (editor/'porymap.project.cfg').write_text(cfg)
    layouts=[];groups={'group_order':[]};inventory=[];gfxids=set()
    for folder in sorted((src/'maps').iterdir()):
        m=json.loads((folder/'map.json').read_text());name=f'Preserve_{donor}_{m["group"]}_{m["map"]}'
        lid='LAYOUT_'+name.upper();base=f'data/layouts/{name}'
        dest=editor/base;dest.mkdir(parents=True,exist_ok=True)
        for f in ['blockdata.bin','border.bin']:shutil.copy2(folder/f,dest/('map.bin' if f=='blockdata.bin' else f))
        assert (dest/'map.bin').stat().st_size==m['width']*m['height']*2
        layouts.append(dict(id=lid,name=name+'_Layout',width=m['width'],height=m['height'],primary_tileset=symbol(m['primary_tileset']),secondary_tileset=symbol(m['secondary_tileset']),border_filepath=base+'/border.bin',blockdata_filepath=base+'/map.bin',border_width=m['border']['width'],border_height=m['border']['height']))
        for t in ['primary_tileset','secondary_tileset']:assert m[t] in tilesets
        group=f'gMapGroup_Preserve_{donor}_{m["group"]}'
        if group not in groups:groups['group_order'].append(group);groups[group]=[]
        groups[group].append(name)
        obj=dict(id='MAP_'+name.upper(),name=name,layout=lid,music='MUS_DUMMY',region_map_section='MAPSEC_NONE',requires_flash=False,weather='WEATHER_NONE',map_type='MAP_TYPE_NONE',allow_cycling=False,allow_escaping=False,allow_running=False,show_map_name=False,battle_scene='MAP_BATTLE_SCENE_NORMAL',connections=None,object_events=[],warp_events=[],coord_events=[],bg_events=[])
        write(editor/'data/maps'/name/'map.json',obj)
        (editor/'data/maps'/name/'scripts.inc').write_text('@ Asset-only preservation: no donor gameplay.\n')
        gfxids.update(n['graphics_id'] for n in m['npcs'])
        inventory.append(dict(donor=donor,id=f'{m["group"]}.{m["map"]}',name=m['name'],group=m['group'],map=m['map'],width=m['width'],height=m['height'],objects=len(m['npcs']),warps=len(m['warps']),coord_events=len(m['coord_events']),bg_events=len(m['bg_events']),connections=len(m['connections']),primary_tileset=m['primary_tileset'],secondary_tileset=m['secondary_tileset'],header_pointer=m['header_pointer'],layout_pointer=m['layout_pointer'],blockdata_sha256=sha(folder/'blockdata.bin'),border_sha256=sha(folder/'border.bin'),editor_map=name,active=False))
    write(editor/'data/layouts/layouts.json',dict(layouts_table_label='gMapLayouts',layouts=layouts));write(editor/'data/maps/map_groups.json',groups)
    # Shared FRLG/Emerald graphics-info ABI confirmed against pret/pokefirered.
    # Discovery remains heuristic: extracted candidates are reference art, never linked.
    catalog=ObjectSpriteCatalog(data,out/'object_art_candidates')
    catalog.discover()
    art=catalog.extract(gfxids | set(range(catalog.static_count)))
    for asset in art.values():asset['runtime_enabled']=False;asset['verification']='HEURISTIC_REFERENCE_REQUIRES_ID_AND_FRAME_CLOSURE_REVIEW'
    write(out/'object_art_candidates/sprites/review_manifest.json',art)
    csvout(out/'maps.csv',inventory);csvout(out/'behaviors.csv',behaviors)
    write(out/'animations.json',list(callbacks.values()))
    expected=444 if donor=='bwa' else 701;assert len(inventory)==expected
    # Full checksum inventory includes the source anchor, palettes, raw behaviors and art.
    prepare(repo,editor)
    hashes={p.relative_to(out).as_posix():sha(p) for p in sorted(out.rglob('*')) if p.is_file() and p.name not in ['preservation_manifest.json','review.md']}
    pending=sum(bool(int(x['callback'],16)) for x in callbacks.values())
    report=dict(format='Reborn Donor Preservation v1',donor=donor,rom=manifest['rom'],maps=len(inventory),tilesets=len(tilesets),object_graphics_ids=len(gfxids),object_art_candidates=sum(a.get('status')=='extracted' for a in art.values()),static_graphics_table_size=catalog.static_count,art_ids_catalogued=len(art),animation_headers=len(callbacks),animation_callbacks_pending=pending,behavior_high_ids=sum(x['status']=='HIGH_BEHAVIOR_REQUIRES_TRANSLATION' for x in behaviors),gameplay_imported=False,new_live_maps=0,status='SOURCE_AND_EDITOR_PRESERVED_RUNTIME_ASSET_CLOSURE_PENDING',files=hashes)
    write(out/'preservation_manifest.json',report)
    (out/'review.md').write_text(f'# {donor.upper()} donor preservation\n\n{len(inventory)} usable maps, {len(tilesets)} normalized tilesets; all blockdata, borders, palettes, metatiles and raw FRLG attributes preserved and checksummed. Object counts are populated from actual NPC arrays. All duplicate/legacy maps remain reference-only.\n\nOpen `editor` as a separate Porymap project. It is an asset-only workspace with no build target, objects, events, warps, connections or donor scripts. Donor relationships and events remain in `reference/export` for research. Do not copy its map registry over Reborn. Native gameplay constants copied for editor parsing only.\n\nFull hash-verified ROM anchor retains otherwise unextracted graphical data. {report["object_art_candidates"]}/{len(art)} catalogued graphics IDs yielded heuristic art candidates (all discovered static IDs plus map-referenced dynamic IDs); table identity, frame closure and dynamic IDs require review. These are not verified runtime art. {pending} nonzero tileset callbacks retain exact header/pointer references but animation frame extraction and Reborn scheduling are pending. {report["behavior_high_ids"]} normalized metatiles have behavior IDs beyond the 8-bit editor field; raw 32-bit attributes are losslessly retained. All behavior semantics still require a FRLG-to-Reborn translation contract before future activation.\n\nThis completes source preservation and editor staging, not runtime asset integration. Existing live maps and ROM are unchanged.\n')
    docs=repo/'docs/la_world/donor_preservation'/donor;docs.mkdir(parents=True,exist_ok=True)
    shutil.copy2(out/'review.md',docs/'review.md')
    for file in ['maps.csv','animations.json']:
        shutil.copy2(out/file,docs/file)
    write(docs/'coverage.json',{k:v for k,v in report.items() if k!='files'})
    print({k:v for k,v in report.items() if k not in ['files','rom']},flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[4]);ap.add_argument('--donor',choices=['bwa','swsh','both'],default='both');args=ap.parse_args()
    repo=args.repo.resolve()
    # Protect all live map/layout/tileset definitions and runtime source files.
    tracked=[p for root in ['data','src','include'] for p in (repo/root).rglob('*') if p.is_file()]
    before={str(p):sha(p) for p in tracked}
    for donor in (['bwa','swsh'] if args.donor=='both' else [args.donor]):run(repo,donor)
    assert all(sha(Path(p))==h for p,h in before.items()),'Live assets changed'
    print('PASS: all existing data/src/include files unchanged')
if __name__=='__main__':main()
