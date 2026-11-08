Kanto_ThreeIsland_DunsparceTunnel_MapScripts::
	.byte 0

KantoAR_2_34_ThreeIsland_DunsparceTunnel_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_35_SEVENISLAND_SEVAULTCANYON_TANOBYKEY, 7, 8
	goto KantoAR_InspectionFinish
