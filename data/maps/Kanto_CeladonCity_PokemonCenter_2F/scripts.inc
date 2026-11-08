Kanto_CeladonCity_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_10_13_CeladonCity_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_14_CELADONCITY_GAMECORNER, 9, 7
	goto KantoAR_InspectionFinish
