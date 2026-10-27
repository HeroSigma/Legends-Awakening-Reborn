Kanto_SafariZone_East_RestHouse_MapScripts::
	.byte 0

KantoAR_1_68_SafariZone_East_RestHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_69_SAFARIZONE_NORTH_RESTHOUSE, 6, 5
	goto KantoAR_InspectionFinish
