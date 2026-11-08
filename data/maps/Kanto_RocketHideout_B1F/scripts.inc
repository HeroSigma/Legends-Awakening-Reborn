Kanto_RocketHideout_B1F_MapScripts::
	.byte 0

KantoAR_1_42_RocketHideout_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_43_ROCKETHIDEOUT_B2F, 17, 8
	goto KantoAR_InspectionFinish
