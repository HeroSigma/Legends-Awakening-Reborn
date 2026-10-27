Kanto_SSAnne_1F_Room4_MapScripts::
	.byte 0

KantoAR_1_15_SSAnne_1F_Room4_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_16_SSANNE_1F_ROOM5, 3, 4
	goto KantoAR_InspectionFinish
