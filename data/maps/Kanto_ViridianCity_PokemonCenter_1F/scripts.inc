Kanto_ViridianCity_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_5_4_ViridianCity_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_5_5_VIRIDIANCITY_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
