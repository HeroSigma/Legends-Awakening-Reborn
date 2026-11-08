Kanto_ViridianCity_Mart_MapScripts::
	.byte 0

KantoAR_5_3_ViridianCity_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_5_4_VIRIDIANCITY_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
