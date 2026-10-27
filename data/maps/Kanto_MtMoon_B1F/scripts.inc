Kanto_MtMoon_B1F_MapScripts::
	.byte 0

KantoAR_1_2_MtMoon_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_3_MTMOON_B2F, 24, 20
	goto KantoAR_InspectionFinish
