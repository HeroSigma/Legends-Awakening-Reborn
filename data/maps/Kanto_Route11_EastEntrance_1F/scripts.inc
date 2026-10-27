Kanto_Route11_EastEntrance_1F_MapScripts::
	.byte 0

KantoAR_22_0_Route11_EastEntrance_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_22_1_ROUTE11_EASTENTRANCE_2F, 6, 5
	goto KantoAR_InspectionFinish
