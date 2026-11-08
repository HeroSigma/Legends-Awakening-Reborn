Kanto_FuchsiaCity_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_11_5_FuchsiaCity_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_11_6_FUCHSIACITY_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
