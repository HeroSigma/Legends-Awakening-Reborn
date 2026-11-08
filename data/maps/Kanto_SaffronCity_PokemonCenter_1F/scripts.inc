Kanto_SaffronCity_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_14_6_SaffronCity_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_14_7_SAFFRONCITY_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
