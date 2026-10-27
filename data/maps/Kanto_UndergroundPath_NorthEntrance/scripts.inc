Kanto_UndergroundPath_NorthEntrance_MapScripts::
	.byte 0

KantoAR_1_30_UndergroundPath_NorthEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_31_UNDERGROUNDPATH_NORTHSOUTHTUNNEL, 4, 31
	goto KantoAR_InspectionFinish
