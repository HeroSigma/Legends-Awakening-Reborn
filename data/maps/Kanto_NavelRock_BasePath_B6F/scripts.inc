Kanto_NavelRock_BasePath_B6F_MapScripts::
	.byte 0

KantoAR_2_48_NavelRock_BasePath_B6F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_49_NAVELROCK_BASEPATH_B7F, 3, 3
	goto KantoAR_InspectionFinish
