Kanto_SSAnne_1F_Room2_MapScripts::
	.byte 0

KantoAR_1_13_SSAnne_1F_Room2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_14_SSANNE_1F_ROOM3, 3, 4
	goto KantoAR_InspectionFinish
