Kanto_BattleColosseum_4P_MapScripts::
	.byte 0

KantoAR_0_3_BattleColosseum_4P_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_0_4_UNIONROOM, 7, 6
	goto KantoAR_InspectionFinish
