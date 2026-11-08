Kanto_FourIsland_MapScripts::
	.byte 0

KantoAR_3_15_FourIsland_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_16_FIVEISLAND, 12, 10
	goto KantoAR_InspectionFinish
