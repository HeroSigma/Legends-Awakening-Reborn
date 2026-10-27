Kanto_NavelRock_SummitPath_3F_MapScripts::
	.byte 0

KantoAR_2_40_NavelRock_SummitPath_3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_41_NAVELROCK_SUMMITPATH_4F, 3, 3
	goto KantoAR_InspectionFinish
