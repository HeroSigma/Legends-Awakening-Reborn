Kanto_NavelRock_BasePath_B5F_MapScripts::
	.byte 0

KantoAR_2_47_NavelRock_BasePath_B5F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_48_NAVELROCK_BASEPATH_B6F, 3, 3
	goto KantoAR_InspectionFinish
