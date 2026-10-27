Kanto_ThreeIsland_MapScripts::
	.byte 0

KantoAR_3_14_ThreeIsland_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_15_FOURISLAND, 24, 22
	goto KantoAR_InspectionFinish
