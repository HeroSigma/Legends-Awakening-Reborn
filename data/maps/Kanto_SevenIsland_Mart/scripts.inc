Kanto_SevenIsland_Mart_MapScripts::
	.byte 0

KantoAR_31_2_SevenIsland_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_31_3_SEVENISLAND_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
