Kanto_Route2_House_MapScripts::
	.byte 0

KantoAR_15_1_Route2_House_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_15_2_ROUTE2_EASTBUILDING, 7, 6
	goto KantoAR_InspectionFinish
