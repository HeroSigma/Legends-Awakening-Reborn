Kanto_DiglettsCave_NorthEntrance_MapScripts::
	.byte 0

KantoAR_1_36_DiglettsCave_NorthEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_37_DIGLETTSCAVE_B1F, 42, 40
	goto KantoAR_InspectionFinish
