# Four-region map cleanup

Requested 2026-11-15: retain Kanto, Johto, Hoenn, and Sinnoh and reclaim ROM space
from other regions. Galar had already been removed; this pass retires Unova,
the remaining active extra region. No active Alola, Kalos, or Paldea map groups
were found. Shared system/link maps and assets needed by the retained regions
remain.

## Changes

- Strip 33 Unova maps of their events, connections, and scripts. Preserve their
  group/number slots as compatibility entries pointing to Littleroot's layout.
- Replace 31 exclusive layout payloads with assembler aliases. The mapjson
  generator's new `alias_of` field emits no duplicate blockdata or tileset data;
  existing layout constants and table indices remain unchanged.
- Remove 37 Unova-only tilesets and 148 private graphics/metatile/palette
  declarations from active source headers. Source artwork stays on disk for
  recovery and does not occupy ROM when no longer included.
- Remove the Nuvema/Accumula full-sheet streaming payloads and 36 Unova wild
  encounter tables. Keep shared renderer hooks as no-ops.
- Remove the Unova developer travel choices and test-new-game overrides.
- Redirect old saved locations and warp destinations in the five retired map
  groups to Littleroot (10, 10), without resetting party, inventory, story flags,
  or battery saves. This migration still needs an interactive old-save check.

Removed map/layout definitions, scripts, tileset declarations, and streaming
source are preserved as noncompiled archival records beside this file. They are
not included by any build source. Existing external archives are untouched.

## Validation

`make -j2` and `git diff --check` pass. `validation.json` records:

- 2,657 retained map definitions unchanged; all map/layout IDs unchanged.
- 2,619 retained layout definitions checked; linked border/blockdata compared.
- 1,234 retained linked graphics/palette/metatile declarations byte-exact.
- Retired graphics and full-sheet payload symbols absent from the linked ROM.
- Retired-map classification checked for all 256 signed map-group values.
- Six-second mGBA offscreen process smoke using an isolated temporary ROM/save.
  This is not visual map or gameplay testing.

Used ROM fell from 33,544,192 to 32,746,452 bytes, recovering 797,740 bytes
(779.04 KiB). Available ROM is now 807,980 bytes (789.04 KiB); the final .gba
still pads to 32 MiB. Static EWRAM usage fell by 4,248 bytes to 257,460 bytes.
These measurements include the existing uncommitted Lucario work in the tested
working tree and are not clean-main build measurements.

To repeat linked validation, retain the ELF and ROM from before pruning and run:

```sh
python3 tools/la_world/validate_four_region_pruning.py \
  --before-elf /path/to/before.elf --before-rom /path/to/before.gba
```

The test package replaces only `Legend Test.gba`. The permanent main ROM and all
battery saves/save states must remain unchanged.
