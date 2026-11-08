Kanto_Route21_North_MapScripts::
	.byte 0

KantoAR_3_39_Route21_North_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_40_ROUTE21_SOUTH, 12, 48
	goto KantoAR_InspectionFinish
