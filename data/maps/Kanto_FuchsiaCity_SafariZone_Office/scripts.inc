Kanto_FuchsiaCity_SafariZone_Office_MapScripts::
	.byte 0

KantoAR_11_2_FuchsiaCity_SafariZone_Office_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_11_3_FUCHSIACITY_GYM, 7, 13
	goto KantoAR_InspectionFinish
