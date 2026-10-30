# Sword & Shield party menu

Ports Montblanc / montmoguri's swsh_party_menu at 440043c9 to the current Legends Awakening Reborn engine. Source: https://github.com/montmoguri/pokeemerald-expansion/wiki/Sword-%26-Shield-Party-Menu . The donor credits RavePossum, Kasen, hedara, Archie, ShantyTown and Doodle; retain their upstream credits.

The six-slot list, large selected Pokemon, move/ability preview, held item actions, party switching and battle selection use the donor presentation. Red accent shades are replaced by the teal shades from our installed SwSh summary. Field skills, preferred follower (all six slots), Ride, Recall and Automatic remain available. Field skill pages contain at most five skills plus Follower/Next/Back to fit eight actions. Long field menus expose companions through Field Skills.

The existing bag, item effects, level/EV caps and party identities remain authoritative. Shared training limit/effect functions moved into training_items.c so the old menu remains buildable behind the configuration switch. SwSh quantity selection uses those limits, including partial final EV gains and candy caps. The native summary and its Tera display/relearning stay in place. PC access remains at Pokemon Centers. Shadows are disabled because this engine's animation API does not have the donor shadow task; normal Pokemon animation remains enabled.

No save format or map changes. EWRAM 261376/262144 bytes; ROM 32722568/33554432 bytes. Tests use isolated emulator saves only.

## Validation

687 native checks on one ROM hash: 50 party checks (six follower slots, reordering, summary, held items, eggs/fainted display and both storage modes), 16 real wild-battle selection/cancel/switch checks, 79 bulk training checks, 96 ground-ride checks and 446 Start-menu lifecycle checks. Pinned reports and screenshots are in this folder. Storage remains 14 or 60 boxes according to the existing option.
