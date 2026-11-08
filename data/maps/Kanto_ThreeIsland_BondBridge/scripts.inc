Kanto_ThreeIsland_BondBridge_MapScripts::
	.byte 0

KantoAR_3_48_ThreeIsland_BondBridge_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_49_THREEISLAND_PORT, 16, 9
	goto KantoAR_InspectionFinish
