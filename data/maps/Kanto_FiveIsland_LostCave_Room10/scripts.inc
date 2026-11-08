Kanto_FiveIsland_LostCave_Room10_MapScripts::
	.byte 0

KantoAR_2_22_FiveIsland_LostCave_Room10_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_23_FIVEISLAND_LOSTCAVE_ROOM11, 5, 5
	goto KantoAR_InspectionFinish
