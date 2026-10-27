Kanto_TwoIsland_MapScripts::
	.byte 0

KantoAR_3_13_TwoIsland_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_14_THREEISLAND, 11, 20
	goto KantoAR_InspectionFinish
