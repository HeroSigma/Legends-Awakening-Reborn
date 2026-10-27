Kanto_FuchsiaCity_Gym_MapScripts::
	.byte 0

KantoAR_11_3_FuchsiaCity_Gym_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_11_4_FUCHSIACITY_HOUSE1, 4, 3
	goto KantoAR_InspectionFinish
