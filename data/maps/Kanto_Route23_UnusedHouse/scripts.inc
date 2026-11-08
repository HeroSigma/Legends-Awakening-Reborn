Kanto_Route23_UnusedHouse_MapScripts::
	.byte 0

KantoAR_29_0_Route23_UnusedHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_30_0_ROUTE25_SEACOTTAGE, 7, 5
	goto KantoAR_InspectionFinish
