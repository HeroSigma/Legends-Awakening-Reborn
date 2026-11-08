Kanto_SafariZone_East_MapScripts::
	.byte 0

KantoAR_1_64_SafariZone_East_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_65_SAFARIZONE_NORTH, 28, 19
	goto KantoAR_InspectionFinish
