from pathlib import Path
import shutil,json
P=Path('/home/allan/projects/Legends-Awakening-Reborn');f=P/'Makefile';backup=P/'.la_work/triple_layer/original/Makefile'
if not backup.exists():shutil.copy2(f,backup)
s=f.read_text();block='''
# Reject stale two-layer outputs from legacy importers before compiling tilesets.
.PHONY: check-metatile-format
check-metatile-format:
	@python3 tools/la_world/check_triple_layer_format.py

$(C_BUILDDIR)/tilesets.o: | check-metatile-format
'''
if '.PHONY: check-metatile-format' not in s:f.write_text(s.rstrip()+'\n'+block)
D=P/'docs/la_world/triple_layer';(D/'README.md').write_text('''# Triple-layer metatiles

All 446 registered metatile files (159,434 records) use 12 u16 entries: bottom BG3, middle BG2, top BG1. Existing IDs, tile references, flip bits, palette choices, attributes, collisions, map layouts and source pixels were retained. Existing two-layer artwork now occupies the same physical backgrounds with an explicit unused third layer; this does not separate grass already baked into an image.

BWA Nuvema remains the active map, as requested. Source Unova sheets are retained for future work.

Porymap: reload the project. The Tileset Editor now exposes all three layers. enable_triple_layer_metatiles=1 is set, and NUM_TILES_PER_METATILE=12 enables automatic detection in supported Porymap versions.

Compatibility fixes cover eight-entry door animation frames, shop menu layer compaction, and Secret Base decoration selection sprites/palettes. Converted stock NORMAL tiles retain the original 0x3014 bottom filler. Legacy donor attributes with undefined layer types retain their original no-draw behavior; this migration does not change those attributes.

New triple-layer artwork should leave an empty layer where a shop UI opens over it: the shop menu consumes one of the map backgrounds. Existing converted two-layer tiles already satisfy this (including stock filler handling).

Validation: 177,006 preservation/placement assertions, native ASan/UBSan tests of the actual rendering/door/shop/decoration code, 844 linked metatile/attribute array comparisons and a successful normal ROM build. No emulator playtest was performed. ROM uses 32,229,076 bytes of the 33,554,432-byte limit; EWRAM/IWRAM usage unchanged.

Backups: .la_work/triple_layer/original. conversion.json lists every migrated file and original/converted hashes. protected_files.json verifies unchanged map, attribute, artwork and palette files. validation.json contains the verification results.

Older import scripts that still emit eight-entry metatiles must be updated before use. The build now rejects stale two-layer outputs instead of silently compiling corrupted maps. Do not rerun the one-time converter on already migrated data.

Reference: https://github.com/pret/pokeemerald/wiki/Triple-layer-metatiles
Porymap: https://huderlem.github.io/porymap/manual/settings-and-options.html
''');print('Build format guard and migration documentation added.')
