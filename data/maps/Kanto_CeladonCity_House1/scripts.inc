Kanto_CeladonCity_House1_MapScripts::
	.byte 0

KantoAR_10_18_CeladonCity_House1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_19_CELADONCITY_HOTEL, 8, 7
	goto KantoAR_InspectionFinish
