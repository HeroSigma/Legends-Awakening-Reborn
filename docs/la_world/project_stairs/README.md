# Project stair behavior pass

Implemented: restore 71 vertical stair definitions in 30 tilesets from preserved FireRed-source MB_ROCK_STAIRS metadata; restore another 102 definitions in 25 tilesets by exact graphics/layer/flip matching against five manually reviewed Hoenn stair graphics. These counts include some definitions in unused asset banks. Non-normal behaviors, warp stairs, ladders, original artwork and existing map geometry are preserved. Five importers now retain native MB_ROCK_STAIRS in future imports.

The previously tested Accumula full-sheet collision/elevation data is now in its existing registered test slot in the main source project. Its vertical stair passage also has native vertical stair animation behavior, while the lower staircase retains diagonal movement, side guards and separate land elevations. The main playable release ROM is not replaced.

Coverage: all 2686 registered map definitions resolve to tileset attributes; the resulting data inventory contains 1922 tagged stair cells in 229 maps. This is a data inventory, not a claim that every staircase was visually reviewed or walked. Existing sideways stair definitions are preserved, rather than assigning diagonal movement to ordinary horizontal paths. Ordinary floor artwork that visually resembles stairs remains unclassified; no whole-map height rewrites were guessed.

Validation: successful build, 713 valid registered tileset formats, Python syntax checks, linked override-byte checks for emitted arrays, native mGBA vertical movement and return in Route105 and HnSTest_NewBarkTown, native sideways descent in HnSTest_Route31, full Accumula lower-stair ascent/descent, zero full-sheet stream failures. No full-region gameplay regression or every-map walkthrough has been completed.

Review still required: custom/unlabelled stair artwork; land-height authoring on maps whose landings currently share elevations; follower-specific stair pacing; representative movement on other regions and map variants. Kanto_IndigoPlateau_Exterior loaded black in the direct-warp harness, and Johto_Olivine_City_Section_01 failed to load correctly in that harness. They are not counted as passed, and these load failures have not been diagnosed as pre-existing versus introduced. Their map geometry and original stair definitions were not edited. See runtime_validation.json for the checks that actually passed.

Test ROM: C:/Users/aadair/Downloads/Legends-Awakening-Reborn/Legend Test.gba. Restart the emulator after replacing it; old emulator states and saved map-view cells may retain previous collisions. Main release ROM and both existing battery saves are preserved during packaging.

Backups of changed existing source files are under /home/allan/projects/Legends-Awakening-Reborn/.la_work/project_stairs_backup. Attribute overrides and restoration ledgers are under data/project_stairs and docs/la_world/project_stairs. The read-only auditor is tools/la_world/audit_project_stairs.py.
