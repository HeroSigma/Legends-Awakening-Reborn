Kanto_NavelRock_1F_MapScripts::
	.byte 0

KantoAR_2_36_NavelRock_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_37_NAVELROCK_SUMMIT, 9, 13
	goto KantoAR_InspectionFinish
