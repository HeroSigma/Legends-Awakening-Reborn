Kanto_Route15_WestEntrance_2F_MapScripts::
	.byte 0

KantoAR_24_1_Route15_WestEntrance_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_25_0_ROUTE16_HOUSE, 4, 3
	goto KantoAR_InspectionFinish
