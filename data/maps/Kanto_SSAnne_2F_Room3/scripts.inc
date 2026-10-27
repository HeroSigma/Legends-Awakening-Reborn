Kanto_SSAnne_2F_Room3_MapScripts::
	.byte 0

KantoAR_1_20_SSAnne_2F_Room3_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_21_SSANNE_2F_ROOM4, 3, 4
	goto KantoAR_InspectionFinish
