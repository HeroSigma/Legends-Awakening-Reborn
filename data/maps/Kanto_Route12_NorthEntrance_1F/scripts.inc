Kanto_Route12_NorthEntrance_1F_MapScripts::
	.byte 0

KantoAR_23_0_Route12_NorthEntrance_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_23_1_ROUTE12_NORTHENTRANCE_2F, 6, 5
	goto KantoAR_InspectionFinish
