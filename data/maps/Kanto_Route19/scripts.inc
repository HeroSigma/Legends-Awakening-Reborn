Kanto_Route19_MapScripts::
	.byte 0

KantoAR_3_37_Route19_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_38_ROUTE20, 60, 10
	goto KantoAR_InspectionFinish
