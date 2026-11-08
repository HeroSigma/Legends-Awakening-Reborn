# Legends Awakening Reborn

## Optional 60-box collection storage

This branch shares the compact PC expansion developed for Legends Awakening Reborn, based on pokeemerald-expansion.

- Normal mode: 14 boxes, original storage records and side activities.
- Collection mode: 60 boxes / 1,800 slots, compact records and transactional saves.
- In-game Options > PC BOXES > A; switching requires two confirmations and clears boxed Pokémon.
- Party and story progress remain. Collection mode simplifies nicknames, original-trainer/met history and cosmetic personality data, and disables retired side activities.

Read the [integration and porting notes](docs/compact-pc/README.md) before applying this to another project. The complete Reborn runtime passed testing; this extracted branch is a porting reference and still needs an independent build and ABI reconciliation. It is not a universal drop-in patch.

No playable ROM or player save is supplied. Existing upstream licenses and credits continue to apply. See the original [pokeemerald-expansion project](https://github.com/rh-hideout/pokeemerald-expansion).
