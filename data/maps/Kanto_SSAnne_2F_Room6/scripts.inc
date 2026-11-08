Kanto_SSAnne_2F_Room6_MapScripts::
	.byte 0

KantoAR_1_23_SSAnne_2F_Room6_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_24_SSANNE_B1F_ROOM1, 3, 4
	goto KantoAR_InspectionFinish
