Kanto_PokemonTower_4F_MapScripts::
	.byte 0

KantoAR_1_91_PokemonTower_4F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_92_POKEMONTOWER_5F, 12, 10
	goto KantoAR_InspectionFinish
