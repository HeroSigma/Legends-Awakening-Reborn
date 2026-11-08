Kanto_RockTunnel_1F_MapScripts::
	.byte 0

KantoAR_1_81_RockTunnel_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_82_ROCKTUNNEL_B1F, 24, 20
	goto KantoAR_InspectionFinish
