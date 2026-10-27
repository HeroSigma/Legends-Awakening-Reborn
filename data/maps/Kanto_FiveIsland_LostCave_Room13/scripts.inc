Kanto_FiveIsland_LostCave_Room13_MapScripts::
	.byte 0

KantoAR_2_25_FiveIsland_LostCave_Room13_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_26_FIVEISLAND_LOSTCAVE_ROOM14, 5, 5
	goto KantoAR_InspectionFinish
