Kanto_SSAnne_B1F_Room3_MapScripts::
	.byte 0

KantoAR_1_26_SSAnne_B1F_Room3_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_27_SSANNE_B1F_ROOM4, 3, 4
	goto KantoAR_InspectionFinish
