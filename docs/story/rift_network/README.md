# Rift research and detector

Birch calls immediately after Wattson's first defeat. The invitation survives saving. Existing saves that already finished the rescue and earned the Dynamo Badge receive it on entering Mauville Gym. Speaking to Birch in his lab also supports an already-badged save that missed the call.

Birch upgrades the existing Journal into the Rift Tracker and installs the detector. Before this appointment, the original Journal remains unchanged and does not show the signal registry. Afterward the Start menu label and all three pages change: investigation, signals, research notes. Current leads follow the existing Wally/family/May progression.

## Art and purpose

- The original animated Gym artwork remains the design for placed travel rifts. No replacement violet spiral or new blue sprite is installed.
- Natural blue wormholes embedded in donor maps are preserved exactly. They are intended for future Pokemon encounter stories, rather than generic regional travel.
- Hoopa's golden ring remains its own signature and its existing scene is unchanged.

## Gates and placements

The registry.json catalogs all 24 external entrances into donor Ultra Space maps. A shared native warp guard checks natural wormholes in arrow, stair, door and ordinary warp paths before destination setup. It does not block ordinary doors or return links inside Ultra Space. The native maps, tiles and original destinations are retained.

All natural wormholes require the detector and victory over the Hoenn League (FLAG_SYS_GAME_CLEAR). Eight Badges alone are insufficient. They then remain story-sealed until their individual encounters/stories are authored. No donor warp is silently activated as a reward for obtaining the detector. This pass does not release those future Pokemon encounters.

Additional placed travel rifts are deferred for the user to select their locations. The original Gym/Kanto story passage remains intact.

Detector status and field permissions share the same gate function. Before League victory, natural wormholes repel the player and explain their danger. A qualified party still sees a story seal when research is incomplete.

Persistent state uses repurposed, otherwise unused Mystery Gift slots 0x40DE-0x40E0. These slots are excluded from Mystery Gift resets. The older 0x40F7-0x40F9 aliases were shared with menu themes and DexNav, and are no longer used for story state. No save layout expansion is required. The survey mask records only the first 16 checked entries; it is not used as an access permission. The completion slot is reserved for authored encounter stories.

## Follow-up immersion ideas

Have rivals report sightings through calls, let local NPCs react after major incidents, and return to Paradigm with evidence that changes each professor's working theory. Keep uncertain destinations uncertain; the detector should help investigate, not predict the plot.

## Validation

Prior League-gate mGBA integration: 184 rift-research checks, 19 existing Paradigm chapter checks and 23 complete Route 10 / Power Plant rescue checks. Includes actual lab interaction, native map-wormhole gate dialogue, badge/story permissions for every registry entry, menu page/exit behavior, and measured dialogue line widths. Test batteries are isolated from the player save.

League-gate follow-up: all 24 native wormholes also provide an A-button interaction at their existing map tile. This keeps their artwork intact and explains the League requirement even where a donor wormhole tile is blocked. Integration checks distinguish eight Badges from the actual League-clear flag, then verify that the later story seal remains.

## Destination clarification

Natural map wormholes retain their existing Ultra Space destinations and the Hoenn League requirement. Their later story seals remain in place. The two experimental Timeless Woods / Desert Ruins travel objects have been removed, together with their detector entries. Additional teleportation locations are deferred for the user to choose. The existing Mauville Gym / Kanto rescue passage is preserved.

Latest destination clarification validation: 176 native Rift Tracker and natural-wormhole checks pass with the unplaced travel pair removed. The 24 original Ultra Space warp destinations were compared directly to the registry.

Oak joins the tracker lab visit, offers one level-5 Kanto starter (Bulbasaur, Charmander or Squirtle), and sends the player to meet Blue in Fallarbor at X14 Y10. Gifts go to the PC when the party is full and remain available if storage is full. Old tracker builds can revisit Birch to install the independently saved tracker and meet Oak.

Oak/Blue validation: 44 starter and introduction checks, 77 dialogue-fit checks, and 176 Rift Tracker regression checks passed. Tested all three species at level 5, repeat-proof gifts, map persistence, full-party PC delivery, full-storage retry, independent menu/DexNav state, Mystery Gift reset safety and the Fallarbor introduction.
