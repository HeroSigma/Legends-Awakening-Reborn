# Random wild SOS encounters

Ordinary wild encounters and dedicated DexNav searches have a 1-in-8 chance of using the SOS battle format when the player has at least two battle-ready Pok?mon. This uses the existing player-controlled double format. The wild caller starts alone; it is not guaranteed to summon a helper before being defeated or caught.

At the end of a surviving turn, the call succeeds 25% of the time above half HP, 50% at half HP or below, and 75% at quarter HP or below. Only one helper can be present, and at most two helpers can arrive. Calls are checked once per turn with a two-turn interval following a call attempt after the first successful arrival. Defeating the original caller prevents further calls.

Helpers are the caller's exact species/form, two levels lower (or the same level at levels 1?2), with ordinary random IVs. This preserves regional species and DexNav search identity. Helpers use the regular wild shiny roll, applicable Charm/DexNav modifiers, and the existing shiny egg-move chance. They do not overwrite the caller or advance guardian quests.

Normal capture rules apply: while two wild opponents are alive, a Ball cannot be aimed; with one remaining, catching works normally. Running, losing and catching clear the temporary SOS session. The original guardian encounter still blocks capture and awards its own quest receipt only on victory.

Other scripted/story encounters, trainers, existing wild doubles, NPC partner battles, Safari/Frontier formats, Legendary/Mythical species, Ultra Beasts, Paradox Pok?mon and Totem species are excluded. A party with fewer than two ready Pok?mon keeps ordinary encounters. No save structure or world map changes are required.

The SOS session uses eight bytes of temporary state. The ordinary and guardian modes share arrival/controller handling but have separate capture and quest-completion rules.

## Validation

The final ROM passed 280 native mGBA checks across random encounter/DexNav eligibility, a 1,000-trial frequency sample, helper generation, low-HP probabilities, actual helper capture, guardian battle/field regression and live Wattson Mega battles. All emulator saves are isolated from the user's battery save.
