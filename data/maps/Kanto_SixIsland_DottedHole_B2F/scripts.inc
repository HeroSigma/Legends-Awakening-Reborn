Kanto_SixIsland_DottedHole_B2F_MapScripts::
	.byte 0

KantoAR_1_117_SixIsland_DottedHole_B2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_118_SIXISLAND_DOTTEDHOLE_B3F, 5, 5
	goto KantoAR_InspectionFinish
