Kanto_SSAnne_1F_Room5_MapScripts::
	.byte 0

KantoAR_1_16_SSAnne_1F_Room5_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_17_SSANNE_1F_ROOM7, 3, 4
	goto KantoAR_InspectionFinish
