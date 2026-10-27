Kanto_NavelRock_Base_MapScripts::
	.byte 0

KantoAR_2_38_NavelRock_Base_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_39_NAVELROCK_SUMMITPATH_2F, 3, 3
	goto KantoAR_InspectionFinish
