# Project working instructions

## Release ROM policy

User instruction: use ONE permanent playable release file:
C:/Users/aadair/Downloads/Legends-Awakening-Reborn/Legends-Awakening-Reborn.gba
(WSL: /mnt/c/Users/aadair/Downloads/Legends-Awakening-Reborn/Legends-Awakening-Reborn.gba).

After a requested rebuild, replace this ROM in place. Do not create a new version-named ROM or release folder for routine updates. Preserve its paired Legends-Awakening-Reborn.sav; never overwrite, delete or reset it during packaging. The initial migration may copy the previous RTC-Friendly-Intro battery save only if the permanent save does not exist. Existing archival ROMs remain untouched.

## Protagonist dialogue

Aren and Aria are speaking protagonists. In story conversations, give the player spoken questions, responses and decisions using SP_NAME_PLAYER and their chosen name. Internal thoughts are occasional characterization, not a substitute for participation. NPCs should respond to what the player actually says instead of inferring an unspoken request. Preserve existing story flags, rewards and scene gates when improving dialogue unless a progression change is explicitly needed.

Use the established dialogue colors: player LIGHT_BLUE, Brendan GREEN, May/Red RED, Wally LIGHT_GREEN. The field message renderer supplies these defaults from the active speaker; explicit script color controls remain supported. Researcher/narrator dialogue uses the normal readable color.
