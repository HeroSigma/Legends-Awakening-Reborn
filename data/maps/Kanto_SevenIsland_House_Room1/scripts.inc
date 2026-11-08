Kanto_SevenIsland_House_Room1_MapScripts::
	.byte 0

KantoAR_31_0_SevenIsland_House_Room1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_31_1_SEVENISLAND_HOUSE_ROOM2, 6, 4
	goto KantoAR_InspectionFinish
