# Requested feature upgrade pass

User choices: Sword & Shield summary (rather than BW summary), PokéRide included, theme-compatible UI recolored to teal/green where practical; otherwise retain original styling. Preserve custom story scripts, six-member legal competitive trainer teams, badge caps, expanded bag categories, scientist Tera changes and 60-box collection mode. Restore playable Hyper Brendan/May visuals without changing chosen names or story identities.

Requested review/integration queue: stat editor; main-menu mugshot UI; custom starter briefcase UI; field mugshots; BW battle UI; SwSh summary, party, PC, bag and message box; dynamic scaling; preferred follower; multiuse candies/EV items; battle DNS; upgradable rod; repeat cutscene skip; dynamic palettes; seasons if feasible; dynamic move descriptions; Ditto faces; encounter text; mid-battle evolution; connected multiregion map; decapitalization; quest icons; color variants; PokéRide.

Sources are the user-provided feature links; locally inspected donor branches live under .la_work/feature-review. Do not blindly merge old branch saves or vanilla story files. Record exact adopted commits and compatibility decisions as work proceeds. This file records remaining work, not a claim that the listed features are already implemented.

## First integration milestone

Implemented and built:
- Playable Hyper roster Brendan/May walking sheets; native Brendan/May action palettes, action sheets and battle pictures restored. Story names remain chosen by the player.
- Sword & Shield summary adapted from montmoguri/pokeemerald-expansion `swsh_summary_screen`, commit b1e4c0d9. Credits to Monty and contributors documented in that project; original source attribution remains in the imported files. Teal accent palette, visible Tera, mint nature, IV/EV and existing move relearning support. Contest pages disabled. Native animation and boxed storage adapters retained.
- Party-relative ordinary trainer scaling adapted from GraionDilach/spinarakgreen `dynamic-scaling-on-113`, commit 7838db7a: raise the authored baseline to the highest eligible player party level, bounded by the badge cap. Regenerate legal species and moves at the resulting level; include party level in cache invalidation. Authored gym teams and protected scripted fights remain on their own levels. Wild badge progression remains independent.

Validation: 28 protagonist/summary checks including the final normal and compact PC boxes; 17 scaling boundary/cache checks; 17,963 full competitive roster checks; 446 Start menu return checks. Reports include the exact tested ROM hash. Native emulator tests use disposable saves.

Not yet implemented: PokéRide and all other entries in the requested queue. Donor checkouts are review material, not completed integrations. In particular, SwSh party/bag/storage/message UI is not enabled merely because the SwSh summary is enabled. Only the first milestone above is ready for playtesting.

Compatibility constraints: EWRAM uses 261,320/262,144 bytes and ROM 32,637,696/33,554,432 bytes after this milestone. Further features require a memory budget, especially ride state, palette effects and replacement storage UI. Do not change SaveBlock layouts or bypass compact storage to fit donor code.
