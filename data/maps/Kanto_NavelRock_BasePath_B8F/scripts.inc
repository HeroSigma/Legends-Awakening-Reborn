Kanto_NavelRock_BasePath_B8F_MapScripts::
	.byte 0

KantoAR_2_50_NavelRock_BasePath_B8F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_51_NAVELROCK_BASEPATH_B9F, 3, 3
	goto KantoAR_InspectionFinish
