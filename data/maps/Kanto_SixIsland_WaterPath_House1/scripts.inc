Kanto_SixIsland_WaterPath_House1_MapScripts::
	.byte 0

KantoAR_41_0_SixIsland_WaterPath_House1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_41_1_SIXISLAND_WATERPATH_HOUSE2, 4, 3
	goto KantoAR_InspectionFinish
