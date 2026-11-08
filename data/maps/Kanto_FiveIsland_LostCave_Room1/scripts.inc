Kanto_FiveIsland_LostCave_Room1_MapScripts::
	.byte 0

KantoAR_2_13_FiveIsland_LostCave_Room1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_14_FIVEISLAND_LOSTCAVE_ROOM2, 5, 5
	goto KantoAR_InspectionFinish
