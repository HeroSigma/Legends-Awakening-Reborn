Kanto_Route8_MapScripts::
	.byte 0

KantoAR_3_26_Route8_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_27_ROUTE9, 36, 7
	goto KantoAR_InspectionFinish
