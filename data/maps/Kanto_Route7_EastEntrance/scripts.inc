Kanto_Route7_EastEntrance_MapScripts::
	.byte 0

KantoAR_19_0_Route7_EastEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_20_0_ROUTE8_WESTENTRANCE, 6, 5
	goto KantoAR_InspectionFinish
