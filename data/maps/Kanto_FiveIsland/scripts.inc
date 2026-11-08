Kanto_FiveIsland_MapScripts::
	.byte 0

KantoAR_3_16_FiveIsland_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_17_SEVENISLAND, 9, 10
	goto KantoAR_InspectionFinish
