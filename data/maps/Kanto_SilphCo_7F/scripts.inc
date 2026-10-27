Kanto_SilphCo_7F_MapScripts::
	.byte 0

KantoAR_1_53_SilphCo_7F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_54_SILPHCO_8F, 15, 9
	goto KantoAR_InspectionFinish
