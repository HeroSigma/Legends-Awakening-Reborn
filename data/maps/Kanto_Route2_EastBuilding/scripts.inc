Kanto_Route2_EastBuilding_MapScripts::
	.byte 0

KantoAR_15_2_Route2_EastBuilding_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_15_3_ROUTE2_VIRIDIANFOREST_NORTHENTRANCE, 7, 6
	goto KantoAR_InspectionFinish
