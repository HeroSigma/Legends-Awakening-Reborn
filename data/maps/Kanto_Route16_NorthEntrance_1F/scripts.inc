Kanto_Route16_NorthEntrance_1F_MapScripts::
	.byte 0

KantoAR_25_1_Route16_NorthEntrance_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_25_2_ROUTE16_NORTHENTRANCE_2F, 6, 5
	goto KantoAR_InspectionFinish
