# Evil-team dialogue colors

Ordinary field dialogue uses a faction foreground while retaining the existing namebox, border and shadow. Current named speakers map to their affiliation: Giovanni to Rocket, Cyrus to Galactic, Shadow Triad to Plasma, and Aqua Grunt to Aqua.

| Faction | Color | Script speaker |
| --- | --- | --- |
| Rocket | Crimson | SP_NAME_TEAM_ROCKET |
| Aqua | Deep blue | SP_NAME_TEAM_AQUA |
| Magma | Burnt orange | SP_NAME_TEAM_MAGMA |
| Galactic | Violet | SP_NAME_TEAM_GALACTIC |
| Plasma | Steel blue | SP_NAME_TEAM_PLASMA |
| Flare | Scarlet | SP_NAME_TEAM_FLARE |
| Skull | Charcoal | SP_NAME_TEAM_SKULL |
| Yell | Magenta | SP_NAME_TEAM_YELL |
| Star | Dark gold | SP_NAME_TEAM_STAR |
| Aether Foundation | Teal | SP_NAME_AETHER_FOUNDATION |

For future scenes, set the matching speaker before the message and restore SP_NAME_NONE after the conversation. Generic faction speakers are available now; this does not automatically identify untagged legacy dialogue or add new story encounters. Named members can be added to the central affiliation table as scenes are written. Explicit authored color controls take priority. Existing speaker IDs and save data are unchanged.

A single dynamic text foreground slot is loaded after each message-frame palette, so successive factions and neutral dialogue do not inherit stale colors. The native speaker-color test checks every affiliation and existing character defaults; screenshots show current story speakers.
