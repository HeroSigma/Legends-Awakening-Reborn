Kanto_FiveIsland_LostCave_Room5_MapScripts::
	.byte 0

KantoAR_2_17_FiveIsland_LostCave_Room5_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_18_FIVEISLAND_LOSTCAVE_ROOM6, 5, 5
	goto KantoAR_InspectionFinish
