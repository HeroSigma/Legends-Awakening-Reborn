Kanto_FiveIsland_LostCave_Room3_MapScripts::
	.byte 0

KantoAR_2_15_FiveIsland_LostCave_Room3_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_16_FIVEISLAND_LOSTCAVE_ROOM4, 5, 5
	goto KantoAR_InspectionFinish
