Kanto_NavelRock_BasePath_B11F_MapScripts::
	.byte 0

KantoAR_2_53_NavelRock_BasePath_B11F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_54_NAVELROCK_B1F, 8, 3
	goto KantoAR_InspectionFinish
