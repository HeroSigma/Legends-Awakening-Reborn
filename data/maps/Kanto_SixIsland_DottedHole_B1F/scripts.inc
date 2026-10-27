Kanto_SixIsland_DottedHole_B1F_MapScripts::
	.byte 0

KantoAR_1_116_SixIsland_DottedHole_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_117_SIXISLAND_DOTTEDHOLE_B2F, 5, 5
	goto KantoAR_InspectionFinish
