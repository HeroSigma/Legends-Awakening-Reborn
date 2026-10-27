Kanto_DiglettsCave_SouthEntrance_MapScripts::
	.byte 0

KantoAR_1_38_DiglettsCave_SouthEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_39_VICTORYROAD_1F, 22, 10
	goto KantoAR_InspectionFinish
