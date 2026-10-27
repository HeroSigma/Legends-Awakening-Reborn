Kanto_SixIsland_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_37_0_SixIsland_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_37_1_SIXISLAND_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
