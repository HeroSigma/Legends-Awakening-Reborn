Kanto_SixIsland_RuinValley_MapScripts::
	.byte 0

KantoAR_3_61_SixIsland_RuinValley_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_62_SEVENISLAND_TRAINERTOWER, 58, 15
	goto KantoAR_InspectionFinish
