Kanto_Route25_SeaCottage_MapScripts::
	.byte 0

KantoAR_30_0_Route25_SeaCottage_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_31_0_SEVENISLAND_HOUSE_ROOM1, 4, 3
	goto KantoAR_InspectionFinish
