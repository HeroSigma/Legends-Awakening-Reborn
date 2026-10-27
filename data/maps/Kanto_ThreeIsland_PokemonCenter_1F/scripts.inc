Kanto_ThreeIsland_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_34_1_ThreeIsland_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_34_2_THREEISLAND_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
