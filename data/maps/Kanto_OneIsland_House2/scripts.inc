Kanto_OneIsland_House2_MapScripts::
	.byte 0

KantoAR_32_3_OneIsland_House2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_32_4_ONEISLAND_HARBOR, 8, 5
	goto KantoAR_InspectionFinish
