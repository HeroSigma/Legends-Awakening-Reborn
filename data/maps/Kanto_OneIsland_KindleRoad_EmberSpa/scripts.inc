Kanto_OneIsland_KindleRoad_EmberSpa_MapScripts::
	.byte 0

KantoAR_2_57_OneIsland_KindleRoad_EmberSpa_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_58_BIRTHISLAND_HARBOR, 8, 5
	goto KantoAR_InspectionFinish
