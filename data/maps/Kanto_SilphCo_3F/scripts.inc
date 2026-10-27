Kanto_SilphCo_3F_MapScripts::
	.byte 0

KantoAR_1_49_SilphCo_3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_50_SILPHCO_4F, 17, 9
	goto KantoAR_InspectionFinish
