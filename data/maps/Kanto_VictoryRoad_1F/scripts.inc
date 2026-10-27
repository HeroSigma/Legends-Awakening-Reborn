Kanto_VictoryRoad_1F_MapScripts::
	.byte 0

KantoAR_1_39_VictoryRoad_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_40_VICTORYROAD_2F, 25, 11
	goto KantoAR_InspectionFinish
