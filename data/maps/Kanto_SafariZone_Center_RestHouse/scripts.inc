Kanto_SafariZone_Center_RestHouse_MapScripts::
	.byte 0

KantoAR_1_67_SafariZone_Center_RestHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_68_SAFARIZONE_EAST_RESTHOUSE, 6, 5
	goto KantoAR_InspectionFinish
