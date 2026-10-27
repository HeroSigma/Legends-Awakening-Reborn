Kanto_PokemonTower_3F_MapScripts::
	.byte 0

KantoAR_1_90_PokemonTower_3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_91_POKEMONTOWER_4F, 12, 10
	goto KantoAR_InspectionFinish
