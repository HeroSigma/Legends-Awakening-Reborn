Kanto_PewterCity_Gym_MapScripts::
	.byte 0

KantoAR_6_2_PewterCity_Gym_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_6_3_PEWTERCITY_MART, 5, 4
	goto KantoAR_InspectionFinish
