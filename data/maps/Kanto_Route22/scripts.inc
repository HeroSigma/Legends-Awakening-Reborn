Kanto_Route22_MapScripts::
	.byte 0

KantoAR_3_41_Route22_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_42_ROUTE23, 12, 77
	goto KantoAR_InspectionFinish
