Kanto_NavelRock_BasePath_B3F_MapScripts::
	.byte 0

KantoAR_2_45_NavelRock_BasePath_B3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_46_NAVELROCK_BASEPATH_B4F, 3, 3
	goto KantoAR_InspectionFinish
