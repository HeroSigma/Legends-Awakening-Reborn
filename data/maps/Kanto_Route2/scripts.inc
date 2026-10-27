Kanto_Route2_MapScripts::
	.byte 0

KantoAR_3_20_Route2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_21_ROUTE3, 42, 10
	goto KantoAR_InspectionFinish
