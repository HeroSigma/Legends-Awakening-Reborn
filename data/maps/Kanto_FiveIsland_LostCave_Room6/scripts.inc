Kanto_FiveIsland_LostCave_Room6_MapScripts::
	.byte 0

KantoAR_2_18_FiveIsland_LostCave_Room6_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_19_FIVEISLAND_LOSTCAVE_ROOM7, 5, 5
	goto KantoAR_InspectionFinish
