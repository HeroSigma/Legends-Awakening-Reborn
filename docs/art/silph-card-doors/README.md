# Silph Card Key door graphics

The imported DS-style Silph tileset had incomplete gate definitions: horizontal gate tops retained floor, and vertical gate bottoms were plain floor with unrelated behavior attributes. The scripts still applied blocking collision, leaving visible gaps and hidden blocking cells.

Repair metatiles 0x3B0, 0x3B1, 0x3C4 and 0x3C5 by assembling existing metal-panel tiles. Horizontal tops use continuous panel texture; vertical bottoms continue their middle sections. Set the four definitions to normal two-layer gate attributes. Keep graphics, palette, dimensions and all other metatiles unchanged. Update the matching legacy BVD entries and record the project override in tileset.json; retain the raw donor attributes as reference.

No map coordinates, Card Key rules or saved door flags change. The native audit captures all twenty doors closed and open. Security tests check every scripted doorway cell on first entry and after unlocking/re-entry, including the always-open ninth-floor bed doors. Existing key/reward/save checks, normal Rocket approaches and the full rescue/Flannery sequence are retained.

See comparison.png and before-all-doors.png / after-all-doors.png for native-emulator captures.

## Stair compatibility correction

The donor uses 0x3B0/0x3B1/0x3C4/0x3C5 for staircase artwork and directional
stair behavior as well. Restore those original definitions. The four repaired
gate sections now occupy dedicated unused slots 0x3AB/0x3AC/0x3B2/0x3B3 and use
METATILE_LA_SilphCo_* labels only in the card-door scripts. These slots are absent
from every map and border using this secondary tileset. Keep both the runtime
three-layer definitions and the editor BVD synchronized.

The native stair test walks all twenty up/down connections, leaves each arrival
landing, and checks return travel after save/load (85 checks). The 332 security
and reward checks also pass. Player saves are never loaded in these tests.
