Kanto_TrainerTower_6F_MapScripts::
	.byte 0

KantoAR_2_6_TrainerTower_6F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_7_TRAINERTOWER_7F, 7, 10
	goto KantoAR_InspectionFinish
