Kanto_Route13_MapScripts::
	.byte 0

KantoAR_3_31_Route13_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_32_ROUTE14, 10, 30
	goto KantoAR_InspectionFinish
