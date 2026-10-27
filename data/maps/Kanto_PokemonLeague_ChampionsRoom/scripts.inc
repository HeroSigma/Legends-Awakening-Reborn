Kanto_PokemonLeague_ChampionsRoom_MapScripts::
	.byte 0

KantoAR_1_79_PokemonLeague_ChampionsRoom_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_81_ROCKTUNNEL_1F, 24, 20
	goto KantoAR_InspectionFinish
