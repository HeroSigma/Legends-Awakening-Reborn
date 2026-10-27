Kanto_SilphCo_6F_MapScripts::
	.byte 0

KantoAR_1_52_SilphCo_6F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_53_SILPHCO_7F, 18, 9
	goto KantoAR_InspectionFinish
