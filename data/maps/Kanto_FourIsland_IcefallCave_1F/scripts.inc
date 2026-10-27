Kanto_FourIsland_IcefallCave_1F_MapScripts::
	.byte 0

KantoAR_1_111_FourIsland_IcefallCave_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_112_FOURISLAND_ICEFALLCAVE_B1F, 12, 9
	goto KantoAR_InspectionFinish
