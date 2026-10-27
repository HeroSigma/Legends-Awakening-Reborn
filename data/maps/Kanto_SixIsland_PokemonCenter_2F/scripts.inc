Kanto_SixIsland_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_37_1_SixIsland_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_37_2_SIXISLAND_HARBOR, 8, 5
	goto KantoAR_InspectionFinish
