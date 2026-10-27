Kanto_CeruleanCity_PokemonCenter_1F_MapScripts::
	.byte 0

KantoAR_7_3_CeruleanCity_PokemonCenter_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_7_4_CERULEANCITY_POKEMONCENTER_2F, 7, 5
	goto KantoAR_InspectionFinish
