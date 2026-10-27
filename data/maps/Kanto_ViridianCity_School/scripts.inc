Kanto_ViridianCity_School_MapScripts::
	.byte 0

KantoAR_5_2_ViridianCity_School_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_5_3_VIRIDIANCITY_MART, 5, 4
	goto KantoAR_InspectionFinish
