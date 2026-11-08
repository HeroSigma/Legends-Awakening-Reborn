# Fly-gated low flight

On a supported flying mount, B toggles takeoff and landing after the existing Fly unlock and field-move eligibility are satisfied. The rider rises 12 pixels and the mount animates while hovering. L+R and Recall require landing first. Menus preserve height and the correct protagonist. Indoors, invalid mounts and scripted scenes can safely land the player.

This is bounded low flight: native route collision, objects, walls, ledges, water access and story triggers are unchanged. It does not enable free-flight collision exemptions or let a flying land mount enter water without native Surf. World-map Fly travel remains the existing system with its own destination gates. Supported swimming/flying mounts can take off while surfing once both Surf and Fly are permitted; landing over water retains the water mount and offshore dismount remains blocked.

No avatar flags or save fields are repurposed. Air mode and height are temporary runtime state; saving occurs at the unchanged legal tile position. Climbing and reverse-ledge traversal remain disabled pending story progression rules.

Validation: 52 native aerial checks across both protagonists/storage modes, Fly rejection before unlock, actual B takeoff/landing, unchanged position and movement flags, movement on open paths, wall collision preserved in air, dismount/switch refusal aloft, menu return, gender, saving and indoor landing. Final regression also passes 74 water checks (including swimming/flying mounts), 96 ground checks, 28 protagonist/summary checks and 446 Start menu checks. All test saves are isolated.
