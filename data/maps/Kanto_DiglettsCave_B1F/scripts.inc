Kanto_DiglettsCave_B1F_MapScripts::
	.byte 0

KantoAR_1_37_DiglettsCave_B1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_38_DIGLETTSCAVE_SOUTHENTRANCE, 5, 4
	goto KantoAR_InspectionFinish
