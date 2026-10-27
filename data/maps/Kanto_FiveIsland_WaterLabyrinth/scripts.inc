Kanto_FiveIsland_WaterLabyrinth_MapScripts::
	.byte 0

KantoAR_3_55_FiveIsland_WaterLabyrinth_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_56_FIVEISLAND_MEADOW, 12, 23
	goto KantoAR_InspectionFinish
