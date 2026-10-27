Kanto_FiveIsland_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_36_1_FiveIsland_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_36_2_FIVEISLAND_HARBOR, 8, 5
	goto KantoAR_InspectionFinish
