Kanto_CinnabarIsland_Mart_MapScripts::
	.byte 0

KantoAR_12_7_CinnabarIsland_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_13_0_INDIGOPLATEAU_POKEMONCENTER_1F, 12, 12
	goto KantoAR_InspectionFinish
