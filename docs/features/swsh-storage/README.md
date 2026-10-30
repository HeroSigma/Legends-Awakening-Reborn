# Sword & Shield storage interface

Ports Montblanc / montmoguri's swsh_storage_system at abf0ef3494878e0e06d5306933bd3940dfe564b4. Source: https://github.com/montmoguri/pokeemerald-expansion/wiki/Sword-%26-Shield-Storage-System . Credits also include Zatsu (alpha blend) and hedara (info-panel offsets); shared SwSh assets retain existing credits.

The party strip, box grid, Start information panel, item workflows, summary access and type wallpapers use teal accents matching our summary and party menus. Existing PC entry points and boxed form/sprite updates dispatch to the new interface.

## 14/60-box compatibility

The existing storage backend and save format remain authoritative. All navigation limits, box scans and party sentinels use GetStorageBoxCount(). Direct donor box-array accesses use GetBoxedMonPtr. Normal mode keeps 14 boxes; collection mode exposes 60 boxes/1800 slots. The fixed 15-box chooser grid is disabled; the scrolling chooser handles all boxes. No save-format or map changes. Remote party-menu PC access remains disabled.

The integration test now stores temporary Pokemon in unused IWRAM below the stack and outside its trampoline, rather than overlapping EWRAM gWindows. This avoids a preexisting test scratch-buffer collision exposed by the changed allocation layout.

## Validation

2678 native checks on the pinned ROM hash: 36 new storage checks in both profiles (final-box transfer across the wrap, summary, withdrawal, no duplicates, save/load, held-item transfer); 2196 production storage/profile/save checks including all 1800 slots, continued saves and conversion gates; 446 Start-menu lifecycle checks. Tests use isolated saves. Reports and screenshots are pinned here.

Build: EWRAM 261376/262144 bytes, IWRAM 28140/32768 bytes, ROM 32695736/33554432 bytes. Release updates the permanent ROM and preserves its paired save.
