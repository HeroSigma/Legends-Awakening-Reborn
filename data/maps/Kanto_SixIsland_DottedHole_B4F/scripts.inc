Kanto_SixIsland_DottedHole_B4F_MapScripts::
	.byte 0

KantoAR_1_119_SixIsland_DottedHole_B4F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_120_SIXISLAND_DOTTEDHOLE_SAPPHIREROOM, 8, 7
	goto KantoAR_InspectionFinish
