Kanto_Route5_MapScripts::
	.byte 0

KantoAR_3_23_Route5_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_24_ROUTE6, 12, 20
	goto KantoAR_InspectionFinish
