Kanto_SSAnne_2F_Room2_MapScripts::
	.byte 0

KantoAR_1_19_SSAnne_2F_Room2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_20_SSANNE_2F_ROOM3, 3, 4
	goto KantoAR_InspectionFinish
