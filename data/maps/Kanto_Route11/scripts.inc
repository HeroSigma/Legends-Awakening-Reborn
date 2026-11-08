Kanto_Route11_MapScripts::
	.byte 0

KantoAR_3_29_Route11_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_30_ROUTE12, 9, 63
	goto KantoAR_InspectionFinish
