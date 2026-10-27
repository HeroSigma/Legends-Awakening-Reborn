Kanto_Route8_WestEntrance_MapScripts::
	.byte 0

KantoAR_20_0_Route8_WestEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_21_0_ROUTE10_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
