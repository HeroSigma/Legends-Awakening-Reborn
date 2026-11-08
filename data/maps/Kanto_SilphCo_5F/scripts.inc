Kanto_SilphCo_5F_MapScripts::
	.byte 0

KantoAR_1_51_SilphCo_5F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_52_SILPHCO_6F, 15, 9
	goto KantoAR_InspectionFinish
