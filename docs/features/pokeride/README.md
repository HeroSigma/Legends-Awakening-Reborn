# Ground PokeRide

After Running Shoes, choose a healthy supported Pokemon in Party -> Follower -> Ride outdoors. L+R dismounts. Recall also dismounts. Follower remains under Field Skills when the main party menu is full.

Uses seated Brendan/May art and donor positioning data. The normal follower hides while mounted; its preference is preserved. Ground travel uses native foot collision and running-speed movement. Obstacles, trainers, one-way ledges, water and story gates remain authoritative. Native Surf, Fly and Dive remain unchanged. Donor free-flight, swimming and reverse-ledge-climbing controls are not enabled in this ground integration.

Eggs, fainted/unsupported Pokemon, indoor maps, bikes, Surf, Dive and NPC travel partners cannot start a ride. Scripted scenes and entering buildings dismount. Sprite resets safely recreate mounts after menus and battles. Save structures are unchanged; booting a save starts on foot. The native underwater flag remains intact.

Credits: Aio Silver and Lucky Capybara, EE-Ride-System ride-system branch dbca61f7; originally derived from Pokabbie's Emerald Rogue. Imported riding art and species positioning; adapted rendering, movement and lifecycle for Reborn. Seated sheets convert as separate 16x32 frames.
https://github.com/silversisama/EE-Ride-System/tree/ride-system

Validation: 96 native ride checks across both protagonists and storage modes, real party-menu selection, eligibility gates, movement, switching, menu returns, dismount/control release, indoor dismount, wild battle escape/return, and saving while mounted. Also passed 44 follower, 48 identity and 446 Start menu regressions. All tests use isolated saves.

Current extensions: [Water mounts](../pokeride-water/README.md) and [Fly-gated low flight](../pokeride-air/README.md). The ground integration above is retained as the foundation; native Surf now supports water mounts and eligible flying mounts can toggle bounded low flight.
