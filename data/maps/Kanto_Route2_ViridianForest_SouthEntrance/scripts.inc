Kanto_Route2_ViridianForest_SouthEntrance_MapScripts::
	.byte 0

KantoAR_15_0_Route2_ViridianForest_SouthEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_15_1_ROUTE2_HOUSE, 4, 3
	goto KantoAR_InspectionFinish
