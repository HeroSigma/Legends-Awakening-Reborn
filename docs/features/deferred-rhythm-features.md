# Deferred Rhythm-inspired features

User priority recorded 2026-10-29: finish the original feature list before starting any of the features below. Inspection is complete only at the preliminary level; these are not implemented or authorized to jump ahead of the original work.

Current original-list milestone: Sword & Shield party menu completed. Sword & Shield storage interface is the next proposed UI milestone and must preserve both normal and compact 60-box storage. Continue the remaining original feature work before returning to this backlog.

## Deferred backlog

1. Wild double battles in selected areas, requiring two usable Pokemon.
2. Regional swarms / mass outbreaks, with announcements.
3. Dynamic regional weather, preserving scripted weather and story gates.
4. Hidden Grottos, with encounter/reward pools and regeneration rules to be designed.
5. Dynamax raids: raid bosses, shields, partner handling, post-victory capture, rewards and reset tracking.
6. Pokemon World Tournament as the planned Battle Frontier replacement, with recognizable trainers, bracket progression and existing competitive team rules. Final formats and level rules remain to be designed for our game.

This ordering is a preliminary recommendation, not a locked design. Rhythm is a reference, not a direct FireRed-code transplant into Emerald.

## Inspection notes

Supplied reference: C:/Users/aadair/Downloads/Pokemon Rhythm Release v1.1.1 (v1.1.1).gba (the actual supplied filename uses accented Pokemon). SHA256 e6fe880d1c0dd5dcebed3ad4f1ac3bd5fd97d115b34c444bf746b96baa9e0887.

Rhythm ROM text describes raid pillars, partners, rewards, post-victory catching and a Wish Piece reset service. Its World Tournament dialogue describes three selected Pokemon at level 100, three qualifiers and a 16-trainer bracket. Those are reference-game dialogue findings, not adopted rules. Exact raid shield counts, turn limits, reward odds, swarm schedules, grotto regeneration and weather probabilities have not been runtime verified.

Our project already has ordinary Dynamax/Max Moves, wild-double support (random chance currently zero), mass-outbreak infrastructure and daily weather cycling. These foundations do not mean the deferred features are complete. Detailed local inspection: .la_work/rhythm-inspection/report.md and accompanying extracted-text reports.

Creator release reference: https://www.reddit.com/r/PokemonROMhacks/comments/1xearcg/pok%C3%A9mon_rhythm_official_release_v100/


## Saved raid approach — 2026-11-07

User requested saving the completed reference review. Prefer native Expansion
integration using PR 10319 for newer battle hooks and PR 2869 for presentation,
partner selection and post-win capture references. Both are closed, unmerged WIP;
neither is ready for wholesale merging. CFRU remains a mechanics reference.
Start with an isolated player-plus-NPC versus single-boss Max Raid and validate
combat, shields, partner replacement, capture/rewards and cleanup before den
placement. This remains a future feature; saving research does not enable raids.

Review: [Expansion PR comparison](raids/expansion-pr-review.md) and
[CFRU feasibility](raids/cfru-feasibility.md). Free static EWRAM and free runtime
heap are different budgets and must be measured separately.
