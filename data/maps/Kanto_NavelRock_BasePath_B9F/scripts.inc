Kanto_NavelRock_BasePath_B9F_MapScripts::
	.byte 0

KantoAR_2_51_NavelRock_BasePath_B9F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_52_NAVELROCK_BASEPATH_B10F, 3, 3
	goto KantoAR_InspectionFinish
