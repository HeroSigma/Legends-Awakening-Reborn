Kanto_NavelRock_Summit_MapScripts::
	.byte 0

KantoAR_2_37_NavelRock_Summit_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_38_NAVELROCK_BASE, 10, 15
	goto KantoAR_InspectionFinish
