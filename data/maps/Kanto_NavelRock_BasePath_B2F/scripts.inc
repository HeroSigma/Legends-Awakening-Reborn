Kanto_NavelRock_BasePath_B2F_MapScripts::
	.byte 0

KantoAR_2_44_NavelRock_BasePath_B2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_45_NAVELROCK_BASEPATH_B3F, 3, 3
	goto KantoAR_InspectionFinish
