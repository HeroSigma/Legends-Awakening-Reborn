Kanto_TrainerTower_Lobby_MapScripts::
	.byte 0

KantoAR_2_10_TrainerTower_Lobby_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_11_TRAINERTOWER_ELEVATOR, 1, 4
	goto KantoAR_InspectionFinish
