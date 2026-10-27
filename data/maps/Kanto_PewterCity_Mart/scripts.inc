Kanto_PewterCity_Mart_MapScripts::
	.byte 0

KantoAR_6_3_PewterCity_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_6_4_PEWTERCITY_HOUSE1, 4, 3
	goto KantoAR_InspectionFinish
