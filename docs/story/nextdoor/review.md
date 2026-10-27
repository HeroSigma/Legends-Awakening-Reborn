# Next-door story sequence

Hazel is Birch's wife. Brendan and May are both introduced as his children and
field assistants, regardless of the player's gender. Each becomes a future
rival: Brendan is inquisitive and competitive; May cares about the displaced
Pokémon and is equally ready to battle.

The conversation follows Elara's downstairs report. It acknowledges the rifts,
non-native sightings and Colress's research coordination without explaining
Elara's history, Caelum or the mysterious package. No time-of-day greeting is used.

The next objective is Birch's lab, then the path north to Route 101. The scene
sets the native rival introduction and Littleroot progression states so the
existing Birch rescue/starter flow remains available. No battle, reward,
starter, badge, encounter or interregional travel unlock occurs here.

## State
- FLAG_LA_MET_BRENDAN_AND_MAY: persistent completion, existing unused flag 0x29.
- FLAG_HIDE_LA_NEXTDOOR_RIVALS: temporary actor visibility, existing unused 0x2A.
- Native FLAG_MET_RIVAL_MOM and relevant house state advance to 2.
- Native VAR_LITTLEROOT_RIVAL_STATE advances to 3; town state advances to 1.
- VAR_TEMP_3 schedules a preview-save resume; VAR_TEMP_4 distinguishes entrance
  staging from an arbitrary-position resume. No persistent save fields are added.

New games use Hazel's existing entrance approach, followed by both rivals joining
the conversation. Previously greeted pre-Birch saves receive the scene on their
next visit, without relocating the player or applying entrance-only movements.
Completed saves do not replay it. Saves already past Birch's rescue are not
rewound to force this introduction.

## Actors and maps
Only the two existing canonical Littleroot house 1F files gain objects; no groups,
map identities, layouts or registries change. Both houses contain the same two
named actor roles, with visibility restricted to the correct next-door house.
The player’s own house never displays them.

Actor paths were checked against the current layout's collision cells. Brendan
uses x4 in May's house / x6 in Brendan's house; May uses x5. Both start at y5. Hazel steps aside; Brendan approaches the player from the side and May from above. Departure paths lead to the real stairs and front door.
Ground-floor scene actors disappear after departing. The resident rival appears upstairs and walks through the upper aisle to the PC on the first visit; later visits keep that PC position.
Native upstairs first-meeting variants and Poké Ball triggers stay suppressed, but the appropriate native bedroom rival is visible at the PC.

Hazel, Brendan, May and the player use the project nameboxes. Every authored text
page fits two lines; no third-line scroll splits a sentence.

This change introduces both rivals. Later Route 103 and other native rival
battles still use Emerald's existing active-rival selection and can be authored
as the story reaches those scenes.



## Restaging update
Brendan's authored dialogue is green and May's is red, including the upstairs
follow-up interactions. Both use the existing Ruby/Sapphire overworld art.
Native normal rival graphics pointers also use that art; player art is unchanged.

For Aren, May goes upstairs and Brendan leaves. For Aria, May leaves and Brendan
goes upstairs. Paths use the real stair/door tiles, avoid the player and Hazel,
and the upstairs path uses the upper aisle rather than the bed footprint.

FLAG_LA_RIVAL_SETTLED_AT_PC uses existing unused flag 0x2B to prevent the upstairs
walk replaying. Previously completed introductions reconcile to this state on a
later visit without repeating the conversation. Arbitrary-position preview
resumes use safe actor removal instead of walking through the saved player.

Final validation: 84 next-door checks passed, including Ruby graphics pointers, adjacent approach positions, departures, PC arrival, PC save/Continue persistence, both genders and preview-save resumes. Bedroom: 42 checks. Intro: 5. Wild pools: 59. All reports match the final ROM.
