Kanto_NavelRock_BasePath_B10F_MapScripts::
	.byte 0

KantoAR_2_52_NavelRock_BasePath_B10F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_53_NAVELROCK_BASEPATH_B11F, 3, 3
	goto KantoAR_InspectionFinish
