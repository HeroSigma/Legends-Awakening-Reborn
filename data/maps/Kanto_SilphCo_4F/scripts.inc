Kanto_SilphCo_4F_MapScripts::
	.byte 0

KantoAR_1_50_SilphCo_4F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_51_SILPHCO_5F, 21, 11
	goto KantoAR_InspectionFinish
