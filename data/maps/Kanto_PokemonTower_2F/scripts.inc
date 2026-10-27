Kanto_PokemonTower_2F_MapScripts::
	.byte 0

KantoAR_1_89_PokemonTower_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_90_POKEMONTOWER_3F, 13, 10
	goto KantoAR_InspectionFinish
