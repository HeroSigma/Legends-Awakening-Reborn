Kanto_OneIsland_KindleRoad_MapScripts::
	.byte 0

KantoAR_3_45_OneIsland_KindleRoad_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_46_ONEISLAND_TREASUREBEACH, 12, 20
	goto KantoAR_InspectionFinish
