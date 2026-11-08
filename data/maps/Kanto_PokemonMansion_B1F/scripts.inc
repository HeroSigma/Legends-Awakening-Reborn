Kanto_PokemonMansion_B1F_MapScripts::
	.byte 0

KantoAR_1_62_PokemonMansion_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_63_SAFARIZONE_CENTER, 25, 22
	goto KantoAR_InspectionFinish
