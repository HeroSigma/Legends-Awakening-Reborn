Kanto_PokemonTower_5F_MapScripts::
	.byte 0

KantoAR_1_92_PokemonTower_5F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_93_POKEMONTOWER_6F, 12, 8
	goto KantoAR_InspectionFinish
