Kanto_FiveIsland_LostCave_Room4_MapScripts::
	.byte 0

KantoAR_2_16_FiveIsland_LostCave_Room4_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_17_FIVEISLAND_LOSTCAVE_ROOM5, 5, 5
	goto KantoAR_InspectionFinish
