Kanto_TwoIsland_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_33_3_TwoIsland_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_33_4_TWOISLAND_HARBOR, 8, 5
	goto KantoAR_InspectionFinish
