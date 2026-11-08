Kanto_ViridianCity_House_MapScripts::
	.byte 0

KantoAR_5_0_ViridianCity_House_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_5_1_VIRIDIANCITY_GYM, 10, 12
	goto KantoAR_InspectionFinish
