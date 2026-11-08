Kanto_FuchsiaCity_SafariZone_Entrance_MapScripts::
	.byte 0

KantoAR_11_0_FuchsiaCity_SafariZone_Entrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_11_1_FUCHSIACITY_MART, 5, 4
	goto KantoAR_InspectionFinish
