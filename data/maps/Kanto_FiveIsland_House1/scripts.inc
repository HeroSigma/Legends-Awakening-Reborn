Kanto_FiveIsland_House1_MapScripts::
	.byte 0

KantoAR_36_3_FiveIsland_House1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_36_4_FIVEISLAND_HOUSE2, 4, 3
	goto KantoAR_InspectionFinish
