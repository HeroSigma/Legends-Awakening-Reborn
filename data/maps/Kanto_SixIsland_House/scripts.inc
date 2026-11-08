Kanto_SixIsland_House_MapScripts::
	.byte 0

KantoAR_37_3_SixIsland_House_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_37_4_SIXISLAND_MART, 5, 4
	goto KantoAR_InspectionFinish
