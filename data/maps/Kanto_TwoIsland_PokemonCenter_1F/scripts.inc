Kanto_TwoIsland_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_33_2_TwoIsland_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_33_3_TWOISLAND_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
