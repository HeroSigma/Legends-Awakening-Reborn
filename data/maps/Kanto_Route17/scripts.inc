Kanto_Route17_MapScripts::
	.byte 0

KantoAR_3_35_Route17_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_36_ROUTE18, 30, 9
	goto KantoAR_InspectionFinish
