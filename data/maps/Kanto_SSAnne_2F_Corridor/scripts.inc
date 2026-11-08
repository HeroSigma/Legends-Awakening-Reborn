Kanto_SSAnne_2F_Corridor_MapScripts::
	.byte 0

KantoAR_1_6_SSAnne_2F_Corridor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_7_SSANNE_3F_CORRIDOR, 11, 3
	goto KantoAR_InspectionFinish
