Kanto_CeladonCity_GameCorner_MapScripts::
	.byte 0

KantoAR_10_14_CeladonCity_GameCorner_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_15_CELADONCITY_GAMECORNER_PRIZEROOM, 4, 5
	goto KantoAR_InspectionFinish
