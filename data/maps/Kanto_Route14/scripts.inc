Kanto_Route14_MapScripts::
	.byte 0

KantoAR_3_32_Route14_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_33_ROUTE15, 36, 7
	goto KantoAR_InspectionFinish
