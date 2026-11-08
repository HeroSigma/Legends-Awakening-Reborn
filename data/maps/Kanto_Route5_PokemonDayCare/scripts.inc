Kanto_Route5_PokemonDayCare_MapScripts::
	.byte 0

KantoAR_17_0_Route5_PokemonDayCare_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_17_1_ROUTE5_SOUTHENTRANCE, 4, 5
	goto KantoAR_InspectionFinish
