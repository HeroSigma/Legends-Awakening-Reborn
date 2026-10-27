Kanto_Route16_House_MapScripts::
	.byte 0

KantoAR_25_0_Route16_House_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_25_1_ROUTE16_NORTHENTRANCE_1F, 6, 11
	goto KantoAR_InspectionFinish
