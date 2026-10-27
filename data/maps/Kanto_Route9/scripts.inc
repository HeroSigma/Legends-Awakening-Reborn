Kanto_Route9_MapScripts::
	.byte 0

KantoAR_3_27_Route9_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_28_ROUTE10, 11, 41
	goto KantoAR_InspectionFinish
