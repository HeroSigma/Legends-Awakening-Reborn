Kanto_ThreeIsland_House3_MapScripts::
	.byte 0

KantoAR_34_5_ThreeIsland_House3_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_34_6_THREEISLAND_HOUSE4, 4, 3
	goto KantoAR_InspectionFinish
