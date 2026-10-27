Kanto_Route25_MapScripts::
	.byte 0

KantoAR_3_44_Route25_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_45_ONEISLAND_KINDLEROAD, 10, 70
	goto KantoAR_InspectionFinish
