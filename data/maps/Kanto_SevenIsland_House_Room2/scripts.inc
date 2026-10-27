Kanto_SevenIsland_House_Room2_MapScripts::
	.byte 0

KantoAR_31_1_SevenIsland_House_Room2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_31_2_SEVENISLAND_MART, 5, 4
	goto KantoAR_InspectionFinish
