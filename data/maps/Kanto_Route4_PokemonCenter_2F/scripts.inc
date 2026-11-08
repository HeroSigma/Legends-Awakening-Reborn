Kanto_Route4_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_16_1_Route4_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_17_0_ROUTE5_POKEMONDAYCARE, 6, 3
	goto KantoAR_InspectionFinish
