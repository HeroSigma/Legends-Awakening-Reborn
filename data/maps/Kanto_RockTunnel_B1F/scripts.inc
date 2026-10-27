Kanto_RockTunnel_B1F_MapScripts::
	.byte 0

KantoAR_1_82_RockTunnel_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_83_SEAFOAMISLANDS_1F, 19, 12
	goto KantoAR_InspectionFinish
