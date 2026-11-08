Kanto_ThreeIsland_House1_MapScripts::
	.byte 0

KantoAR_34_0_ThreeIsland_House1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_34_1_THREEISLAND_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
