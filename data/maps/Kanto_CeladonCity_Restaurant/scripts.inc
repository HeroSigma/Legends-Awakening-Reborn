Kanto_CeladonCity_Restaurant_MapScripts::
	.byte 0

KantoAR_10_17_CeladonCity_Restaurant_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_18_CELADONCITY_HOUSE1, 4, 3
	goto KantoAR_InspectionFinish
