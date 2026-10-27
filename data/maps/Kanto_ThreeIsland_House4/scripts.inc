Kanto_ThreeIsland_House4_MapScripts::
	.byte 0

KantoAR_34_6_ThreeIsland_House4_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_34_7_THREEISLAND_HOUSE5, 4, 3
	goto KantoAR_InspectionFinish
