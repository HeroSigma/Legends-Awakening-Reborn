Kanto_SilphCo_10F_MapScripts::
	.byte 0

KantoAR_1_56_SilphCo_10F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_57_SILPHCO_11F, 6, 10
	goto KantoAR_InspectionFinish
