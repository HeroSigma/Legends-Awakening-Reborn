Kanto_FourIsland_IcefallCave_Back_MapScripts::
	.byte 0

KantoAR_1_113_FourIsland_IcefallCave_Back_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_114_FIVEISLAND_ROCKETWAREHOUSE, 16, 9
	goto KantoAR_InspectionFinish
