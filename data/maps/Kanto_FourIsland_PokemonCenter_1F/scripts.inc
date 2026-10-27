Kanto_FourIsland_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_35_1_FourIsland_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_35_2_FOURISLAND_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
