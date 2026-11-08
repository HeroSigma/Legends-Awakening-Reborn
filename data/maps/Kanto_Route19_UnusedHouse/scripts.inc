Kanto_Route19_UnusedHouse_MapScripts::
	.byte 0

KantoAR_27_0_Route19_UnusedHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_28_0_ROUTE22_NORTHENTRANCE, 7, 6
	goto KantoAR_InspectionFinish
