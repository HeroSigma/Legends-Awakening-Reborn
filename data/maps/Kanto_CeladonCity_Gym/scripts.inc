Kanto_CeladonCity_Gym_MapScripts::
	.byte 0

KantoAR_10_16_CeladonCity_Gym_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_10_17_CELADONCITY_RESTAURANT, 7, 5
	goto KantoAR_InspectionFinish
