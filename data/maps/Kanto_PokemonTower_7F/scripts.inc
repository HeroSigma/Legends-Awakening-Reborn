Kanto_PokemonTower_7F_MapScripts::
	.byte 0

KantoAR_1_94_PokemonTower_7F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_95_POWERPLANT, 24, 17
	goto KantoAR_InspectionFinish
