Kanto_ViridianCity_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_5_5_ViridianCity_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_6_0_PEWTERCITY_MUSEUM_1F, 13, 5
	goto KantoAR_InspectionFinish
