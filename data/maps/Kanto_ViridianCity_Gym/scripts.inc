Kanto_ViridianCity_Gym_MapScripts::
	.byte 0

KantoAR_5_1_ViridianCity_Gym_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_5_2_VIRIDIANCITY_SCHOOL, 6, 3
	goto KantoAR_InspectionFinish
