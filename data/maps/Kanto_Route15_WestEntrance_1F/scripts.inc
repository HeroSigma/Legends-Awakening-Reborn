Kanto_Route15_WestEntrance_1F_MapScripts::
	.byte 0

KantoAR_24_0_Route15_WestEntrance_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_24_1_ROUTE15_WESTENTRANCE_2F, 6, 5
	goto KantoAR_InspectionFinish
