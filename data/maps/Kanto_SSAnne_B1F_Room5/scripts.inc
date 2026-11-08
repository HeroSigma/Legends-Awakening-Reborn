Kanto_SSAnne_B1F_Room5_MapScripts::
	.byte 0

KantoAR_1_28_SSAnne_B1F_Room5_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_29_SSANNE_1F_ROOM6, 3, 4
	goto KantoAR_InspectionFinish
