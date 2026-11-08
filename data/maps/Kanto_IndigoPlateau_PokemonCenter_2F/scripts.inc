Kanto_IndigoPlateau_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_13_1_IndigoPlateau_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_14_0_SAFFRONCITY_COPYCATSHOUSE_1F, 4, 5
	goto KantoAR_InspectionFinish
