Kanto_FiveIsland_LostCave_Room8_MapScripts::
	.byte 0

KantoAR_2_20_FiveIsland_LostCave_Room8_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_21_FIVEISLAND_LOSTCAVE_ROOM9, 5, 5
	goto KantoAR_InspectionFinish
