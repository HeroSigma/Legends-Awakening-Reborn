Kanto_SSAnne_CaptainsOffice_MapScripts::
	.byte 0

KantoAR_1_11_SSAnne_CaptainsOffice_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_12_SSANNE_1F_ROOM1, 3, 4
	goto KantoAR_InspectionFinish
