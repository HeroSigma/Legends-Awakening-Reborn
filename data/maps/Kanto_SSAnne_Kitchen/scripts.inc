Kanto_SSAnne_Kitchen_MapScripts::
	.byte 0

KantoAR_1_10_SSAnne_Kitchen_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_11_SSANNE_CAPTAINSOFFICE, 4, 5
	goto KantoAR_InspectionFinish
