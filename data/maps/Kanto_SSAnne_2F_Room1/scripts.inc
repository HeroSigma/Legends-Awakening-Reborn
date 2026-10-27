Kanto_SSAnne_2F_Room1_MapScripts::
	.byte 0

KantoAR_1_18_SSAnne_2F_Room1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_19_SSANNE_2F_ROOM2, 3, 4
	goto KantoAR_InspectionFinish
