Kanto_SafariZone_SecretHouse_MapScripts::
	.byte 0

KantoAR_1_71_SafariZone_SecretHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_72_CERULEANCAVE_1F, 19, 12
	goto KantoAR_InspectionFinish
