Kanto_OneIsland_House1_MapScripts::
	.byte 0

KantoAR_32_2_OneIsland_House1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_32_3_ONEISLAND_HOUSE2, 4, 3
	goto KantoAR_InspectionFinish
