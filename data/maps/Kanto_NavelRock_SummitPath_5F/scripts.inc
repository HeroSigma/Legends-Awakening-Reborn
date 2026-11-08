Kanto_NavelRock_SummitPath_5F_MapScripts::
	.byte 0

KantoAR_2_42_NavelRock_SummitPath_5F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_43_NAVELROCK_BASEPATH_B1F, 3, 3
	goto KantoAR_InspectionFinish
