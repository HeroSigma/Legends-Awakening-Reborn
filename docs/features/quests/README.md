# Legends quests and field tools

## Player controls

The second Start-menu page has Quests, unlocked field tools, Legends Store and Exit.
Quests use PokemonSanFran's Unbound-style list and lower information panel, recolored teal.
Up/Down scrolls; L/R switches Main/Side; Select cycles All/Active/Ready/Done.
A opens the two objectives, and A again claims a ready reward. B returns from
objectives to the list; B on the list or Start closes the screen.
Each record shows its state, quest giver's overworld appearance, location,
two checked objectives, and reward. A requests a ready reward. Claims still require
the correct Gym, town, or Birch's Lab; the menu does not deliver rewards remotely.

The Journal has been retired. Birch presents a Rift Tracker Key Item after Wattson.
The Start shortcut and bag item open the same tracker. Existing upgraded saves can
recover the physical tool by speaking to Birch. DexNav uses a radar icon, the
tracker a scanner, and the store a gold coin. The native menu frame is retained.

## Current content

Main 0–9: delivery/Tera Orb, Birch rescue/Red/Mega Ring, Route 103/DexNav,
Petalburg Woods/Pokevial, Devon/Tera research, Dewford/Dynamax Band,
museum/Rowan/Z-Power Ring, Power Plant/Rift Tracker, Wally's ongoing search,
Oak's Kanto partner/Blue introduction.

Main 10–17: Hoenn Gym trials in badge order:
Roxanne—Rockium Z; Brawly—Fightinium Z; Wattson—Manectite;
Flannery—Firium Z; Norman—Normalium Z; Winona—Altarianite;
Tate/Liza—Psychium Z; Juan—Waterium Z.
Winning the badge makes the reward ready. The previous Gym trial reward must
already be claimed. First-win scripts and repeat leader interactions attempt
delivery, while the quest menu offers the same claim in that Gym.
Full bags or full stacks leave the reward ready.

Side 18: Rustboro City field researcher at (29,21), three Super Potions for Focus Sash.
Side 19: Oldale Town Ralts enthusiast at (17,11), one non-shiny Ralts for its shiny
counterpart. Party selection and a second confirmation precede the exchange.
This same-species exchange preserves the selected partner's other data and held item,
so cancellation, a full party or full PC cannot delete a Pokemon.
Each sidequest pays once.

Side 20–43: one research permit per existing natural wormhole. Locations remain
hidden in the quest menu until the detector is unlocked. Actual League victory and
the tracker are required before surveying counts. Visit/interact with that entrance,
then claim its individual permit at Birch's Lab. Only that source entrance opens;
native Ultra Space destinations and return warps are retained. The Gym/Kanto story
passage remains independent. New travel-rift placements remain deferred.

Wally's investigation stays active: finding the northern lead does not falsely mark
him rescued. No unfinished later story is invented or completed by this framework.

## Rewards, compatibility and extension

Existing native receipt flags/vars are authoritative, so old story gifts display
as Claimed without being paid again. New two-bit records use flags 0x493–0x4EA
(accepted/surveyed and claimed). These are ordinary persistent flags, not daily flags.
No save structure is expanded. Item IDs already in use stay unchanged; Rift Tracker
is appended, and expanded bag loading supports older item-count payloads.

One-time authored story gifts record eligibility before attempting their native
give-item transaction. Tera Orb, Mega Ring, Pokevial and Rowan's ring use the shared
reward-ring presentation; Dewford retains its authored Hoopa/band pickup scene.
Gym and individual research claims use the same ring presentation. The effect uses
the donor ring's empty frame recolored gold and a falling native item icon, without
summoning Hoopa each time. It releases its sprite resources before resuming dialogue.

Definitions: src/data/legends_quests.h.
State/transactions/menu: src/legends_quests.c.
Field scripts: data/scripts/legends_quests.inc.
Rift safety: src/rift_tracker.c and data/scripts/legends_rift_research.inc.
Native integration test: tools/la_world/story/test_quests.py.

Design reference: PokemonSanFran's Unbound Quest Menu documentation:
https://github.com/PokemonSanFran/pokeemerald/wiki/Unbound-Quest-Menu
The screen artwork and layout are adapted from that branch's graphics/quest_menu,
recolored and flattened for our native overlay. Credit: PokemonSanFran, Skeli,
ghoulslash, HN, Karathan, Mcboy, Greenphx, BSBob, MM and Tustin2121.
The controller and quest ledger remain project-native; that branch's save structures
were not merged. The ring frame derives from the existing Hyper donor Hoopa/ring
asset; the three tool icons derive from the project's existing item art.
