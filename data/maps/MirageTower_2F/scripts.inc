MirageTower_2F_MapScripts::
	map_script MAP_SCRIPT_ON_FRAME_TABLE, CaveHole_CheckFallDownHole
	map_script MAP_SCRIPT_ON_TRANSITION, CaveHole_FixCrackedGround
	map_script MAP_SCRIPT_ON_RESUME, MirageTower_2F_SetHoleWarp
	.byte 0

MirageTower_2F_SetHoleWarp:
	setstepcallback STEP_CB_CRACKED_FLOOR
	setholewarp MAP_MIRAGE_TOWER_1F
	end


@ Project-owned reservation; registered asset map, no donor gameplay.
MirageTower_2F_EventScript_HyperConstruction_Registered1::
	lock
	faceplayer
	msgbox MirageTower_2F_Text_HyperConstruction_Registered1, MSGBOX_DEFAULT
	release
	end

MirageTower_2F_Text_HyperConstruction_Registered1:
	.string "This area is under construction.\p"
	.string "Please check back later!$"
