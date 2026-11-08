Kanto_SilphCo_9F_MapScripts::
	.byte 0

KantoAR_1_55_SilphCo_9F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_56_SILPHCO_10F, 11, 9
	goto KantoAR_InspectionFinish
