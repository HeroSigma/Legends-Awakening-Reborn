Kanto_SSAnne_B1F_Corridor_MapScripts::
	.byte 0

KantoAR_1_8_SSAnne_B1F_Corridor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_9_SSANNE_DECK, 12, 9
	goto KantoAR_InspectionFinish
