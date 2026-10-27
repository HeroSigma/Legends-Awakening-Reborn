Kanto_Route4_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_16_0_Route4_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_16_1_ROUTE4_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
