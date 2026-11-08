# Competitive trainer rules

After the National Dex gift, all 845 populated normal trainer entries in the active registry use six-member competitive teams. This includes ordinary trainers, rivals, villains, Gym Leaders, the Elite Four, the Champion and registered rematches. The four approved Route 102 teams remain intact.

Seventeen entries are protected: the empty trainer, seven scripted early Red/rival tutorial/partner teams, two art placeholders and seven Frontier facility identities. Frontier uses its own team/rules system. Unpopulated regional NPC placeholders are not turned into battles. This does not import or activate any donor story system.

## Team identity and legality

Teams are fixed by trainer identity and specialty, with native signature Pokémon retained for ordinary trainers and authored specialist cores filling out their teams. Weather cores support rain, sun, sand or snow; other cores cover balance, recovery/status and Trick Room. There is no random species bag. The editable authoring source is tools/la_world/author_competitive_trainers.py; the generated profile manifest records every covered and protected entry.

Runtime party construction resolves legal evolutionary stages for the actual encounter level. Move preferences select only moves supported by this project's level-up, teachable or egg learnsets. Sets use STAB, appropriate attack categories, coverage, recovery/status or setup. Doubles choices add Protect and available speed control/redirection/support, and avoid selecting indiscriminate friendly-fire coverage. Species with genuinely limited movepools may retain empty trailing move slots.

Every Pokémon has six 31 IVs and a legal 508-point EV spread, with a matching nature and useful held item. Trick Room attackers use HP/investment and a Speed-lowering nature while retaining the requested perfect IVs. Trainers have at least two usable healing items; their gimmick held item is separate. Major characters have exactly one guaranteed shiny, their last/signature Pokémon. Ordinary trainers have no guaranteed shiny.

Each trainer gets one supported Tera or Z-Move user. The choice derives from player Trainer ID and opponent identity; resetting or changing battle format does not reroll it. The selected Pokémon has a compatible attack, and other members cannot use another gimmick. Mega/Dynamax variants are not added by this ruleset.

The existing native Smart AI handles switching, viability, setup and battle choices. These are themed competitive RPG teams, not a claim of optimal play in every matchup or enforcement of all official VGC tournament clauses.

## Progression and format

Party experience and Rare Candy caps activate after receiving the Dex: Roxanne 16, Brawly 20, Wattson 26, Flannery 32, Norman 37, Winona 43, Tate and Liza 49, Juan 56, League 65. All trainer parties stay at or below the current cap. Ordinary route levels retain their progression tier; leader rematches can rise to the current cap. Later regional badge caps await their story progression; after Champion the current party cap is 100.

Wild scaling still caps at the next Gym/League opponent's lowest member level, now read from the active competitive roster rather than obsolete native levels. It remains distinct from the player's next-ace cap. Encounter locations, time-of-day themes and no-encounter maps are unchanged.

Gym Leaders and League opponents ask for Singles or Doubles before an eligible fight, including rematches. Yes selects Doubles and No/B selects Singles. With fewer than two able Pokémon, the game explains the requirement and uses Singles. Both formats retain the original victory, badge, reward, defeat and story continuation scripts. Story battles retain their intended format; story-specific early Red/partner teams are protected.

## Verification and testing

Native mGBA tests construct all 845 teams at caps 16, 20, 26, 32, 37, 43, 49, 56, 65 and 100. They check move/evolution/EV/ability legality, cap compliance, pre-Dex preservation and protected entries. Actual generated parties verify IVs and shiny aces in both 14-box and 60-box modes. Format tests exercise real menu input, Singles/Doubles battle initialization, Tate and Liza Singles, one-Pokémon fallback, native gimmick eligibility and the normal badge continuation after a simulated victory. Combat AI performance itself is not exhaustively proven by these checks.

Use the permanent Legends-Awakening-Reborn.gba with its existing battery save. Receiving the Dex enables these rules. Already-defeated trainers are not reset. No new save fields or save reset are required. Player battery files are never opened by the test runner.
