Kanto_Route7_MapScripts::
	.byte 0

KantoAR_3_25_Route7_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_26_ROUTE8, 35, 10
	goto KantoAR_InspectionFinish
