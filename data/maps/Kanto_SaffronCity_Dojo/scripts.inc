Kanto_SaffronCity_Dojo_MapScripts::
	.byte 0

KantoAR_14_2_SaffronCity_Dojo_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_14_3_SAFFRONCITY_GYM, 14, 12
	goto KantoAR_InspectionFinish
