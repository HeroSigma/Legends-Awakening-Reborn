Kanto_FuchsiaCity_House2_MapScripts::
	.byte 0

KantoAR_11_8_FuchsiaCity_House2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_11_9_FUCHSIACITY_HOUSE3, 4, 3
	goto KantoAR_InspectionFinish
