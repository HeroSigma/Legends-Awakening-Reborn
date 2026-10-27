Kanto_PokemonLeague_AgathasRoom_MapScripts::
	.byte 0

KantoAR_1_77_PokemonLeague_AgathasRoom_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_78_POKEMONLEAGUE_LANCESROOM, 16, 12
	goto KantoAR_InspectionFinish
