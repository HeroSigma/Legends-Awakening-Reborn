Kanto_BattleColosseum_2P_MapScripts::
	.byte 0

KantoAR_0_0_BattleColosseum_2P_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_0_1_TRADECENTER, 7, 4
	goto KantoAR_InspectionFinish
