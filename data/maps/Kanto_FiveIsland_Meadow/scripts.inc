Kanto_FiveIsland_Meadow_MapScripts::
	.byte 0

KantoAR_3_56_FiveIsland_Meadow_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_57_FIVEISLAND_MEMORIALPILLAR, 17, 30
	goto KantoAR_InspectionFinish
