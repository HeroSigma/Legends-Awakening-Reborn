Kanto_UndergroundPath_SouthEntrance_MapScripts::
	.byte 0

KantoAR_1_32_UndergroundPath_SouthEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_33_UNDERGROUNDPATH_WESTENTRANCE, 8, 5
	goto KantoAR_InspectionFinish
