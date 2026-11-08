Kanto_TwoIsland_CapeBrink_House_MapScripts::
	.byte 0

KantoAR_40_0_TwoIsland_CapeBrink_House_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_41_0_SIXISLAND_WATERPATH_HOUSE1, 4, 3
	goto KantoAR_InspectionFinish
