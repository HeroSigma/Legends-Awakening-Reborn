Kanto_SixIsland_PatternBush_MapScripts::
	.byte 0

KantoAR_1_121_SixIsland_PatternBush_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_122_SIXISLAND_ALTERINGCAVE, 17, 12
	goto KantoAR_InspectionFinish
