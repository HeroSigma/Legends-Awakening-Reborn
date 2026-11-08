Kanto_FourIsland_IcefallCave_B1F_MapScripts::
	.byte 0

KantoAR_1_112_FourIsland_IcefallCave_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_113_FOURISLAND_ICEFALLCAVE_BACK, 12, 15
	goto KantoAR_InspectionFinish
