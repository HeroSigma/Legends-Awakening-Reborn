Kanto_PewterCity_Museum_2F_MapScripts::
	.byte 0

KantoAR_6_1_PewterCity_Museum_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_6_2_PEWTERCITY_GYM, 6, 8
	goto KantoAR_InspectionFinish
