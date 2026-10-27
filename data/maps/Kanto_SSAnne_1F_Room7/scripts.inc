Kanto_SSAnne_1F_Room7_MapScripts::
	.byte 0

KantoAR_1_17_SSAnne_1F_Room7_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_18_SSANNE_2F_ROOM1, 3, 4
	goto KantoAR_InspectionFinish
