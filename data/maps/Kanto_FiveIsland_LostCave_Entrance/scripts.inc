Kanto_FiveIsland_LostCave_Entrance_MapScripts::
	.byte 0

KantoAR_2_12_FiveIsland_LostCave_Entrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_13_FIVEISLAND_LOSTCAVE_ROOM1, 5, 5
	goto KantoAR_InspectionFinish
