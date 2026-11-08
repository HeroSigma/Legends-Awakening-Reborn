Kanto_ThreeIsland_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_34_2_ThreeIsland_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_34_3_THREEISLAND_MART, 5, 4
	goto KantoAR_InspectionFinish
