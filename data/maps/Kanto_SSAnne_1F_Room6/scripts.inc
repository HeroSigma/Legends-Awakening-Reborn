Kanto_SSAnne_1F_Room6_MapScripts::
	.byte 0

KantoAR_1_29_SSAnne_1F_Room6_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_30_UNDERGROUNDPATH_NORTHENTRANCE, 8, 5
	goto KantoAR_InspectionFinish
