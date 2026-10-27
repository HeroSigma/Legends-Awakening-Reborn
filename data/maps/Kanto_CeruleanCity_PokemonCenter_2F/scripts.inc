Kanto_CeruleanCity_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_7_4_CeruleanCity_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_7_5_CERULEANCITY_GYM, 8, 7
	goto KantoAR_InspectionFinish
