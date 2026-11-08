Kanto_SSAnne_Exterior_MapScripts::
	.byte 0

KantoAR_1_4_SSAnne_Exterior_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_5_SSANNE_1F_CORRIDOR, 15, 9
	goto KantoAR_InspectionFinish
