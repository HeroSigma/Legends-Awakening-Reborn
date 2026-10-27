Kanto_CinnabarIsland_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_12_6_CinnabarIsland_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_12_7_CINNABARISLAND_MART, 5, 4
	goto KantoAR_InspectionFinish
