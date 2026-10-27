Kanto_FourIsland_IcefallCave_Entrance_MapScripts::
	.byte 0

KantoAR_1_110_FourIsland_IcefallCave_Entrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_111_FOURISLAND_ICEFALLCAVE_1F, 10, 8
	goto KantoAR_InspectionFinish
