Kanto_SSAnne_3F_Corridor_MapScripts::
	.byte 0

KantoAR_1_7_SSAnne_3F_Corridor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_8_SSANNE_B1F_CORRIDOR, 11, 4
	goto KantoAR_InspectionFinish
