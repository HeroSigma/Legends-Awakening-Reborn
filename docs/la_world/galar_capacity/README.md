# Galar ROM capacity audit

Current 32 MiB ROM uses 31,564,900 bytes, leaving 1,989,532 bytes (1.897 MiB). Nine Galar maps and seven tileset banks are already present and subtracted from the estimates.

| Scope | Total maps | New maps | Additional bytes | Additional MiB | More space needed with 256 KiB reserve |
|---|---:|---:|---:|---:|---:|
| Visually selected subset | 56 | 47 | 511,956 | 0.488 | None |
| All non-excluded candidates | 484 | 475 | 2,134,876 | 2.036 | 407,488 bytes / 0.389 MiB |
| Entire donor including legacy and superseded maps | 701 | 692 | 2,662,378 | 2.539 | 934,990 bytes / 0.892 MiB |

## Candidate cost

Layouts and borders: 1,160,648 bytes. Shared graphics, metatiles, attributes and palettes: 884,324 bytes across 56 additional tileset banks. Map declarations, inspection support and travel records: approximately 89,904 bytes, including 1,474 additional warp records and 176 additional connections.

## Method and limits

Measured every exported layout and compressed each tile bank using the project's gbagfx converter. Counted shared banks once; existing imported banks were reused. Palette allowance is 13 native palette slots per bank. Metadata allowance is 160 bytes per new map plus 8 bytes per warp and 12 per connection. No geometry deduplication assumed. A 256 KiB reserve covers alignment, travel repairs and modest additional support. These are asset-and-travel estimates, not a linked import build.

The 484 count is a capacity upper bound for non-excluded candidates, not 484 verified Galar maps. The review has 428 maps awaiting manual review, 197 excluded legacy maps and 20 superseded maps. Complete travel still requires destination remapping, dynamic warp handling and validation of malformed/inherited links. Merely allocating their records does not prove an explorable region.

Excluded from budget: donor story scripts, trainer/NPC graphics, custom music, encounters and new animations. These need a separate budget if wanted.

Recommendation: free at least another 0.5 MiB for the candidate asset-and-travel import; prefer 1 MiB additional headroom while selecting and repairing the full region. No live map or import selections were changed by this audit.
