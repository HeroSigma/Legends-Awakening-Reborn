Kanto_CeladonCity_GameCorner_PrizeRoom_MapScripts::
	.byte 0

KantoAR_10_15_CeladonCity_GameCorner_PrizeRoom_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_16_CELADONCITY_GYM, 6, 10
	goto KantoAR_InspectionFinish
