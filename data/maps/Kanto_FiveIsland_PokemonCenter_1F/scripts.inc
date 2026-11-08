Kanto_FiveIsland_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_36_0_FiveIsland_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_36_1_FIVEISLAND_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
