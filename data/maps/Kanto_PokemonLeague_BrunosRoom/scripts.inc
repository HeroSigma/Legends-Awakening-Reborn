Kanto_PokemonLeague_BrunosRoom_MapScripts::
	.byte 0

KantoAR_1_76_PokemonLeague_BrunosRoom_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_77_POKEMONLEAGUE_AGATHASROOM, 6, 6
	goto KantoAR_InspectionFinish
