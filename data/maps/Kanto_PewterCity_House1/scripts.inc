Kanto_PewterCity_House1_MapScripts::
	.byte 0

KantoAR_6_4_PewterCity_House1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_6_5_PEWTERCITY_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
