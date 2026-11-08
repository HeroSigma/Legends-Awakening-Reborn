Kanto_NavelRock_SummitPath_4F_MapScripts::
	.byte 0

KantoAR_2_41_NavelRock_SummitPath_4F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_42_NAVELROCK_SUMMITPATH_5F, 3, 3
	goto KantoAR_InspectionFinish
