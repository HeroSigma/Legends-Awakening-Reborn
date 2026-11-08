Kanto_Route20_MapScripts::
	.byte 0

KantoAR_3_38_Route20_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_39_ROUTE21_NORTH, 12, 2
	goto KantoAR_InspectionFinish
