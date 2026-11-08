Kanto_RocketHideout_B3F_MapScripts::
	.byte 0

KantoAR_1_44_RocketHideout_B3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_45_ROCKETHIDEOUT_B4F, 12, 12
	goto KantoAR_InspectionFinish
