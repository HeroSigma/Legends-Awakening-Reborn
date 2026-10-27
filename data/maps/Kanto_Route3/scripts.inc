Kanto_Route3_MapScripts::
	.byte 0

KantoAR_3_21_Route3_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_22_ROUTE4, 54, 11
	goto KantoAR_InspectionFinish
