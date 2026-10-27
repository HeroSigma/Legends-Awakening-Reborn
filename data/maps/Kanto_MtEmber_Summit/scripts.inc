Kanto_MtEmber_Summit_MapScripts::
	.byte 0

KantoAR_1_101_MtEmber_Summit_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_102_MTEMBER_RUBYPATH_B5F, 8, 7
	goto KantoAR_InspectionFinish
