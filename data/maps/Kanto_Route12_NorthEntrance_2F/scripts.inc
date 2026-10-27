Kanto_Route12_NorthEntrance_2F_MapScripts::
	.byte 0

KantoAR_23_1_Route12_NorthEntrance_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_23_2_ROUTE12_FISHINGHOUSE, 4, 3
	goto KantoAR_InspectionFinish
