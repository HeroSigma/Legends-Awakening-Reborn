Kanto_NavelRock_Exterior_MapScripts::
	.byte 0

KantoAR_2_0_NavelRock_Exterior_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_1_TRAINERTOWER_1F, 7, 10
	goto KantoAR_InspectionFinish
