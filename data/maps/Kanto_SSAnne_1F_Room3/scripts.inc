Kanto_SSAnne_1F_Room3_MapScripts::
	.byte 0

KantoAR_1_14_SSAnne_1F_Room3_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_15_SSANNE_1F_ROOM4, 3, 4
	goto KantoAR_InspectionFinish
