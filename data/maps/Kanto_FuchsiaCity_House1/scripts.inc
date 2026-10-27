Kanto_FuchsiaCity_House1_MapScripts::
	.byte 0

KantoAR_11_4_FuchsiaCity_House1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_11_5_FUCHSIACITY_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
