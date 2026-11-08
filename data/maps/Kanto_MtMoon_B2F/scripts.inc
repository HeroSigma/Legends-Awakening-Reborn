Kanto_MtMoon_B2F_MapScripts::
	.byte 0

KantoAR_1_3_MtMoon_B2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_4_SSANNE_EXTERIOR, 32, 9
	goto KantoAR_InspectionFinish
