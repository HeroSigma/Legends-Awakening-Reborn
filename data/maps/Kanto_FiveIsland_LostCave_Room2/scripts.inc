Kanto_FiveIsland_LostCave_Room2_MapScripts::
	.byte 0

KantoAR_2_14_FiveIsland_LostCave_Room2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_15_FIVEISLAND_LOSTCAVE_ROOM3, 5, 5
	goto KantoAR_InspectionFinish
