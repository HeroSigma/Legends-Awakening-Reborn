Kanto_SaffronCity_MrPsychicsHouse_MapScripts::
	.byte 0

KantoAR_14_8_SaffronCity_MrPsychicsHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_14_9_SAFFRONCITY_POKEMONTRAINERFANCLUB, 5, 8
	goto KantoAR_InspectionFinish
