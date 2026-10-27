Kanto_SSAnne_B1F_Room2_MapScripts::
	.byte 0

KantoAR_1_25_SSAnne_B1F_Room2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_26_SSANNE_B1F_ROOM3, 3, 4
	goto KantoAR_InspectionFinish
