Kanto_NavelRock_Harbor_MapScripts::
	.byte 0

KantoAR_2_59_NavelRock_Harbor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_1_VIRIDIANCITY, 24, 20
	goto KantoAR_InspectionFinish
