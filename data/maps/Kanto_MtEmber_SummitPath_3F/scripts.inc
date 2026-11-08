Kanto_MtEmber_SummitPath_3F_MapScripts::
	.byte 0

KantoAR_1_100_MtEmber_SummitPath_3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_101_MTEMBER_SUMMIT, 8, 11
	goto KantoAR_InspectionFinish
