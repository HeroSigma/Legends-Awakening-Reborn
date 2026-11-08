Kanto_SilphCo_11F_MapScripts::
	.byte 0

KantoAR_1_57_SilphCo_11F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_58_SILPHCO_ELEVATOR, 1, 4
	goto KantoAR_InspectionFinish
