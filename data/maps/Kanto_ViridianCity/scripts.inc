Kanto_ViridianCity_MapScripts::
	.byte 0

KantoAR_3_1_ViridianCity_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_2_PEWTERCITY, 24, 20
	goto KantoAR_InspectionFinish
