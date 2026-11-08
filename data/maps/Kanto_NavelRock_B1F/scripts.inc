Kanto_NavelRock_B1F_MapScripts::
	.byte 0

KantoAR_2_54_NavelRock_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_55_NAVELROCK_FORK, 14, 50
	goto KantoAR_InspectionFinish
