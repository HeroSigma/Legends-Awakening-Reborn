Kanto_CeruleanCave_B1F_MapScripts::
	.byte 0

KantoAR_1_74_CeruleanCave_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_75_POKEMONLEAGUE_LORELEISROOM, 6, 6
	goto KantoAR_InspectionFinish
