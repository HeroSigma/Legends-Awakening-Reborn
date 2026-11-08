Kanto_FiveIsland_LostCave_Room9_MapScripts::
	.byte 0

KantoAR_2_21_FiveIsland_LostCave_Room9_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_22_FIVEISLAND_LOSTCAVE_ROOM10, 5, 5
	goto KantoAR_InspectionFinish
