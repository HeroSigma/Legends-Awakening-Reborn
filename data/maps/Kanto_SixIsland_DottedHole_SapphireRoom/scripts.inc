Kanto_SixIsland_DottedHole_SapphireRoom_MapScripts::
	.byte 0

KantoAR_1_120_SixIsland_DottedHole_SapphireRoom_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_121_SIXISLAND_PATTERNBUSH, 55, 16
	goto KantoAR_InspectionFinish
