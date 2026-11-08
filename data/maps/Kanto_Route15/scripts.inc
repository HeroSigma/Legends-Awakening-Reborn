Kanto_Route15_MapScripts::
	.byte 0

KantoAR_3_33_Route15_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_34_ROUTE16, 28, 8
	goto KantoAR_InspectionFinish
