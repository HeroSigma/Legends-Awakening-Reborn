Kanto_PewterCity_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_6_5_PewterCity_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_6_6_PEWTERCITY_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
