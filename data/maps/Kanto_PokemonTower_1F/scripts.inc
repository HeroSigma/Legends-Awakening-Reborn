Kanto_PokemonTower_1F_MapScripts::
	.byte 0

KantoAR_1_88_PokemonTower_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_89_POKEMONTOWER_2F, 11, 10
	goto KantoAR_InspectionFinish
