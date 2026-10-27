Kanto_FuchsiaCity_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_11_6_FuchsiaCity_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_11_7_FUCHSIACITY_WARDENSHOUSE, 6, 6
	goto KantoAR_InspectionFinish
