Kanto_PewterCity_MapScripts::
	.byte 0

KantoAR_3_2_PewterCity_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_3_CERULEANCITY, 25, 20
	goto KantoAR_InspectionFinish
