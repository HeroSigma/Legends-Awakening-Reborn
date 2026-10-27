Kanto_PokemonMansion_2F_MapScripts::
	.byte 0

KantoAR_1_60_PokemonMansion_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_61_POKEMONMANSION_3F, 19, 16
	goto KantoAR_InspectionFinish
