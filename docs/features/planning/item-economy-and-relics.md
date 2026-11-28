# Item economy, training costs and special relics ? proposal

Date: 2026-11-28

Status: Implementation approved in parts. Part one implements Cap-funded IV/EV drafts and introductory Cap access. Parts two onward remain pending; their locations, quests and relic restrictions are still proposals.

## Part one delivered

- After Brawly, open the Stats page of the summary and press START. All adjustments stay in a draft; SELECT opens a payment review. B or L/R with a draft offers Apply / Discard / Keep editing. START still previews 31 All; use L/R in the main editor to change party members.
- One Gold Bottle Cap pays for any changed IV configuration on one Pokemon, including deliberate zero IVs. One regular Bottle Cap pays for any EV changes on that Pokemon. A combined batch costs one of each. Reverted values, previews and discards cost nothing. Missing Caps or a changed target cannot partially apply or charge.
- The scientist offers a one-time optional kit of one Gold and one regular Cap after Brawly. Declining retains eligibility. Both items must fit and be granted before the claim flag is saved (`FLAG_LA_TRAINING_CAP_KIT`, reserved 0x906).
- Regular Caps enter Legends Store after Brawly (base 5,000; normal 6,250; sale 5,000). Gold Caps enter after Flannery (base 12,000; normal 15,000; sale 12,000). Both are in the Bag's Training category. XL EXP Candy still unlocks after Winona.
- Nature and ability changes are staged with the same draft, but retain their existing free pricing in this part. Mint/Ability item charges, treasure exchanges, relic exclusions, Plate placements and the Devon Memory vendor are not implemented here.
- The review reuses the existing stats window buffer, and party sprite graphics are allocated once per editor visit. This avoids the GBA heap exhaustion exposed by repeated party switching.

The design below records the full plan; only the delivered scope above is current gameplay.

## Gimmick stock milestones delivered

User refinement: keep ordinary Mega Stones and Z-Crystals in the Legends Store.
Ordinary Z-Crystals (including non-Legendary signature crystals) unlock after
Brawly's Knuckle Badge. Ordinary Mega Stones unlock after Wattson's Dynamo Badge.
The existing story devices and exploration/quest rewards retain their own gates.

The Store excludes ten Legendary/Mythical Mega Stones and six corresponding
Z-Crystals, including Tapunium Z. Previously owned items remain usable. Both
catalog visibility and direct purchase validation use the same exclusion.

Wattson's initial badge battle uses Mega Manectric. Before the Dynamo Badge,
losses/retries keep the Mega introduction; after the badge, Gym gimmicks rotate
as before. This does not force an early Mega introduction onto other leaders.

The remaining ordinary-shop relic exclusions are now implemented through the
shared `Item_IsQuestRelic` policy. It covers the primal Orbs, six Sinnoh dragon
relics, Soul Dew, Rusted weapons, Ogerpon Masks, Urshifu Scrolls, Legendary form
keys/tickets (including Meteorite), all four Drives, all 17 Plates and all 17
Memories, as well as the previously excluded Legendary Mega/Z items.

Ordinary Marts filter their catalogs and revalidate purchases; Legends Store
uses the same policy for visibility, prices and direct purchases. Existing
ownership, scripted gifts, item use and story/encounter flags remain independent.
Arceus Plate placements, the dedicated Devon Memory shop and new treasure quests
remain pending as separate parts.

## 1. Requested direction

1. Replace the proposed cash fees for IV/EV editing with Bottle Cap costs.
2. Spend one Gold Bottle Cap to change a Pokémon's IVs, with 31 as the maximum.
3. Spend one regular Bottle Cap for changes to a Pokémon's EVs.
4. Give otherwise underused treasures meaningful research, quest and encounter roles.
5. Remove Legendary/Mythical-associated items from ordinary shops, including Legends Store. Explicitly include the Red/Blue Orbs and the Adamant, Lustrous and Griseous item families.
6. Scatter Arceus's Plates across different areas.
7. Sell Silvally Memories only in Devon's basement, after the Type: Null story unlock.
8. Produce and commit this plan first; do not implement these changes yet.

The original money example is superseded by the Bottle Cap proposal. Do not charge both Caps and that money fee unless separately approved.

## 2. Training transaction design

### Recommended exact charging rules

| Confirmed change to one Pokémon | Cost |
|---|---|
| Any number of IV fields, including 31 All | 1 Gold Bottle Cap |
| Any number of EV fields | 1 Bottle Cap |
| Both IVs and EVs in the same confirmed batch | 1 Gold Bottle Cap + 1 Bottle Cap |
| Preview, cancel, or return every value to its original value | Nothing |
| Insufficient required Caps | No charge and no changes |

Editing HP, Attack and Speed EVs is **one EV batch**, not three payments. Editing both the IVs and EVs of those stats costs one of each Cap. Each Pokémon has its own transaction; cycling through a whole party must not share one payment.

Recommended interpretation of ?change IVs (max 31)?: keep the existing 0?31 range, including deliberate 0 Attack/Speed builds. A Gold Cap pays for the entire confirmed IV configuration; it is not restricted to raising every stat to 31. Hidden Power's IV-pattern tool must use the same charge. This is a proposed game-specific training service, not a claim about the items' original-game behavior.

Keep the existing maximums: 252 per EV stat and 510 total; 252/252/6 remains valid. Resetting EVs to zero counts as an EV change. Preserve Pokémon identity, ability/nature unless explicitly edited, Tera type, HP damage, status, fainted state and storage position.

### Important implementation finding

The current editor writes edits immediately through `ApplyRightPanelStatChange`, `ApplyHiddenPowerBits` and `StatEditor_Recalculate` in `src/stat_editor.c`; boxed edits use `StorageWriteMon`. Adding a Cap deduction to each button press would overcharge and would not provide a reliable cancellation path.

Implementation should therefore:

1. Copy the selected Pokémon's original data into a stable editing buffer. Keep a separate draft for preview/stat calculations; do not retain a pointer to the compact-PC decode scratch buffer across slot changes.
2. Route all mutation paths through the draft, including individual edits, 31 All, EV reset, Hidden Power patterns and shortcuts.
3. Compare original and final IV/EV values to calculate the two charges. Selecting a value and then reverting it must produce no charge.
4. Add an explicit **Apply changes** confirmation showing the Pokémon, changed fields, required Caps and available quantities.
5. On Pokémon/box cycling or closing with an edited draft, offer Apply / Discard / Keep editing. Never silently write changes when cycling.
6. Before committing, revalidate the target and its unlock, IV/EV limits and all required items. Commit inventory and Pokémon data together; a failed operation must restore both. Use the existing party/compact-storage APIs and retain ordinary manual saving.
7. Apply nothing when a required Cap is missing. Do not consume a Gold Cap first and leave a half-finished transaction when the regular Cap is unavailable.
8. Recalculate stats while preserving existing HP/status behavior, then refresh the summary and Bag counts.

### Cap access and prices ? recommendations needing approval

Currently the Store unlocks regular Caps at Winona and Gold Caps at the final Hoenn Badge. That would leave the Brawly-unlocked paid editor without normal supplies for much of the story.

Recommended replacement:

| Resource | Proposed access | Suggested base price | Normal Legends Store price / sale |
|---|---|---:|---:|
| Bottle Cap | Store after Brawly; repeatable research/battle rewards | ?5,000 | ?6,250 / ?5,000 |
| Gold Bottle Cap | An optional post-Brawly research quest gives one; Store after Flannery; rarer later rewards | ?12,000 | ?15,000 / ?12,000 |

These prices and revised stock gates are suggestions, not approved changes. A full IV+EV transaction would cost one of each item; quest-earned Caps offer an alternative to buying them. Keep a renewable regular-Cap source and a slower renewable Gold-Cap source.

Move both Caps into the Bag's Training category, update their descriptions to explain the editor, and keep unique story relics separate from this consumable currency.

### Related training-item uses ? additional recommendations

- Nature changes: consume the matching Mint, so freely changing nature cannot bypass the Mint economy.
- Switching ordinary ability slots: consume an Ability Capsule. Entering a Hidden Ability: consume an Ability Patch and respect its availability gate. Decide the return-from-Hidden-Ability rule explicitly before implementation.
- Keep the existing Tera scientist/shard costs and grindable Tera Shards. Do not add a free alternate Tera-edit route.
- Keep basic move relearning, the unlocked friendship service and level catch-up as currently designed unless separately changed.
- Heart Scales could become an alternate payment for the existing paid Egg Move tutor. Preserve species compatibility and the current money option; do not charge for ordinary summary move relearning.

## 3. Ordinary-shop exclusion policy

Create a central item-acquisition policy used by both catalog display and purchase validation. Use explicit item IDs/family metadata, not name fragments: **Life Orb, Flame Orb, Toxic Orb and Adrenaline Orb are ordinary battle items**, and Adamant Mint is not Adamant Orb.

The policy should classify items as ordinary stock, training stock, unique relic, exploration-only Plate, Devon-only Memory or story key. Catalog filters, quantity/confirmation screens and direct purchase calls must agree. Audit ordinary Mart inventories and future special vendors so they cannot accidentally reintroduce restricted relics.

### Legendary/Mythical-associated items to exclude from ordinary sales

| Family | Existing items to cover | Proposed acquisition |
|---|---|---|
| Hoenn primal relics | Red Orb, Blue Orb | Separate story/quest relics connected to the allied villains' research and later Groudon/Kyogre investigations |
| Sinnoh dragon relics | Adamant Orb, Lustrous Orb, Griseous Orb; Adamant Crystal, Lustrous Globe, Griseous Core | Paradigm investigations into time, space and the Distortion World; do not collapse the older held items and newer form items into one object |
| Eon relic | Soul Dew | Latias/Latios research quest |
| Legendary/Mythical Mega Stones | Mewtwonite X/Y, Latiasite, Latiosite, Diancite; also existing Zygardite, Heatranite, Darkranite, Zeraorite and Magearnite | Matching species/story research rewards; audit all form-change tables for additional or future stones |
| Legendary/Mythical Z-Crystals | Mewnium Z, Solganium Z, Lunalium Z, Marshadium Z, Ultranecrozium Z | Matching species/research milestones. Keep ordinary type Z-Crystals under their current rules |
| Genesect modules | Douse, Shock, Burn and Chill Drives | Recover and restore research modules through a Genesect/Colress-related chapter |
| Galar relics | Rusted Sword, Rusted Shield | Recovery/restoration quests before the relevant Legendary encounters |
| Ogerpon relics | Wellspring, Hearthflame and Cornerstone Masks | Regional folklore/recovery quest; keep the species' existing form mechanics |
| Kubfu/Urshifu items | Scroll of Darkness, Scroll of Waters | Earned trials, subject to a separately planned Kubfu chapter |
| Existing Legendary/Mythical key items | Gracidea, Reveal Glass, DNA Splicers, Zygarde Cube, Prison Bottle, N-Solarizer, N-Lunarizer, Reins of Unity; relevant tickets/maps | Already excluded by the Key Item rule in Legends Store; keep them protected in every future vendor and route them through their matching quests |
| Arceus items | All 17 existing Plates | Exploration/research placement; never ordinary sales |
| Type: Null/Silvally items | All 17 Memories | Devon basement vendor only, after the permanent Type: Null unlock |

This is a concrete starting manifest, not a claim that auditing future item/form additions is unnecessary. The implementation audit should reconcile every Legendary/Mythical form-change item, held-item association and species-specific Z-Crystal against the policy. Generic items used by many Pokémon, such as ordinary type boosters, are not excluded just because a Legendary can hold them.

Do not delete items or reset flags in existing saves. Previously owned relics can remain; encounter access still follows story, League and quest requirements. Decide case by case whether an early-owned relic satisfies a quest's item requirement; possession alone must not bypass a required investigation.

## 4. Arceus Plate exploration plan

The project contains **17 typed Plates**, not a separate Normal Plate. Normal Arceus does not need an invented replacement item. Keep Plates as reusable held artifacts rather than consuming them at a shrine.

The following are proposed destinations/themes, not implemented or walkability-verified placements. Map IDs, story access, collision, actor capacity and trigger paths must be checked before placing anything.

| Plate | Candidate area | Discovery idea |
|---|---|---|
| Flame | Mt. Chimney | A volcanic research cache following the alliance confrontation |
| Splash | Abandoned Ship | A submerged research compartment after Dive access |
| Zap | Kanto Power Plant | An optional sealed annex; preserve the reactor/Miraidon/Wally sequence |
| Meadow | Timeless Woods | A woodland shrine on the accessible mainland, separate from the natural wormhole |
| Icicle | Shoal Cave | An ice/tide puzzle |
| Fist | Granite Cave | A Dewford-era training/research side quest |
| Toxic | Kanto Pokémon Mansion | A contamination investigation once the area is actually opened by the story |
| Earth | Hoenn desert ruins | A buried chamber reached through an archaeology quest |
| Sky | Sky Pillar | An optional ledge/shrine once legitimate story access exists |
| Mind | Johto Ruins of Alph | An inscription puzzle and Unown research |
| Insect | Petalburg Woods | An ecosystem investigation on a later return visit |
| Stone | Rusturf Tunnel | A geological side chamber, clear of the existing rescue cutscene |
| Spooky | Kanto Pokémon Tower | A memorial/research quest |
| Draco | Meteor Falls | A deeper dragon shrine behind the intended traversal/story gate |
| Dread | Johto Dark Cave | A shadowed chamber with a local investigation |
| Iron | Devon basement | An earned research reward from a metallurgy experiment; never vendor stock |
| Pixie | Johto Ilex Forest | A sanctuary investigation once that chapter is accessible |

Spread discoveries across existing Hoenn, Kanto, Johto and special-area content. Do not require a full Unova region or assume unimplemented regional travel is ready. A final Plate/archeology quest can require the League, the relevant investigations and the recorded discoveries before an Arceus encounter becomes available.

For every placement, record map ID, coordinates, a unique pickup flag, quest prerequisite, acquisition source and a short lore note. Add persistent discovery flags/checklist entries; retaining or equipping a Plate must not erase the discovery record. A rift should never bypass its existing seal simply because the player carries a Plate.

## 5. Devon-only Memories

The current Devon basement connection leads to `MAP_HYPERHOENN_34_10_BASEMENT`. Verify its current player-edited layout before adding a technician/terminal.

1. Plan a Type: Null acquisition/rescue chapter first. Aether research recovered during a Paradigm case would fit; Gladion could guide that chapter when introduced. This is a story suggestion, not an existing implemented event or a new independent villain operation.
2. Set a dedicated permanent Type: Null unlock flag only after successful acquisition, including delivery to storage when the party is full. Do not infer the unlock merely from having seen the species, a temporary party loan, a trade or debug inventory.
3. Put a Memory Technician/vendor in the basement. Before the flag, give research dialogue. After the flag, open the dedicated list.
4. Remove every Memory from Legends Store and all ordinary vendor inventories. Validate the basement source and story flag in the purchase function as well as the menu.
5. Sell the 17 existing typed Memories. No Normal Memory needs to be invented.
6. Proposed fixed price: ?8,000 per Memory, without Legends Store daily category sales. Duplicate purchases may remain available for different builds; maintain a resale price below purchase price.
7. Once unlocked, the shop remains available when Type: Null evolves into Silvally, moves to storage or leaves the active party. Unlocking is a story milestone, not a party-slot requirement.

This chapter needs its own story flag and actor placement plan; this proposal does not allocate a flag or edit the basement map.

## 6. Treasure uses and additional quest ideas

First audit existing uses. Fossils, Honey, Heart Scales, colored shards and Shoal materials may already have mechanics; preserve useful existing exchanges. Nugget-type treasures already have a valid role as money and do not all need to become mandatory keys.

| Treasure family | Proposed role | Implementation approach |
|---|---|---|
| Stardust / Star Piece / Comet Shard | Paradigm astronomy/rift research; later Jirachi or Deoxys leads | Repeatable sample commissions for common materials; a distinct completed investigation/provenance flag gates the rare encounter lead |
| Pearl / Big Pearl / Pearl String | Ocean research and an eventual marine Mythical investigation | NPC commissions and a beacon-restoration chain; League and story checks remain separate from material possession |
| Red / Blue / Yellow / Green Shards | Expanded research-material exchanges or crafting | Preserve existing shard trades; distinguish these ordinary shards from the grindable Tera Shards; no free bypass of Tera treatment costs |
| Tiny / Big / Balm Mushrooms | Forest restoration or specialist research commissions | Use common samples for repeatable quests; a rare forest investigation could lead toward a future Celebi chapter |
| Heart Scale | Optional alternate Egg Move tutoring payment | One explicit quote/confirmation and species compatibility check; keep ordinary move relearning free |
| Shoal Salt / Shoal Shell | Ocean shrine research and existing Shell Bell crafting | Preserve the existing recipe if active; add a separate quest ledger rather than silently spending the player's crafting materials |
| Rare Bone / fossils | Archaeological expeditions, murals and ancient-rift clues | Preserve fossil revival; use expedition completion/evidence to unlock research stages rather than treating every fossil as a Legendary key |
| Relic Copper / Silver / Gold / Vase / Band / Statue / Crown | Museum restoration and an ancient-civilization investigation | Register/display rare relics, preferably retaining them; discoveries can feed an Arceus/ruins research chain without immediate encounter access |
| Strange Souvenir | Guardian-island research led by an Alolan visitor | Can use existing special areas; a full Alola region is not required. Protect any unique quest specimen from loss |
| Odd Keystone | A Spiritomb/echo investigation | Spiritomb is a special **non-Legendary** encounter. Preserve any existing activation method before extending it |
| Pretty Feather | Bird conservation/tracking commissions | Optional field observations can introduce later Legendary-bird research; purchasing feathers alone must not finish the investigation |
| Nugget / Big Nugget | Funding Cap purchases and other training | Keep their primary cash role. Any refinery exchange should be checked against normal sell/buy values to avoid bad deals or profitable loops |

### Safeguards for these uses

- Common materials can be consumed by repeatable exchanges, with confirmation. Unique relics should normally be inspected/registered and retained.
- If a treasure becomes a unique Legendary quest artifact, remove it from ordinary sales too, or require separate earned research evidence. Buying a generic sample cannot replace the story investigation.
- Protect unique relics/Plates from accidental selling or tossing, or provide a documented recovery route. A recorded discovery does not disappear when the item is held by a Pokémon or moved to storage.
- Provide recovery for mandatory items sold before this feature existed; do not require a new game.
- Avoid requiring a rare one-time treasure to unlock several mutually exclusive quest lines. Loan/registration can cover multiple investigations without repeatedly consuming it.
- Item possession is one prerequisite, not an automatic Legendary/Mythical encounter. Preserve League, quest, location and existing story-capture gates.
- Villain research remains part of Giovanni's alliance. Do not write new isolated Aqua/Magma/Plasma operations as unrelated competing plots.

## 7. Implementation order after approval

1. **Cap economy and editor transaction safety.** Agree on batch semantics, Cap availability/prices and whether Nature/Ability costs are included. Add draft/confirmation/rollback behavior before charging anything.
2. **Central acquisition policy and full special-item audit.** Add the explicit manifest, restrict all relevant catalogs and direct purchase paths, and check other acquisition sources such as pickups, gifts, held-item loot and future rewards.
3. **Type: Null chapter and Devon Memory vendor.** Finish the acquisition flag/party-full handling first, then add the basement actor and shop. Ask for Porymap to be saved/closed before the later map edit.
4. **Plate registry and a small first placement batch.** Validate actual maps and walking paths, then place a few Plates and test their quest/pickup flags. Expand the remaining regional placements with their story chapters.
5. **Treasure commissions and relic investigations.** Build on the existing main/side quest system. Start with repeatable Cap-earning research and one optional investigation rather than introducing all encounter chains at once.
6. **Legendary/Mythical finales.** Connect proven quest chains to the intended encounters, retaining all story capture exceptions and existing rift gates.

Normal gameplay restrictions and developer debug tools should be distinguished explicitly. Debug Fill Bag can remain a test tool; it must not silently mark research discoveries or story quests complete.

## 8. Verification checklist for the future implementation

- One Pokémon with three changed EV stats costs exactly one regular Cap; combined IV+EV edits cost exactly one of each.
- No charge for a no-op, reverting to original values, cancellation, missing resources or failed target validation.
- Confirming repeatedly without a new change cannot consume another Cap. Cycling Pokémon cannot share one payment across the team.
- Cover every editing path, including 31 All and Hidden Power patterns, and preserve 252/252/6 and other legal spreads.
- Party and ordinary/expanded PC editing preserve identity, HP damage, fainted state, status and normal save/load behavior.
- Before the appropriate badge, editing remains locked. Cap sources become available when the approved economy says they should.
- Every restricted Legendary/Mythical item is absent from ordinary catalog and direct purchases; ordinary Orbs/Mints and general battle items remain available under their own rules.
- Memories cannot be bought remotely or before Type: Null's unlock. The Devon vendor continues working after evolution/storage changes.
- Every Plate has a unique flag, a reachable tile and an intentional story prerequisite; revisits and reloads do not duplicate it.
- Unique relic recovery, existing saves, already-owned items and prior sales do not softlock quests.
- Common crafting inputs cannot generate an infinite-money or Cap resale loop, bypass a power-stock gate or replace required research evidence.
- Existing rift, League, trainer-battle and scripted capture restrictions remain intact.

## 9. Current code references and deliverable boundary

Reviewed: `src/stat_editor.c`, `src/legends_store.c`, `src/bag_categories.c`, `src/data/items.h`, `include/constants/items.h`, the Devon first-floor basement connection, and the established progression/quest documentation.

This commit contains this proposal only. It does not change the stat editor, costs, shops, map objects, item placements, Type: Null access, quest flags or playable ROM. Existing gameplay work was already committed before this planning pass. Unrelated user research files remain untouched.
