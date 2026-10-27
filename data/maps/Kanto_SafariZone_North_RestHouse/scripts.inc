Kanto_SafariZone_North_RestHouse_MapScripts::
	.byte 0

KantoAR_1_69_SafariZone_North_RestHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_70_SAFARIZONE_WEST_RESTHOUSE, 6, 5
	goto KantoAR_InspectionFinish
