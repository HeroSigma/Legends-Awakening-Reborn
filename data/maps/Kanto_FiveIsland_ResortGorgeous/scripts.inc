Kanto_FiveIsland_ResortGorgeous_MapScripts::
	.byte 0

KantoAR_3_54_FiveIsland_ResortGorgeous_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_55_FIVEISLAND_WATERLABYRINTH, 16, 10
	goto KantoAR_InspectionFinish
