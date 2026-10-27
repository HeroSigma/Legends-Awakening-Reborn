Kanto_FourIsland_PokemonDayCare_MapScripts::
	.byte 0

KantoAR_35_0_FourIsland_PokemonDayCare_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_35_1_FOURISLAND_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
