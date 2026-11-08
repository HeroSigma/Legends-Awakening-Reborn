# Optional legacy feature switch

Default: LA_FREE_SPACE=1 in include/config/free_space.h. Build override: make BUILD_NAME=emerald-sinnoh-assets LA_FREE_SPACE=1 -j8.
Use a separate BUILD_NAME or clean/rebuild when changing command-line flags, because Make does not track flag changes. LA_FREE_SPACE=0 restores original feature sources. The complete multi-region build with everything enabled currently exceeds 32 MiB; restoring features does not expand ROM capacity.

Disabled: Trainer Hill; Tower, Factory, Pike, Pyramid, Arena, Dome and Palace engines; contests, link contests, paintings and contest AI; roulette/slots; Dodrio Berry Picking/Pokemon Jump; GameCube multiboot payload. 56 facility map scripts use disabled-feature messages. Map IDs, save structures and shared facility/Pokemon data are retained for compatibility and possible PWT reuse. Shared graphics and music are not indiscriminately deleted.

GBA Cable Club, Union Room, trading and link battles remain compiled; their source files are unchanged. Disabled asynchronous specials resume the caller on a task tick. Disabled minigames return through the provided exit callback.

Checks: trimmed build passes; all 20 restored feature modules and event scripts/Colosseum payload compile with LA_FREE_SPACE=0; linked Kanto/Johto/BWA validators pass; GameCube payload symbols are absent. Kanto checks now compare linked palettes with donor colors and decompress linked tile graphics byte-for-byte. Live trading, link battling and Kanto rendering require play testing.

Used ROM: 32,937,040 bytes. Free: 617,392 bytes (602.9 KiB). Final ROM padded to 32 MiB. Net reduction versus the corrected-palette overflowing build: 623,856 bytes. Audio remains around 10 MiB and is the next audit target; no tracks or samples removed in this pass.

## Second cleanup pass

Separate Mega cry samples are excluded in free-space mode using the engine's existing base-cry/pitch fallback. Mega forms, stats, abilities and battle mechanics remain. Slowbro and Rayquaza now also honor this existing configuration. Setting LA_FREE_SPACE=0 restores separate Mega samples.

Audio samples, voice groups and key-split tables use separate linker sections in free-space mode, so truly unreferenced data can be discarded. All 610 song table entries keep their IDs and pointers; no music tracks were deleted. 45 unreferenced disabled-feature graphics are excluded. Additional ContestHall and BattleTent scripts are guarded, and Battle Tent entry functions are disabled with the other Frontier facilities.

Latest used space: 31,564,900 bytes. Free: 1,989,532 bytes (1.90 MiB). This pass saved 1,372,140 bytes versus the first free-space ROM. 1221 retained sample payloads match the previous ROM byte-for-byte. Both restored audio/graphics/species branches and restored Battle Tent/event scripts compile. Kanto/Johto/BWA linked checks pass. Actual sound playback and link play remain for runtime testing.

## English fonts and facility UI cleanup

Free-space mode removes all six Japanese font graphics and their width tables. English font styles remain. Japanese glyph branches are excluded; the old Japanese-only bold renderer falls back to the normal English font. Frontier Pass entry points return to their callers/field instead of loading the disabled facility interface. Additional unused facility graphics are guarded. Original branches compile with LA_FREE_SPACE=0.

Champion Island is reserved for PWT: its maps, buildings, geometry, tilesets and travel links remain. Shared Frontier trainer/Pokemon data are retained for possible PWT use.

Used ROM: 31,392,188 bytes; free: 2,162,244 bytes; this pass saved 172,712 bytes. Kanto, Johto, BWA and audio validators pass. All nine English glyph banks remain; Japanese glyph symbols are absent. Runtime menu/font checks remain for play testing.

## Bard cleanup

Free-space mode excludes Bard word/pitch tables and replaces the 51 phoneme song slots with silent song headers. Song IDs remain stable. Easy Chat, old-man save data, ordinary music, cries and link functions remain. The Bard caller uses its existing empty-word skip path; no lyrics play. LA_FREE_SPACE=0 restores original singing and phoneme slots.

Used ROM: 31,112,904 bytes; free: 2,441,528 bytes. Saved 279,284 bytes versus English-Free-Space-3. The 2,134,876-byte candidate Galar estimate leaves 306,652 bytes. All regional and audio checks pass, with 1,170 retained sample payloads byte-exact and all 610 song IDs stable. Restored Bard and audio sources compile. Runtime Bard dialogue remains unverified.
