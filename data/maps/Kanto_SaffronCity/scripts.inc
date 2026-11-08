Kanto_SaffronCity_MapScripts::
	.byte 0

KantoAR_3_10_SaffronCity_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_11_SAFFRONCITY_CONNECTION, 24, 25
	goto KantoAR_InspectionFinish
