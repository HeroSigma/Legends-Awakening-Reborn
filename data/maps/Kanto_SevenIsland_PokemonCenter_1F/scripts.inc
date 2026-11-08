Kanto_SevenIsland_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_31_3_SevenIsland_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_31_4_SEVENISLAND_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
