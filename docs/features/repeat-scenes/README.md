# Repeat battle conversations

Repeat-only conversation skipping for Route 103's Brendan/May/Red meeting, the Petalburg Woods Triad introduction and the Rusturf Tunnel grunt introduction. First visits play normally. After an introduction reaches its battle boundary, later attempts offer “You've seen this conversation. Skip to the battle?” Yes takes the short path; No or B keeps the full scene.

The approach follows HashtagMarky's Basic Cutscene Skipping reference (https://github.com/HashtagMarky/pokeemerald/tree/dev-cutscene-skipping, e243824): persistent viewed flags and authored skip destinations. It uses the project's native script/yes-no system rather than importing a global input task or interrupting active movement. There are no new sprites, options or save-layout fields. Existing saves begin with these previously unused flags unset.

Each shortcut rejoins the original script before its mandatory battle. Opponents, partner, battle format, healing and loss handling remain unchanged. First-time post-battle dialogue and rewards always play. The Woods path fades out briefly and restores the exact Devon, Silph and Triad positions and facings before combat. The three viewed flags are distinct from completion, theft and reward flags, and are set only after the full introduction has been seen. They survive normal save/load and a loss, allowing a retry without the repeated conversation.

The feature is opt-in per scene. Other scenes retain their current behavior. This pass covers the existing replayable early-story battle introductions; completed one-time scenes do not gain replay or extra rewards.

Native tests use disposable saves. Coverage includes first visits, watching again, skipping, both storage modes, correct Woods staging, mandatory battle entry and format, no early rewards, completion/reward parity, restored controls and saved viewed flags. Native battle end handlers inject outcomes for state/reward tests; combat difficulty is not inferred from those fixtures. Existing Woods loss/retry and full Route 103 battle tests provide additional regression coverage.
