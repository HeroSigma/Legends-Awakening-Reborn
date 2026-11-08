Kanto_Route10_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_21_0_Route10_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_21_1_ROUTE10_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
