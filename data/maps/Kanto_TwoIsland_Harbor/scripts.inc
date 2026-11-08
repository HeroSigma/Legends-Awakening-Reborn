Kanto_TwoIsland_Harbor_MapScripts::
	.byte 0

KantoAR_33_4_TwoIsland_Harbor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_34_0_THREEISLAND_HOUSE1, 4, 3
	goto KantoAR_InspectionFinish
