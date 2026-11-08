Kanto_SSAnne_B1F_Room1_MapScripts::
	.byte 0

KantoAR_1_24_SSAnne_B1F_Room1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_25_SSANNE_B1F_ROOM2, 3, 4
	goto KantoAR_InspectionFinish
