Kanto_MtEmber_SummitPath_2F_MapScripts::
	.byte 0

KantoAR_1_99_MtEmber_SummitPath_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_100_MTEMBER_SUMMITPATH_3F, 10, 5
	goto KantoAR_InspectionFinish
