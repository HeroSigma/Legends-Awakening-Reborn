Kanto_SSAnne_1F_Room1_MapScripts::
	.byte 0

KantoAR_1_12_SSAnne_1F_Room1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_13_SSANNE_1F_ROOM2, 3, 4
	goto KantoAR_InspectionFinish
