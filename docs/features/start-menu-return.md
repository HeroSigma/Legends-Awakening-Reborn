# Start menu return regression

The reported return to the intro was reproduced by loading an emulator save state made before subsequent ROM rebuilds. The stored main callback was 0x08168581; in the current ROM that address is inside SetWarpDestinationToFixedHoleWarp, not a valid main callback. Advancing that state entered CB2_InitCopyrightScreenAfterBootup and CB2_ExpansionIntro, matching the report.

Emulator save states retain RAM, executable callback addresses and tasks from their original build. They are not portable between these rebuilt ROMs. Use the game's battery save and Continue after updating the ROM; make new emulator states only after that normal load. Keep the ROM's permanent filename and preserve the paired battery save.

The outdated slot was preserved with a .pre-update-backup suffix so Quick Load cannot select it accidentally. No battery-save bytes or ROM code were changed for this investigation.

The native mGBA regression uses an isolated new-game battery. It covers all 16 combinations of menu unlocks, direct B/Start exits, returns from Pokedex, Pokemon, Bag, trainer card and Options, rapid repeated B input, and Journal exits in both 14-box and 60-box modes. All 288 assertions passed. The test never loads or writes the player's battery save.
