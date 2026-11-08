Kanto_SafariZone_West_RestHouse_MapScripts::
	.byte 0

KantoAR_1_70_SafariZone_West_RestHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_71_SAFARIZONE_SECRETHOUSE, 6, 5
	goto KantoAR_InspectionFinish
