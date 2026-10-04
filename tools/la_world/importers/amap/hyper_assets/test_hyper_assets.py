#!/usr/bin/env python3
"""Revalidate the ported asset contracts, not Hyper's already-proven extraction."""
import hashlib, importlib.util, json, re, subprocess, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
REPORT=ROOT/'.la_work/amap/hyper_asset_integration'
SPEC=importlib.util.spec_from_file_location('port',Path(__file__).with_name('port_hyper_assets.py'))
PORT=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(PORT)

CANARY_REPORT=ROOT/'.la_work/amap/hyper_hoenn_canary1/receipt.json'
def current_expected_hash(f,original):
    # Exact, sequential receipt chain; historical asset-stage hashes stay intact.
    expected=original
    for number,maps in [(1,['OldaleTown','Route102','OldaleTown_Mart']),(2,['LittlerootTown','Route101','Route103','PetalburgCity'])]:
        p=ROOT/f'.la_work/amap/hyper_hoenn_canary{number}/receipt.json'
        if p.exists():
            receipt=PORT.load(p);assert receipt['canonical_maps_replaced']==maps
            change=receipt['changed_baseline_files'].get(f)
            if change:
                assert change['before']==expected,(f,'historical receipt-chain mismatch')
                expected=change['after']
    return expected

def animation_host_test(plan):
    runtime=(ROOT/'src/hyper_tileset_anims.inc').read_text()
    frames=re.findall(r'^static const u16 (sHyperAssetAnimFrameData_\w+)\[\]',runtime,re.M)
    callbacks=[x['callback'] for x in plan['tilesets'] if x['callback'].startswith('InitTilesetAnim_HyperAsset_')]
    prefix='''#include <assert.h>
#include <stdint.h>
#include <stddef.h>
#include <stdio.h>
typedef uint8_t u8;
typedef uint16_t u16;
#define BG_VRAM ((uintptr_t)0x06000000)
#define TILE_OFFSET_4BPP(x) ((x)*32)
#define TILE_SIZE_4BPP 32
static u16 sPrimaryTilesetAnimCounter, sPrimaryTilesetAnimCounterMax;
static u16 sSecondaryTilesetAnimCounter, sSecondaryTilesetAnimCounterMax;
static void (*sPrimaryTilesetAnimCallback)(u16);
static void (*sSecondaryTilesetAnimCallback)(u16);
static unsigned requests, total;
static void AppendTilesetAnimToBuffer(const u16 *, u16 *, u16);
'''
    prefix+=runtime+'\n'
    prefix+='static const struct { const u16 *data; size_t size; } ranges[] = {\n'+ '\n'.join('{'+n+',sizeof('+n+')},' for n in frames)+'\n};\n'
    prefix+='''static void AppendTilesetAnimToBuffer(const u16 *src, u16 *dest, u16 size)
{
    size_t i;
    int found=0;
    assert(size>0 && size%32==0);
    assert((uintptr_t)dest>=BG_VRAM && (uintptr_t)dest+size<=BG_VRAM+1024*32);
    for (i=0;i<sizeof(ranges)/sizeof(ranges[0]);i++)
        if (src==ranges[i].data && size<=ranges[i].size) found=1;
    assert(found);
    assert(++requests<=20);
    total++;
}
int main(void)
{
    unsigned tick;
'''
    for c in callbacks:
        primary='_Primary_' in c
        chosen='sPrimaryTilesetAnimCallback' if primary else 'sSecondaryTilesetAnimCallback'
        prefix+=f'    {c}();\n    assert({chosen}!=NULL);\n    for(tick=0;tick<256;tick++){{ requests=0; {chosen}(tick); }}\n'
    # Exercise every actual Hoenn primary/secondary generic callback combination.
    by_symbol={x['symbol']:x for x in plan['tilesets']};pairs=set()
    for layout in plan['layouts']:
        a=by_symbol[layout['primary_tileset']]['callback'];b=by_symbol[layout['secondary_tileset']]['callback']
        if a.startswith('InitTilesetAnim_HyperAsset_') and b.startswith('InitTilesetAnim_HyperAsset_'):pairs.add((a,b))
    for a,b in sorted(pairs):prefix+=f'    {a}(); {b}();\n    for(tick=0;tick<256;tick++){{requests=0; sPrimaryTilesetAnimCallback(tick);sSecondaryTilesetAnimCallback(tick);}}\n'
    prefix+='    printf("Validated %u DMA frame transfers.\\n",total); return 0;\n}\n'
    source=REPORT/'hyper_animation_host_test.c';source.write_text(prefix)
    executable=REPORT/'hyper_animation_host_test'
    subprocess.run(['gcc','-std=c17','-O1','-g','-fsanitize=address,undefined',str(source),'-o',str(executable)],check=True,capture_output=True,text=True)
    result=subprocess.run([str(executable)],check=True,capture_output=True,text=True)
    return {'callbacks':len(callbacks),'paired_hoenn_combinations':len(pairs),'ticks_per_case':256,'sanitizers':'address,undefined','result':result.stdout.strip()}

class HyperAssetPortTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan=PORT.load(REPORT/'reborn_hyper_asset_integration_plan.json');cls.receipt=PORT.load(REPORT/'integration_receipt.json');cls.donor=ROOT/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export';cls.prior=ROOT.parent/'Legends-Awakening'
    def test_no_canonical_registration_or_donor_gameplay_transfer(self):
        self.assertFalse(self.plan['map_activation']);self.assertFalse(self.plan['donor_gameplay_scripts_imported']);self.assertEqual(0,self.receipt['canonical_maps_replaced'])
        bindings=(ROOT/'src/hyper_asset_graphics_bindings.inc').read_text()
        if CANARY_REPORT.exists():
            expected_maps={'MAP_OLDALE_TOWN','MAP_ROUTE102','MAP_OLDALE_TOWN_MART'}
            if (ROOT/'.la_work/amap/hyper_hoenn_canary2/receipt.json').exists():expected_maps.update(['MAP_LITTLEROOT_TOWN','MAP_ROUTE101','MAP_ROUTE103','MAP_PETALBURG_CITY'])
            self.assertEqual(expected_maps,set(re.findall(r'\{(MAP_\w+),',bindings)))
            self.assertFalse(PORT.load(CANARY_REPORT)['hyper_gameplay_imported'])
        else:self.assertNotRegex(bindings,r'\{\s*MAP_')
        for x in self.plan['layouts']:self.assertFalse(x['registered_in_canonical_map_table'])
        self.assertNotRegex((ROOT/'src/data/object_events/hyper_assets.inc').read_text(),r'FLAG_|VAR_[A-Z]|EventScript_|setvar|callnative')
    def test_existing_gameplay_assets_canaries_flags_save_and_hooks_unchanged(self):
        baseline=PORT.load(REPORT/'protected_baseline.json')
        for f,digest in baseline.items():
            if not PORT.derived_build_file(f) and f not in ['include/constants/layouts.h','data/layouts/layouts.inc','data/layouts/layouts_table.inc']:self.assertEqual(current_expected_hash(f,digest),PORT.digest(ROOT/f),f)
    def test_generated_assets_and_shared_source_receipt_hashes(self):
        for collection in ['generated_files_sha256','shared_source_files']:
            for f,digest in self.receipt[collection].items():self.assertEqual(current_expected_hash(f,digest),PORT.digest(ROOT/f),f)
    def test_lossless_layout_border_and_collision_elevation_pack(self):
        for x in self.plan['layouts']:
            b=(ROOT/x['blockdata_path']).read_bytes();self.assertEqual(x['blockdata_sha256'],hashlib.sha256(b).hexdigest());self.assertEqual(x['dimensions'][0]*x['dimensions'][1]*2,len(b))
            p=next((self.donor/'maps').glob(f'{int(x["donor_id"].split(".")[0]):02}.{int(x["donor_id"].split(".")[1]):02}_*/border.bin'))
            self.assertEqual(p.read_bytes(),(ROOT/x['border_path']).read_bytes())
    def test_tileset_compression_and_recovered_attribute_high_bits(self):
        names=PORT.enums(ROOT/'include/constants/metatile_behaviors.h')
        for x in self.plan['tilesets']:
            base=ROOT/x['path'];prior=self.prior/'data/tilesets'/x['source_id'].split('_')[0]/('amap_'+x['source_id'].lower())
            self.assertEqual((base/'tiles.4bpp').read_bytes(),PORT.decompress_lz((base/'tiles.4bpp.lz').read_bytes()))
            self.assertEqual([v&0xFF00 for v in PORT.u16s(prior/'metatile_attributes.bin')],[v&0xFF00 for v in PORT.u16s(base/'metatile_attributes.bin')])
        x=next(x for x in self.plan['tilesets'] if x['source_id']=='secondary_083DF77C');attrs=PORT.u16s(ROOT/x['path']/'metatile_attributes.bin')
        for index in [508,509]:self.assertEqual(names['MB_NORMAL'],attrs[index]&255)
    def test_source_used_behaviors_translate_to_current_semantics(self):
        catalog=PORT.load(Path(__file__).parent/'reference/hyper_behavior_source_catalog.json');source_names={x['source_id']:x['baseline_name'] for x in catalog['behaviors']};target=PORT.enums(ROOT/'include/constants/metatile_behaviors.h')
        by_id={x['source_id']:x for x in self.plan['tilesets']}
        for layout in self.plan['layouts']:
            source_map=next((self.donor/'maps').glob(f'{int(layout["donor_id"].split(".")[0]):02}.{int(layout["donor_id"].split(".")[1]):02}_*/map.json'));meta=PORT.load(source_map)
            for role,key in enumerate([meta['primary_tileset'],meta['secondary_tileset']]):
                source_attrs=PORT.u16s(self.donor/'tilesets'/key/'metatile_attributes.bin');destination=PORT.u16s(ROOT/by_id[key]['path']/'metatile_attributes.bin')
                used={v&1023 for v in PORT.u16s(ROOT/layout['blockdata_path']) if ((v&1023)>=512)==bool(role)}
                for global_index in used:
                    i=global_index-512 if role else global_index;v=source_attrs[i]&255;name='MB_NORMAL' if v in (0x1f,0x2d) else source_names[v]
                    self.assertEqual(target[name],destination[i]&255,(layout['donor_id'],key,i))
    def test_animation_port_retains_prior_runtime_semantics(self):
        source=(self.prior/'src/amap_tileset_anims_generated.inc').read_text();callbacks=[x['callback'].replace('HyperAsset','AMap') for x in self.plan['tilesets'] if x['callback'].startswith('InitTilesetAnim_HyperAsset_')]
        expected,_=PORT.runtime_subset(source,callbacks);self.assertEqual(expected,(ROOT/'src/hyper_tileset_anims.inc').read_text())
        special=next(x for x in self.plan['tilesets'] if x['source_id']=='secondary_083DFCC4');self.assertEqual('InitTilesetAnim_BattleDome',special['callback'])
    def test_dynamic_graphics_and_expansion_owned_initializers_remain_authoritative(self):
        self.assertEqual(11,len(self.plan['canonical_dynamic_gfx_audit']))
        for x in self.plan['canonical_dynamic_gfx_audit']:self.assertTrue(all(x['labels_present_in_reborn'].values()))
        text=(ROOT/'src/event_object_movement.c').read_text();body=text[text.index('GetObjectEventGraphicsInfo(u16 graphicsId)'):text.index('static void SetObjectEventDynamicGraphicsId(',text.index('GetObjectEventGraphicsInfo(u16 graphicsId)'))]
        self.assertLess(body.index('VarGetObjectEventGraphicsId'),body.index('HyperAssets_GetCanonicalObjectGraphics'))
        self.assertLess(body.index('SpeciesToGraphicsInfo'),body.index('HyperAssets_GetCanonicalObjectGraphics'))
    def test_object_frames_and_animation_abi_bounds(self):
        minimum={'sAnimTable_Standard':9,'sAnimTable_Inanimate':1,'sAnimTable_CuttableTree':4,'sAnimTable_BreakableRock':5}
        for x in self.plan['object_graphics']:
            self.assertGreaterEqual(x['frame_count'],minimum[x['anims']]);p=ROOT/f'graphics/object_events/hyper/gfx_{x["source_graphics_id"]:03}.4bpp'
            self.assertEqual(x['frame_size']*x['frame_count'],p.stat().st_size)
            self.assertEqual(x['graphics_sha256'],PORT.digest(p))
        self.assertEqual([205,206],[x['source_graphics_id'] for x in self.plan['object_graphics'] if x['inherited_prior_visual_edit']])
    def test_palette_namespace_dedup_and_index_capacity(self):
        self.assertEqual(16,self.plan['counts']['deduplicated_sprite_palettes']);tags={x['palette_tag'] for x in self.plan['object_graphics']};self.assertEqual(set(range(0xD800,0xD810)),tags)
        self.assertNotRegex((ROOT/'include/constants/event_objects.h').read_text(),r'OBJ_EVENT_GFX_HYPER')
    def test_recovered_animation_callbacks_and_paired_dma_bounds(self):
        self.__class__.host_result=animation_host_test(self.plan)
        self.assertEqual(20,self.host_result['callbacks']);self.assertGreater(self.host_result['paired_hoenn_combinations'],0)

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(HyperAssetPortTests);result=unittest.TextTestRunner(verbosity=2).run(suite)
    PORT.dump(REPORT/'test_results.json',{'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'passed':result.wasSuccessful(),'animation_host':getattr(HyperAssetPortTests,'host_result',None)})
    raise SystemExit(0 if result.wasSuccessful() else 1)
