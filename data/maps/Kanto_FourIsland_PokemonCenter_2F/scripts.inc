Kanto_FourIsland_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_35_2_FourIsland_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_35_3_FOURISLAND_HOUSE1, 4, 3
	goto KantoAR_InspectionFinish
