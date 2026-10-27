Kanto_SevenIsland_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_31_4_SevenIsland_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_31_5_SEVENISLAND_UNUSEDHOUSE, 4, 3
	goto KantoAR_InspectionFinish
