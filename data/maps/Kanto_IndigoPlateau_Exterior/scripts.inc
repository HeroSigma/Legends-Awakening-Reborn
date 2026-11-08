Kanto_IndigoPlateau_Exterior_MapScripts::
	.byte 0

KantoAR_3_9_IndigoPlateau_Exterior_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_10_SAFFRONCITY, 33, 32
	goto KantoAR_InspectionFinish
