# Legends Awakening Story and Character Planning Guide

Updated 7 November 2026. Project snapshot c5a0b902f1 on test/qol-first-three.

This guide records the story currently implemented and the donor characters available for the next chapters. The main unresolved thread is Wally and Kirlia's separation from the player after the Kanto Power Plant incident. Birch's tracker upgrade and Oak's request to meet Blue in Fallarbor create the next planning junction.

The game title is **Legends Awakening**. Reborn identifies the restarted project and repository. It is not part of the in-game title.

## How to use this guide

- **Implemented** means the scene exists in the current scripts. It does not mean every possible save and playthrough has been manually reviewed.
- **Open thread** means a deliberate mystery or an unfinished next chapter. It is not an established answer.
- **Available art** means a file has been preserved, named or matched. It does not automatically mean the character is placed in the game.
- **Shared grunt art** means the donor uses a generic portrait for a named trainer. That does not establish a unique portrait of that person.
- **Candidate** means a plausible visual identification that needs approval before assignment.
- The companion character_inventory.csv contains exact donor references, overworld status, back-sheet status, notes and story presence. The JSON copy preserves the same inventory for future tooling.

## Story rules already established

Aren and Aria are speaking protagonists. They introduce themselves, ask questions and respond aloud. Their chosen player name is used. Internal thoughts support characterization without replacing conversations.

Elara is the player's mother. Norman is an established ally and mentor, not the player's father. Brendan and May are both part of the cast. Red speaks and Pikachu stays with him, even when Red battles with a fresh partner.

Characters displaced from another region do not automatically know they are in Hoenn. Introductions and regional discoveries should happen on screen. The player does not know the names of unfamiliar professors merely because their voices joined a call.

Villain factions may investigate the same rifts for different reasons. The story has not established that Aqua, Plasma, Rocket and Galactic are a single alliance. Their actions should not be treated as proof of cooperation without a scene that establishes it.

New chapters should review dialogue, facing, entrances, exits, camera movement, text color, rewards and recovery after losing. Story battles do not ask Singles or Doubles. That choice belongs to Gym and League battles outside fixed story encounters.

## Implemented story chronology

### Opening and the strange delivery

The creator's opening frames a world larger than one region and asks the player to explore and question things that seem out of place. Birch introduces himself and seems to recognize the player's name. That recognition is a clue, not an explanation.

The player wakes after a recurring dream about being sent away. A PC delivery notice refers to an order the player does not remember placing. After setting the clock, the player speaks with Elara and receives an unexplained parcel containing the Tera Orb. The sender remains unknown.

**Open threads:** Who sent the parcel and PC notice? What does the dream recall? Why does Birch recognize the name?

### The Littleroot news report and next door

The TV reports unstable openings, views of distant landscapes and unusual Pokemon outbreaks. Colress is named as the scientist coordinating the investigation. Elara recognizes his name and avoids explaining why.

The next-door family scene introduces Brendan and May and connects the player to Birch's fieldwork. Hazel's family conversations have been staged and polished. The report establishes rifts as a public concern before the player encounters one directly.

**Open threads:** Elara's history with Colress, and how his investigation relates to the professors later calling themselves Paradigm.

### Birch rescue and Red's arrival

The starter case offers nine choices: Treecko, Torchic, Mudkip, Riolu, Shinx, Ralts, Gible, Eevee and Rockruff.

After the choice, the player faces a level-100 Iron Valiant in a protected forced loss. It cannot be captured in this scene. Red calls for Pikachu to use Thunderbolt from off screen, defeats the attacker, then enters with Pikachu from the northern path. Birch takes everyone back to the lab.

**Open thread:** Why was such a dangerous Pokemon there, and how does its appearance connect to the rifts?

### The first lab visit and the Mega Ring

Birch recognizes Red and asks how he reached Hoenn. Red explains that he came through a portal and knows his way around Hoenn from an earlier journey. The player and Red exchange introductions.

Birch gives Red **Charmander**, found near a rift and brought to the lab by an aide. Red says it feels like being back in Kanto. This replaces the earlier Riolu plan; Red receives Charmander regardless of the player's starter.

Red's introductory spar is another protected loss. Pikachu remains beside him while he uses his new partner. Red congratulates the player and gives the Mega Ring, then leaves with Pikachu.

### Route 103 and the Littleroot farewell

The player partners with Red against Brendan and May. Both rivals recognize Red, and the player learns he is a Champion from Kanto who is starting fresh while investigating the rifts.

If the player chose a nonstandard Hoenn starter, Brendan and May comment on the unconventional choice. On returning to the lab, Birch gives the National Pokedex and DexNav. May gives Poke Balls.

Elara hears the player's account and gives the Running Shoes. She privately thinks of Caelum and wonders whether this was planned. The player does not hear that thought.

**Continuity:** The player partnered with Red, not with Brendan or May. Rustboro dialogue has been corrected accordingly.

### Route 102 and the call from Timeless Woods

At X12-14 Y8, the player hears their name and notices the opening toward Timeless Woods. The scene works whether or not the nearby Youngster battle happened first.

The player notices that a trainer blocks the left-side approach and says there must be another way in. This gives a reason to explore instead of assuming the first path is usable.

**Open thread:** Who or what knows the player's name and is calling from the Woods?

### Timeless Woods and the stolen device

On entering, the player feels that the place is familiar without knowing why. At X16 Y13, the camera reveals Giovanni and Cyrus facing each other with a ball-shaped object between them. Giovanni picks it up.

They discuss stabilizing rifts, controlling reliable crossings and keeping the professors and young Trainers from finding the device. They leave to the right. The player recognizes them without remembering where and decides that Birch needs to hear about it.

The overworld object uses the preserved golden-ball appearance. The ball graphic is a representation; the story has not established the device's full nature.

**Open threads:** The player's recognition, the device's origin, its limits, and the two villains' larger plan.

### Petalburg and Wally's first partner

After leaving the Woods, the player seeks Norman's help reaching Birch. The player describes the men's R and G markings. Norman appears to recognize them, but Wally's arrival interrupts the explanation.

Wally's Ralts encounter includes an actual visible overworld Ralts and a moment of trust and reassurance. After the catching sequence, Norman says he has relayed the report to Birch. Wally is not yet part of the rift investigation.

**Polish check:** Keep the first Ralts presentation consistent with the shiny Kirlia used later.

### Petalburg Woods and the Shadow Triad

A Devon researcher and visiting Silph researcher compare rift readings captured by a modified Silph Scope. One Shadow Triad member demands the recording.

The player fights that member in a fixed story singles battle. The other two appear afterward, take the backup drive and retreat north. The researchers retain numerical readings. The player is directed toward Devon in Rustboro.

The rescue rewards the **Pokevial**, with three full-party heals and refills at a Pokemon Center. The Silph researcher has movement and reacts during the scene.

**Open thread:** What the Triad needs the stolen recording for, and how it relates to the stabilizing device.

### Rustboro and Rusturf Tunnel

Roxanne remains the first Rustboro milestone and has a level-16 cap. The Devon theft sequence follows the Gym progression.

Aqua steals research hardware. The player pursues the thief into Rusturf Tunnel, protects Peeko, recovers the package and meets Briney. Spoken exchanges replace silent assumptions about why the player is helping.

The Aqua theft acknowledges the earlier research incident without asserting an alliance with the Triad.

### Devon and the basement researcher

Mr Stone discusses the hardware and missing Silph recordings. Birch joins by office call, acknowledges Norman's report and coordinates the investigation. This is not yet a physical gathering of all the professors.

Stone sends the player toward Steven in Dewford and Captain Stern in Slateport. The PokeNav remains part of this progression. The departing scientist invites the player to visit the basement.

The basement Tera scientist explains automatic primary-type shard collection after defeated or caught wild Pokemon, rare Stellar bonuses, and Tera changes costing 50 matching shards or 150 Stellar Shards. The scientist's introduction is part of enabling this system.

### Rustboro May and Silver

After May's Rustboro battle, the team is healed and Silver arrives from the north. He introduces himself as a displaced Johto traveler, learns where he is, then challenges the player.

Silver's six-member team follows his Johto families, with a shiny Totodile ace. After losing, he shares what he saw and heads north to investigate alone. The revised staging keeps the rival conversation coherent and avoids actors vanishing during Silver's entrance.

**Open thread:** Silver's next encounter and what his independent investigation uncovers.

### Dewford and Hoopa

A sound cue near the Pokemon Center draws the player toward the extra Route 106 area. The camera reveals the combined Hoopa-and-ring asset emerging and vanishing.

Hoopa leaves a Dynamax Band. The player reacts to finding it and keeps it, uncertain how Hoopa obtained it.

Hoopa's golden rings are intentionally distinct from the broader rift phenomenon. The scene can mislead the player into suspecting Hoopa, but the story has not confirmed that it caused the other openings. Steven's overworld appearance is the selected Hyper gfx_134.

### Slateport museum and Barry

Barry rushes into the museum looking for a public phone, unaware that the crowd belongs to Team Aqua. He arrives before the player's battle and fights his own grunt while the player fights one grunt.

These are staged as separate singles encounters. There is no verified Barry back sprite supporting a player-side partner battle.

Archie enters and exchanges dialogue with Barry and the player. He describes the sea splitting open and wants Stern's equipment to investigate. Barry introduces himself; after the incident, the player explains that this is Hoenn. Barry is shocked and rushes off before receiving the full explanation.

**Open threads:** The sea rift, Aqua's next move and Barry's attempts to contact home.

### Route 110 and Rowan

Birch and Rowan are investigating readings from New Mauville. Rowan approaches the player. When he hears about Barry, he asks where the boy went; the player explains the museum and his search for a phone.

Rowan gives the Z-Power Ring found near a generator after a surge. Barry replaces the standard rival battle in this part of the journey, with a team based on his established Pokemon families.

**Continuity:** The professor here is Rowan, not the earlier Oak proposal. Oak's personal introduction happens later in Birch's lab.

### Mauville and the first Kanto crossing

Wally now has a shiny Kirlia. The Gym scene starts automatically on entry, with Wally and Kirlia reacting to the energy. The portal sits above the statue area. Scott's interruption has been removed.

The player, Wally and Kirlia enter the Gym-style travel rift. They arrive at the actual Kanto Route 10 map at X9 Y44. The sign at X6 Y42 identifies the area, and the player explores the full Kanto Power Plant.

Wattson is inside holding the breaker situation under control, facing the box at X2 Y9 from X2 Y10. The reactor interaction is at X8 Y11.

### Miraidon and the separated return

Shutting down the reactor draws Miraidon toward the player. Its regular Pokemon overworld sprite is used. The level-70 battle is a forced loss and capture is blocked.

Afterward, Wattson takes the left exit. The player checks on Wally and Kirlia before returning through the outdoor rift.

Only the player and Wattson arrive in Mauville Gym. **Wally and Kirlia do not return with them.** That absence is intentional, not a missing-actor bug.

### Paradigm and Wattson's Gym

The player calls Birch and reports Route 10, the Power Plant, Miraidon and the missing pair. Birch and Rowan are on a joint call with six colleagues.

The Paradigm Society consists of **Birch, Elm, Rowan, Oak, Juniper, Sycamore, Kukui and Burnet**. Paradigm is the short name. Unfamiliar voices remain unnamed to the player until properly introduced.

The group agrees to investigate readings and reach out to other Trainers. After the call, Wattson visibly walks north. Before his Gym battle he explains how he reached Kanto and what he found at the reactor.

### Wally calls and the Verdanturf report

After Wattson's victory, Wally's registration call is queued. He and Kirlia are safe but still in Kanto. He already knows where he is from the Route 10 visit.

Kirlia is helping him look for a way home. Wally asks the player to tell his family in Verdanturf. The player promises to do so and to update Birch.

The uncle receives the report. May joins the search. Wally remains absent from the house.

### Returning to Timeless Woods

May meets the player at the old device clearing. A Triad scout knows that Wally reached Kanto and says the device has moved. The scout claims to be following Giovanni and Cyrus as well.

The scout warns that something was left active near the northern opening. May stays to watch the area. The player insists on informing Paradigm before another crossing.

**Current planning edge:** This is an investigation lead, not permission to enter the natural Ultra Space wormhole before the League.

### Birch Oak and the Rift Tracker

After Wattson's first defeat, Birch calls and asks the player to visit the Littleroot lab with the PokeNav and Journal. Wally's family can be helped first.

Oak is with Birch. Birch introduces him as Professor Oak from Kanto and one of the earlier call's voices. Oak introduces himself as Samuel Oak and responds to the player's concern for Wally.

Birch installs the detector and changes the Adventure Journal into the **Rift Tracker**. The tracker shows investigation leads, detected signals and research notes. It distinguishes discovery from permission to enter.

Oak offers **one level-5 Bulbasaur, Charmander or Squirtle**. The player previews and confirms the choice. A full party sends the gift to the PC; full storage leaves the offer available. The gift cannot be claimed repeatedly.

Oak asks the player to meet his grandson **Blue in Fallarbor**. This is a second Kanto starter opportunity, not a replacement for the original starter choice.

### Blue in Fallarbor

Blue is placed at X14 Y10 and becomes available after Oak's gift. The player introduces themselves, mentions Oak and explains Wally's situation.

Blue is comparing unusual Pokemon reports and tracks in the ash. He has heard Red is in Hoenn and agrees to compare evidence with Paradigm.

This is an introduction and investigation hook. A new Blue battle, starter choice, team reveal or player-side partner battle has not been added to this meeting.

## Rift rules that future chapters must preserve

| Appearance | Purpose | Current access |
| --- | --- | --- |
| Natural blue map wormholes | Lead into their existing Ultra Space areas for future Pokemon stories | Detector and actual Hoenn League victory required, then individual story permission |
| Animated Gym style rifts | Travel between places | Existing Mauville Gym and Kanto Route 10 passage belongs to the rescue chapter |
| Hoopa and golden ring | Hoopa's own passage signature and the Dewford mystery | Existing scripted appearance; not proof it causes all rifts |

All 24 catalogued external natural wormhole entrances retain their original Ultra Space destinations and map artwork. Eight Badges alone do not satisfy the League requirement.

Extra travel-rift locations are undecided. The experimental Timeless Woods and Desert Ruins travel pair was removed. Do not silently restore it.

The remaining natural-wormhole encounter stories are not authored yet. The League is a necessary condition, not an automatic release of every sealed destination.

## Player knowledge and character knowledge

| Subject | What is established | What remains unknown |
| --- | --- | --- |
| Professors | The player has met Birch, Rowan and Oak in person | Physical introductions to Elm, Juniper, Sycamore, Kukui and Burnet |
| Wally | Alive in Kanto with Kirlia, looking for a way home | A reliable return route and why his crossing separated |
| Giovanni and Cyrus | Took the device and want controlled crossings | Their end goal, the device's origin and each man's commitment |
| Shadow Triad | Stole Scope recordings and knows about Wally | Whether its account is trustworthy and who receives the information |
| Aqua | Investigates an opening at sea and steals equipment | What Archie intends to do with the readings |
| Hoopa | Appeared through a golden ring and left the Band | Where the Band came from and its connection to the larger mystery |
| Elara | Recognizes Colress and privately thinks of Caelum | Her history and what she understands about the player |
| Colress | Publicly named as research coordinator | His relationship to Paradigm and his actual agenda |

## Story decisions still open

1. Decide the next playable objective after Blue's introduction. The existing scene compares evidence but does not launch a finished Fallarbor chapter.
2. Establish how the player updates Birch after learning Wally is safe. Avoid leaving a spoken promise unresolved.
3. Explain why Wally and Kirlia reached Route 10 again while the player and Wattson returned to the Gym.
4. Decide what the scout meant by the northern opening without unlocking the natural Ultra Space route before the League.
5. Give Giovanni and Cyrus separate motivations for the device and decide whether their cooperation lasts.
6. Define the Triad's employer and its relationship to Colress, N and Ghetsis. Their involvement is not yet established.
7. Continue Archie's sea-rift thread and choose when Magma enters the custom story.
8. Resolve Colress's opening-news role versus the Paradigm Society's research role.
9. Decide which rivals receive full regional arcs and which remain tournament or side-story guests.
10. Choose future Gym-style teleport locations and their return routes. These choices are intentionally deferred.
11. Author each post-League Ultra Space Pokemon event and its access conditions.
12. Decide how Caelum, Elara, the dream, Birch's recognition and the anonymous Tera Orb delivery connect.

## Suggested introduction groups

These are planning options, not implemented scenes.

- **Kanto response:** Blue, Oak, Red and Green or Leaf can connect the player to the Kanto displacement problem. Lance and the named Rocket executives have strong HnS support.
- **Johto investigation:** Elm, Ethan, Silver, Kris, Lyra, Eusine and Kurt provide a natural group for legends, unusual signals and practical research.
- **Sinnoh evidence:** Rowan, Barry, Lucas, Dawn and Cynthia can examine the rifts and Cyrus. Palmer also creates a personal connection to Barry.
- **Unova research conflict:** Juniper, Cheren, N, Colress, Ghetsis and the Triad provide several distinct viewpoints. Do not introduce them as a united faction by default.
- **Kalos energy specialists:** Sycamore's physical art still needs matching. Most Kalos Gym and Elite Four battle portraits are available, while their overworld matches are less complete.
- **Alola and Ultra Space:** Kukui, Burnet, Lillie, Gladion, Lusamine and Faba are strong thematic candidates. Many physical NPC matches still need work before scenes can be staged.
- **Galar Dynamax follow-up:** Gloria, Hop, Bede and Marnie already have selected overworld sprites. Leon and the Gym cast have battle art. This can pay off the Band found after Hoopa.
- **World Tournament:** Frontier Brains, regional leaders and Champions can appear without needing a full regional story arc. Retaining their characters does not require retaining every old facility.

## Character inventory overview

The catalogue has 222 planning entries. It includes individual characters, a few supporting groups and faction grunt pools. Alternate outfits and regional aliases are kept under the same identity.

- Both art types available: 91
- Portrait available: 86
- Overworld available: 11
- No dedicated art matched: 13
- Shared grunt art only: 13
- Candidate needs visual approval: 8

A matching overworld and front portrait do not by themselves guarantee a validated runtime import. HnS named source art can be selected and registered when needed. Most later-region leaders currently have strong battle art and still need an overworld match.

A back sprite is needed for a character shown on the player's side of a battle. It is not required for normal opponent battles or dialogue. Do not promise a player-and-rival double battle based only on a front portrait.

### Donor coverage

| Donor | Preserved front entries | Back coverage and caution |
| --- | --- | --- |
| Hyper Emerald | 250 | 12 sheets; several character labels are still tentative |
| Black and White Advanced | 148 | 6 donor slots; identities of generic player/demo slots need review |
| Sword and Shield donor | 148 | 6 donor slots; distinct Galar art is mixed with reused entries |
| Aesthetic Red | 148 | 6 donor slots; native Kanto alternatives are useful |
| Mercury | 147 | Archived only; one front slot failed extraction; many overworld palettes need review |
| Stone Dragon 3 | 148 | Front and back archive exists; no complete named overworld catalogue was preserved |
| HnS | 234 named source fronts | 14 named source back sheets, including Gold, Kris, Lance and Silver |
| GS Chronicles | No recovered front catalogue | Original source ROM is missing; map exports alone do not prove character art |

These are image-slot counts, not unique people. Many entries are generic classes, alternate outfits or duplicate artwork. The preserved overworld inventory also contains props, Pokemon, fallback palettes and unresolved candidates.

### Readiness key for the tables

- **Both**: a front portrait and a named or selected overworld source are available.
- **Front**: battle portrait available; overworld still needs matching.
- **OW**: named or selected overworld available; dedicated front not matched.
- **Shared**: only generic grunt art is associated with the named donor trainer.
- **Review**: plausible asset match awaiting approval.
- **Story**: the identity exists in current story/native scripts but lacks a dedicated donor match in this audit.

Multi-role characters appear once: Blue is in the rival table and Malva is in the faction table. A faction connection does not establish a character as an enemy in this story.

The full CSV records the sources and qualifications behind each row. Table source abbreviations are H for Hyper, N for HnS, B for BWA and S for SWSH.

### Protagonists and recurring rivals

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Aren | Speaking protagonist | Both | native/brendan player art |
| Aria | Speaking protagonist | Both | native/may player art |
| Red | Protagonist and Champion | Both | H set2_044 |
| Blue | Rival Champion and Gym Leader | Both | H set2_000 |
| Green or Leaf | Female protagonist | Both | H set2_002 |
| Ethan or Gold | Protagonist | Both | H set2_003 |
| Kris | Protagonist | Both | H set2_005 |
| Lyra | Protagonist | Both | H set2_006 |
| Silver | Rival | Both | H set2_004 |
| Brendan | Rival and protagonist | Both | H set2_052 |
| May | Rival and protagonist | Both | H set2_051 |
| Wally | Rival | Both | H set1_070 |
| Lucas | Protagonist | Both | H set2_010 |
| Dawn | Protagonist | Front | H set2_008 |
| Barry | Rival | Both | H set2_009 |
| Hilbert | Protagonist | Both | H set2_011 |
| Hilda | Protagonist | Both | H set2_012 |
| Nate | Protagonist | Both | H set2_014 |
| Rosa | Protagonist | Both | H set2_015 |
| Cheren | Rival and Gym Leader | Both | H set3_051 |
| Hugh | Rival | Both | H set2_016 |
| Calem | Protagonist and rival | Both | H set2_018 |
| Serena | Protagonist and rival | Both | H set2_019 |
| Elio | Protagonist | Both | H set2_020 |
| Selene | Protagonist | Both | H set2_021 |
| Hau | Rival | Front | H set3_071 |
| Gladion | Rival and Aether connection | Both | H set2_046 |
| Victor | Protagonist | Front | H set2_047 |
| Gloria | Protagonist | Both | H set2_048 |
| Hop | Rival | Both | S set1_106 |
| Bede | Rival and Fairy Gym Leader | Both | S set1_100 |
| Marnie | Rival and Gym Leader | Both | H set3_095 |
| Klara | Isle of Armor rival | Front | H set1_089 |
| Avery | Isle of Armor rival | Front | H set1_090 |
| Rei | Protagonist | Front | H set1_054 |
| Akari | Protagonist | Front | H set2_027 |
| Elaine | Lets Go protagonist | Front | H set3_001 |
| Trace | Lets Go rival | Front | H set3_072 |
| Ash | Trainer and protagonist | Both | H set2_022 |
| Alain | Rival | Both | H set2_023 |
| Paul | Rival | Front | H set2_024 |
| Zinnia | Lorekeeper | Both | H set2_007 |

### Kanto Gym and League cast

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Brock | Gym Leader | Both | N leader_brock_hns |
| Misty | Gym Leader | Both | N leader_misty_hns |
| Lt Surge | Gym Leader | Both | N leader_surge_hns |
| Erika | Gym Leader | Both | N leader_erika_hns |
| Koga | Gym Leader and Johto Elite Four | Both | N elite_four_koga_hns |
| Sabrina | Gym Leader | Both | N leader_sabrina_hns |
| Blaine | Gym Leader | Both | N leader_blaine_hns |
| Janine | Gym Leader | Both | N leader_janine_hns |
| Lorelei | Elite Four | Both | N elite_four_lorelei_frlg |
| Bruno | Elite Four | Both | N elite_four_bruno_hns |
| Agatha | Elite Four | Both | N elite_four_agatha_frlg |

### Kanto and Johto Gym and League cast

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Lance | Elite Four and Champion | Both | N champion_lance_hns |

### Johto Gym and League cast

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Falkner | Gym Leader | Both | N leader_falkner_hns |
| Bugsy | Gym Leader | Both | N leader_bugsy_hns |
| Whitney | Gym Leader | Both | N leader_whitney_hns |
| Morty | Gym Leader | Both | N leader_morty_hns |
| Chuck | Gym Leader | Both | N leader_chuck_hns |
| Jasmine | Gym Leader | Both | N leader_jasmine_hns |
| Pryce | Gym Leader | Both | N leader_pryce_hns |
| Clair | Gym Leader | Both | N leader_clair_hns |
| Will | Elite Four | Both | N elite_four_will_hns |
| Karen | Elite Four | Both | N elite_four_karen_hns |

### Hoenn Gym and League cast

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Roxanne | Gym Leader | Both | H set1_040 |
| Brawly | Gym Leader | Both | H set1_041 |
| Wattson | Gym Leader | Both | H set1_042 |
| Flannery | Gym Leader | Both | H set1_043 |
| Norman | Gym Leader and mentor | Both | H set1_044 |
| Winona | Gym Leader | Both | H set1_045 |
| Tate | Gym Leader | Both | H set1_046 |
| Liza | Gym Leader | Both | H set1_046 |
| Juan | Gym Leader | Both | H set1_047 |
| Sidney | Elite Four | Both | H set1_036 |
| Phoebe | Elite Four | Both | H set1_037 |
| Glacia | Elite Four | Both | H set1_038 |
| Drake | Elite Four | Both | H set1_039 |
| Steven | Champion | Both | H set1_081 |
| Wallace | Gym Leader and Champion | Both | H set2_028 |

### Sinnoh Gym and League cast

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Roark | Gym Leader | Front | H set3_025 |
| Gardenia | Gym Leader | Front | H set3_026 |
| Maylene | Gym Leader | Front | H set3_027 |
| Crasher Wake | Gym Leader | Front | H set3_028 |
| Fantina | Gym Leader | Front | H set3_029 |
| Byron | Gym Leader | Front | H set3_030 |
| Candice | Gym Leader | Front | H set3_031 |
| Volkner | Gym Leader | Front | H set3_032 |
| Aaron | Elite Four | Front | H set3_033 |
| Bertha | Elite Four | Front | H set3_034 |
| Flint | Elite Four | Front | H set3_035 |
| Lucian | Elite Four | Front | H set3_036 |
| Cynthia | Champion | Both | B set1_104 |

### Unova Gym and League cast

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Cilan | Gym Leader | Front | H set3_037 |
| Chili | Gym Leader | Front | H set3_038 |
| Cress | Gym Leader | Front | H set3_039 |
| Lenora | Gym Leader | Front | H set3_040 |
| Burgh | Gym Leader | Front | H set3_041 |
| Clay | Gym Leader | Front | H set3_043 |
| Skyla | Gym Leader | Front | H set3_044 |
| Brycen | Gym Leader | Front | H set3_045 |
| Drayden | Gym Leader | Front | H set3_046 |
| Roxie | Gym Leader | Front | H set3_052 |
| Marlon | Gym Leader | Front | H set3_053 |
| Grimsley | Elite Four | Front | H set3_047 |
| Marshal | Elite Four | Front | H set3_048 |
| Shauntal | Elite Four | Front | H set3_049 |
| Caitlin | Elite Four | Front | H set3_050 |
| Alder | Champion | Front | H set2_030 |
| Iris | Gym Leader and Champion | Both | H set2_031 |

### Kalos Gym and League cast

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Viola | Gym Leader | Front | H set3_055 |
| Grant | Gym Leader | Front | H set3_057 |
| Korrina | Gym Leader | Front | H set3_059 |
| Ramos | Gym Leader | Front | H set3_058 |
| Clemont | Gym Leader | Front | H set3_060 |
| Valerie | Gym Leader | Front | H set3_061 |
| Olympia | Gym Leader | Front | H set3_062 |
| Wulfric | Gym Leader | Front | H set3_063 |
| Drasna | Elite Four | Front | H set3_065 |
| Wikstrom | Elite Four | Front | H set3_066 |
| Siebold | Elite Four | Front | H set3_067 |
| Diantha | Champion | Front | H set2_032 |

### Villain teams and executives

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Malva | Elite Four and Flare connection | Front | H set3_064 |
| Giovanni | Rocket leader | Both | H set2_034 |
| Archie | Aqua leader | Both | H set1_013 |
| Matt | Aqua admin | Front | H set1_010 |
| Shelly | Aqua admin | Front | H set1_012 |
| Maxie | Magma leader | Both | H set1_076 |
| Tabitha | Magma admin | Front | H set1_069 |
| Courtney | Magma admin | Front | H set2_055 |
| Cyrus | Galactic leader | Both | H set2_038 |
| N | Plasma and rival role | Both | H set2_013 |
| Ghetsis | Plasma leader | Front | H set2_039 |
| Lysandre | Flare leader | Front | H set2_040 |
| Shadow Triad | Plasma agents | Both | B set1_099 |
| Archer | Rocket executive | Both | N archer_hns |
| Ariana | Rocket executive | Both | N ariana_hns |
| Petrel | Rocket executive | Both | N petrel_hns |
| Proton | Rocket executive | Both | N proton_hns |
| Mars | Galactic commander | Shared | H set3_080 |
| Jupiter | Galactic commander | Shared | H set3_080 |
| Saturn | Galactic commander | Shared | H set3_079 |
| Zinzolin | Plasma sage | Shared | H set3_081 |
| Bronius | Plasma sage | Shared | H set3_081 |
| Giallo | Plasma sage | Shared | H set3_081 |
| Gorm | Plasma sage | Shared | H set3_081 |
| Ryoku | Plasma sage | Shared | H set3_081 |
| Xerosic | Flare scientist | Shared | H set3_083 |
| Aliana | Flare scientist | Shared | H set3_084 |
| Bryony | Flare scientist | Shared | H set3_084 |
| Celosia | Flare scientist | Shared | H set3_084 |
| Mable | Flare scientist | Shared | H set3_084 |
| Aqua grunts | Faction enemy pool | Front | H set1_001 |
| Magma grunts | Faction enemy pool | Front | H set1_008 |
| Rocket grunts | Faction enemy pool | Front | H set2_058 |
| Rainbow Rocket grunts | Faction enemy pool | Front | H set3_075 |
| Galactic grunts | Faction enemy pool | Front | H set3_079 |
| Plasma grunts | Faction enemy pool | Front | H set3_081 |
| Flare grunts | Faction enemy pool | Front | H set3_083 |

### Alola Gym and League cast

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Hala | Island Kahuna | Front | H set3_004 |
| Olivia | Island Kahuna and Elite Four | Front | H set3_002 |
| Nanu | Island Kahuna | Front | H set2_056 |
| Hapu | Island Kahuna | Front | H set3_003 |

### Galar Gym and League cast

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Milo | Gym Leader | Front | H set3_085 |
| Nessa | Gym Leader | Front | H set3_086 |
| Kabu | Gym Leader | Front | H set3_087 |
| Bea | Gym Leader | Front | H set3_088 |
| Allister | Gym Leader | Front | H set3_089 |
| Opal | Gym Leader | Front | H set3_090 |
| Gordie | Gym Leader | Front | H set3_092 |
| Melony | Gym Leader | Front | H set3_093 |
| Piers | Gym Leader and Team Yell connection | Front | H set3_094 |
| Raihan | Gym Leader | Front | H set3_096 |
| Leon | Champion | Front | H set3_073 |

### Professors research and lore

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Birch | Paradigm professor | OW | Not matched |
| Oak | Paradigm professor | Both | N professor_oak_frlg |
| Rowan | Paradigm professor | OW | Not matched |
| Elm | Paradigm professor | OW | Not matched |
| Juniper | Paradigm professor | OW | Not matched |
| Sycamore | Paradigm professor | Story | Not matched |
| Kukui | Paradigm professor | Front | H set3_074 |
| Burnet | Paradigm professor | Story | Not matched |
| Samson Oak | Regional researcher | Both | N samson_oak_hns |
| Colress | Researcher and Plasma connection | Front | H set3_078 |
| Lillie | Aether story character | Front | H set3_077 |
| Lusamine | Aether leader | Front | H set3_000 |
| Faba | Aether executive | Front | H set2_041 |
| Volo | Antagonist and lore character | Front | H set2_049 |

### Frontier and specialist guests

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Noland | Frontier Brain | Both | N factory_head_noland |
| Greta | Frontier Brain | Both | N arena_tycoon_greta |
| Tucker | Frontier Brain | Both | N dome_ace_tucker |
| Lucy | Frontier Brain | Both | N pike_queen_lucy |
| Spenser | Frontier Brain | Both | N palace_maven_spenser |
| Brandon | Frontier Brain | Both | N pyramid_king_brandon |
| Anabel | Frontier Brain | Both | N salon_maiden_anabel |
| Palmer | Battle Tower Tycoon and Barry father | Front | H set2_025 |

### Other named supporting characters

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Eusine | Legendary researcher | Both | N eusine_hns |
| Bill | Researcher | OW | Not matched |
| Kurt | Apricorn craftsman | OW | Not matched |
| Daisy | Kanto supporting character | OW | Not matched |
| Mr Fuji | Kanto supporting character | OW | Not matched |
| Celio | Sevii network researcher | OW | Not matched |

### Visual candidates to approve

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Bianca | Rival | Review | Not matched |
| Sonia | Researcher | Review | S set1_135 |
| Rose | League chairman and antagonist | Review | S set1_108 |
| Oleana | Macro Cosmos executive | Review | S set1_127 |
| Magnolia | Professor | Review | S set1_123 |
| Peony | Explorer and former Champion | Review | S set1_107 |
| Cogita | Lore character | Review | H set2_017 |
| Lisia | Contest performer | Review | H set2_054 |

### Current story supporting cast

| Character | Role | Art | Front source |
| --- | --- | --- | --- |
| Elara | Story supporting cast | Story | Not matched |
| Hazel | Story supporting cast | Story | Not matched |
| Caelum | Story supporting cast | Story | Not matched |
| Mr Stone | Story supporting cast | Story | Not matched |
| Briney | Story supporting cast | Story | Not matched |
| Captain Stern | Story supporting cast | Story | Not matched |
| Devon researcher | Story supporting cast | Story | Not matched |
| Silph researcher | Story supporting cast | Story | Not matched |
| Wally family | Story supporting cast | Story | Not matched |
| Professor Cozmo | Story supporting cast | Story | Not matched |
| Lanette | Story supporting cast | Story | Not matched |
| Scott | Story supporting cast | OW | Not matched |
| Hoopa | Story supporting cast | OW | Not matched |

## Back sprites and ally battle planning

Verified named back sheets include Brendan, May, Red, Leaf, Wally and Steven in the Hyper or HnS archives. HnS also provides named Gold, Kris, Lance and Silver back art. These source identities are useful starting points; a new player-side partner still needs animation, palette and battle testing.

Hyper back_008 Blue, back_009 Hilbert, back_010 Ash and back_011 Silver retain review labels in the gallery. Prefer the named HnS Silver sheet for a verified Silver source. Do not count the tentative Blue sheet as a finished partner implementation.

Barry has no verified back sheet in the current donor audit. The museum's parallel singles staging deliberately avoids requiring one.

## Identities needing a verified donor match

The following are useful planning targets, but no dedicated match has been established in this audit. An unlabelled asset may still exist. These entries must not be counted as ready characters.

- Chase - Kanto protagonist.
- Elesa - Unova Gym Leader.
- Shauna - Kalos rival.
- Tierno - Kalos rival.
- Trevor - Kalos rival.
- Guzma - Skull leader.
- Plumeria - Skull admin.
- Ilima - Alola captain.
- Lana - Alola captain.
- Kiawe - Alola captain.
- Mallow - Alola captain.
- Sophocles - Alola captain.
- Acerola - Alola captain and Elite Four.
- Mina - Alola captain.
- Kahili - Alola Elite Four.
- Molayne - Alola Elite Four.
- Mustard - Galar mentor.
- Honey - Galar dojo supporting cast.
- Sordward - Galar antagonist.
- Shielbert - Galar antagonist.
- Adaman - Hisui leader.
- Irida - Hisui leader.
- Laventon - Hisui professor.
- Nemona - Paldea rival.
- Arven - Paldea companion.
- Penny - Paldea companion.
- Sada - Paldea professor.
- Turo - Paldea professor.
- Geeta - Paldea Champion.
- Clavell - Paldea director.
- Iono - Paldea Gym Leader.
- Rika - Paldea Elite Four.
- Carmine - Kitakami rival.
- Kieran - Blueberry rival.

## Identity and continuity cautions

- Green and Leaf are one planning entry here. Decide the intended name and canon before treating them as separate people.
- Gold and Ethan, Black and Hilbert, Blake and Nate, and X and Calem are donor naming differences.
- Hao is Hau; Lily is Lillie; Alaine is Alain.
- Past Red, past Archie, past Maxie, past Ghetsis, Rainbow Rocket Giovanni and corrupted Lusamine are alternate versions or outfits. They become separate story individuals only if the plot deliberately establishes that.
- Hyper's generic Rocket, Galactic, Plasma and Flare portraits are reused for several named admins in its trainer records. That reuse is not a unique visual identification.
- Aqua's intended named admins are Matt and Shelly. Amber is not an additional unique admin in the current plan.
- Tate and Liza have separate overworld actors but share a combined front portrait in the selected Hyper set.
- HnS preserved named assets are not all newly placed NPCs. The inventory separates registration from source availability.
- Pokemon regional encounter pools are only being developed in selected areas. The project has not completed a universal native-region distribution for every Pokemon.
- Natural wormholes remain off limits before the Hoenn League. Their Ultra Space events are future work even when their maps are preserved.

## Planning worksheet for each new scene

1. Where does the player arrive, and what story or Badge condition starts the scene?
2. What does each person know before speaking, and what does the player learn on screen?
3. Which exact overworld and portrait will be used? Is a back sprite needed?
4. Where do actors enter, stand, face and leave? Is there a clear return route?
5. What evidence, objective or relationship changes when the scene ends?
6. What reward is given, and what happens with a full bag, full party or full PC?
7. What happens after losing, cancelling, leaving the map, saving or revisiting?
8. Which facts are still theories? Which names should remain unknown to the player?
9. Does the new scene respect the League gate and the deferred teleport-location decision?
10. What can be manually playtested before the next chapter is written?

## Source index

The current scripts are authoritative when an older README describes an abandoned version.

- Opening and bedroom: docs/story/intro_draft1/dialogue.json; docs/story/bedroom_prologue/dialogue.json; data/scripts/legends_downstairs.inc; data/scripts/legends_nextdoor.inc
- Littleroot and Red: data/scripts/legends_littleroot_arc.inc; docs/story/birch_red_rescue/README.md; src/starter_choose.c
- Woods and Petalburg: data/maps/Hoenn_Timeless_Woods/scripts.inc; data/scripts/legends_petalburg.inc; docs/story/woods_triad/README.md
- Rustboro and Silver: docs/story/rustboro/README.md; docs/story/rustboro_silver/README.md; data/maps/RustboroCity/scripts.inc
- Dewford: data/maps/DewfordTown/scripts.inc; data/maps/Hoenn_Route_106/scripts.inc
- Museum and Rowan: data/maps/SlateportCity_OceanicMuseum_2F/scripts.inc; data/maps/Route110/scripts.inc
- Kanto crossing: data/maps/Kanto_PowerPlant_Rift/scripts.inc; data/maps/Kanto_Route10/map.json; data/maps/Kanto_PowerPlant/map.json
- Paradigm and family report: data/maps/MauvilleCity_Gym/scripts.inc; data/maps/MauvilleCity/scripts.inc; data/maps/VerdanturfTown_WandasHouse/scripts.inc
- Tracker Oak and Blue: data/scripts/legends_rift_research.inc; src/rift_tracker.c; docs/story/rift_network/registry.json
- Front and back library: docs/art/donor-portraits/manifest.json; docs/art/donor-portraits/user-labels.json; docs/art/donor-portraits/hyper-trainer-classes.csv
- Overworld library: docs/art/npc_roster/manifest.json; docs/la_world/donor_npcs/manifest.json; docs/la_world/donor_npcs/named_characters.json; assets/donor_npcs/hns/graphics/object_events/pics/people
- Complete planning inventory: docs/story/planning/character_inventory.csv and character_inventory.json

## Git snapshot

The implementation snapshot was committed as c5a0b902f1 on test/qol-first-three. This guide and its audit files are a separate documentation update so future story decisions can evolve without rewriting that implementation snapshot.
