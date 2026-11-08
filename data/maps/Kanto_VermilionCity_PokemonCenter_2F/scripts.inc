Kanto_VermilionCity_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_9_2_VermilionCity_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_9_3_VERMILIONCITY_POKEMONFANCLUB, 6, 8
	goto KantoAR_InspectionFinish
