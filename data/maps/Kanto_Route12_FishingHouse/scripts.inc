Kanto_Route12_FishingHouse_MapScripts::
	.byte 0

KantoAR_23_2_Route12_FishingHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_24_0_ROUTE15_WESTENTRANCE_1F, 6, 6
	goto KantoAR_InspectionFinish
