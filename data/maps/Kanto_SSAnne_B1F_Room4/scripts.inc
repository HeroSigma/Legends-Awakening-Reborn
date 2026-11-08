Kanto_SSAnne_B1F_Room4_MapScripts::
	.byte 0

KantoAR_1_27_SSAnne_B1F_Room4_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_28_SSANNE_B1F_ROOM5, 3, 4
	goto KantoAR_InspectionFinish
