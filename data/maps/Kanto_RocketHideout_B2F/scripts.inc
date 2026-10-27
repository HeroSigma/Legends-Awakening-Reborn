Kanto_RocketHideout_B2F_MapScripts::
	.byte 0

KantoAR_1_43_RocketHideout_B2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_44_ROCKETHIDEOUT_B3F, 8, 13
	goto KantoAR_InspectionFinish
