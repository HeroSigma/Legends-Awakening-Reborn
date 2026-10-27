# 60-box collection storage

Integrated in Reborn on 2026-10-27. The existing normal save format remains supported. No new game is required for an existing normal-mode battery save.

## Player controls

Open **Options during gameplay**, highlight **PC BOXES**, and press **A**. Read both warnings. The second confirmation clears all boxed Pokemon and switches between normal 14-box storage and 60-box collection storage. Party Pokemon, story progress, box names/wallpapers and active fusion partners remain. Save the game to commit the mode change.

The title-screen Options menu cannot change storage modes. Boxed fusion bodies must be unfused before changing modes, preventing orphaned fusion partners. Normal PC navigation reaches all 60 boxes; the Jump popup offers ten-box jumps with L/R.

Use the in-game **Continue** feature after updating the ROM. Emulator save states created by an older build contain an incompatible RAM layout and must not be loaded.

## Collection-mode data

1,800 slots use 31 bytes each: 55,800 record bytes, plus names, wallpapers, header and four full native fusion records. Nicknames become species names; original trainer identity/met history and cosmetic personality patterns are simplified. Foreign ownership/language distinctions are retained with normalized identities. Regenerated names use Latin rendering to avoid Japanese five-character truncation.

Retained: species/forms, experience, moves, PP bonuses, held item, Tera type, exact EVs/IVs, ability slot, original/minted nature, gender, shiny status, friendship/hatch cycles, hyper training, egg flags, ball, evolution tracker, Wurmple branch, PID modulo 100 for rare evolution outcomes, Beauty for Feebas, Pokerus, Dynamax level, Gigantamax factor, shadow/fateful flags, Champion ribbon and markings. PC storage heals HP/status/PP. Other Contest statistics/ribbons and temporary-form timers are not stored.

Native PC accessors, summary-screen pointer/cache lifetimes, scans, debug tools, lotteries, Pokenav and healing now use the selected storage mode. Species/egg/move/item queries read compact records directly; healing only processes the decoded cache because stored compact records are already healed. The populated 1,800-slot scan is measured in the integration report.

## Save layout

Normal mode serializes the original 14-box/14-sector layout, retaining native legacy activities and the existing save ABI. Collection mode streams retained story data and compact PC data across two 16-sector banks in standard 128 KiB flash. The paired emulator RTC trailer is untouched by ROM packaging.

Collection banks include sector checksums/CRC, unique logical IDs, consistent generations, payload/header CRC and an ABI fingerprint. Saves alternate complete banks. Profile transitions first protect a completed checkpoint before crossing the 14/16-sector boundaries. Incremental/link and special-sector save paths are guarded to prevent native Hall of Fame/Trainer Hill/recorded-battle writes into collection data.

The expanded bank currently uses 64,968 of 65,152 payload bytes: **184 bytes spare**. Regenerate the ABI audit and generated span table after save-layout changes. A change to the compact bit layout requires an explicit save-format version migration.

## Retired in collection mode

Battle Frontier/Battle Tents, Contests, Trainer Hill, Secret Bases/decorating, legacy record-mixing/Union Room chat/minigame records, legacy mystery/e-Reader buffers, random TV/news and selected legacy records are omitted or blocked. Historical Hall of Fame teams are not stored in collection mode; League progression and ceremony remain. Maps are retained for repurposing. Normal mode retains its native records/activities; switching back cannot reconstruct records discarded by collection mode.

Exact omissions are in `layout_audit.json`; entry/special gates are in `retired_feature_gates.json`. Gate generation is reusable:

```sh
python3 tools/la_world/storage/generate_feature_gates.py --check
```

## Verification

- Host codec tests: 30,000 randomized round trips with address/undefined-behavior sanitizers, exact EV edge cases and fast-read comparisons.
- Native ARM adapter/bank tests: all 1,800 slots, live cache edits, invalid-record rejection, atomic flush, relocation in both directions, normal-record retention, confirmed/cancelled mode transitions, foreign-name rendering and markings.
- Production integration: real Options confirmations/cancellation/title restriction; all 1,800 slots; Box 60 rendering/wrap; save/load and soft-reset Continue; deliberately corrupted newest sector and recovery; independent host decoding of native flash; both profile transitions; legacy save reload; eggs/hatch progress; activity gates; boxed-fusion protection.
- Full opening chapter for both genders and all three starters in both storage modes, including save/Continue.
- Existing battery copied read-only into an isolated emulator for compatibility; original file unchanged.
- NPC/art and Timeless Woods regressions; normal build registered-tileset checks.

Test scripts never program the player's real battery file. The existing-save test reads it and programs an isolated emulator copy only. The playable release and its battery are guarded during component tests.

Run tests sequentially when possible:

```sh
make -j8
python3 tools/la_world/storage/validate.py
python3 tools/la_world/storage/test_pc_integration.py
python3 tools/la_world/storage/test_existing_save.py
python3 tools/la_world/importers/amap/hns_runtime/test_littleroot_red_arc.py
LA_TEST_COLLECTION=1 python3 tools/la_world/importers/amap/hns_runtime/test_littleroot_red_arc.py
python3 tools/la_world/importers/amap/hns_runtime/test_npc_roster.py
python3 tools/la_world/importers/amap/hns_runtime/test_timeless_conspiracy.py
```

Evidence: `integration/validation.json`, `integration/existing_save_compatibility.json`, `collection_story/runtime_validation.json`, `validation.json`, `layout_audit.json`, and the existing story/NPC validation reports. Final ROM packaging is recorded in `release.json`.
