Kanto_SixIsland_WaterPath_House2_MapScripts::
	.byte 0

KantoAR_41_1_SixIsland_WaterPath_House2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_42_0_SEVENISLAND_SEVAULTCANYON_HOUSE, 4, 3
	goto KantoAR_InspectionFinish
