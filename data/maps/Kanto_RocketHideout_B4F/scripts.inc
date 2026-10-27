Kanto_RocketHideout_B4F_MapScripts::
	.byte 0

KantoAR_1_45_RocketHideout_B4F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_46_ROCKETHIDEOUT_ELEVATOR, 3, 4
	goto KantoAR_InspectionFinish
