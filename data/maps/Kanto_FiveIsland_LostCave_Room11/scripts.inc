Kanto_FiveIsland_LostCave_Room11_MapScripts::
	.byte 0

KantoAR_2_23_FiveIsland_LostCave_Room11_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_24_FIVEISLAND_LOSTCAVE_ROOM12, 5, 5
	goto KantoAR_InspectionFinish
