Kanto_Route10_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_21_1_Route10_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_22_0_ROUTE11_EASTENTRANCE_1F, 6, 6
	goto KantoAR_InspectionFinish
