Kanto_NavelRock_BasePath_B4F_MapScripts::
	.byte 0

KantoAR_2_46_NavelRock_BasePath_B4F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_47_NAVELROCK_BASEPATH_B5F, 3, 3
	goto KantoAR_InspectionFinish
