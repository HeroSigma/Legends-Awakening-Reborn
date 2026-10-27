Kanto_OneIsland_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_32_1_OneIsland_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_32_2_ONEISLAND_HOUSE1, 4, 3
	goto KantoAR_InspectionFinish
