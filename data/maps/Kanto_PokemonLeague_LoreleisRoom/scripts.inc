Kanto_PokemonLeague_LoreleisRoom_MapScripts::
	.byte 0

KantoAR_1_75_PokemonLeague_LoreleisRoom_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_76_POKEMONLEAGUE_BRUNOSROOM, 6, 6
	goto KantoAR_InspectionFinish
