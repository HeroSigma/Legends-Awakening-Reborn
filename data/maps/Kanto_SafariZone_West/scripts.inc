Kanto_SafariZone_West_MapScripts::
	.byte 0

KantoAR_1_66_SafariZone_West_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_67_SAFARIZONE_CENTER_RESTHOUSE, 6, 5
	goto KantoAR_InspectionFinish
