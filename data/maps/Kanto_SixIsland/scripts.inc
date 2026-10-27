Kanto_SixIsland_MapScripts::
	.byte 0

KantoAR_3_18_SixIsland_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_19_ROUTE1, 12, 18
	goto KantoAR_InspectionFinish
