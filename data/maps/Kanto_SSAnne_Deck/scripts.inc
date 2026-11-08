Kanto_SSAnne_Deck_MapScripts::
	.byte 0

KantoAR_1_9_SSAnne_Deck_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_10_SSANNE_KITCHEN, 9, 9
	goto KantoAR_InspectionFinish
