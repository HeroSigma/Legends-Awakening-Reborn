Kanto_FuchsiaCity_WardensHouse_MapScripts::
	.byte 0

KantoAR_11_7_FuchsiaCity_WardensHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_11_8_FUCHSIACITY_HOUSE2, 5, 5
	goto KantoAR_InspectionFinish
