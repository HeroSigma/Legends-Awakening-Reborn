Kanto_PokemonMansion_1F_MapScripts::
	.byte 0

KantoAR_1_59_PokemonMansion_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_60_POKEMONMANSION_2F, 19, 17
	goto KantoAR_InspectionFinish
