Kanto_SaffronCity_PokemonCenter_2F_MapScripts::
	.byte 0

KantoAR_14_7_SaffronCity_PokemonCenter_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_14_8_SAFFRONCITY_MRPSYCHICSHOUSE, 4, 3
	goto KantoAR_InspectionFinish
