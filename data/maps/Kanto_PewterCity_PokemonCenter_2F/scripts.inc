Kanto_PewterCity_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_6_6_PewterCity_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_6_7_PEWTERCITY_HOUSE2, 4, 3
	goto KantoAR_InspectionFinish
