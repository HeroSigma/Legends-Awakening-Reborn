Kanto_Route18_MapScripts::
	.byte 0

KantoAR_3_36_Route18_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_37_ROUTE19, 12, 1
	goto KantoAR_InspectionFinish
