Kanto_ThreeIsland_House2_MapScripts::
	.byte 0

KantoAR_34_4_ThreeIsland_House2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_34_5_THREEISLAND_HOUSE3, 4, 3
	goto KantoAR_InspectionFinish
