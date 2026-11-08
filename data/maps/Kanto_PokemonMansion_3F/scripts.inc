Kanto_PokemonMansion_3F_MapScripts::
	.byte 0

KantoAR_1_61_PokemonMansion_3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_62_POKEMONMANSION_B1F, 19, 18
	goto KantoAR_InspectionFinish
