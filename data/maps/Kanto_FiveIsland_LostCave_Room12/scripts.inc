Kanto_FiveIsland_LostCave_Room12_MapScripts::
	.byte 0

KantoAR_2_24_FiveIsland_LostCave_Room12_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_25_FIVEISLAND_LOSTCAVE_ROOM13, 5, 5
	goto KantoAR_InspectionFinish
