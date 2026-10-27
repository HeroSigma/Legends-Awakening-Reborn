Kanto_Route10_MapScripts::
	.byte 0

KantoAR_3_28_Route10_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_29_ROUTE11, 37, 10
	goto KantoAR_InspectionFinish
