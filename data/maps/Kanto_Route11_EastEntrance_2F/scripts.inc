Kanto_Route11_EastEntrance_2F_MapScripts::
	.byte 0

KantoAR_22_1_Route11_EastEntrance_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_23_0_ROUTE12_NORTHENTRANCE_1F, 5, 6
	goto KantoAR_InspectionFinish
