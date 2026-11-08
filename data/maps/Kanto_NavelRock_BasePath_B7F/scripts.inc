Kanto_NavelRock_BasePath_B7F_MapScripts::
	.byte 0

KantoAR_2_49_NavelRock_BasePath_B7F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_50_NAVELROCK_BASEPATH_B8F, 3, 3
	goto KantoAR_InspectionFinish
