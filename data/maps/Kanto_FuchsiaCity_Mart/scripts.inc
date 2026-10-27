Kanto_FuchsiaCity_Mart_MapScripts::
	.byte 0

KantoAR_11_1_FuchsiaCity_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_11_2_FUCHSIACITY_SAFARIZONE_OFFICE, 12, 4
	goto KantoAR_InspectionFinish
