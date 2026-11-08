Kanto_FiveIsland_LostCave_Room7_MapScripts::
	.byte 0

KantoAR_2_19_FiveIsland_LostCave_Room7_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_20_FIVEISLAND_LOSTCAVE_ROOM8, 5, 5
	goto KantoAR_InspectionFinish
