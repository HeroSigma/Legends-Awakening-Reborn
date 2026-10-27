Kanto_UndergroundPath_EastEntrance_MapScripts::
	.byte 0

KantoAR_1_35_UndergroundPath_EastEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_36_DIGLETTSCAVE_NORTHENTRANCE, 5, 4
	goto KantoAR_InspectionFinish
