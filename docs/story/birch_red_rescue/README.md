# Birch / Red rescue

The canonical Route 101 bag gives the normal level 5 starter, then starts the first battle against fixed level 100 Iron Valiant. This story opponent bypasses the route, time-of-day, badge and evolution encounter pools. Its only move is Aerial Ace, ensuring a fast, accurate loss against each normal starter. Running remains blocked by the first-battle rules.

Red calls “Pikachu! Use Thunderbolt!” from offscreen in red text. A targeted lightning sprite, flash, sound and shake strike the attacker; it blinks out. Red and Pikachu walk south down the northern path from (11,9)/(12,9), south into the clearing and west along row 11, ending at (6,12)/(7,12), Red introduces himself, and Birch takes the player to the existing lab scene. Red uses his dedicated NPC graphics.

## Saved state

- `FLAG_LA_MET_RED` (0x02C): completed introduction.
- `FLAG_HIDE_LA_BIRCH_RESCUE_RED` (0x02D): shared temporary actor visibility; hidden on Route 101 transition.
- `FLAG_LA_BIRCH_RESCUE_BATTLE` (0x02E): scoped first-battle override, cleared immediately on field return.
- `VAR_LA_BIRCH_RESCUE_STATE` (0x404E): 0 unstarted, 1 battle, 2 rescue, 3 complete.

Existing `FLAG_RESCUED_BIRCH`, starter identity, Pokémon-get flag, Route 101 and Birch lab state retain native ownership. Rescue is marked complete only after Red intervenes. No save structure expansion or ID renumbering. No changes to completed-save progression.

The first-battle callback heals before field return. The scoped loss bypasses whiteout text and money deduction. Ordinary battle outcomes remain unchanged.

Validation uses a disposable mGBA session for each starter and player gender; it never reads the permanent battery save.
