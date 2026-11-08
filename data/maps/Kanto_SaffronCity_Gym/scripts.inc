Kanto_SaffronCity_Gym_MapScripts::
	.byte 0

KantoAR_14_3_SaffronCity_Gym_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_14_4_SAFFRONCITY_HOUSE, 4, 3
	goto KantoAR_InspectionFinish
