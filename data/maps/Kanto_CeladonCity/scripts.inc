Kanto_CeladonCity_MapScripts::
	.byte 0

KantoAR_3_6_CeladonCity_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_7_FUCHSIACITY, 23, 20
	goto KantoAR_InspectionFinish
