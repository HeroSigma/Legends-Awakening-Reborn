Kanto_UndergroundPath_WestEntrance_MapScripts::
	.byte 0

KantoAR_1_33_UndergroundPath_WestEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_34_UNDERGROUNDPATH_EASTWESTTUNNEL, 40, 3
	goto KantoAR_InspectionFinish
