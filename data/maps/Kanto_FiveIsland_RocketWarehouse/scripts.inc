Kanto_FiveIsland_RocketWarehouse_MapScripts::
	.byte 0

KantoAR_1_114_FiveIsland_RocketWarehouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_115_SIXISLAND_DOTTEDHOLE_1F, 8, 5
	goto KantoAR_InspectionFinish
