Kanto_Route18_EastEntrance_1F_MapScripts::
	.byte 0

KantoAR_26_0_Route18_EastEntrance_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_26_1_ROUTE18_EASTENTRANCE_2F, 6, 5
	goto KantoAR_InspectionFinish
