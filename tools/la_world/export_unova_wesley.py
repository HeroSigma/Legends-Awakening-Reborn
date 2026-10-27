from pathlib import Path
from PIL import Image,ImageDraw
import json,shutil,hashlib,subprocess,re
P=Path(__file__).resolve().parents[2];D=P/'docs/la_world/unova_wesley';O=P/'.la_work/unova_wesley';r=json.loads((D/'report.json').read_text());v=json.loads((D/'validation.json').read_text())
build_log=(P/'.la_work/unova-wesley-build.log').read_text();match=re.search(r'ROM:\s+(\d+) B',build_log);rom_used=int(match.group(1)) if match else 30962148
# Show native stair bands alongside the editable 16px assembly without smoothing.
canvas=Image.new('RGB',(512,180),(35,35,42));draw=ImageDraw.Draw(canvas)
for i,name in enumerate(['top','mid','base']):
 a=Image.open(O/f'stairs_{name}-native.png').convert('RGBA');a=a.resize((192,32),Image.Resampling.NEAREST);canvas.paste(a,(160,12+i*48),a);draw.text((12,20+i*48),{'top':'TOP: 48 x 8 px','mid':'MIDDLE: 48 x 8 px','base':'BASE: 48 x 8 px'}[name],fill='white')
draw.text((12,158),'8px tread bands are paired into editable 16px metatiles.',fill='white');canvas.save(O/'Stairs-native-bands.png')
notes=f'''# WesleyFG Unova / Nuvema implementation

Nuvema Town is rebuilt as a 40 x 40 editable map using `gTileset_UnovaGeneral_Primary` and `gTileset_UnovaNuvema_Secondary`. Open `Unova_NuvemaTown` after reopening the project in Porymap. The Prefabs tab has {r['porymap_prefabs']} Unova assemblies and sections, including separate building roof, wall, eave and entrance rows and stair top/middle/base pieces.

## Source artwork and native scale

Artwork: WesleyFG. The three provided original building, nature and vehicle PNG files are retained unchanged under `graphics/unova_wesley/source/`. The additional user-provided `nuvema_town_bw_by_wesleyfg_d3r861t.png` supplies the exact forest and coastline / boardwalk / ocean crops and composition reference. The map is rebuilt from metatiles, not flattened into a full-map image.

No source art was resized or smoothed. Native blue-house art is 70 x 87 pixels, padded to 5 x 6 metatiles; the lab is 142 x 110 pixels, padded to 10 x 7. The ruler measures 16 x 16 map rows, including partial edges. Stair tread top/middle/base bands are each 48 x 8 pixels. Side panels retain their native 16 x 48 pixels. Paired tread bands produce TopMiddle, MiddleMiddle and MiddleBase 16-pixel-high editor pieces; the middle can repeat.

## Capacity and palettes

| Resource | Primary used / free | Secondary used / free |
| --- | --- | --- |
| 8 x 8 graphics patterns | {r['primary_graphics_tiles']} / {r['primary_graphics_free']} | {r['secondary_graphics_tiles']} / {r['secondary_graphics_free']} |
| 16 x 16 metatiles | {r['primary_metatiles']} / {r['primary_metatiles_free']} | {r['secondary_metatiles']} / {r['secondary_metatiles_free']} |

Both banks have 512 slots and padded files. Graphics usage includes the primary blank tile and 16 reserved animated water tiles; deduplication includes flipped patterns. Thirteen material palettes use transparent index zero and at most 15 opaque RGB5 colors each. Grass, trees, paths, earth, ocean, stone, blue roofs, orange roofs, wood/windows, metal, boardwalk, hedges/flowers and white fence/sign materials are separated. There is no whole-sheet global quantization. See `report.json` for exact crops, dimensions, palettes and counts.

Shared assets include 47 organic path states, reusable forest interior/edge/partial/cluster assemblies, earth/coast pieces, rocks, flowers, fences, signs and stairs. Four ocean frames animate 16 private primary tile slots at indices 384..399, switching every 16 ticks.

## Map and event changes

Changed Nuvema files: `data/maps/Unova_NuvemaTown/map.json`, its existing layout entry in `data/layouts/layouts.json`, and map / border blocks under `data/layouts/AMap_3_0_Nuvema_Town_Layout/`. Both new tilesets are registered in the normal graphics, metatile, header and label includes. The editor prefab file is `data/tilesets/unova_wesley_prefabs.json`, configured in `porymap.project.cfg`.

All {len(json.loads((P/'data/maps/Unova_NuvemaTown/map.json').read_text())['object_events'])} existing NPC identities, flags, scripts and movement types are preserved. Positions were adjusted to reachable path cells; exact original/new coordinates are recorded in `report.json`. Nuvema travel arrival is (19,23). The original exterior has zero active door warps; pending donor records remain inactive. Doors are passable entrance tiles, but interior transitions still need wiring.

Route 1's road at x22..24 aligns with Nuvema x25..27 using reciprocal offsets +3 / -3. Route 1's original terrain and tilesets are retained. A local runtime translation adapts each map's seven-row connection strip to its own graphics; this strip is a palette-compatible approximation. Other map connections are unchanged. A Nuvema-only border hook extends forest on land edges and ocean below the waterfront.

## Verification

Normal game build: PASS. ROM uses {rom_used:,} of 33,554,432 bytes ({33554432-rom_used:,} bytes remain before padding). New tileset headers, ocean frames, callback and boundary translation tables are present in the linked ROM.

Dedicated validation: PASS ({v['assertions']} assertions). Checks include file sizes and indices, palettes, collision / behaviors, editor prefabs, water frame sizes, event preservation and reciprocal road alignment. {v['reachable_ground_tiles']} ground tiles are reachable from the travel arrival, including all four door cells, northern exit and waterfront. Before/after and atlas previews are rendered from the actual GBA files.

Porymap native UI and a walking playthrough have not been performed in this session. The normal headless test runner passed its targeted LoadSheetGraphicsInfo object-graphics regression (1/1); the full battle suite was not run. Linked graphics, metatiles, attributes, palettes and animation frames were also verified byte-for-byte against the ROM.

## Limits and future assets

GBA conversion reduces colors locally to RGB5 / 15 opaque colors per palette; native pixel geometry stays intact. The supplied ocean is a still texture, so its animation consists of subtle native-pixel scrolling phases. Boundary graphics between the new Nuvema and old BWA Route 1 are approximate. These are explicit engine adaptations, not a resolution reduction.

Eight native transparent vehicle crops are prepared in `graphics/unova_wesley/vehicles/`: three boats and two cargo ship orientations for Castelia, truck and loader for Driftveil, aircraft for Mistralton. They are source preparations for later object-sprite conversion, not active sprites or wasted Nuvema metatiles. No other city's tileset was created.

## Rebuilding the assets

Run in order: `rebuild_unova_wesley.py`, `integrate_unova_wesley.py`, `prepare_unova_editor_and_connections.py`, `validate_unova_wesley.py`, then the normal game build. Scripts are under `tools/la_world/`. Original files used for the before preview are retained in `.la_work/unova_wesley/original/`.
'''
(D/'README.md').write_text(notes)
(P/'graphics/unova_wesley/source/CREDITS.md').write_text('Original Unova artwork by WesleyFG. User-provided original PNG downloads are retained unchanged. Building, nature and vehicle sheets plus the supplied Nuvema town reference are used for derived GBA assets. Preserve this attribution.\n')
export=Path('/mnt/c/Users/aadair/Downloads/Legends-Awakening-Reborn/Unova-Wesley-Nuvema');export.mkdir(parents=True,exist_ok=True)
for name in ['Nuvema-before.png','Nuvema-after.png','Nuvema-before-after.png','Unova-primary-metatiles.png','Unova-Nuvema-metatiles.png','Stairs-native-bands.png']:shutil.copy2(O/name,export/name)
for name in ['README.md','report.json','validation.json']:shutil.copy2(D/name,export/name)
rom=export/'Legends-Awakening-Reborn-Unova-Wesley-Nuvema.gba';shutil.copy2(P/'pokeemerald.gba',rom)
(export/'ROM-SHA256.txt').write_text(hashlib.sha256(rom.read_bytes()).hexdigest()+'  '+rom.name+'\n')
print('Exported ROM, previews, stair diagram and implementation report to '+str(export))

