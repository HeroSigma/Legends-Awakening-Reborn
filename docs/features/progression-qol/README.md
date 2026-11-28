# Capture and training progression

- Strange Ball is excluded from Legends Store. It has zero capture chance on ordinary species and guaranteed capture on species flagged sub-Legendary, restricted Legendary or Mythical. Ultra Beasts and ordinary Paradox species are not included; Legendary Miraidon/Koraidon qualify in catchable encounters. Classification reads the actual wild specimen, so Transform cannot bypass the rule. Existing story, trainer and ghost capture restrictions run first. Zero odds use the normal failed-throw script before critical/victory-catch overrides, avoiding a division by zero. Normal failed-throw consumption is unchanged.
- Birch gives one Strange Ball during the one-time Rift Tracker briefing, without explaining its hidden capture rule. Existing completed briefings do not replay. Its original vague item description is unchanged.
- Master Ball Store access and battle use require the Hoenn League completion flag. The generic overworld Master Ball pickup remains sealed until then. Existing/debug-owned copies cannot bypass the battle-use gate.
- New games start with one EXP Share switched on. Continuing an older save grants a missing copy and enables it, while preserving an existing owner's on/off setting. The received-item flag prevents a duplicate from Mr. Stone.
- The QoL scientist requires Roxanne's Stone Badge. His dialogue explains this and points players toward Brawly for individual stats.
- Summary stat editing, including the editor's initializer, requires Brawly's Knuckle Badge. Ordinary summary viewing and move relearning remain available.

No new saved variables or item IDs were added. Native validation covers real wild-battle throw dispatch, Ditto disguise, Legendary/Mythical successes, ordinary/UB/Paradox failures, victory-catch override failure, both protected story encounters, Master Ball purchases and use, EXP Share migration/toggle preservation, scientist locked/unlocked scripts, and actual summary shortcut gates. The post-unlock summary suite covers stat edits and compact storage. Its retired scientist EV-preset assertion is replaced with the current Max Friendship service. Store economy tests run with League completion set.

Results: 65 progression/capture checks, 35 summary/editor checks, 939 Store checks. Tests use isolated batteries and never load the player's save.
