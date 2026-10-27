Kanto_MtEmber_SummitPath_1F_MapScripts::
	.byte 0

KantoAR_1_98_MtEmber_SummitPath_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_99_MTEMBER_SUMMITPATH_2F, 15, 22
	goto KantoAR_InspectionFinish
