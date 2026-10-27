Kanto_SixIsland_DottedHole_1F_MapScripts::
	.byte 0

KantoAR_1_115_SixIsland_DottedHole_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_116_SIXISLAND_DOTTEDHOLE_B1F, 5, 5
	goto KantoAR_InspectionFinish
