Kanto_SilphCo_1F_MapScripts::
	.byte 0

KantoAR_1_47_SilphCo_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_48_SILPHCO_2F, 18, 12
	goto KantoAR_InspectionFinish
