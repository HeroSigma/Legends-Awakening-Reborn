Kanto_SSAnne_2F_Room4_MapScripts::
	.byte 0

KantoAR_1_21_SSAnne_2F_Room4_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_22_SSANNE_2F_ROOM5, 3, 4
	goto KantoAR_InspectionFinish
