# Giovanni's alliance — canon and reveal order

Giovanni united the villain factions before the current story. Their different
research methods and personal ambitions contribute to one coordinated operation.
This supersedes any earlier planning suggestion that Aqua and Magma investigate
independently or oppose Giovanni/Cyrus.

## Completed-scene corrections

- Timeless Woods: MAN IN SUIT and BLUE-HAIRED MAN replace named speaker boxes.
  Their exchange establishes that several teams supply data and are keeping their
  operations quiet. Neither name is spoken here.
- Petalburg Woods: the Shadow Triad takes the Scope images for Command to calibrate
  the recovered device. It is an allied assignment.
- Slateport museum: Archie's offshore measurements form part of a larger operation.
  He retains his own voice and motives; his crew's loyalty to him is unchanged.
- Kanto Power Plant: after the player agrees to shut down the reactor, Rocket
  Control interrupts over the station radio. It cites Giovanni's orders and says
  the other teams await the readings. The player and Wattson answer; Control tries
  to stop the shutdown. The player cuts the channel and shuts down the reactor.
  Miraidon's uncatchable level-70 encounter, healing, Wattson's left exit, Wally's
  disappearance, and all original rescue progression remain intact.
- Mauville Paradigm call: only if the transmission was heard, the player reports
  Giovanni's name. Birch connects it to Norman's description; Rowan recognizes a
  shared operation. The full coalition roster and Cyrus's identity remain unrevealed.
- Timeless Woods return: the scout guards their transport route rather than
  pursuing Giovanni/Cyrus as enemies. A player who heard the transmission can ask
  about Giovanni by name; older completed-rescue saves retain the R/G description.
- Tracker lead: describes a scout guarding their route.

## Persistent knowledge and compatibility

FLAG_LA_HEARD_GIOVANNI (0x26C) records the completed transmission.
It is set after the radio exchange, before the native shutdown continues.
Declining the console does not set it. Subsequent console visits do not repeat it.
The Paradigm report and Woods question use the flag rather than assuming knowledge.
Existing completed-rescue saves are not rewound and their battle/reward flags are
not changed. All current menus, quests and storage changes are retained.

Anonymous speakers retain Rocket crimson and Galactic violet via the central
speaker-color table. ROCKET CONTROL has no Giovanni portrait: this is a radio
operator reporting his orders, not an early face-to-face meeting with Giovanni.

## Ashes and Echoes planning constraint — not implemented yet

Magma's geothermal amplification supports the alliance's device calibration.
Aqua's equipment and offshore readings support the same work. Archie may supervise
a handoff or the summit operation; he must not arrive as Magma's independent enemy.
The shared plan can coexist with rivalry over methods and credit.
The next chapter should reveal additional roles gradually, not list every villain
during this first transmission.
