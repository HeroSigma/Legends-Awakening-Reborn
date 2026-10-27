Kanto_PewterCity_Museum_1F_MapScripts::
	.byte 0

KantoAR_6_0_PewterCity_Museum_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_6_1_PEWTERCITY_MUSEUM_2F, 9, 4
	goto KantoAR_InspectionFinish
