Kanto_Route16_MapScripts::
	.byte 0

KantoAR_3_34_Route16_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_35_ROUTE17, 11, 80
	goto KantoAR_InspectionFinish
