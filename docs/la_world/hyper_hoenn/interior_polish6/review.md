# Hoenn interior polish batch 6: gyms and Battle Frontier

Reviewed 55 rooms: 10 Hoenn gym floors and 45 Battle Frontier interiors. Seven contact sheets were reviewed, with zero invalid used palette references. 55 rooms use Hyper assets: 39 exact donor blockdata and 16 reconciled. Expansion-original rooms: none. Frontier outdoor plazas and Kanto gyms are excluded.

No new map defects were established and no maps, assets, scripts or gameplay were edited in this batch. Use the Batch 5 ROM. The renderer now supports native JASC palettes; batch 6 is reusable.

Static audit checked 170 warp arrivals and 186 active actors. It emitted 15 access warnings, retained in the raw audit: 14 actors in four Frontier rooms without ordinary warp entries, and Wattson behind puzzle-controlled electric barriers. These are triaged as RUNTIME_STATE_REQUIRED, not automatically cleared as tested. Source hooks and scene ownership remain native; facility entry, generated rooms and puzzle completion require in-game validation.

Native-cell comparison covers 12,935 cells across all 55 rooms. Forty-nine match baseline collision, elevation and behavior exactly. Fortree, Mossdeep and Sootopolis gym floors retain native collision and behavior with existing Hyper elevation adjustments. Lavaridge floors also have prior steam-hole/warp adapters (13 behavior differences and one collision difference); these remain explicitly queued for runtime validation. The existing Canary 5 importer documents these adapters. No historical geometry was reverted.

Petalburg is an intentional 9-by-112 stacked-room layout; inspect its individual rendered PNG rather than the reduced overview. Battle Pyramid Floor is a runtime-generated template, not a finished static room. All native challenge/save/reward systems remain authoritative.

Review does not prove gym puzzles or full Frontier challenges. Complete the runtime checklist before marking mechanics validated. Build/linked asset checks are in validation.md.
