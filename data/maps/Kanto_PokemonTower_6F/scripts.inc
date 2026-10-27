Kanto_PokemonTower_6F_MapScripts::
	.byte 0

KantoAR_1_93_PokemonTower_6F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_94_POKEMONTOWER_7F, 12, 10
	goto KantoAR_InspectionFinish
