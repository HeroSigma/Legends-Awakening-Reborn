Kanto_Route5_SouthEntrance_MapScripts::
	.byte 0

KantoAR_17_1_Route5_SouthEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_18_0_ROUTE6_NORTHENTRANCE, 4, 5
	goto KantoAR_InspectionFinish
