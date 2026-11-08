Kanto_SSAnne_1F_Corridor_MapScripts::
	.byte 0

KantoAR_1_5_SSAnne_1F_Corridor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_6_SSANNE_2F_CORRIDOR, 17, 12
	goto KantoAR_InspectionFinish
