Kanto_TwoIsland_CapeBrink_MapScripts::
	.byte 0

KantoAR_3_47_TwoIsland_CapeBrink_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_48_THREEISLAND_BONDBRIDGE, 48, 10
	goto KantoAR_InspectionFinish
