Kanto_Route1_MapScripts::
	.byte 0

KantoAR_3_19_Route1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_20_ROUTE2, 17, 40
	goto KantoAR_InspectionFinish
