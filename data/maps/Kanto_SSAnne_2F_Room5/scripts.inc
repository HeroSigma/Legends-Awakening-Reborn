Kanto_SSAnne_2F_Room5_MapScripts::
	.byte 0

KantoAR_1_22_SSAnne_2F_Room5_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_23_SSANNE_2F_ROOM6, 3, 4
	goto KantoAR_InspectionFinish
