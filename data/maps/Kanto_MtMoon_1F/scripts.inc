Kanto_MtMoon_1F_MapScripts::
	.byte 0

KantoAR_1_1_MtMoon_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_2_MTMOON_B1F, 23, 17
	goto KantoAR_InspectionFinish
