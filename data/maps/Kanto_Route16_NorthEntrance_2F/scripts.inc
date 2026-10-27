Kanto_Route16_NorthEntrance_2F_MapScripts::
	.byte 0

KantoAR_25_2_Route16_NorthEntrance_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_26_0_ROUTE18_EASTENTRANCE_1F, 6, 6
	goto KantoAR_InspectionFinish
