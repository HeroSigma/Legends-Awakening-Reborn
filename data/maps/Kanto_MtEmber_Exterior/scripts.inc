Kanto_MtEmber_Exterior_MapScripts::
	.byte 0

KantoAR_1_97_MtEmber_Exterior_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_98_MTEMBER_SUMMITPATH_1F, 2, 9
	goto KantoAR_InspectionFinish
