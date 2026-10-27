Kanto_SevenIsland_TanobyRuins_MapScripts::
	.byte 0

KantoAR_3_65_SevenIsland_TanobyRuins_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_4_0_PALLETTOWN_PLAYERSHOUSE_1F, 4, 5
	goto KantoAR_InspectionFinish
