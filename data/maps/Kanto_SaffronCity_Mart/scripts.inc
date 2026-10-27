Kanto_SaffronCity_Mart_MapScripts::
	.byte 0

KantoAR_14_5_SaffronCity_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_14_6_SAFFRONCITY_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
