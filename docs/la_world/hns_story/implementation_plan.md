# Separate Heart & Soul story build

Status: dependency audit and campaign correspondence staged; story is not enabled.
User selected a separate new-save story build on 2026-10-25. Preserve the existing exploration ROM and saves.

## Required implementation

1. Independent story state: map donor progression flags, variables, trainer defeat state and sixteen badges into a dedicated versioned state bank. Preserve all current regional save fields and legacy exploration saves. New Bark's source variable 0x4075 overlaps native VAR_ROUTE122_STATE; Goldenrod's 0x4069 overlaps native VAR_ROUTE110_STATE. Audit remaining collisions before writing state.
2. Separate output and object directory: story and exploration builds must not share configuration-dependent objects or output save basenames. Fresh story initialization removes exploration supplies, all-badge grants, inspection travel and forced visible story actors.
3. Script migration: namespace source labels and local object IDs, rebind all MAP references and corrected warp indices, restore story flags and map/coordinate callbacks, and resolve conditional duplicate source labels. Preserve user-edited geometry and existing canonical identities.
4. Engine support: resolve the audit's missing native functions; add required source-native functionality through project adapters. Do not stub required progression functions with success/no-op returns.
5. Battles and rewards: migrate trainer parties, trainer artwork, battle text, rematch identities, TM/HM/item awards, regional encounter tables and independently persistent defeat state.
6. Core services and travel: Cut, Rock Smash, Strength, Surf, Waterfall, Dive, Rock Climb, berry/apricorn harvesting where present, PC/storage, shops, nurses/healing and correct regional blackout destinations. Avoid reusing Hoenn's berry-state slots or heal identities.
7. Validate story milestones in order. Activate completed dependencies together; a build that loads maps is not evidence that a campaign works.

## Campaign validation sequence

- New Bark initialization, Mom, Elm, starter selection and Mr. Pokemon.
- First rival encounter, return to Elm and starter-dependent rival party/state.
- Violet/Sprout Tower/Falkner; Azalea/Slowpoke Well/Kurt/Bugsy/Ilex.
- Goldenrod/Whitney/Radio/Bicycle/Sudowoodo; Ecruteak/Burned Tower/Morty/Surf.
- Olivine/Lighthouse/Cianwood/Chuck/medicine/Jasmine.
- Lake of Rage/Rocket Hideout/Pryce/Goldenrod Radio Tower takeover.
- Ice Path/Blackthorn/Clair/Dragon's Den and source legendary requirements.
- Route 27/Tohjo Falls/Route 26/Victory Road/Elite Four/Champion.
- S.S. Aqua and Kanto arrival; Power Plant/Snorlax and all eight Kanto Gyms.
- Blue, Mt. Silver and Red; postgame and optional services independently.

Test both genders and starter branches, defeat/retry, item-full cases, purchase/cancel, blackout, save/reload and inter-region regressions. Reconcile the held S.S. Aqua/port exit before marking the Kanto campaign reachable.

## Audit limits

The dependency graph is conservative: it includes optional content and source conditional branches. Missing-symbol counts require inspection, not automatic copying. Five selected facility maps have no source script file; 125 duplicate label names need conditional/source-owner resolution. The source reference ZIP is quarantined and is not included by Reborn's script assembler.
