# DexNav equipment chaining

Implemented on this feature branch; not merged into reborn.

For already-caught DexNav targets, a separate bonus roll grants a Mega Stone from the target evolution family or a Z-Crystal of its primary type. Milestones: chain 10 = 10%, 25 = 20%, 50 = 35%, 100+ = 50%. If the roll fails, existing native DexNav item rules apply. Charmander can yield either Charizard stone or Firium Z; non-Mega species can yield their primary-type crystal.

Uses native chain progression/reset and the caught flag. Ordinary wild equipment, explicit scripted encounters, levels, shard rewards and save layout are unchanged. These rates apply to the bonus roll, not the combined chance of every held item. No guarantees or legendary spawning are added.

Validation: see dexnav-equipment-chaining-validation.json. Full-ROM native ARM checks cover milestone boundaries, uncaught/invalid targets and actual item rolls. Runtime checklist: start a real chain, inspect held-item hints, catch/Thief/Covet, break chain, change maps, save/reload.
