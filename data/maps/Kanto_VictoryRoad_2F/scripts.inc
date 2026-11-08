Kanto_VictoryRoad_2F_MapScripts::
	.byte 0

KantoAR_1_40_VictoryRoad_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_41_VICTORYROAD_3F, 22, 11
	goto KantoAR_InspectionFinish
