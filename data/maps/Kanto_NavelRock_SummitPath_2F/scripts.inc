Kanto_NavelRock_SummitPath_2F_MapScripts::
	.byte 0

KantoAR_2_39_NavelRock_SummitPath_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_40_NAVELROCK_SUMMITPATH_3F, 3, 3
	goto KantoAR_InspectionFinish
