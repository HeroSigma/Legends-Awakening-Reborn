#!/usr/bin/env python3
"""Port the proven Hyper asset bank without installing donor gameplay or maps."""
import argparse, collections, hashlib, json, re, shutil, struct
from pathlib import Path

ROM_SHA='73d6faeb29bcc15e1627a6f237e99e11ddea8429ed31ec30057560ee069a546f'
SHARED=['src/data/tilesets/headers.h','src/data/tilesets/graphics.h','src/data/tilesets/metatiles.h','include/tileset_anims.h','src/tileset_anims.c','src/event_object_movement.c']
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def emit(p,data):
    p.parent.mkdir(parents=True,exist_ok=True)
    b=data.encode() if isinstance(data,str) else data
    if not p.exists() or p.read_bytes()!=b:p.write_bytes(b)
def dump(p,obj):emit(p,json.dumps(obj,indent=2,sort_keys=True)+'\n')
def u16s(p):
    b=p.read_bytes();return struct.unpack('<'+'H'*(len(b)//2),b)
def enums(p):
    text=re.sub(r'/\*.*?\*/|//[^\n]*','',p.read_text(),flags=re.S)
    body=re.search(r'enum\s*\{(.*?)NUM_METATILE_BEHAVIORS',text,re.S)[1]
    names={};v=0
    for row in body.split(','):
        row=row.strip()
        if not row:continue
        if '=' in row:name,x=map(str.strip,row.split('='));v=int(x,0)
        else:name=row
        assert re.fullmatch(r'MB_\w+',name),row
        names[name]=v;v+=1
    return names

def decompress_lz(b):
    assert b[0]==0x10;size=int.from_bytes(b[1:4],'little');out=bytearray();pos=4
    while len(out)<size:
        flags=b[pos];pos+=1
        for bit in range(7,-1,-1):
            if len(out)>=size:break
            if flags&(1<<bit):
                a,c=b[pos:pos+2];pos+=2;distance=((a&15)<<8|c)+1
                for _ in range((a>>4)+3):out.append(out[-distance])
            else:out.append(b[pos]);pos+=1
    return bytes(out[:size])

def managed_include(path,line,anchor=None):
    s=path.read_text()
    if line in s:return
    if anchor:
        assert s.count(anchor)==1,(path,anchor);s=s.replace(anchor,anchor+'\n'+line)
    else:s=s.rstrip()+'\n\n'+line+'\n'
    emit(path,s)

def derived_build_file(rel):
    p=Path(rel)
    return rel=='include/constants/map_event_ids.h' or (rel.startswith('data/maps/') and p.name in ('events.inc','header.inc','connections.inc'))

def source_snapshot(repo,donor,old):
    result={}
    for base in [repo/'data',repo/'src',repo/'include',repo/'graphics',donor]:
        for p in sorted(base.rglob('*')):
            if p.is_file() and str(p.relative_to(repo)) not in SHARED:result[str(p.relative_to(repo))]=digest(p)
    return result

def runtime_subset(old_text,callbacks):
    prefix=old_text[:old_text.index('/* Exact source-ROM 4bpp animation frame data. */')]
    definitions={};ordered=[]
    for match in re.finditer(r'^static const[^\n]*\s+(\w+)(?:\[\])?\s*=\s*\{.*?^\};',old_text,re.M|re.S):
        definitions[match[1]]=match[0];ordered.append(match[1])
    for match in re.finditer(r'^void (InitTilesetAnim_AMap_\w+)\(void\)\n\{.*?^\}',old_text,re.M|re.S):
        definitions[match[1]]=match[0];ordered.append(match[1])
    needed=set(callbacks);pending=list(needed)
    while pending:
        name=pending.pop();assert name in definitions,name
        for ref in re.findall(r'\bsAMap\w+',definitions[name]):
            if ref in definitions and ref not in needed:needed.add(ref);pending.append(ref)
    result=prefix+'\n'.join(definitions[n] for n in ordered if n in needed)+'\n'
    result=result.replace('AMap','HyperAsset').replace('A-MAP','HYPER ASSET')
    return result,{'definitions':len(needed),'callbacks':len(callbacks),'frame_data_arrays':sum(n.startswith('sAMapAnimFrameData') for n in needed)}

def build(repo,old,donor,report,apply):
    repo=repo.resolve();old=old.resolve();donor=donor.resolve();report=report.resolve()
    manifest=load(donor/'manifest.json');assert manifest['rom']['sha256']==ROM_SHA
    correspondence=load(repo/'.la_work/amap/hyper_hoenn_replacement/hyper_hoenn_replacement_manifest.json')
    records=correspondence['maps'];assert len(records)==518
    tilesets=sorted({t for r in records for t in r['hyper']['tilesets']})
    old_behaviors=enums(old/'include/constants/metatile_behaviors.h');new_behaviors=enums(repo/'include/constants/metatile_behaviors.h');old_names={v:k for k,v in old_behaviors.items()}
    animation_report=load(old/'amap_tileset_animation_integration_report.json');assignments=animation_report['callback_assignments'];assert not animation_report['errors']
    report.mkdir(parents=True,exist_ok=True)
    baseline_path=report/'protected_baseline.json'
    if not baseline_path.exists():
        dump(baseline_path,source_snapshot(repo,donor,old))
        for f in SHARED:emit(report/'shared_source_backup'/f,(repo/f).read_bytes())
    raw_baseline=load(baseline_path);protected={f:h for f,h in raw_baseline.items() if not derived_build_file(f)};derived={f:{'before':h,'after':digest(repo/f)} for f,h in raw_baseline.items() if derived_build_file(f) and (repo/f).exists() and digest(repo/f)!=h}
    for f,h in protected.items():assert (repo/f).is_file() and digest(repo/f)==h,f'Protected input changed: {f}'
    generated={};tile_rows=[];graphics_lines=[];metatile_lines=[];header_lines=[];callbacks=[];provenance={};behavior_changes=0
    def stage(path,data):generated[str(path)]=data.encode() if isinstance(data,str) else data
    # Validate the earlier recovered custom behavior exception across actual uses.
    custom_uses=collections.Counter();referenced=collections.defaultdict(set);inactive_custom_attributes=[]
    source_maps=[load(p) for p in sorted((donor/'maps').glob('*/map.json'))]
    for d in source_maps:
        p=next((donor/'maps').glob(f'{d["group"]:02}.{d["map"]:02}_*/blockdata.bin'))
        for w in u16s(p):
            mid=w&1023;role=0 if mid<512 else 1;key=d['primary_tileset'] if role==0 else d['secondary_tileset'];referenced[key].add(mid if role==0 else mid-512)
            if d['secondary_tileset']=='secondary_083DF77C' and (w&1023) in (1020,1021):
                assert ((w>>10)&3)==1,'Custom decorative behavior guard failed';custom_uses[w&1023]+=1
    for key in tilesets:
        role,address=key.split('_');capital=role.title();symbol=f'Hyper_{capital}_{address}';base=Path(f'data/tilesets/{role}/hyper_{key.lower()}');prior=old/f'data/tilesets/{role}/amap_{key.lower()}';export=donor/'tilesets'/key
        meta=load(export/'tileset.json');assert prior.exists(),prior
        raw=(export/'tiles.4bpp').read_bytes();padded=(prior/'tiles.4bpp').read_bytes();compressed=(prior/'tiles.4bpp.lz').read_bytes()
        assert padded.startswith(raw) and not any(padded[len(raw):]),key
        assert decompress_lz(compressed)==padded,key
        assert hashlib.sha256(raw).hexdigest()==meta['sha256']['tiles_4bpp'],key
        old_mt=(prior/'metatiles.bin').read_bytes();source_mt=(export/'metatiles.bin').read_bytes();assert old_mt.startswith(source_mt),key
        # Prior asset bank contains one extra visual metatile, not a script.
        if len(old_mt)!=len(source_mt) and any(old_mt[len(source_mt):]):assert key=='secondary_083DF71C' and len(old_mt)-len(source_mt)==16
        attrs=list(u16s(prior/'metatile_attributes.bin'));source_attrs=u16s(export/'metatile_attributes.bin');translated=[]
        source_names={x['source_id']:x['baseline_name'] for x in load(Path(__file__).parent/'reference/hyper_behavior_source_catalog.json')['behaviors']}
        for index,value in enumerate(attrs):
            source_value=source_attrs[index]&255 if index<len(source_attrs) else value&255
            name=source_names.get(source_value,old_names[value&255])
            if source_value in (0x1F,0x2D):
                if not (key=='secondary_083DF77C' and index=={0x1F:509,0x2D:508}[source_value]):
                    assert index not in referenced[key],(key,index)
                    inactive_custom_attributes.append({'tileset':key,'index':index,'source_behavior':source_value,'action':'Neutral unused slot; never referenced by any of 922 source layouts. Future scripted tile substitutions require explicit review.'})
                name='MB_NORMAL'
            assert name in new_behaviors,(key,name)
            target=new_behaviors[name];assert target<256,(key,name,target)
            translated.append((value&0xFF00)|target);behavior_changes+=(value&255)!=target
        # Recovered special slots are already neutralized. Keep their proven guard.
        if key=='secondary_083DF77C':
            for index in (508,509):assert translated[index]&255==new_behaviors['MB_NORMAL']
        stage(base/'tiles.4bpp.lz',compressed);stage(base/'tiles.4bpp',padded);stage(base/'tiles.png',(prior/'tiles.png').read_bytes());stage(base/'metatiles.bin',old_mt);stage(base/'metatile_attributes.bin',struct.pack('<'+'H'*len(translated),*translated))
        palette_lines=[]
        for slot in range(13):
            path=prior/f'palettes/{slot:02}.gbapal';assert path.stat().st_size==32
            stage(base/f'palettes/{slot:02}.gbapal',path.read_bytes())
            pal_text=prior/f'palettes/{slot:02}.pal'
            if pal_text.exists():stage(base/f'palettes/{slot:02}.pal',pal_text.read_bytes())
            source_pal=export/f'palettes/{slot:02}.pal'
            if source_pal.exists():
                rgb=[tuple(map(int,line.split())) for line in source_pal.read_text().splitlines()[3:19]]
                assert struct.pack('<16H',*(a//8|b//8<<5|c//8<<10 for a,b,c in rgb))==path.read_bytes(),(key,slot)
            palette_lines.append(f'    INCBIN_U16("{base}/palettes/{slot:02}.gbapal"),')
        graphics_lines.append(f'const u16 ALIGNED(4) gTilesetPalettes_{symbol}[][16] =\n{{\n'+ '\n'.join(palette_lines)+'\n};\n'+f'const u32 gTilesetTiles_{symbol}[] = INCBIN_U32("{base}/tiles.4bpp.lz");')
        metatile_lines.append(f'const u16 gMetatiles_{symbol}[] = INCBIN_U16("{base}/metatiles.bin");\nconst u16 gMetatileAttributes_{symbol}[] = INCBIN_U16("{base}/metatile_attributes.bin");')
        old_symbol=f'gTileset_AMap_{capital}_{address}';cb=assignments.get(old_symbol,'NULL')
        if cb.startswith('InitTilesetAnim_AMap_'):callbacks.append(cb);cb=cb.replace('AMap','HyperAsset')
        header_lines.append(f'const struct Tileset gTileset_{symbol} =\n{{\n    .isCompressed = TRUE,\n    .isSecondary = {"FALSE" if role=="primary" else "TRUE"},\n    .tiles = gTilesetTiles_{symbol},\n    .palettes = gTilesetPalettes_{symbol},\n    .metatiles = gMetatiles_{symbol},\n    .metatileAttributes = gMetatileAttributes_{symbol},\n    .callback = {cb},\n}};')
        tile_rows.append({'source_id':key,'symbol':f'gTileset_{symbol}','path':str(base),'callback':cb,'metadata':meta,'recovered_extension_bytes':len(old_mt)-len(source_mt),'source_graphics_sha256':hashlib.sha256(raw).hexdigest(),'recovered_graphics_sha256':hashlib.sha256(padded).hexdigest(),'source_attributes_sha256':digest(export/'metatile_attributes.bin'),'recovered_attributes_sha256':digest(prior/'metatile_attributes.bin'),'translated_attributes_sha256':hashlib.sha256(generated[str(base/'metatile_attributes.bin')]).hexdigest()})
        for p in prior.rglob('*'):
            if p.is_file():provenance[str(p)]=digest(p)
    for kind,lines in [('graphics',graphics_lines),('metatiles',metatile_lines),('headers',header_lines)]:stage(Path(f'src/data/tilesets/hyper_{kind}.h'),'/* Proven Hyper asset bank; no map registration or gameplay. */\n'+'\n\n'.join(lines)+'\n')
    old_runtime=(old/'src/amap_tileset_anims_generated.inc').read_text();runtime,runtime_summary=runtime_subset(old_runtime,callbacks)
    stage(Path('src/hyper_tileset_anims.inc'),runtime)
    stage(Path('include/hyper_tileset_anims.h'),'#ifndef GUARD_HYPER_TILESET_ANIMS_H\n#define GUARD_HYPER_TILESET_ANIMS_H\n'+'\n'.join(f'void {c.replace("AMap","HyperAsset")}(void);' for c in callbacks)+'\n#endif\n')
    layout_rows=[]
    for r in records:
        d=r['hyper'];folder=donor/Path(d['map_json_path']).relative_to(donor.relative_to(repo));base=Path('data/hyper_assets/layouts')/d['id'];source=folder.parent
        for original,target in [('blockdata.bin','map.bin'),('border.bin','border.bin')]:stage(base/target,(source/original).read_bytes())
        layout_rows.append({'canonical_id':r['canonical']['id'],'canonical_name':r['canonical']['name'],'donor_id':d['id'],'dimensions':d['dimensions'],'primary_tileset':next(x['symbol'] for x in tile_rows if x['source_id']==d['tilesets'][0]),'secondary_tileset':next(x['symbol'] for x in tile_rows if x['source_id']==d['tilesets'][1]),'blockdata_path':str(base/'map.bin'),'border_path':str(base/'border.bin'),'blockdata_sha256':d['blockdata_sha256'],'donor_header_pointer':d['header_pointer'],'donor_layout_pointer':d['layout_pointer'],'registered_in_canonical_map_table':False})
    # Port the earlier sprite definitions, with disjoint symbols and palette tags.
    info_text=(old/'src/data/object_events/object_event_graphics_info.h').read_text()
    info_text=info_text.split('// A-MAP BATCH SPRITES BEGIN: graphics info')[1].split('// A-MAP BATCH SPRITES END')[0]
    infos={int(n):body for n,body in re.findall(r'const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_AMap(\d+) = (\{.*?\};)',info_text,re.S)}
    pics=(old/'src/data/object_events/object_event_pic_tables.h').read_text()
    pic_tables={int(n):body for n,body in re.findall(r'static const struct SpriteFrameImage sPicTable_AMap(\d+)\[\] = (\{.*?\};)',pics,re.S)}
    object_lines=[];pic_lines=[];info_lines=[];palette_lines=[];object_rows=[];palettes={}
    for gfx in sorted(infos):
        prior_pic=old/f'graphics/object_events/pics/amap/gfx_{gfx:03}.4bpp';prior_pal=old/f'graphics/object_events/palettes/amap/gfx_{gfx:03}.gbapal'
        exported=donor/f'sprites/gfx_{gfx:03}';sm=load(exported/'sprite.json')
        source_frames=(exported/'frames.4bpp').read_bytes();prior_frames=prior_pic.read_bytes()
        assert len(prior_frames)==len(source_frames),gfx
        if prior_frames!=source_frames:assert gfx in (205,206),'Unexpected prior art variation' 
        assert prior_pal.read_bytes()==(exported/'palette.gbapal').read_bytes(),gfx
        pal=prior_pal.read_bytes();assert len(pal)==32
        if pal not in palettes:
            index=len(palettes);palettes[pal]=index
            stage(Path(f'graphics/object_events/hyper/palettes/{index:02}.gbapal'),pal)
            object_lines.append(f'const u16 gObjectEventPal_HyperAsset{index:02}[] = INCBIN_U16("graphics/object_events/hyper/palettes/{index:02}.gbapal");')
            palette_lines.append(f'    {{gObjectEventPal_HyperAsset{index:02}, 0x{0xD800+index:04X}}},')
        palette_index=palettes[pal];tag=0xD800+palette_index
        stage(Path(f'graphics/object_events/hyper/gfx_{gfx:03}.4bpp'),prior_pic.read_bytes())
        object_lines.append(f'const u32 gObjectEventPic_HyperAsset{gfx:03}[] = INCBIN_U32("graphics/object_events/hyper/gfx_{gfx:03}.4bpp");')
        pic_lines.append(f'static const struct SpriteFrameImage sPicTable_HyperAsset{gfx:03}[] = '+pic_tables[gfx].replace('AMap','HyperAsset'))
        body=infos[gfx].replace('AMap','HyperAsset');body=re.sub(r'\.paletteTag = 0x[0-9A-Fa-f]+',f'.paletteTag = 0x{tag:04X}',body)
        info_lines.append(f'const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_HyperAsset{gfx:03} = '+body)
        object_rows.append({'source_graphics_id':gfx,'graphics_info_symbol':f'gObjectEventGraphicsInfo_HyperAsset{gfx:03}','palette_tag':tag,'palette_index':palette_index,'frame_count':sm['frame_count'],'frame_size':sm['expected_frame_size'],'source_reserved_sprite_size':sm['frame_size'],'source_frame_sizes':sm['frame_sizes'],'source_graphics_info_pointer':sm['graphics_info_pointer'],'anims':re.search(r'\.anims = (\w+)',body)[1],'graphics_sha256':digest(prior_pic),'export_graphics_sha256':digest(exported/'frames.4bpp'),'inherited_prior_visual_edit':prior_frames!=source_frames,'palette_sha256':digest(prior_pal),'width':sm['width'],'height':sm['height']})
        provenance[str(prior_pic)]=digest(prior_pic);provenance[str(prior_pal)]=digest(prior_pal)
    current_movement=(repo/'src/event_object_movement.c').read_text();pi=current_movement.index('static const struct SpritePalette sObjectEventSpritePalettes[]');pe=current_movement.index('\n};',pi)
    native_palette_count=len(re.findall(r'^\s*\{',current_movement[pi:pe],re.M))
    assert native_palette_count+len(palettes)<255,'Palette index ABI capacity exceeded'
    constants='\n'.join(p.read_text(errors='replace') for p in (repo/'include/constants').glob('*object*pal*.h'))
    assert not any(int(v,16) in range(0xD800,0xD800+len(palettes)) for v in re.findall(r'0x([\da-fA-F]+)',constants))
    object_bank='/* Ported proven renderer data; donor gameplay is absent. */\n'+'\n'.join(object_lines+pic_lines+info_lines)+'\n'
    object_bank+='static const struct ObjectEventGraphicsInfo *const sHyperSourceObjectGraphics[] = {\n'+'\n'.join(f'    [{x}] = &gObjectEventGraphicsInfo_HyperAsset{x:03},' for x in sorted(infos))+'\n};\n'
    object_bank+='''
const struct ObjectEventGraphicsInfo *HyperAssets_GetSourceObjectGraphicsInfo(u16 sourceId)
{
    if (sourceId < ARRAY_COUNT(sHyperSourceObjectGraphics))
        return sHyperSourceObjectGraphics[sourceId];
    return NULL;
}

struct HyperAssetGraphicsBinding
{
    u16 canonicalMap;
    u16 expansionGraphicsId;
    const struct ObjectEventGraphicsInfo *graphicsInfo;
};

/* Deliberate opt-in only. Reviewed per-symbol visual structs must preserve
 * canonical animation/player/berry contracts. The sentinel activates no maps. */
static const struct HyperAssetGraphicsBinding sHyperAssetGraphicsBindings[] = {
#include "../../hyper_asset_graphics_bindings.inc"
    {0xFFFF, 0xFFFF, NULL},
};

static const struct ObjectEventGraphicsInfo *HyperAssets_GetCanonicalObjectGraphics(u16 graphicsId)
{
    u32 i;
    u16 currentMap = (gSaveBlock1Ptr->location.mapGroup << 8) | gSaveBlock1Ptr->location.mapNum;
    for (i = 0; sHyperAssetGraphicsBindings[i].canonicalMap != 0xFFFF; i++)
    {
        const struct HyperAssetGraphicsBinding *binding = &sHyperAssetGraphicsBindings[i];
        if (binding->canonicalMap == currentMap && binding->expansionGraphicsId == graphicsId)
            return binding->graphicsInfo;
    }
    return NULL;
}
'''
    stage(Path('src/data/object_events/hyper_assets.inc'),object_bank)
    stage(Path('src/data/object_events/hyper_palettes.inc'),'/* Deduplicated visual palette bank; existing tags retain their meanings. */\n'+'\n'.join(palette_lines)+'\n')
    bindings=repo/'src/hyper_asset_graphics_bindings.inc'
    stage(Path('src/hyper_asset_graphics_bindings.inc'),bindings.read_bytes() if bindings.exists() else '/* No canonical maps opted in. Later reviewed bindings use MAP_* and OBJ_EVENT_GFX_* symbols. */\n')
    stage(Path('include/hyper_assets.h'),'''#ifndef GUARD_HYPER_ASSETS_H
#define GUARD_HYPER_ASSETS_H
struct ObjectEventGraphicsInfo;
/* Source IDs name visual assets only; they are never assigned to event gameplay IDs. */
const struct ObjectEventGraphicsInfo *HyperAssets_GetSourceObjectGraphicsInfo(u16 sourceId);
#endif
''')
    # Current canonical hooks already supply these expansion-owned variables.
    dynamic_report=load(old/'amap_dynamic_gfx_deep_trace_verified_report.json');dynamic=[]
    for row in dynamic_report['maps']:
        if not row['safe_graphics_subroutines']:continue
        canonical=row['native_counterpart'];path=repo/'data/maps'/canonical/'scripts.inc';text=path.read_text();labels=[x['label'] for x in row['safe_graphics_subroutines']]
        dynamic.append({'canonical_name':canonical,'verified_prior_labels':labels,'labels_present_in_reborn':{label:bool(re.search(r'^'+re.escape(label)+r':',text,re.M)) for label in labels},'canonical_hook_sha256':digest(path),'action':'KEEP_EXISTING_EXPANSION_INIT; do not copy old imported-map wrappers or donor variables.'})
    evidence_files=[old/'amap_tileset_animation_integration_report.json',old/'src/amap_tileset_anims_generated.inc',old/'include/constants/metatile_behaviors.h',old/'src/data/object_events/object_event_graphics_info.h',old/'src/data/object_events/object_event_pic_tables.h',old/'amap_dynamic_gfx_deep_trace_verified_report.json',old/'amap_p1_final_mapped_closure_verifier_v0_6_7_report.json',old/'amap_p2_persistent_flag_bridge_postapply_verifier_v0_4_22_review.md',Path('/mnt/c/Users/aadair/Downloads/tools/amap_behavior_translation_v0_1_2/README.md')]
    for p in evidence_files:provenance[str(p)]=digest(p)
    components=[
      {'component':'Recovered tileset graphics/palettes/metatiles','solved':'Correct original tile indices, palette banks, rendering data and required padding.','reborn_before':'MISSING Hyper bank; BWA/SWSH use separate assets.','direct_port':'YES, into disjoint Hyper symbols and directories.','regenerate':'Declarations, namespaces and provenance. Reuse proven compressed/art data.','dependencies':['full export ROM identity','prior asset bank'],'validation':['decompress against recovered padded tiles','export-prefix/palette comparison','full ROM build']},
      {'component':'Behavior translation v0.1.2','solved':'126 semantic behavior mappings plus two guarded decorative facade overrides.','reborn_before':'No Hyper-specific translated attributes. Expansion behavior enum exists.','direct_port':'Algorithm/evidence YES; numeric destination bytes NO.','regenerate':'Low behavior byte by recovered source semantics to current enum; reapply the proven custom exception even if an old generated binary was rebuilt; retain all high attribute bits.','dependencies':['prior translated attributes','current enum','exact custom-use guard'],'validation':['all selected attribute names','collision/elevation/layout hashes unchanged','traversal canary']},
      {'component':'Tileset animation integration v0.2','solved':'Mask/modulo/conditional/continuation descriptors and Battle Dome palette callback.','reborn_before':'Missing generated Hyper frame/runtime bank; native animation DMA/Battle Dome support present.','direct_port':'YES; reuse recovered exact frame payloads and runtime semantics.','regenerate':'Reachable Hoenn subset and symbols/prototypes; no ROM archaeology.','dependencies':['prior generated runtime','prior callback assignments','Reborn DMA ABI'],'validation':['descriptor/frame bounds','256-tick host simulation','native build','animated Hoenn canary']},
      {'component':'Object graphics closure / recovered sprite bank','solved':'Static art/frame/palette/graphics ABI plus prior 46-map/460-object runtime closure.','reborn_before':'Canonical native sprites present; recovered Hyper bank missing.','direct_port':'Renderer definitions/art YES. Imported event mutations/IDs NO.','regenerate':'Disjoint symbols; deduplicate palettes; per-canonical-symbol opt-in visual bindings.','dependencies':['recovered sprites','current renderer ABI'],'validation':['194 exact frame/palette checks','animation index bounds','palette capacity/tags','full build','NPC/dynamic visual canary']},
      {'component':'Dynamic GFX verified bridge v0.2','solved':'Called/merged expansion graphics initializers on formerly additive maps.','reborn_before':'Native dynamic-GFX resolver and canonical initializers already present.','direct_port':'No map wrapper transfer required for canonical replacement.','regenerate':'Audit existing canonical initializers; opt-in visual lookup after native resolution.','dependencies':['native OBJ_EVENT_GFX_VAR_*','expansion hook ownership'],'validation':['11 initializer families audited','both genders/state changes','native variables/hooks unchanged']},
      {'component':'Persistent flag bridge','solved':'Historical Hyper imported-event state/save routing.','reborn_before':'Expansion/project save and flags authoritative.','direct_port':'NO; reference only.','regenerate':'Nothing.','dependencies':[],'validation':['flags/vars/save source hashes unchanged']},
      {'component':'Layout/blockdata/border package','solved':'Lossless source world geometry, collision and elevation.','reborn_before':'Full export available, canonical layouts unchanged.','direct_port':'YES into an unregistered asset staging bank.','regenerate':'Canonical-name correspondence and asset-only paths.','dependencies':['replacement manifest'],'validation':['518 block/border hashes','no canonical registration','later event/warp-coordinate ledger']},
    ]
    plan={'schema':'reborn-hyper-asset-integration-v1','policy':'Hyper supplies world/assets; expansion supplies gameplay brain. Prior recovery is proven and reused, not rediscovered per map.','components':components,'counts':{'hoenn_layout_assets':len(layout_rows),'tilesets':len(tile_rows),'animated_tilesets':len(callbacks)+1,'generic_animation_callbacks':len(callbacks),'sprite_graphics':len(object_rows),'deduplicated_sprite_palettes':len(palettes),'translated_behavior_values_changed':behavior_changes},'animation':runtime_summary,'custom_behavior_uses':dict(custom_uses),'inactive_custom_attributes':inactive_custom_attributes,'canonical_dynamic_gfx_audit':dynamic,'tilesets':tile_rows,'layouts':layout_rows,'object_graphics':object_rows,'map_activation':False,'donor_gameplay_scripts_imported':False,'save_abi_changed':False,'canary':{'canonical_maps':[{'name':'OldaleTown','donor_id':'0.10'},{'name':'Route102','donor_id':'0.17'},{'name':'OldaleTown_Mart','donor_id':'2.4'}],'purpose':'Reborn asset-stack integration: outdoor world/grass/water, primary animations, trainer/berry/item art, native rival dynamic graphics, indoor doorway/palette transition.','ownership':'Keep canonical map constants, expansion scripts/NPCs/state/encounters/heals/warp targets/connections. Deliberately remap coordinates to Hyper geometry later.','executed':False,'required_tests':['world graphics/collision/elevation/grass/door behavior','water/flower animation and map transitions','rival both genders via expansion initializer','NPC facing/walking, trainer battle, item/berry behavior','Mart purchase/cancel','gate scene with prerequisites unmet/met','normal travel, blackout, save/reload/re-entry','BWA/SWSH regression visits']}}
    dump(report/'reborn_hyper_asset_integration_plan.json',plan);dump(report/'prior_asset_provenance.json',provenance)
    emit(report/'reborn_hyper_asset_integration_plan.md',review(plan))
    if apply:
        for rel,data in generated.items():emit(repo/rel,data)
        for kind in ('graphics','metatiles','headers'):managed_include(repo/f'src/data/tilesets/{kind}.h',f'#include "hyper_{kind}.h"')
        managed_include(repo/'include/tileset_anims.h','#include "hyper_tileset_anims.h"',anchor='#define GUARD_TILESET_ANIMS_H')
        managed_include(repo/'src/tileset_anims.c','#include "hyper_tileset_anims.inc"')
        managed_include(repo/'src/event_object_movement.c','#include "data/object_events/hyper_assets.inc"',anchor='#include "data/object_events/object_event_graphics_info_followers.h"')
        managed_include(repo/'src/event_object_movement.c','#include "hyper_assets.h"',anchor='#include "global.h"')
        path=repo/'src/event_object_movement.c';text=path.read_text()
        pal_include='#include "data/object_events/hyper_palettes.inc"'
        if pal_include not in text:
            start=text.index('static const struct SpritePalette sObjectEventSpritePalettes[]');end=text.index('\n};',start);chunk=text[start:end];assert '#ifdef BUGFIX' in chunk;chunk=chunk.replace('#ifdef BUGFIX',pal_include+'\n#ifdef BUGFIX');text=text[:start]+chunk+text[end:]
        hook='''    /* Visual-only opt-in after expansion dynamic/species resolution. */
    const struct ObjectEventGraphicsInfo *hyperGraphics = HyperAssets_GetCanonicalObjectGraphics(graphicsId);
    if (hyperGraphics != NULL)
        return hyperGraphics;

'''
        if hook not in text:
            anchor='    if (graphicsId >= NUM_OBJ_EVENT_GFX)\n';assert text.count(anchor)==1;text=text.replace(anchor,hook+anchor)
        emit(path,text)
        for f,h in protected.items():assert digest(repo/f)==h,f'Protected input modified: {f}'
        dump(report/'asset_catalog.json',{'tilesets':tile_rows,'layouts':layout_rows,'object_graphics':object_rows})
        receipt={'applied_asset_infrastructure':True,'canonical_maps_replaced':0,'hyper_gameplay_scripts_imported':0,'graphics_bindings_active':False,'protected_existing_files':len(protected),'generated_build_outputs_refreshed_from_preexisting_user_sources':derived,'protected_existing_files_unchanged':True,'generated_files_sha256':{rel:digest(repo/rel) for rel in generated},'shared_source_files':{f:digest(repo/f) for f in SHARED},'runtime_canary_executed':False}
        dump(report/'integration_receipt.json',receipt)
    print(json.dumps({'mode':'apply' if apply else 'audit','counts':plan['counts'],'report':str(report)},indent=2))

def review(plan):
    lines=['# Reborn Hyper Asset Integration Plan','','**Reuse the proven Hyper recovery stack. Hyper supplies world/assets; expansion supplies the gameplay brain.** No canonical replacement or donor gameplay transfer is part of this implementation.','','| Prior component | Solved | Already in Reborn | Port / regeneration | Required validation |','|---|---|---|---|---|']
    for c in plan['components']:lines.append('| '+ ' | '.join([c['component'],c['solved'],c['reborn_before'],c['direct_port']+' '+c['regenerate'],'; '.join(c['validation'])])+' |')
    lines+=['','Component dependencies are recorded explicitly in the JSON plan. Prior closure/behavior/animation evidence is pinned by source hashes. No map-by-map extraction rediscovery is proposed.','',f'Asset scope: {plan["counts"]}.','', 'Recovered tiles/palettes are reused with their validated zero padding. Metatile index 144 of secondary 083DF71C is an existing extra visual-only recovered asset. Attribute behaviors are rebound by semantic names; high attribute bits and world collision/elevation remain unchanged. Animation data is pruned to the reachable Hoenn callback/frame subset and namespaced, retaining the proven conditional/continuation engine and the expansion Battle Dome callback.','', 'The object bank retains proven graphic/frame definitions, with identical palettes deduplicated into a disjoint 0xD800 namespace. It introduces no event graphics enum IDs, source flags/vars, NPCs or story hooks. The renderer resolves native dynamic-GFX variables first. Per-canonical-map/symbol visual bindings default to empty; current canonical and BWA/SWSH graphics therefore retain their existing paths. Dynamic GFX initializer audits do not install old additive-map wrappers.','', 'The staged layout bank contains source blocks and borders only. Canonical layout/map-group tables remain untouched. The flag bridge, old save routing, object-restoration edits, map script wrappers and donor NPC/script ownership are deliberately not ported.','', '## Meaningful later replacement canary','','Prepare **OldaleTown ← 0.10, Route102 ← 0.17, OldaleTown_Mart ← 2.4** as a connected three-map canonical batch. This tests a Hyper overworld, terrain/grass/door behavior, primary animation, static NPC/trainer/item/berry art, expansion-owned rival dynamic graphics, and an indoor palette transition.','', 'Keep canonical map names/IDs, story hooks, NPC gameplay, flags/vars, encounters, healing/blackout/Fly, connection targets and warp destination semantics. Reconcile actor/trigger/door coordinates to the source geometry with a reviewed ledger. Bind visual graphics by current expansion symbols, including the native resolved Brendan/May rival states, not source numeric dynamic IDs. No added donor NPCs or scripts.','', 'Runtime exit cases: both player genders and rival states; unmet/met Oldale gate prerequisites; walking/facing/interactions; trainer battle and berries/items; Mart purchase/cancel; animation across re-entry; ordinary travel, blackout and save/reload; validated BWA/SWSH regression visits. This batch is recommended, not executed.','', '## Validation boundary','','Asset-data checks and the normal ROM build establish Reborn compatibility of the reusable infrastructure. Runtime checks on canonical Hyper geometry remain the later canary exit condition. The integration receipt records the exact source changes and protected files. The previous five-map static-geometry shortlist remains a geometry comparison, not a statement that Hyper extraction is unproven.']
    return '\n'.join(lines)+'\n'

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=Path.cwd());p.add_argument('--prior-repo',type=Path);p.add_argument('--donor',type=Path);p.add_argument('--report',type=Path);p.add_argument('--apply',action='store_true');a=p.parse_args()
    build(a.repo,a.prior_repo or a.repo.parent/'Legends-Awakening',a.donor or a.repo/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export',a.report or a.repo/'.la_work/amap/hyper_asset_integration',a.apply)
