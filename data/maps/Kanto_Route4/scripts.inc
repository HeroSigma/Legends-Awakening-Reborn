Kanto_Route4_MapScripts::
	.byte 0

KantoAR_3_22_Route4_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_23_ROUTE5, 26, 20
	goto KantoAR_InspectionFinish
