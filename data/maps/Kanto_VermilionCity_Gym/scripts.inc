Kanto_VermilionCity_Gym_MapScripts::
	.byte 0

KantoAR_9_6_VermilionCity_Gym_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_9_7_VERMILIONCITY_HOUSE3, 4, 3
	goto KantoAR_InspectionFinish
