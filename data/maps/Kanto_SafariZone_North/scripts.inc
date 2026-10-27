Kanto_SafariZone_North_MapScripts::
	.byte 0

KantoAR_1_65_SafariZone_North_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_66_SAFARIZONE_WEST, 28, 18
	goto KantoAR_InspectionFinish
