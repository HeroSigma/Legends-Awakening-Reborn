# Preferred Pokémon follower

Select a Pokémon in the field party menu, then FOLLOWER. FOLLOW ME chooses it without moving the battle lead; RECALL keeps companions in their Balls; AUTOMATIC restores the first healthy eligible party member. When a party menu already has nine rows, FOLLOWER remains available under FIELD SKILLS. Battle, link and egg menus do not gain these actions. Existing indoor, story, NPC-partner and follower-disable restrictions remain in force.

Selection matches personality, original trainer ID and species across party swaps, with the chosen slot breaking ties for identical specimens. This prevents compact/debug Pokémon with duplicated personality and trainer IDs from selecting an earlier, different species. A fainted, egg, bad egg or absent selection falls back to the normal eligible companion. Healing restores a preferred companion still in the party. Compact storage regenerates personality when withdrawing, so choose FOLLOW ME again after withdrawing a compact-stored Pokémon. Automatic and Recall are persistent as well.

Uses previously unused variables 0x40FA–0x40FF without extending SaveBlocks, adding EWRAM state, or changing PC serialization. Zero/default saves retain automatic followers.

Inspired by Kasenn's toggle_follower_from_party_menu branch (cbe04a7a); implementation adapted to Reborn's modern party arrays and compact storage, rather than importing the donor SaveBlock3 field.
Source: https://github.com/Kasenn/pokeemerald-expansion-kasen/tree/toggle_follower_from_party_menu

Validation: 44 native follower/UI/save checks across both storage modes and 446 Start menu return checks. Test batteries are isolated from the user's save. Screenshots and ROM-hashed report are adjacent.

Collision regression recreates all six species from the reported party, gives every member the same personality and trainer ID, and checks selection of each slot, Sneasler/Scraggy swapping and save reloads in both storage modes. Existing older follower preferences remain readable; selecting FOLLOW ME again records the stronger identity key.
