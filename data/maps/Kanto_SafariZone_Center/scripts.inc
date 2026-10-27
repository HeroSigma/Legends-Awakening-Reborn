Kanto_SafariZone_Center_MapScripts::
	.byte 0

KantoAR_1_63_SafariZone_Center_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_64_SAFARIZONE_EAST, 24, 16
	goto KantoAR_InspectionFinish
