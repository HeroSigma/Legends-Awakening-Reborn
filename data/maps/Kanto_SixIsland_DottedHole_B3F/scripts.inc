Kanto_SixIsland_DottedHole_B3F_MapScripts::
	.byte 0

KantoAR_1_118_SixIsland_DottedHole_B3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_119_SIXISLAND_DOTTEDHOLE_B4F, 5, 5
	goto KantoAR_InspectionFinish
