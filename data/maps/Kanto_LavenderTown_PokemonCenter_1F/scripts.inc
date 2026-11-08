Kanto_LavenderTown_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_8_0_LavenderTown_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_8_1_LAVENDERTOWN_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
