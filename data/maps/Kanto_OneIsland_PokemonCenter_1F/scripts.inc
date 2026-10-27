Kanto_OneIsland_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_32_0_OneIsland_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_32_1_ONEISLAND_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
