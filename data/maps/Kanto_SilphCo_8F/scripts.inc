Kanto_SilphCo_8F_MapScripts::
	.byte 0

KantoAR_1_54_SilphCo_8F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_55_SILPHCO_9F, 15, 5
	goto KantoAR_InspectionFinish
