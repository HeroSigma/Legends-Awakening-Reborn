Kanto_ThreeIsland_Mart_MapScripts::
	.byte 0

KantoAR_34_3_ThreeIsland_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_34_4_THREEISLAND_HOUSE2, 4, 3
	goto KantoAR_InspectionFinish
