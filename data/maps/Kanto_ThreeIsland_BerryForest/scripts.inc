Kanto_ThreeIsland_BerryForest_MapScripts::
	.byte 0

KantoAR_1_109_ThreeIsland_BerryForest_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_110_FOURISLAND_ICEFALLCAVE_ENTRANCE, 12, 23
	goto KantoAR_InspectionFinish
