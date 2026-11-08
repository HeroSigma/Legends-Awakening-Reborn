Kanto_PokemonLeague_LancesRoom_MapScripts::
	.byte 0

KantoAR_1_78_PokemonLeague_LancesRoom_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_79_POKEMONLEAGUE_CHAMPIONSROOM, 6, 10
	goto KantoAR_InspectionFinish
