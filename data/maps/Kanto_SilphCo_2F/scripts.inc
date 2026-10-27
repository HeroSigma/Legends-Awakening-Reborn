Kanto_SilphCo_2F_MapScripts::
	.byte 0

KantoAR_1_48_SilphCo_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_49_SILPHCO_3F, 19, 12
	goto KantoAR_InspectionFinish
