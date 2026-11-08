Kanto_CeladonCity_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_10_12_CeladonCity_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_13_CELADONCITY_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
