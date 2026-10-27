Kanto_VermilionCity_PokemonFanClub_MapScripts::
	.byte 0

KantoAR_9_3_VermilionCity_PokemonFanClub_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_9_4_VERMILIONCITY_HOUSE2, 4, 3
	goto KantoAR_InspectionFinish
