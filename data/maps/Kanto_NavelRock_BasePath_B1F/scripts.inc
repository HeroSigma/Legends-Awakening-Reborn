Kanto_NavelRock_BasePath_B1F_MapScripts::
	.byte 0

KantoAR_2_43_NavelRock_BasePath_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_44_NAVELROCK_BASEPATH_B2F, 3, 3
	goto KantoAR_InspectionFinish
