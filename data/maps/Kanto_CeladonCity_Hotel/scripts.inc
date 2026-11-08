Kanto_CeladonCity_Hotel_MapScripts::
	.byte 0

KantoAR_10_19_CeladonCity_Hotel_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_11_0_FUCHSIACITY_SAFARIZONE_ENTRANCE, 4, 4
	goto KantoAR_InspectionFinish
