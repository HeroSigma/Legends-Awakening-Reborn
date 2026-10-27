Kanto_SaffronCity_House_MapScripts::
	.byte 0

KantoAR_14_4_SaffronCity_House_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_14_5_SAFFRONCITY_MART, 5, 4
	goto KantoAR_InspectionFinish
