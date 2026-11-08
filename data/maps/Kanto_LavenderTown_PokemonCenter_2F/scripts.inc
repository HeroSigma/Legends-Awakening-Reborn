Kanto_LavenderTown_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_8_1_LavenderTown_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_8_2_LAVENDERTOWN_VOLUNTEERPOKEMONHOUSE, 4, 3
	goto KantoAR_InspectionFinish
