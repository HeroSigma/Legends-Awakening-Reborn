# Pokemon Center setup in collection mode

The broad activity-name gate intercepted InitUnionRoom on ordinary Pokemon Center resume scripts and SetLilycoveLadyGfx during Lilycove transition setup. This displayed the unavailable-activity message during normal map entry.

Allow InitUnionRoom, SetLilycoveLadyGfx and Script_GetLilycoveLadyId as supporting setup/identity routines. Actual Union Room entry and contest gameplay specials remain blocked. The generator preserves this explicit exception when regenerated.

Validation: ROM build and 713-tileset format check passed; 58 isolated map-initializer assertions across both storage modes and all three Lilycove Lady variants passed; 2,202 production storage/menu/save assertions passed. Tests use isolated emulator flash and do not open the player's save.
