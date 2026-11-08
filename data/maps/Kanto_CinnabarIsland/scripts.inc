Kanto_CinnabarIsland_MapScripts::
	.byte 0

KantoAR_3_8_CinnabarIsland_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_9_INDIGOPLATEAU_EXTERIOR, 12, 10
	goto KantoAR_InspectionFinish
