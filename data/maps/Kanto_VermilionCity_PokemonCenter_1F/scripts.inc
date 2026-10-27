Kanto_VermilionCity_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_9_1_VermilionCity_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_9_2_VERMILIONCITY_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
